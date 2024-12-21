from pydantic import BaseModel
from typing import Optional, List

class ExtractedData(BaseModel):
    title: Optional[str]
    headers: List[str]
    about_section: Optional[str]
    services_section: Optional[str]
    meta_description: Optional[str]
    industry: Optional[str]
    company_size: Optional[str]
    location: Optional[str]

class ResponseModel(BaseModel):
    message: str
    data: ExtractedData
