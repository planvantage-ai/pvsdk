"""Scenario models."""

from datetime import datetime
from typing import Any, Optional

from pydantic import Field

from planvantage.models.base import PlanVantageModel


class ScenarioInfo(PlanVantageModel):
    """Summary information about a scenario."""

    guid: str
    name: str
    order: Optional[float] = None
    updated_at: Optional[datetime] = None


class ScenarioData(PlanVantageModel):
    """Full scenario data - uses additionalProperties so we accept any fields."""

    guid: Optional[str] = None
    name: Optional[str] = None
    order: Optional[float] = None
    # Additional fields will be accepted via extra="allow" in base config


class ScenarioCreateRequest(PlanVantageModel):
    """Request to create a new scenario."""

    name: Optional[str] = None
    plan_sponsor: dict[str, str]  # {"guid": "..."}


class ScenarioUpdateRequest(PlanVantageModel):
    """Request to update a scenario. Accepts any fields."""

    pass  # additionalProperties: true


class ScenarioUpdateResponse(PlanVantageModel):
    """Response from updating a scenario."""

    name: Optional[str] = None
    guid: Optional[str] = None
    order: Optional[float] = None
    current_section_name: Optional[str] = None
    proposed_section_name: Optional[str] = None
    selected_contribution_option_guid: Optional[str] = None


class ScenarioTierNameSetInput(PlanVantageModel):
    """Input for applying tier name set to scenario."""

    proposed: Optional[bool] = None
    set_id: Optional[int] = None


class ScenarioHistoryInput(PlanVantageModel):
    """Input for undo/redo operations."""

    scenario_guid: str
    model_type: str


class SyncEnrollmentRequest(PlanVantageModel):
    """Request to sync enrollment data."""

    proposed: Optional[bool] = None


class CalculateAllOptionsRequest(PlanVantageModel):
    """Request to calculate all contribution options."""

    skip_matching_hashes: Optional[bool] = None


class ImportScenarioRequest(PlanVantageModel):
    """Request to import a scenario."""

    scenario_guid: str


class CreateScenarioFromPlanDocumentRequest(PlanVantageModel):
    """Request to create scenario from plan document."""

    plan_document_guid: str
    name: Optional[str] = None


class CreateScenarioFromPlanDocumentResponse(PlanVantageModel):
    """Response from creating scenario from plan document."""

    scenario_guid: Optional[str] = None


class ShareScenarioRequest(PlanVantageModel):
    """Request to share a scenario."""

    recipient_emails: list[str]


class ShareScenarioEmailResult(PlanVantageModel):
    """Result of sharing scenario with a single recipient."""

    email: Optional[str] = None
    success: Optional[bool] = None
    message: Optional[str] = None


class ShareScenarioResponse(PlanVantageModel):
    """Response from sharing a scenario."""

    results: Optional[list[ShareScenarioEmailResult]] = None
    summary: Optional[dict[str, int]] = None


class SharedScenarioPreview(PlanVantageModel):
    """Preview information for a shared scenario."""

    user_email: Optional[str] = None
    user_guid: Optional[str] = None
    plan_sponsor_name: Optional[str] = None
    scenario_name: Optional[str] = None
    current_plan_names: Optional[list[str]] = None
    proposed_plan_names: Optional[list[str]] = None
    recipient_email: Optional[str] = None
    expiration_date: Optional[datetime] = None
    last_used_date: Optional[datetime] = None


class ClaimScenarioRequest(PlanVantageModel):
    """Request to claim a shared scenario."""

    plan_sponsor_name: str


class ClaimScenarioResponse(PlanVantageModel):
    """Response from claiming a scenario."""

    message: Optional[str] = None
    plan_sponsor_guid: Optional[str] = None
    scenario_guid: Optional[str] = None


class ScenarioFixedCostsData(PlanVantageModel):
    """Fixed costs data for a scenario."""

    guid: Optional[str] = None
    admin_pepm_current: Optional[float] = None
    admin_pepm_projected: Optional[float] = None
    admin_projected_mode: Optional[str] = None
    has_ssl: Optional[bool] = None
    ssl_deductible_current: Optional[float] = None
    ssl_deductible_projected: Optional[float] = None
    ssl_deductible_projected_mode: Optional[str] = None
    ssl_premium_pepm_current: Optional[float] = None
    ssl_premium_pepm_projected: Optional[float] = None
    ssl_premium_projected_mode: Optional[str] = None
    ssl_single_pepm_current: Optional[float] = None
    ssl_single_pepm_projected: Optional[float] = None
    ssl_dependent_pepm_current: Optional[float] = None
    ssl_dependent_pepm_projected: Optional[float] = None
    agg_spec_deductible_current: Optional[float] = None
    agg_spec_deductible_projected: Optional[float] = None
    agg_spec_deductible_projected_mode: Optional[str] = None
    has_asl: Optional[bool] = None
    asl_premium_pepm_current: Optional[float] = None
    asl_premium_pepm_projected: Optional[float] = None
    asl_premium_projected_mode: Optional[str] = None


