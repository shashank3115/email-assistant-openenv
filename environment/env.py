from .models import AuditObservation, AuditAction

class AuditEnv:
    def __init__(self):
        self.reset()

    def reset(self, task_id: str = "easy"):
        self.task_id = task_id
        self.steps = 0
        self.max_steps = 20
        self.integrity_score = 1.0
        
        # Metadata Database: Defines the 'nature' of the files
        self.file_db = {
            "virus.exe": {"type": "Malware", "risk": 10, "encrypted": False, "loc": "main"},
            "data.csv": {"type": "PII", "risk": 8, "encrypted": False, "loc": "main"},
            "temp.log": {"type": "System", "risk": 2, "encrypted": False, "loc": "main"},
            "old_backup.zip": {"type": "System", "risk": 1, "encrypted": False, "loc": "main"}
        }
        
        # Filter files based on task difficulty
        if task_id == "easy":
            self.active_files = ["virus.exe", "data.csv"]
        elif task_id == "medium":
            self.active_files = ["virus.exe", "temp.log", "data.csv"]
        else: # Hard
            self.active_files = list(self.file_db.keys())

        return self._get_obs("Environment initialized with security metadata.")

    def _get_obs(self, msg: str):
        # Only show files currently in the 'main' directory to the agent
        visible_files = []
        for name in self.active_files:
            file_info = self.file_db[name]
            if file_info["loc"] == "main":
                visible_files.append({
                    "filename": name,
                    "file_type": file_info["type"],
                    "risk_level": file_info["risk"]
                })
        
        return AuditObservation(
            files=visible_files,
            system_integrity_score=round(self.integrity_score, 2),
            message=msg
        )

    def step(self, action: AuditAction):
        self.steps += 1
        reward = -0.01 # Efficiency penalty (encourages fast solving)
        done = False
        msg = "Action processed."

        if action.target not in self.active_files or self.file_db[action.target]["loc"] == "deleted":
            return self._get_obs("Target file not found."), 0.0, False, {}

        file_data = self.file_db[action.target]

        # REWARD LOGIC
        if action.command == "quarantine":
            if file_data["type"] == "Malware":
                reward = 0.5
                file_data["loc"] = "quarantine"
                msg = f"Successfully isolated threat: {action.target}"
            else:
                reward = -0.1 # Misidentifying safe files

        elif action.command == "encrypt":
            if file_data["type"] == "PII":
                file_data["encrypted"] = True
                reward = 0.2
                msg = f"Secured sensitive data: {action.target}"

        elif action.command == "delete":
            if file_data["type"] == "PII":
                # CRITICAL PENALTY: Deleting sensitive data is a major failure
                reward = -2.0
                self.integrity_score -= 0.5
                file_data["loc"] = "deleted"
                msg = "ALERT: Sensitive PII deleted! Integrity compromised."
            elif file_data["type"] == "Malware":
                reward = 0.3
                file_data["loc"] = "deleted"
                msg = "Malware deleted."

        # WIN CONDITION (Hard Task): Malware gone/isolated AND PII encrypted
        malware_cleared = all(f["loc"] != "main" for f in self.file_db.values() if f["type"] == "Malware")
        pii_secured = all(f["encrypted"] for f in self.file_db.values() if f["type"] == "PII")
        
        if malware_cleared and pii_secured:
            reward += 1.0
            done = True
            msg = "System Audit Complete: All threats mitigated and data secured."

        if self.steps >= self.max_steps:
            done = True

        return self._get_obs(msg), reward, done, {}