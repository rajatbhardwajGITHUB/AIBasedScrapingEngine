from pydantic import BaseModel
from typing import Optional, List

class ExtractedData(BaseModel):
    industry: Optional[str]
    company_size: Optional[str]
    location: Optional[str]

class ResponseModel(BaseModel):
    message: str
    data: ExtractedData