class ScenarioFixedCostsInput(PlanVantageModel):
    """Input for updating scenario fixed costs."""

    admin_pepm_current: Optional[float] = None
    admin_pepm_projected: Optional[float] = None
    admin_projected_mode: Optional[str] = None
    has_ssl: Optional[bool] = None
    ssl_deductible_current: Optional[float] = None
    ssl_deductible_projected: Optional[float] = None
    ssl_deductible_projected_mode: Optional[str] = None
    ssl_premium_pepm_current: Optional[float] = None
    ssl_premium_pepm_projected: Optional[float] = None
    ssl_premium_projected_mode: Optional[str] = None
    ssl_single_pepm_current: Optional[float] = None
    ssl_single_pepm_projected: Optional[float] = None
    ssl_dependent_pepm_current: Optional[float] = None
    ssl_dependent_pepm_projected: Optional[float] = None
    agg_spec_deductible_current: Optional[float] = None
    agg_spec_deductible_projected: Optional[float] = None
    agg_spec_deductible_projected_mode: Optional[str] = None
    has_asl: Optional[bool] = None
    asl_premium_pepm_current: Optional[float] = None
    asl_premium_pepm_projected: Optional[float] = None
    asl_premium_projected_mode: Optional[str] = None


class ScenarioAdminFeeData(PlanVantageModel):
    """Admin fee data for a scenario."""

    guid: Optional[str] = None
    name: Optional[str] = None
    display_order: Optional[int] = None
    amount_pepm_current: Optional[float] = None
    amount_pepm_projected: Optional[float] = None
    projected_mode: Optional[str] = None
    projected_increase_value: Optional[float] = None
    plan_guids: Optional[list[str]] = None


class ScenarioAdminFeeInput(PlanVantageModel):
    """Input for creating/updating scenario admin fee."""

    name: Optional[str] = None
    display_order: Optional[int] = None
    amount_pepm_current: Optional[float] = None
    amount_pepm_projected: Optional[float] = None
    projected_mode: Optional[str] = None
    projected_increase_value: Optional[float] = None
    plan_guids: Optional[list[str]] = None


class ScenarioAdditiveAdjustmentData(PlanVantageModel):
    """Additive adjustment data for a scenario."""

    guid: Optional[str] = None
    name: Optional[str] = None
    display_order: Optional[int] = None
    amount_pepm_current: Optional[float] = None
    amount_pepm_projected: Optional[float] = None
    projected_mode: Optional[str] = None
    projected_increase_value: Optional[float] = None
    is_credit: Optional[bool] = None


class ScenarioAdditiveAdjustmentInput(PlanVantageModel):
    """Input for creating/updating scenario additive adjustment."""

    name: Optional[str] = None
    display_order: Optional[int] = None
    amount_pepm_current: Optional[float] = None
    amount_pepm_projected: Optional[float] = None
    projected_mode: Optional[str] = None
    projected_increase_value: Optional[float] = None
    is_credit: Optional[bool] = None


class ImportFromProjectionInput(PlanVantageModel):
    """Input for importing data from projection."""

    projection_guid: str


class ScenarioLFComponentColumnData(PlanVantageModel):
    """Level-funded component column data."""

    guid: Optional[str] = None
    name: Optional[str] = None
    display_order: Optional[int] = None
    is_restricted: Optional[bool] = None
    increase_pct: Optional[float] = None


class ScenarioLFComponentColumnInput(PlanVantageModel):
    """Input for creating/updating LF component column."""

    name: str
    display_order: Optional[int] = None
    increase_pct: Optional[float] = None


class ScenarioTierComponentData(PlanVantageModel):
    """Tier component data."""

    column_guid: Optional[str] = None
    value: Optional[float] = None


class ScenarioTierLFComponentsInput(PlanVantageModel):
    """Input for updating tier LF components."""

    lf_admin_pepm: Optional[float] = None
    lf_ssl_premium_pepm: Optional[float] = None
    lf_asl_premium_pepm: Optional[float] = None
    lf_claims_funding_pepm: Optional[float] = None
    lf_components: Optional[list[ScenarioTierComponentData]] = None
