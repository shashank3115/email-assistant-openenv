from pydantic import BaseModel

class Observation(BaseModel):
    email: str
    step_count: int

class Action(BaseModel):
    label: str  # spam / important / reply

class Reward(BaseModel):
    score: float