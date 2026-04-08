import pydantic
from typing import List, Optional

# 1. Define what the Agent can SEE (Observation)
class AuditObservation(pydantic.BaseModel):
    files: List[str]
    current_content: str
    message: str

# 2. Define what the Agent can DO (Action)
class AuditAction(pydantic.BaseModel):
    command: str  # "list", "read", "delete", "move"
    target: str

# 3. The Environment Class
class AuditEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = {
            "files": ["data_v1.csv", "virus.exe", "notes.txt"],
            "cleaned": False,
            "step_count": 0
        }
        return AuditObservation(
            files=self.state["files"],
            current_content="",
            message="Environment Reset. Task: Remove non-data files."
        )

    def step(self, action: AuditAction):
        self.state["step_count"] += 1
        reward = 0.0
        done = False
        
        if action.command == "delete" and action.target == "virus.exe":
            reward = 0.5  # Partial progress!
            self.state["files"].remove("virus.exe")
            msg = "Deleted dangerous file."
        elif action.command == "move" and action.target == "data_v1.csv":
            reward = 0.5
            msg = "Moved data to secure folder."
            if len(self.state["files"]) == 2: # If virus was already deleted
                reward = 1.0
                done = True
        else:
            msg = "Action completed with no reward."
            
        if self.state["step_count"] >= 5: done = True
        
        return AuditObservation(files=self.state["files"], current_content="", message=msg), reward, done, {}