"""Dashboard models."""

from datetime import datetime
from typing import Any, Optional

from planvantage.models.base import PlanVantageModel


class DashboardInfo(PlanVantageModel):
    """Summary information about a dashboard."""

    guid: str
    name: str
    plan_sponsor_guid: Optional[str] = None
    folder_guid: Optional[str] = None
    updated_at: Optional[datetime] = None


class TierComponentData(PlanVantageModel):
    """Tier component data."""

    column_guid: Optional[str] = None
    value: Optional[float] = None


class TierComponentInput(PlanVantageModel):
    """Input for tier component."""

    column_guid: str
    value: Optional[float] = None


class DashboardPlanTierData(PlanVantageModel):
    """Dashboard plan tier data."""

    guid: Optional[str] = None
    dashboard_plan_guid: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[float] = None
    enrollment: Optional[int] = None
    order: Optional[int] = None
    lf_admin_pepm: Optional[float] = None
    lf_ssl_premium_pepm: Optional[float] = None
    lf_asl_premium_pepm: Optional[float] = None
    lf_claims_funding_pepm: Optional[float] = None
    lf_components: Optional[list[TierComponentData]] = None


class DashboardPlanTierInput(PlanVantageModel):
    """Input for dashboard plan tier."""

    name: Optional[str] = None
    rate: Optional[float] = None
    enrollment: Optional[int] = None
    order: Optional[int] = None
    lf_admin_pepm: Optional[float] = None
    lf_ssl_premium_pepm: Optional[float] = None
    lf_asl_premium_pepm: Optional[float] = None
    lf_claims_funding_pepm: Optional[float] = None


class DashboardPlanData(PlanVantageModel):
    """Dashboard plan data."""

    guid: Optional[str] = None
    dashboard_guid: Optional[str] = None
    name: Optional[str] = None
    carrier: Optional[str] = None
    plan_type: Optional[str] = None
    funding_type: Optional[str] = None
    order: Optional[int] = None
    tiers: Optional[list[DashboardPlanTierData]] = None


class DashboardPlanInput(PlanVantageModel):
    """Input for creating/updating dashboard plan."""

    name: Optional[str] = None
    carrier: Optional[str] = None
    plan_type: Optional[str] = None
    funding_type: Optional[str] = None
    order: Optional[int] = None


class DashboardCustomFieldData(PlanVantageModel):
    """Dashboard custom field definition."""

    guid: Optional[str] = None
    dashboard_guid: Optional[str] = None
    name: Optional[str] = None
    field_type: Optional[str] = None
    order: Optional[int] = None


class DashboardCustomFieldInput(PlanVantageModel):
    """Input for creating/updating custom field."""

    name: str
    field_type: Optional[str] = None
    order: Optional[int] = None


class AdminFeeData(PlanVantageModel):
    """Admin fee data."""

    id: Optional[int] = None
    dashboard_guid: Optional[str] = None
    name: Optional[str] = None
    amount: Optional[float] = None
    fee_type: Optional[str] = None
    is_pepm: Optional[bool] = None
    is_taxable: Optional[bool] = None
    order: Optional[int] = None


class AdminFeeInput(PlanVantageModel):
    """Input for creating/updating admin fee."""

    name: Optional[str] = None
    amount: Optional[float] = None
    fee_type: Optional[str] = None
    is_pepm: Optional[bool] = None
    is_taxable: Optional[bool] = None
    order: Optional[int] = None


class LFComponentColumnData(PlanVantageModel):
    """Level-funded component column data."""

    guid: Optional[str] = None
    dashboard_guid: Optional[str] = None
    name: Optional[str] = None
    display_order: Optional[int] = None
    is_restricted: Optional[bool] = None


class LFComponentColumnInput(PlanVantageModel):
    """Input for LF component column."""

    name: str
    display_order: Optional[int] = None


class DashboardVersionInfo(PlanVantageModel):
    """Summary information about dashboard version."""

    guid: str
    dashboard_guid: Optional[str] = None
    name: str
    data_end_date: Optional[str] = None
    created_at: Optional[datetime] = None


