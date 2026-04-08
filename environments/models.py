from pydantic import BaseModel
from typing import List, Optional

class AuditAction(BaseModel):
    command: str  # list, read, delete, move
    target: str

class AuditObservation(BaseModel):
    files: List[str]
    message: str