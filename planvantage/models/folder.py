"""Folder models."""

from datetime import datetime
from typing import Any, Optional

from planvantage.models.base import PlanVantageModel


class FolderInfo(PlanVantageModel):
    """Summary information about a folder."""

    guid: str
    name: str
    parent_guid: Optional[str] = None
    module: Optional[str] = None
    updated_at: Optional[datetime] = None


class FolderBreadcrumb(PlanVantageModel):
    """Breadcrumb entry for folder navigation."""

    guid: Optional[str] = None
    name: Optional[str] = None


class FolderContents(PlanVantageModel):
    """Contents of a folder."""

    folder: Optional[FolderInfo] = None
    breadcrumbs: Optional[list[FolderBreadcrumb]] = None
    subfolders: Optional[list[FolderInfo]] = None
    items: Optional[list[Any]] = None
    total_items: Optional[int] = None
    page: Optional[int] = None
    page_size: Optional[int] = None


class CreateFolderInput(PlanVantageModel):
    """Input for creating a folder."""

    plan_sponsor_guid: str
    name: str
    module: str
    parent_guid: Optional[str] = None


class UpdateFolderInput(PlanVantageModel):
    """Input for updating a folder."""

    name: Optional[str] = None


class MoveFolderInput(PlanVantageModel):
    """Input for moving a folder."""

    parent_guid: Optional[str] = None


class MoveItemToFolderInput(PlanVantageModel):
    """Input for moving an item to a folder."""

    folder_guid: Optional[str] = None


class BulkMoveInput(PlanVantageModel):
    """Input for bulk moving items."""

    guids: list[str]
    target_folder_guid: Optional[str] = None


class BulkDeleteInput(PlanVantageModel):
    """Input for bulk deleting items."""

    guids: list[str]


class BulkCloneInput(PlanVantageModel):
    """Input for bulk cloning items."""

    guids: list[str]


class BulkOperationResult(PlanVantageModel):
    """Result of a bulk operation."""

    success_count: Optional[int] = None
    failure_count: Optional[int] = None
    failures: Optional[list[dict[str, Any]]] = None
