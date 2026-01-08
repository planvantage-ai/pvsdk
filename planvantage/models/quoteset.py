"""QuoteSet models."""

from datetime import datetime
from typing import Any, Optional

from planvantage.models.base import PlanVantageModel


class QuoteSetInfo(PlanVantageModel):
    """Summary information about a quote set."""

    guid: str
    name: str
    plan_sponsor_guid: Optional[str] = None
    folder_guid: Optional[str] = None
    updated_at: Optional[datetime] = None


class TierLabelData(PlanVantageModel):
    """Tier label configuration."""

    index: Optional[int] = None
    label: Optional[str] = None


class CurrentBaselineData(PlanVantageModel):
    """Current baseline data for quote set."""

    plan_name: Optional[str] = None
    plan_type: Optional[str] = None
    carrier: Optional[str] = None
    funding_type: Optional[str] = None
    tiers: Optional[list[TierLabelData]] = None


class QuoteRowDefData(PlanVantageModel):
    """Quote row definition."""

    row_key: Optional[str] = None
    label: Optional[str] = None
    row_type: Optional[str] = None
    format_type: Optional[str] = None
    is_standard: Optional[bool] = None
    is_visible: Optional[bool] = None
    order: Optional[int] = None


class QuotePlanData(PlanVantageModel):
    """Quote plan data."""

    guid: Optional[str] = None
    quote_guid: Optional[str] = None
    name: Optional[str] = None
    values: Optional[dict[str, Any]] = None


class QuoteData(PlanVantageModel):
    """Quote data."""

    guid: Optional[str] = None
    quote_set_guid: Optional[str] = None
    carrier: Optional[str] = None
    plan_type: Optional[str] = None
    funding_type: Optional[str] = None
    effective_date: Optional[str] = None
    expiration_date: Optional[str] = None
    source_document_guid: Optional[str] = None
    status: Optional[str] = None
    plans: Optional[list[QuotePlanData]] = None
    order: Optional[int] = None


class QuoteDocumentInfo(PlanVantageModel):
    """Quote document summary."""

    guid: str
    quote_set_guid: Optional[str] = None
    filename: str
    status: Optional[str] = None
    file_type: Optional[str] = None
    file_size: Optional[int] = None
    created_at: Optional[datetime] = None


class QuoteDocumentData(PlanVantageModel):
    """Full quote document data."""

    guid: Optional[str] = None
    quote_set_guid: Optional[str] = None
    filename: Optional[str] = None
    status: Optional[str] = None
    file_type: Optional[str] = None
    file_size: Optional[int] = None
    extraction_status: Optional[str] = None
    extraction_error: Optional[str] = None
    extracted_data: Optional[dict[str, Any]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class QuoteSetData(PlanVantageModel):
    """Full quote set data."""

    guid: Optional[str] = None
    name: Optional[str] = None
    plan_sponsor_guid: Optional[str] = None
    folder_guid: Optional[str] = None
    current_baseline: Optional[CurrentBaselineData] = None
    tier_labels: Optional[list[TierLabelData]] = None
    row_defs: Optional[list[QuoteRowDefData]] = None
    quotes: Optional[list[QuoteData]] = None
    documents: Optional[list[QuoteDocumentInfo]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class QuoteSetInput(PlanVantageModel):
    """Input for creating quote set."""

    plan_sponsor_guid: str
    name: Optional[str] = None


class QuoteSetUpdateInput(PlanVantageModel):
    """Input for updating quote set."""

    name: Optional[str] = None
    current_baseline: Optional[CurrentBaselineData] = None
    tier_labels: Optional[list[TierLabelData]] = None


class QuoteSetMoveInput(PlanVantageModel):
    """Input for moving quote set to folder."""

    folder_guid: Optional[str] = None


class QuoteInput(PlanVantageModel):
    """Input for creating quote."""

    carrier: Optional[str] = None
    plan_type: Optional[str] = None
    funding_type: Optional[str] = None
    effective_date: Optional[str] = None
    expiration_date: Optional[str] = None


class QuoteUpdateInput(PlanVantageModel):
    """Input for updating quote."""

    carrier: Optional[str] = None
    plan_type: Optional[str] = None
    funding_type: Optional[str] = None
    effective_date: Optional[str] = None
    expiration_date: Optional[str] = None
    plans: Optional[list[dict[str, Any]]] = None


class QuoteLinkDocumentInput(PlanVantageModel):
    """Input for linking document to quote."""

    document_guid: str


class QuoteRowInput(PlanVantageModel):
    """Input for creating quote row definition."""

    label: str
    row_type: Optional[str] = None
    format_type: Optional[str] = None


class QuoteRowUpdateInput(PlanVantageModel):
    """Input for updating quote row definition."""

    label: Optional[str] = None
    is_visible: Optional[bool] = None
    order: Optional[int] = None


class QuoteRowsReorderInput(PlanVantageModel):
    """Input for reordering quote rows."""

    row_keys: list[str]


class QuotesReorderInput(PlanVantageModel):
    """Input for reordering quotes."""

    quote_guids: list[str]
