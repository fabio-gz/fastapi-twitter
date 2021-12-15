from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Integer

class Tweet(BaseModel):
    id: Optional[str]
    content: str
    created_at: datetime
    by: int