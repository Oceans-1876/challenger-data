from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel


class DataSourceUrls(BaseModel):
    records_by_id: Optional[str]
    records_by_match_names: Optional[str]
    synonyms_by_id: Optional[str]
    vernaculars_by_id: Optional[str]
    endpoint: Optional[str]
    matched_canonical_full: Optional[str]
    matched_canonical_simple: Optional[str]
    matched_name: Optional[str]
    web: Optional[str]


class DataSourceUrlParamType(str, Enum):
    query = "query"
    path = "path"


class DataSourceUrlParams(BaseModel):
    source: str
    attr: str
    source_key: str
    type: DataSourceUrlParamType
    is_batch: bool = False
    batch_limit: Optional[int]


class DataSourceAPIAttrsMapping(BaseModel):
    id: Optional[str]
    valid_id: Optional[str]
    current_id: Optional[str]


class DataSource(BaseModel):
    id: str
    title: str
    title_short: str
    curation: str
    record_count: int
    updated_at: str
    urls: DataSourceUrls = DataSourceUrls()
    urls_params: Dict[str, List[DataSourceUrlParams]] = {}
    url_attrs_mapping: DataSourceAPIAttrsMapping = DataSourceAPIAttrsMapping()
    home_url: Optional[str] = None
    is_outlink_ready: bool = False


DataSources = Dict[str, DataSource]
