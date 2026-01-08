"""AVModel models."""

from datetime import datetime
from typing import Any, Optional

from planvantage.models.base import PlanVantageModel
from planvantage.models.plandesign import PlanDesignData


class AVModelInfo(PlanVantageModel):
    """Summary information about an AV model."""

    guid: str
    name: str
    plan_sponsor_guid: Optional[str] = None
    folder_guid: Optional[str] = None
    updated_at: Optional[datetime] = None


class AVModelData(PlanVantageModel):
    """Full AV model data."""

    guid: Optional[str] = None
    name: Optional[str] = None
    plan_sponsor_guid: Optional[str] = None
    folder_guid: Optional[str] = None
    plan_designs: Optional[list[PlanDesignData]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class AVModelInput(PlanVantageModel):
    """Input for creating/updating AV model."""

    name: Optional[str] = None
