"""Projection models."""

from datetime import datetime
from typing import Any, Optional

from planvantage.models.base import PlanVantageModel


class ProjectionInfo(PlanVantageModel):
    """Summary information about a projection."""

    guid: str
    name: str
    plan_sponsor_guid: Optional[str] = None
    folder_guid: Optional[str] = None
    updated_at: Optional[datetime] = None


class ProjectionPlanTierComponentData(PlanVantageModel):
    """Projection plan tier component data."""

    column_guid: Optional[str] = None
    value: Optional[float] = None


class ProjectionPlanTierData(PlanVantageModel):
    """Projection plan tier data."""

    guid: Optional[str] = None
    projection_plan_guid: Optional[str] = None
    name: Optional[str] = None
    enrollment: Optional[int] = None
    members: Optional[int] = None
    order: Optional[int] = None
    lf_admin_pepm: Optional[float] = None
    lf_ssl_premium_pepm: Optional[float] = None
    lf_asl_premium_pepm: Optional[float] = None
    lf_claims_funding_pepm: Optional[float] = None
    lf_components: Optional[list[ProjectionPlanTierComponentData]] = None


class ProjectionPlanTierInput(PlanVantageModel):
    """Input for projection plan tier."""

    guid: Optional[str] = None
    name: Optional[str] = None
    enrollment: Optional[int] = None
    members: Optional[int] = None


class ProjectionPlanRateData(PlanVantageModel):
    """Projection plan rate data."""

    guid: Optional[str] = None
    tier_guid: Optional[str] = None
    year: Optional[int] = None
    rate: Optional[float] = None


class ProjectionPlanRateInput(PlanVantageModel):
    """Input for projection plan rate."""

    tier_guid: str
    year: int
    rate: Optional[float] = None


class ProjectionPlanData(PlanVantageModel):
    """Projection plan data."""

    guid: Optional[str] = None
    projection_guid: Optional[str] = None
    name: Optional[str] = None
    carrier: Optional[str] = None
    plan_type: Optional[str] = None
    funding_type: Optional[str] = None
    order: Optional[int] = None
    tiers: Optional[list[ProjectionPlanTierData]] = None
    rates: Optional[list[ProjectionPlanRateData]] = None


class ProjectionPlanInput(PlanVantageModel):
    """Input for creating/updating projection plan."""

    name: Optional[str] = None
    carrier: Optional[str] = None
    plan_type: Optional[str] = None
    funding_type: Optional[str] = None
    order: Optional[int] = None


class ProjectionLFTierComponentsInput(PlanVantageModel):
    """Input for updating tier LF components."""

    lf_admin_pepm: Optional[float] = None
    lf_ssl_premium_pepm: Optional[float] = None
    lf_asl_premium_pepm: Optional[float] = None
    lf_claims_funding_pepm: Optional[float] = None
    lf_components: Optional[list[ProjectionPlanTierComponentData]] = None


class ProjectionExperienceMonthCustomValueData(PlanVantageModel):
    """Custom value for experience month."""

    custom_field_guid: Optional[str] = None
    value: Optional[float] = None


class ProjectionExperienceMonthData(PlanVantageModel):
    """Experience month data."""

    guid: Optional[str] = None
    projection_guid: Optional[str] = None
    plan_guid: Optional[str] = None
    month: Optional[str] = None
    enrollment: Optional[int] = None
    members: Optional[int] = None
    medical_paid: Optional[float] = None
    rx_paid: Optional[float] = None
    custom_values: Optional[list[ProjectionExperienceMonthCustomValueData]] = None


class ProjectionExperienceMonthInput(PlanVantageModel):
    """Input for experience month."""

    plan_guid: Optional[str] = None
    month: Optional[str] = None
    enrollment: Optional[int] = None
    members: Optional[int] = None
    medical_paid: Optional[float] = None
    rx_paid: Optional[float] = None
    custom_values: Optional[list[ProjectionExperienceMonthCustomValueData]] = None


class ProjectionExperienceBulkInput(PlanVantageModel):
    """Input for bulk updating experience months."""

    months: list[ProjectionExperienceMonthInput]


