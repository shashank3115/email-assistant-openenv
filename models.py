from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Action(BaseModel):
    call: str = Field(..., description="Action: 'categorize', 'draft', or 'delete'")
    email_id: int = Field(..., description="The ID of the target email")
    payload: Optional[str] = Field(None, description="The category name or draft text")

class Observation(BaseModel):
    inbox: List[Dict[str, Any]]
    last_action_status: str
    current_task_goal: str

class StepResponse(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: Dict[str, Any]
