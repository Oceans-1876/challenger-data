"""
Schemas for data extracted from the summary reports' species index.
"""
from typing import Dict, List, Optional

from pydantic import BaseModel

from .cv import SpeciesIndexDebug
from .global_names import GNMetadata
from .species import GNVerifierMatchedSpecies, SpeciesExtraInfo


class SpeciesIndexGenusSynonym(BaseModel):
    genus: str
    debug: SpeciesIndexDebug


class SpeciesIndexSpecies(BaseModel):
    species: str
    genus_synonym: Optional[SpeciesIndexGenusSynonym]
    matched_species: Optional[str]
    pages: List[int]
    debug: SpeciesIndexDebug


class SpeciesIndexGenus(BaseModel):
    genus: str
    synonym: Optional[str]
    matched_species: Optional[str]
    pages: List[int]
    species: List[SpeciesIndexSpecies]
    debug: SpeciesIndexDebug


class SpeciesIndexJSON(BaseModel):
    metadata: GNMetadata
    species: List[SpeciesIndexSpecies]


class SpeciesIndexVerifiedJSON(BaseModel):
    metadata: GNMetadata
    species: Dict[str, GNVerifierMatchedSpecies]


class SpeciesIndexVerifiedJSONExtra(BaseModel):
    metadata: Dict[str, int]
    species: Dict[str, SpeciesExtraInfo]