class ProjectionCustomFieldData(PlanVantageModel):
    """Projection custom field data."""

    guid: Optional[str] = None
    projection_guid: Optional[str] = None
    name: Optional[str] = None
    field_type: Optional[str] = None
    order: Optional[int] = None


class ProjectionCustomFieldInput(PlanVantageModel):
    """Input for creating/updating custom field."""

    name: str
    field_type: Optional[str] = None
    order: Optional[int] = None


class ProjectionHighCostClaimantData(PlanVantageModel):
    """High cost claimant data."""

    guid: Optional[str] = None
    projection_guid: Optional[str] = None
    plan_guid: Optional[str] = None
    month: Optional[str] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    is_ongoing: Optional[bool] = None
    months_remaining: Optional[int] = None


class ProjectionSSLLaserData(PlanVantageModel):
    """SSL laser data."""

    guid: Optional[str] = None
    amount: Optional[float] = None
    premium: Optional[float] = None


class ProjectionFixedCostsData(PlanVantageModel):
    """Projection fixed costs data."""

    guid: Optional[str] = None
    projection_guid: Optional[str] = None
    has_ssl: Optional[bool] = None
    ssl_deductible: Optional[float] = None
    ssl_premium_pepm: Optional[float] = None
    ssl_single_pepm: Optional[float] = None
    ssl_dependent_pepm: Optional[float] = None
    ssl_lasers: Optional[list[ProjectionSSLLaserData]] = None
    has_asl: Optional[bool] = None
    asl_attachment: Optional[float] = None
    asl_premium_pepm: Optional[float] = None
    admin_pepm: Optional[float] = None


class ProjectionFixedCostsInput(PlanVantageModel):
    """Input for updating fixed costs."""

    has_ssl: Optional[bool] = None
    ssl_deductible: Optional[float] = None
    ssl_premium_pepm: Optional[float] = None
    ssl_single_pepm: Optional[float] = None
    ssl_dependent_pepm: Optional[float] = None
    ssl_lasers: Optional[list[ProjectionSSLLaserData]] = None
    has_asl: Optional[bool] = None
    asl_attachment: Optional[float] = None
    asl_premium_pepm: Optional[float] = None
    admin_pepm: Optional[float] = None


class ProjectionAdjustmentData(PlanVantageModel):
    """Projection adjustment data."""

    completion: Optional[float] = None
    trend: Optional[float] = None
    large_claims: Optional[float] = None
    benefit: Optional[float] = None
    family_size: Optional[float] = None


class ProjectionClaimsAdjustmentData(PlanVantageModel):
    """Claims adjustment settings."""

    large_claims_threshold: Optional[float] = None
    large_claims_add_back_pct: Optional[float] = None


class ProjectionClaimsAssumptionsData(PlanVantageModel):
    """Claims assumptions data."""

    trend_annual: Optional[float] = None
    trend_monthly: Optional[float] = None
    completion_months: Optional[int] = None


class ProjectionCarrierRenewalData(PlanVantageModel):
    """Carrier renewal data."""

    rate_increase: Optional[float] = None
    effective_date: Optional[str] = None


class ProjectionAdminFeeData(PlanVantageModel):
    """Projection admin fee data."""

    guid: Optional[str] = None
    projection_guid: Optional[str] = None
    name: Optional[str] = None
    amount: Optional[float] = None
    fee_type: Optional[str] = None
    is_pepm: Optional[bool] = None
    order: Optional[int] = None
    plan_guids: Optional[list[str]] = None


class ProjectionAdminFeeInput(PlanVantageModel):
    """Input for creating/updating admin fee."""

    name: Optional[str] = None
    amount: Optional[float] = None
    fee_type: Optional[str] = None
    is_pepm: Optional[bool] = None
    order: Optional[int] = None
    plan_guids: Optional[list[str]] = None


class ProjectionLFComponentColumnData(PlanVantageModel):
    """Level-funded component column data."""

    guid: Optional[str] = None
    projection_guid: Optional[str] = None
    name: Optional[str] = None
    display_order: Optional[int] = None
    is_restricted: Optional[bool] = None
    increase_pct: Optional[float] = None


