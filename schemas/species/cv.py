"""
OpenCV schemas
"""
from enum import Enum
from typing import List, Optional, Tuple

from pydantic import BaseModel

Point = Tuple[int, int]


class SpeciesIndexDebug(BaseModel):
    """
    A schema that can be used to store debug information for
    extracted columns from summary reports species index.
    """

    page: int
    column: int
    line: int
    bounding_box: Tuple[int, int, int, int]
    texts: List[str]
    message: str
    need_verification: bool


class SpeciesIndexLineType(str, Enum):
    GENUS = "genus"
    GENUS_SYNONYM = "genus_synonym"
    SPECIES = "species"
    CONTINUATION = "continuation"
    ERROR = "error"


class SpeciesIndexProcessedLine(BaseModel):
    type: SpeciesIndexLineType
    value: Optional[str]
    synonym: Optional[str]
    pages: List[int]
    text: str
    need_verification: bool
