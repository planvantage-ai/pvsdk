"""Exhibit models."""

from datetime import datetime
from typing import Any, Optional

from planvantage.models.base import PlanVantageModel


class ExhibitInfo(PlanVantageModel):
    """Summary information about an exhibit."""

    guid: str
    name: str
    scenario_count: Optional[int] = None
    updated_at: Optional[datetime] = None


class ExhibitScenarioConfigData(PlanVantageModel):
    """Scenario configuration within an exhibit."""

    guid: Optional[str] = None
    scenario_guid: Optional[str] = None
    scenario_name: Optional[str] = None
    order: Optional[float] = None
    display_name: Optional[str] = None
    selected_contribution_option_guid: Optional[str] = None
    is_baseline: Optional[bool] = None
    color: Optional[str] = None


class ExhibitData(PlanVantageModel):
    """Full exhibit data."""

    guid: Optional[str] = None
    plan_sponsor_guid: Optional[str] = None
    name: Optional[str] = None
    show_contributions: Optional[bool] = None
    diff_vs_current: Optional[bool] = None
    diff_vs_status_quo: Optional[bool] = None
    scenario_configs: Optional[list[ExhibitScenarioConfigData]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ExhibitInput(PlanVantageModel):
    """Input for creating an exhibit."""

    name: str
    show_contributions: Optional[bool] = None
    diff_vs_current: Optional[bool] = None
    diff_vs_status_quo: Optional[bool] = None
    scenario_guids: Optional[list[str]] = None
    baseline_guid: Optional[str] = None


class ExhibitUpdateInput(PlanVantageModel):
    """Input for updating an exhibit."""

    name: Optional[str] = None
    show_contributions: Optional[bool] = None
    diff_vs_current: Optional[bool] = None
    diff_vs_status_quo: Optional[bool] = None


class ExhibitScenarioInput(PlanVantageModel):
    """Input for adding a scenario to an exhibit."""

    scenario_guid: str
    order: Optional[float] = None
    display_name: Optional[str] = None
    selected_contribution_option_guid: Optional[str] = None
    is_baseline: Optional[bool] = None
    color: Optional[str] = None


class ExhibitScenarioUpdateInput(PlanVantageModel):
    """Input for updating a scenario config in an exhibit."""

    order: Optional[float] = None
    display_name: Optional[str] = None
    selected_contribution_option_guid: Optional[str] = None
    is_baseline: Optional[bool] = None
    color: Optional[str] = None


class ExhibitApplyContributionInput(PlanVantageModel):
    """Input for applying a contribution option to all scenarios."""

    contribution_option_guid: str


class ContributionOptionInfo(PlanVantageModel):
    """Basic info about a contribution option."""

    guid: Optional[str] = None
    name: Optional[str] = None


class SummaryContributionData(PlanVantageModel):
    """Contribution summary data."""

    option_guid: Optional[str] = None
    option_name: Optional[str] = None
    current_employee_contrib: Optional[float] = None
    status_quo_employee_contrib: Optional[float] = None
    proposed_employee_contrib: Optional[float] = None
    current_employer_cost: Optional[float] = None
    status_quo_employer_cost: Optional[float] = None
    proposed_employer_cost: Optional[float] = None


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


class ExhibitColumnData(PlanVantageModel):
    """Calculated data for a single scenario column in an exhibit."""

    config_guid: Optional[str] = None
    scenario_guid: Optional[str] = None
    display_name: Optional[str] = None
    order: Optional[float] = None
    is_baseline: Optional[bool] = None
    color: Optional[str] = None
    fixed_cost_line_items: Optional[list[FixedCostLineItemData]] = None
    total_enrollment: Optional[int] = None
    total_net_claims: Optional[float] = None
    total_fixed_costs: Optional[float] = None
    total_cost: Optional[float] = None
    cost_pepm: Optional[float] = None
    total_current_cost: Optional[float] = None
    total_status_quo_cost: Optional[float] = None
    contribution: Optional[SummaryContributionData] = None
    diff_vs_current_amount: Optional[float] = None
    diff_vs_current_pct: Optional[float] = None
    diff_vs_status_quo_amount: Optional[float] = None
    diff_vs_status_quo_pct: Optional[float] = None
    calculated_hsa: Optional[float] = None
    has_baseline_mismatch: Optional[bool] = None
    mismatch_warning: Optional[str] = None


class ExhibitFixedCostCellData(PlanVantageModel):
    """A single cell in the exhibit fixed cost grid."""

    scenario_guid: Optional[str] = None
    line_item_guid: Optional[str] = None
    value: Optional[float] = None
    is_auto_calc: Optional[bool] = None
    pepm_calc_active: Optional[bool] = None
    current_pepm: Optional[float] = None
    proposed_pepm: Optional[float] = None


class ExhibitFixedCostRowData(PlanVantageModel):
    """One merged row across all scenarios in the exhibit."""

    name: Optional[str] = None
    order: Optional[int] = None
    cells: Optional[dict[str, ExhibitFixedCostCellData]] = None


class ExhibitTableData(PlanVantageModel):
    """Complete calculated exhibit table data."""

    exhibit_guid: Optional[str] = None
    exhibit_name: Optional[str] = None
    plan_sponsor_guid: Optional[str] = None
    plan_sponsor_name: Optional[str] = None
    settings: Optional[Any] = None  # ExhibitSettingsData
    show_contributions: Optional[bool] = None
    diff_vs_current: Optional[bool] = None
    diff_vs_status_quo: Optional[bool] = None
    current_column: Optional[ExhibitColumnData] = None
    status_quo_column: Optional[ExhibitColumnData] = None
    scenario_columns: Optional[list[ExhibitColumnData]] = None
    fixed_cost_rows: Optional[list[ExhibitFixedCostRowData]] = None
    has_status_quo: Optional[bool] = None
    available_scenarios: Optional[list[Any]] = None
    available_contribution_options: Optional[dict[str, list[ContributionOptionInfo]]] = None


class ExhibitFixedCostRowInput(PlanVantageModel):
    """Input for adding a fixed cost row to an exhibit."""

    name: str


class ExhibitFixedCostReorderInput(PlanVantageModel):
    """Input for reordering fixed cost rows."""

    names: list[str]


class ExhibitPEPMInput(PlanVantageModel):
    """Input for applying PEPM across all scenarios."""

    name: str
    current_pepm: Optional[float] = None
    proposed_pepm: Optional[float] = None


class ExhibitSettingsData(PlanVantageModel):
    """Exhibit settings data."""

    guid: Optional[str] = None
    exhibit_guid: Optional[str] = None
    show_status_quo_column: Optional[bool] = None
    show_enrollment: Optional[bool] = None
    show_pepm: Optional[bool] = None
    show_contributions: Optional[bool] = None
    show_change_vs_current: Optional[bool] = None
    show_change_vs_sq: Optional[bool] = None
    show_dollar_diff: Optional[bool] = None
    show_percent_diff: Optional[bool] = None
    show_pepm_ee_contrib: Optional[bool] = None
    show_pepm_er_cost: Optional[bool] = None
    show_pepm_change_vs_current: Optional[bool] = None
    show_pepm_change_vs_sq: Optional[bool] = None
    show_pepm_dollar_diff: Optional[bool] = None
    show_pepm_percent_diff: Optional[bool] = None
    show_cost_share_pct: Optional[bool] = None
    show_ee_cost_share_pct: Optional[bool] = None
    show_er_cost_share_pct: Optional[bool] = None
    show_contribution_change_vs_current: Optional[bool] = None
    show_contribution_change_vs_sq: Optional[bool] = None
    show_renewal_options_label: Optional[bool] = None
    renewal_options_label: Optional[str] = None
    status_quo_contribution_method: Optional[str] = None