class ProjectionLFComponentColumnInput(PlanVantageModel):
    """Input for LF component column."""

    name: str
    display_order: Optional[int] = None
    increase_pct: Optional[float] = None


class ClaimsProjectionPeriod(PlanVantageModel):
    """Claims projection period data."""

    period: Optional[str] = None
    projected_pmpm: Optional[float] = None
    projected_total: Optional[float] = None


class ClaimsProjectionResult(PlanVantageModel):
    """Claims projection result."""

    base_pmpm: Optional[float] = None
    adjusted_pmpm: Optional[float] = None
    projected_annual: Optional[float] = None
    periods: Optional[list[ClaimsProjectionPeriod]] = None


class ClaimsCustomFieldInfo(PlanVantageModel):
    """Custom field info for claims projection."""

    guid: Optional[str] = None
    name: Optional[str] = None


class ClaimsProjectionData(PlanVantageModel):
    """Claims projection data."""

    result: Optional[ClaimsProjectionResult] = None
    adjustments: Optional[ProjectionAdjustmentData] = None
    assumptions: Optional[ProjectionClaimsAssumptionsData] = None
    claims_adjustment: Optional[ProjectionClaimsAdjustmentData] = None
    custom_fields: Optional[list[ClaimsCustomFieldInfo]] = None


class BenefitAdjustmentVersionData(PlanVantageModel):
    """Benefit adjustment version data."""

    guid: Optional[str] = None
    name: Optional[str] = None
    data_end_date: Optional[str] = None


class BenefitAdjustmentDashboardData(PlanVantageModel):
    """Benefit adjustment dashboard data."""

    guid: Optional[str] = None
    name: Optional[str] = None
    versions: Optional[list[BenefitAdjustmentVersionData]] = None


class BenefitAdjustmentSourceData(PlanVantageModel):
    """Benefit adjustment source data."""

    dashboards: Optional[list[BenefitAdjustmentDashboardData]] = None


class BenefitAdjustmentEnableInput(PlanVantageModel):
    """Input for enabling benefit adjustment."""

    dashboard_version_guid: str


class ProjectionData(PlanVantageModel):
    """Full projection data."""

    guid: Optional[str] = None
    name: Optional[str] = None
    plan_sponsor_guid: Optional[str] = None
    folder_guid: Optional[str] = None
    plans: Optional[list[ProjectionPlanData]] = None
    experience_months: Optional[list[ProjectionExperienceMonthData]] = None
    custom_fields: Optional[list[ProjectionCustomFieldData]] = None
    high_cost_claimants: Optional[list[ProjectionHighCostClaimantData]] = None
    fixed_costs: Optional[ProjectionFixedCostsData] = None
    admin_fees: Optional[list[ProjectionAdminFeeData]] = None
    lf_columns: Optional[list[ProjectionLFComponentColumnData]] = None
    adjustments: Optional[ProjectionAdjustmentData] = None
    claims_adjustment: Optional[ProjectionClaimsAdjustmentData] = None
    claims_assumptions: Optional[ProjectionClaimsAssumptionsData] = None
    carrier_renewal: Optional[ProjectionCarrierRenewalData] = None
    claims_projection: Optional[ClaimsProjectionData] = None
    benefit_adjustment_enabled: Optional[bool] = None
    benefit_adjustment_dashboard_version_guid: Optional[str] = None
    family_size_adjustment_enabled: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ProjectionInput(PlanVantageModel):
    """Input for creating projection."""

    plan_sponsor_guid: str
    name: Optional[str] = None


class ProjectionUpdateInput(PlanVantageModel):
    """Input for updating projection."""

    name: Optional[str] = None


class ProjectionMoveInput(PlanVantageModel):
    """Input for moving projection to folder."""

    folder_guid: Optional[str] = None


class ProjectionImportDashboardInput(PlanVantageModel):
    """Input for importing from dashboard."""

    dashboard_version_guid: str


class ProjectionImportProjectionInput(PlanVantageModel):
    """Input for importing from another projection."""

    source_projection_guid: str
