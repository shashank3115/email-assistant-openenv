from .models import AuditObservation, AuditAction

class AuditEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = {"files": ["data.csv", "virus.exe", "temp.log"], "steps": 0}
        return AuditObservation(files=self.state["files"], message="System Ready")

    def step(self, action: AuditAction):
        self.state["steps"] += 1
        reward = 0.0
        done = False
        
        # Logic for 3 tasks: Delete virus, Delete logs, Keep CSV
        if action.command == "delete":
            if action.target == "virus.exe":
                reward = 0.4
                if "virus.exe" in self.state["files"]: self.state["files"].remove("virus.exe")
            elif action.target == "temp.log":
                reward = 0.3
                if "temp.log" in self.state["files"]: self.state["files"].remove("temp.log")
        
        # Hard task: Finalize cleanup
        if len(self.state["files"]) == 1 and "data.csv" in self.state["files"]:
            reward = 1.0
            done = True
            
        if self.state["steps"] >= 10:
            done = True
            
        return AuditObservation(files=self.state["files"], message="Action processed"), reward, done, {}