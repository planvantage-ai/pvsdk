"""Census models."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field


class ColumnNullDefault(BaseModel):
    """How null/empty values in a census column should be filled in."""

    strategy: str  # "none", "value", "average", "median", "mode"
    value: Optional[Any] = None  # the computed or specified default


class CensusColumnMetadata(BaseModel):
    """Metadata for a single column in an uploaded census file."""

    name: str  # Exact column name as it appeared in the file
    data_type: str  # "text", "integer", "float", "date", "boolean"
    unique_values: Optional[list[str]] = None  # populated for low-cardinality text columns
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    null_count: int = 0
    total_count: int = 0
    null_default: Optional[ColumnNullDefault] = None


class AmbiguousColumnCandidate(BaseModel):
    """A candidate column for plan or tier disambiguation."""

    column_index: int
    header_name: str
    score: int
    sample_values: list[str] = Field(default_factory=list)


class AmbiguousColumnsInfo(BaseModel):
    """Info about ambiguous Plan/Tier column candidates.

    The ``resolved_*`` fields are populated when one of the column types was
    auto-resolved by the backend's scoring heuristic and only the other type
    needs user disambiguation.
    """

    plan_candidates: list[AmbiguousColumnCandidate] = Field(default_factory=list)
    tier_candidates: list[AmbiguousColumnCandidate] = Field(default_factory=list)
    resolved_plan_column: Optional[int] = None
    resolved_tier_column: Optional[int] = None


class CensusSchemaConfig(BaseModel):
    """Census schema — column metadata and disambiguation state.

    The ``columns`` map is keyed by the exact column name as it appeared in
    the uploaded file (case-sensitive). Use case-insensitive lookups in your
    own code if you need to match user input.
    """

    columns: dict[str, CensusColumnMetadata] = Field(default_factory=dict)
    disambiguation_info: Optional[AmbiguousColumnsInfo] = None


class CensusPlanMapping(BaseModel):
    """Mapping from census plan values to a rate plan."""

    census_column: str
    census_values: list[str]
    rate_plan_guid: str
    rate_plan_name: Optional[str] = None
    confidence: float = 0.0
    matched_count: int = 0


class CensusTierMapping(BaseModel):
    """Mapping from census tier values to a standard tier name."""

    census_column: str
    census_values: list[str]
    rate_plan_tier_name_id: int
    tier_name: Optional[str] = None
    confidence: float = 0.0
    matched_count: int = 0


class CensusOptOutMapping(BaseModel):
    """Mapping for opt-out / waived coverage values."""

    census_column: str
    census_values: list[str]
    reason: str  # "waived", "declined", "not_eligible", etc.
    matched_count: int = 0


class CensusMappingInfo(BaseModel):
    """Metadata about the census being mapped."""

    file_name: Optional[str] = None
    total_rows: Optional[int] = None
    enrollment_type: Optional[str] = None  # "enrolled_only" or "all_eligibles"
    subscriber_key_column: Optional[str] = None


class CensusFilterRule(BaseModel):
    """A single filter rule used for include/exclude rules and group criteria."""

    column: str
    operator: str  # "equals", "in", "less_than", "greater_than", "between"
    value: Any = None


class CensusMappingFilters(BaseModel):
    """Filtering rules applied to census rows when computing enrollment."""

    description: Optional[str] = None
    include_rules: Optional[list[CensusFilterRule]] = None
    exclude_rules: Optional[list[CensusFilterRule]] = None


class CensusSubgroup(BaseModel):
    """A single contribution subgroup defined by a filter rule."""

    group_name: str
    filter_rule: CensusFilterRule
    contribution_group_guid: Optional[str] = None
    matched_count: int = 0


class CensusSubgroupConfig(BaseModel):
    """Configuration for splitting census rows into contribution subgroups."""

    enabled: bool = False
    grouping_column: Optional[str] = None
    grouping_type: Optional[str] = None  # "salary_bands" or "custom"
    groups: Optional[list[CensusSubgroup]] = None


class CensusParticipationAdjustment(BaseModel):
    """Configuration for adjusting participation rates after mapping."""

    enabled: bool = False
    type: Optional[str] = None  # "percentage_increase" or "percentage_decrease"
    value: Optional[float] = None
    apply_to: Optional[str] = None  # "all" or a specific plan GUID
    description: Optional[str] = None


class CensusMappingValidation(BaseModel):
    """Validation results for census mappings."""

    unmapped_plan_values: list[str] = Field(default_factory=list)
    unmapped_tier_values: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)


class CensusMappingConfig(BaseModel):
    """Full census mapping configuration."""

    model_config = ConfigDict(populate_by_name=True)

    version: str = ""
    generated_at: Optional[datetime] = None
    census_info: Optional[CensusMappingInfo] = None
    schema_config: Optional[CensusSchemaConfig] = Field(default=None, alias="schema")
    filters: Optional[CensusMappingFilters] = None
    plan_mappings: list[CensusPlanMapping] = Field(default_factory=list)
    tier_mappings: list[CensusTierMapping] = Field(default_factory=list)
    opt_out_mappings: list[CensusOptOutMapping] = Field(default_factory=list)
    unique_plan_values: list[str] = Field(default_factory=list)
    unique_tier_values: list[str] = Field(default_factory=list)
    plan_value_counts: dict[str, int] = Field(default_factory=dict)
    tier_value_counts: dict[str, int] = Field(default_factory=dict)
    plan_tier_counts: Optional[dict[str, dict[str, int]]] = None
    contribution_subgroups: Optional[CensusSubgroupConfig] = None
    participation_adjustment: Optional[CensusParticipationAdjustment] = None
    contribution_group_snapshot: Optional[dict[str, list[str]]] = None
    rate_plan_tier_snapshot: Optional[list[str]] = None
    validation: Optional[CensusMappingValidation] = None


class CensusInfo(BaseModel):
    """Census summary information.

    The census has two independent statuses:

    - ``processing_status``: result of file upload + parse (immutable after upload)
    - ``mapping_status``: result of LLM mapping (separate; may retry without re-uploading)

    Both use the same value space: ``pending``, ``processing``,
    ``disambiguating``, ``mapped``, ``success``, ``failed``.
    """

    guid: str
    name: str
    file_name: str
    file_size: int
    row_count: int
    processing_status: str
    processing_error: Optional[str] = None
    mapping_status: Optional[str] = None
    mapping_error: Optional[str] = None
    schema_config: Optional[CensusSchemaConfig] = None
    created_at: datetime
    updated_at: Optional[datetime] = None


class CensusData(BaseModel):
    """Full census data.

    See :class:`CensusInfo` for the dual-status story (``processing_status``
    vs ``mapping_status``).
    """

    guid: str
    name: str
    file_name: str
    file_type: str
    file_size: int
    row_count: int
    processing_status: str
    processing_error: Optional[str] = None
    mapping_status: Optional[str] = None
    mapping_error: Optional[str] = None
    schema_config: Optional[CensusSchemaConfig] = None
    mapping_config: Optional[CensusMappingConfig] = None
    created_at: datetime
    updated_at: datetime


class PIIDetection(BaseModel):
    """A potential PII column flagged during upload."""

    column_name: str
    column_index: int
    pii_type: str  # "SSN", "Name", "Address", "Phone", "Email"
    detection_type: str  # "header" or "content"
    sample_row: Optional[int] = None
    sample_value: Optional[str] = None  # Masked sample for context


class CensusValidationError(BaseModel):
    """A validation error in census data."""

    row: int
    column: str
    message: str


class CensusUploadResult(BaseModel):
    """Result of census upload operation."""

    success: bool
    census_guid: str
    row_count: int = 0
    plans_found: list[str] = Field(default_factory=list)
    tiers_found: list[str] = Field(default_factory=list)
    errors: list[CensusValidationError] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    pii_detections: Optional[list[PIIDetection]] = None
    needs_disambiguation: bool = False
    ambiguous_columns: Optional[AmbiguousColumnsInfo] = None


class ScenarioCensusInfo(BaseModel):
    """Census mapping information for a scenario."""

    census_guid: str
    census_name: str
    row_count: int
    mapping_config: Optional[CensusMappingConfig] = None
    enrollment_status: str
    expected_enrollment: Optional[dict[str, dict[str, int]]] = None
    current_enrollment: Optional[dict[str, dict[str, int]]] = None


class MigrationChange(BaseModel):
    """A single migration between plans."""

    from_plan: str
    to_plan: str
    count: int
    percentage: float
    reason: str


class MigrationEstimation(BaseModel):
    """Estimated enrollment migration from current to proposed plans."""

    proposed_enrollment: dict[str, dict[str, int]]
    migration_summary: list[MigrationChange] = Field(default_factory=list)
    total_enrollment_delta: int = 0
    confidence: float = 0.0
    rationale: str = ""


class ApplyCensusEnrollmentResult(BaseModel):
    """Result of applying census enrollment."""

    success: bool
    total_records: int = 0
    previous_enrollment: int = 0
    new_enrollment: int = 0
    enrollment_by_plan: dict[str, int] = Field(default_factory=dict)
    enrollment_by_tier: dict[str, int] = Field(default_factory=dict)
    warnings: list[str] = Field(default_factory=list)


class PlanEnrollmentPreview(BaseModel):
    """Enrollment preview for a single plan."""

    guid: str
    name: str
    enrollment: dict[str, int] = Field(default_factory=dict)
    total: int = 0


class EnrollmentSummary(BaseModel):
    """Enrollment summary with plans and total."""

    plans: list[PlanEnrollmentPreview] = Field(default_factory=list)
    total: int = 0


class MigrationPreviewResponse(BaseModel):
    """Response from migration preview endpoints."""

    current_enrollment: Optional[EnrollmentSummary] = None
    proposed_enrollment: Optional[EnrollmentSummary] = None
    participation_change: int = 0
    analysis: Optional[dict[str, Any]] = None
    reasoning: Optional[list[dict[str, Any]]] = None


class StoredMigrationResponse(BaseModel):
    """Stored migration result with staleness info."""

    result: Optional[MigrationPreviewResponse] = None
    stale: bool = False
    instructions: str = ""
    allow_participation_change: bool = False
    source: str = ""
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class CensusTemplateConfig(BaseModel):
    """Configuration for census template download."""

    include_subscriber_key: bool = False
    age_format: Optional[str] = None
    include_zip_code: bool = False
    service_format: Optional[str] = None
    include_gender: bool = False
    include_salary: bool = False
    custom_fields: list[str] = Field(default_factory=list)
