from pydantic import BaseModel
from typing import List, Dict, Any, Optional, Literal

class AuditAction(BaseModel):
    # Added 'quarantine' and 'encrypt' for higher complexity
    command: Literal['list', 'read', 'delete', 'quarantine', 'encrypt', 'move']
    target: str

class FileInfo(BaseModel):
    filename: str
    file_type: Literal['PII', 'Malware', 'System']
    risk_level: int # 0-10

class AuditObservation(BaseModel):
    # Now returns a list of objects with metadata, not just strings
    files: List[Dict[str, Any]] 
    system_integrity_score: float
    message: str