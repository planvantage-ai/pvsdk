"""RatePlan models."""

from enum import Enum
from typing import Optional

from pydantic import Field

from planvantage.models.base import PlanVantageModel


class RateMethod(str, Enum):
    """Rate calculation method."""

    TIER_RATES = "tierRates"
    SINGLE_EE_RATE = "singleEERateWithRatios"
    MANUAL = "manual"


class HSAMethod(str, Enum):
    """HSA calculation method."""

    GROSS = "gross"
    NET = "net"
    SEPARATE = "separate"


class TierNameSetData(PlanVantageModel):
    """Tier name set configuration."""

    id: Optional[int] = None
    name: Optional[str] = None
    tier_names: Optional[list[str]] = None


class RatePlanTierData(PlanVantageModel):
    """Rate plan tier with rate and enrollment."""

    guid: Optional[str] = None
    rate_plan_guid: Optional[str] = None
    order: Optional[float] = None
    tier_name: Optional[str] = None
    tier_ratio: Optional[float] = None
    enrollment: Optional[int] = None
    adult_lives: Optional[float] = None
    hsa_amount: Optional[float] = None
    rate: Optional[float] = None
    rate_override: Optional[float] = None


class RatePlanAdjustmentData(PlanVantageModel):
    """Rate plan adjustment (multiplier applied to base rates)."""

    guid: Optional[str] = None
    rate_plan_guid: Optional[str] = None
    name: Optional[str] = None
    adjustment_factor: Optional[float] = None


class RatePlanData(PlanVantageModel):
    """Full rate plan data."""

    guid: Optional[str] = None
    scenario_guid: Optional[str] = None
    plan_design_guid: Optional[str] = None
    plan_name: Optional[str] = None
    plan_color: Optional[str] = None
    order: Optional[float] = None
    av: Optional[float] = None
    rv: Optional[float] = None
    plan_spread: Optional[float] = None
    tiers: Optional[list[RatePlanTierData]] = None
    adjustments: Optional[list[RatePlanAdjustmentData]] = None


class RatePlanInput(PlanVantageModel):
    """Input for creating rate plan."""

    scenario_guid: str
    plan_design_guid: Optional[str] = None
    plan_name: Optional[str] = None
    order: Optional[float] = None
    plan_spread: Optional[float] = None


class RatePlanTierInput(PlanVantageModel):
    """Input for creating rate plan tier."""

    rate_plan_guid: str
    tier_name: Optional[str] = None
    enrollment: Optional[int] = None
    hsa_amount: Optional[float] = None
    order: Optional[float] = None
    tier_ratio: Optional[float] = None
    rate: Optional[float] = None
    rate_override: Optional[float] = None


class RatePlanAdjustmentInput(PlanVantageModel):
    """Input for creating rate plan adjustment."""

    rate_plan_guid: str
    name: str
    adjustment_factor: float


class RateModelSettingsData(PlanVantageModel):
    """Rate model display settings."""

    guid: Optional[str] = None
    scenario_guid: Optional[str] = None
    show_actuarial_values: Optional[bool] = None
    show_relative_values: Optional[bool] = None
    show_plan_spread: Optional[bool] = None
    show_tier_ratios: Optional[bool] = None
    show_adult_lives: Optional[bool] = None
    show_hsa: Optional[bool] = None
    show_rates_without_hsa: Optional[bool] = None
    show_employer_subsidy_pct: Optional[bool] = None
    show_employee_contribution_pct: Optional[bool] = None
    show_legend: Optional[bool] = None
    show_tier_validation: Optional[bool] = None
    show_plan_annual_totals: Optional[bool] = None
    show_group_totals: Optional[bool] = None
    sync_enrollment_with_rate_model: Optional[bool] = None
    use_rate_override: Optional[bool] = None
    show_subgroup_comparison: Optional[bool] = None


class RateModelAssumptionsData(PlanVantageModel):
    """Rate model assumptions."""

    guid: Optional[str] = None
    scenario_guid: Optional[str] = None
    loss_ratio: Optional[float] = None
    current_loss_ratio: Optional[float] = None
    rate_increase: Optional[float] = None
    rate_method: Optional[RateMethod] = None
    hsa_method: Optional[HSAMethod] = None
    derived_loss_ratio: Optional[float] = None
    claims_auto_calc_mode: Optional[bool] = None


class RatePlanTierNameData(PlanVantageModel):
    """Standard tier name configuration."""

    id: Optional[int] = None
    name: Optional[str] = None


class TierNameSetInput(PlanVantageModel):
    """Input for applying tier name set."""

    tier_name_set_guid: Optional[str] = Field(None, alias="tierNameSetGuid")


class CopyCurrentRatePlanRequest(PlanVantageModel):
    """Request to copy current rate plan to proposed."""

    current_rate_plan_guid: str
