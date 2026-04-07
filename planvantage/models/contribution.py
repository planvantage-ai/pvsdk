"""Contribution models."""

from datetime import datetime
from typing import Any, Optional

from planvantage.models.base import PlanVantageModel


class CensusFilterRule(PlanVantageModel):
    """A single criterion used to match census rows to a contribution group."""

    column: Optional[str] = None
    operator: Optional[str] = None  # "equals", "in", "less_than", "greater_than", "between"
    value: Optional[Any] = None


class ContributionGroupCriteria(PlanVantageModel):
    """Census criteria attached to a contribution group."""

    rules: Optional[list[CensusFilterRule]] = None
    rule_mode: Optional[str] = None  # "and" (default) or "or"


class ContributionTierData(PlanVantageModel):
    """Contribution tier data (shared by current and proposed)."""

    guid: Optional[str] = None
    rate_plan_tier_guid: Optional[str] = None
    order: Optional[float] = None
    tier_name: Optional[str] = None
    hsa_amount: Optional[float] = None
    rate: Optional[float] = None
    contribution: Optional[float] = None
    enrollment: Optional[int] = None


class ContributionPlanData(PlanVantageModel):
    """Contribution plan data (one rate plan inside a contribution group)."""

    contribution_group_guid: Optional[str] = None
    rate_plan_guid: Optional[str] = None
    plan_design_guid: Optional[str] = None
    plan_name: Optional[str] = None
    plan_color: Optional[str] = None
    order: Optional[float] = None
    tiers: Optional[list[ContributionTierData]] = None


class ContributionGroupData(PlanVantageModel):
    """Contribution group data (shared by current and proposed)."""

    guid: Optional[str] = None
    contribution_option_guid: Optional[str] = None
    name: Optional[str] = None
    order: Optional[float] = None
    plans: Optional[list[ContributionPlanData]] = None
    census_criteria: Optional[ContributionGroupCriteria] = None
    matched_census_count: Optional[int] = None
    needs_criteria_reset: Optional[bool] = None
    enrollment_status: Optional[str] = None  # "match", "overridden", "faulty"


class ContributionOptionData(PlanVantageModel):
    """Contribution option data."""

    guid: Optional[str] = None
    scenario_guid: Optional[str] = None
    name: Optional[str] = None
    order: Optional[float] = None
    prompt: Optional[str] = None
    ai_calc_enabled: Optional[bool] = None
    change_since_prompt: Optional[bool] = None
    change_since_ignore: Optional[bool] = None
    processing_status: Optional[str] = None  # pending|processing_groups|processing|success|failed|canceled
    processing_error: Optional[str] = None
    comparison_group_guid: Optional[str] = None
    groups: Optional[list[ContributionGroupData]] = None


class ContributionTierEnrollmentUpdateData(PlanVantageModel):
    """Data for updating contribution tier enrollment."""

    guid: str
    enrollment: int


class ContributionOptionItem(PlanVantageModel):
    """Contribution option library item."""

    key: Optional[str] = None
    name: Optional[str] = None
    prompt: Optional[str] = None


class ContributionOptionImportItem(PlanVantageModel):
    """Item for importing contribution options from another scenario."""

    name: Optional[str] = None
    prompt: Optional[str] = None
    source_option_guid: Optional[str] = None


class ScenarioOptionItems(PlanVantageModel):
    """Contribution options grouped under a scenario in the library view."""

    scenario_guid: Optional[str] = None
    scenario_name: Optional[str] = None
    contribution_options: Optional[list[ContributionOptionItem]] = None


class PlanSponsorItems(PlanVantageModel):
    """Plan sponsor library entry containing scenarios with contribution options."""

    plan_sponsor_guid: Optional[str] = None
    plan_sponsor_name: Optional[str] = None
    scenarios: Optional[list[ScenarioOptionItems]] = None


class ContributionOptionItemsLists(PlanVantageModel):
    """Container returned by /proposedcontributionoption/items.

    ``standard`` holds the built-in option templates; ``library`` holds
    options reusable from other scenarios in the user's plan sponsors.
    """

    standard: Optional[list[ContributionOptionItem]] = None
    library: Optional[list[PlanSponsorItems]] = None


# The proposed-side classes share field shapes with the current-side classes.
# They exist as distinct types so callers can express intent clearly and so
# any future divergence has a place to land.

ProposedContributionGroupData = ContributionGroupData
ProposedContributionTierData = ContributionTierData


class ProposedContributionGroupInput(PlanVantageModel):
    """Input for creating proposed contribution group."""

    contribution_option_guid: str
    name: Optional[str] = None
    order: Optional[float] = None


class ProposedContributionTierInput(PlanVantageModel):
    """Input for updating proposed contribution tier."""

    contribution: Optional[float] = None
    enrollment: Optional[int] = None
    hsa_amount: Optional[float] = None


class ProposedContributionTierEnrollmentUpdate(PlanVantageModel):
    """Enrollment update for proposed contribution tier."""

    guid: str
    enrollment: int


class ProposedContributionOptionStatusData(PlanVantageModel):
    """Status data for proposed contribution option."""

    guid: Optional[str] = None
    status: Optional[str] = None
    is_calculating: Optional[bool] = None
    calc_error: Optional[str] = None
    calc_warning: Optional[str] = None
    calc_hash: Optional[str] = None
    updated_at: Optional[datetime] = None
