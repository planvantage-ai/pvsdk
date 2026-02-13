"""Summary and fixed cost models."""

from datetime import datetime
from typing import Any, Optional

from planvantage.models.base import PlanVantageModel


class SummaryTotalsData(PlanVantageModel):
    """Summary totals section."""

    total_current_enrollment: Optional[int] = None
    total_status_quo_enrollment: Optional[int] = None
    total_proposed_enrollment: Optional[int] = None
    total_current_net_claims: Optional[float] = None
    total_status_quo_net_claims: Optional[float] = None
    total_proposed_net_claims: Optional[float] = None
    total_current_fixed_costs: Optional[float] = None
    total_status_quo_fixed_costs: Optional[float] = None
    total_proposed_fixed_costs: Optional[float] = None
    total_current_cost: Optional[float] = None
    total_status_quo_cost: Optional[float] = None
    total_proposed_cost: Optional[float] = None
    current_pepm: Optional[float] = None
    status_quo_pepm: Optional[float] = None
    proposed_pepm: Optional[float] = None
    status_quo_vs_current_diff: Optional[float] = None
    status_quo_vs_current_diff_pct: Optional[float] = None
    proposed_vs_current_diff: Optional[float] = None
    proposed_vs_current_diff_pct: Optional[float] = None
    proposed_vs_status_quo_diff: Optional[float] = None
    proposed_vs_status_quo_diff_pct: Optional[float] = None


class SummarySettingsData(PlanVantageModel):
    """Summary settings data."""

    guid: Optional[str] = None
    scenario_guid: Optional[str] = None
    show_change_vs_current: Optional[bool] = None
    show_change_vs_sq: Optional[bool] = None
    show_dollar_diff: Optional[bool] = None
    show_percent_diff: Optional[bool] = None
    show_status_quo_column: Optional[bool] = None
    show_enrollment: Optional[bool] = None
    show_pepm: Optional[bool] = None
    show_contributions: Optional[bool] = None
    show_pepm_ee_contrib: Optional[bool] = None
    show_pepm_er_cost: Optional[bool] = None
    show_contribution_change_vs_current: Optional[bool] = None
    show_contribution_change_vs_sq: Optional[bool] = None
    show_pepm_dollar_diff: Optional[bool] = None
    show_pepm_percent_diff: Optional[bool] = None
    show_cost_share_pct: Optional[bool] = None
    show_ee_cost_share_pct: Optional[bool] = None
    show_er_cost_share_pct: Optional[bool] = None
    show_pepm_change_vs_current: Optional[bool] = None
    show_pepm_change_vs_sq: Optional[bool] = None
    status_quo_contribution_method: Optional[str] = None


class SummaryData(PlanVantageModel):
    """Complete summary tab data."""

    scenario_guid: Optional[str] = None
    scenario_name: Optional[str] = None
    has_status_quo: Optional[bool] = None
    rate_increase: Optional[float] = None
    loss_ratio: Optional[float] = None
    current_loss_ratio: Optional[float] = None
    fixed_cost_line_items: Optional[list[Any]] = None  # FixedCostLineItemData
    totals: Optional[SummaryTotalsData] = None
    contribution: Optional[Any] = None  # SummaryContributionData
    current_section_name: Optional[str] = None
    proposed_section_name: Optional[str] = None
    updated_at: Optional[datetime] = None
    calculated_hsa_current: Optional[float] = None
    calculated_hsa_status_quo: Optional[float] = None
    calculated_hsa_proposed: Optional[float] = None
    summary_settings: Optional[SummarySettingsData] = None
    claims_auto_calc_mode: Optional[bool] = None
    derived_loss_ratio: Optional[float] = None


class FixedCostLineItemData(PlanVantageModel):
    """Fixed cost line item data."""

    guid: Optional[str] = None
    scenario_guid: Optional[str] = None
    name: Optional[str] = None
    order: Optional[float] = None
    current_value: Optional[float] = None
    status_quo_value: Optional[float] = None
    proposed_value: Optional[float] = None
    is_auto_calc: Optional[bool] = None
    current_pepm: Optional[float] = None
    proposed_pepm: Optional[float] = None
    pepm_calc_active: Optional[bool] = None


class FixedCostLineItemInput(PlanVantageModel):
    """Input for creating/updating a fixed cost line item."""

    name: Optional[str] = None
    order: Optional[float] = None
    current_value: Optional[float] = None
    status_quo_value: Optional[float] = None
    proposed_value: Optional[float] = None
    is_auto_calc: Optional[bool] = None
    current_pepm: Optional[float] = None
    proposed_pepm: Optional[float] = None
    pepm_calc_active: Optional[bool] = None


class ImportFixedCostLineItemsInput(PlanVantageModel):
    """Input for bulk importing fixed cost line items."""

    line_item_guids: list[str]


class ToggleAutoCalcInput(PlanVantageModel):
    """Input for toggling auto-calc on a line item."""

    line_item_guid: str


class MoveDirectionInput(PlanVantageModel):
    """Input for moving an item up or down."""

    direction: str  # "up" or "down"
