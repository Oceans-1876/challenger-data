from typing import List, Optional

from pydantic import BaseModel


class GNVerifierMatchedSpeciesScore(BaseModel):
    infraSpecificRankScore: int
    fuzzyLessScore: int
    curatedDataScore: int
    authorMatchScore: int
    acceptedNameScore: int
    parsingQualityScore: int


class GNVerifierMatchedSpecies(BaseModel):
    dataSourceId: int
    dataSourceTitleShort: str
    curation: str
    recordId: str
    outlink: Optional[str]
    entryDate: str
    matchedName: str
    matchedCardinality: int
    matchedCanonicalSimple: Optional[str]
    matchedCanonicalFull: Optional[str]
    currentRecordId: str
    currentName: str
    currentCardinality: int
    currentCanonicalSimple: str
    currentCanonicalFull: str
    isSynonym: bool
    classificationPath: Optional[str]
    classificationRanks: Optional[str]
    classificationIds: Optional[str]
    editDistance: int
    stemEditDistance: int
    matchType: str
    scoreDetails: GNVerifierMatchedSpeciesScore


class SpeciesCommonName(BaseModel):
    language: str
    language_code: str
    vernacular: str


class SpeciesSynonym(BaseModel):
    id: int
    url: str
    scientificname: str
    authority: Optional[str]


class SpeciesRecord(BaseModel):
    id: int
    url: str
    scientificname: str
    authority: Optional[str]
    status: str
    unacceptreason: Optional[str]
    taxonRankID: int
    rank: Optional[str]
    valid_id: Optional[int]
    valid_name: Optional[str]
    valid_authority: Optional[str]
    parentNameUsageID: int
    citation: str
    lsid: str
    isBrackish: Optional[int]
    isExtinct: Optional[int]
    isFreshwater: Optional[int]
    isMarine: Optional[int]
    isTerrestrial: Optional[int]
    match_type: str


class SpeciesExtraInfo(BaseModel):
    records: List[SpeciesRecord] = []
    common_names: List[SpeciesCommonName] = []
    synonyms: List[SpeciesSynonym] = []