class DashboardVersionData(PlanVantageModel):
    """Full dashboard version data."""

    guid: Optional[str] = None
    dashboard_guid: Optional[str] = None
    name: Optional[str] = None
    data_end_date: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class DashboardVersionInput(PlanVantageModel):
    """Input for updating dashboard version."""

    name: Optional[str] = None
    data_end_date: Optional[str] = None


class DashboardTierSetInput(PlanVantageModel):
    """Input for applying tier set to dashboard."""

    tier_name_set_id: Optional[int] = None


class DashboardData(PlanVantageModel):
    """Full dashboard data."""

    guid: Optional[str] = None
    name: Optional[str] = None
    plan_sponsor_guid: Optional[str] = None
    folder_guid: Optional[str] = None
    plans: Optional[list[DashboardPlanData]] = None
    custom_fields: Optional[list[DashboardCustomFieldData]] = None
    admin_fees: Optional[list[AdminFeeData]] = None
    lf_columns: Optional[list[LFComponentColumnData]] = None
    versions: Optional[list[DashboardVersionInfo]] = None
    active_version_guid: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class DashboardInput(PlanVantageModel):
    """Input for creating/updating dashboard."""

    plan_sponsor_guid: Optional[str] = None
    name: Optional[str] = None


class DashboardEnrollmentData(PlanVantageModel):
    """Dashboard enrollment data."""

    plan_tier_guid: Optional[str] = None
    month: Optional[str] = None
    enrollment: Optional[int] = None


class DashboardMembersData(PlanVantageModel):
    """Dashboard members data."""

    plan_tier_guid: Optional[str] = None
    month: Optional[str] = None
    members: Optional[int] = None


class DashboardClaimsData(PlanVantageModel):
    """Dashboard claims data."""

    plan_guid: Optional[str] = None
    month: Optional[str] = None
    medical_paid: Optional[float] = None
    rx_paid: Optional[float] = None


class DashboardCustomValueData(PlanVantageModel):
    """Dashboard custom value data."""

    custom_field_guid: Optional[str] = None
    plan_guid: Optional[str] = None
    month: Optional[str] = None
    value: Optional[float] = None


class DashboardLargeClaimData(PlanVantageModel):
    """Dashboard large claim data."""

    guid: Optional[str] = None
    dashboard_version_guid: Optional[str] = None
    plan_guid: Optional[str] = None
    month: Optional[str] = None
    amount: Optional[float] = None
    description: Optional[str] = None


class DashboardDataAvailability(PlanVantageModel):
    """Dashboard data availability information."""

    has_enrollment: Optional[bool] = None
    has_claims: Optional[bool] = None
    has_large_claims: Optional[bool] = None
    earliest_month: Optional[str] = None
    latest_month: Optional[str] = None
    months_count: Optional[int] = None


class DashboardSlideData(PlanVantageModel):
    """Dashboard slide computed data."""

    slide_key: Optional[str] = None
    data: Optional[dict[str, Any]] = None


class DashboardContributionTierData(PlanVantageModel):
    """Dashboard contribution tier data."""

    guid: Optional[str] = None
    plan_tier_guid: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[float] = None
    enrollment: Optional[int] = None
    employer_contribution: Optional[float] = None
    employee_contribution: Optional[float] = None


class DashboardContributionPlanData(PlanVantageModel):
    """Dashboard contribution plan data."""

    guid: Optional[str] = None
    plan_guid: Optional[str] = None
    name: Optional[str] = None
    tiers: Optional[list[DashboardContributionTierData]] = None


class DashboardContributionGroupData(PlanVantageModel):
    """Dashboard contribution group data."""

    guid: Optional[str] = None
    dashboard_guid: Optional[str] = None
    name: Optional[str] = None
    plans: Optional[list[DashboardContributionPlanData]] = None
    order: Optional[int] = None


class DashboardContributionGroupInput(PlanVantageModel):
    """Input for creating/updating dashboard contribution group."""

    name: Optional[str] = None
    order: Optional[int] = None
