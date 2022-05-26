import datetime
from typing import Optional

from pydantic import BaseModel, Field


class GNMetadata(BaseModel):
    gnfinder: Optional[str]
    gnverifier: Optional[str]
    date: str = Field(default_factory=lambda: str(datetime.datetime.now()))
