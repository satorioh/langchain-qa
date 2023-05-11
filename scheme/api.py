from typing import Optional, Dict
from pydantic import BaseModel


class BaseResponse(BaseModel):
    data: Dict
    code: int
