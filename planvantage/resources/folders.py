"""Folders resource."""

from typing import Any, Optional

from planvantage.models.folder import (
    BulkCloneInput,
    BulkDeleteInput,
    BulkMoveInput,
    BulkOperationResult,
    CreateFolderInput,
    FolderContents,
    FolderInfo,
    MoveFolderInput,
    UpdateFolderInput,
)
from planvantage.resources.base import BaseResource


class FoldersResource(BaseResource):
    """Resource for managing folders."""

    def get(self, guid: str) -> FolderInfo:
        """Get a specific folder by GUID.

        Args:
            guid: The folder's unique identifier.

        Returns:
            Folder information.

        Example:
            >>> folder = client.folders.get("folder_abc123")
            >>> print(folder.name)
        """
        data = self._http.get(f"/folder/{guid}")
        return FolderInfo.model_validate(data)

    def list_contents(
        self,
        plan_sponsor_guid: str,
        module: str,
        folder_guid: Optional[str] = None,
        page: int = 1,
        page_size: int = 50,
    ) -> FolderContents:
        """List contents of a folder.

        Args:
            plan_sponsor_guid: The plan sponsor's GUID.
            module: Module name (scenarios, dashboards, projections, etc.).
            folder_guid: Folder GUID, or None for root.
            page: Page number (1-indexed).
            page_size: Items per page.

        Returns:
            Folder contents including subfolders and items.

        Example:
            >>> contents = client.folders.list_contents(
            ...     plan_sponsor_guid="ps_abc",
            ...     module="scenarios"
            ... )
            >>> for item in contents.items:
            ...     print(item.name)
        """
        params = {
            "page": page,
            "pageSize": page_size,
        }
        if folder_guid:
            path = f"/plansponsor/{plan_sponsor_guid}/{module}/folder/{folder_guid}"
        else:
            path = f"/plansponsor/{plan_sponsor_guid}/{module}/folder"
        data = self._http.get(path, params=params)
        return FolderContents.model_validate(data)

    def create(
        self,
        plan_sponsor_guid: str,
        module: str,
        name: str,
        parent_guid: Optional[str] = None,
    ) -> FolderInfo:
        """Create a new folder.

        Args:
            plan_sponsor_guid: The plan sponsor's GUID.
            module: Module name.
            name: Folder name.
            parent_guid: Parent folder GUID, or None for root.

        Returns:
            Created folder information.

        Example:
            >>> folder = client.folders.create(
            ...     plan_sponsor_guid="ps_abc",
            ...     module="scenarios",
            ...     name="2024 Renewals"
            ... )
        """
        request = CreateFolderInput(
            plan_sponsor_guid=plan_sponsor_guid,
            name=name,
            module=module,
            parent_guid=parent_guid,
        )
        data = self._http.post("/folder", json=self._serialize(request))
        return FolderInfo.model_validate(data)

    def update(
        self,
        guid: str,
        name: str,
    ) -> FolderInfo:
        """Update a folder.

        Args:
            guid: The folder's unique identifier.
            name: New folder name.

        Returns:
            Updated folder information.

        Example:
            >>> folder = client.folders.update("folder_abc", name="Archived")
        """
        request = UpdateFolderInput(name=name)
        data = self._http.patch(f"/folder/{guid}", json=self._serialize(request))
        return FolderInfo.model_validate(data)

    def delete(self, guid: str) -> None:
        """Delete a folder.

        Args:
            guid: The folder's unique identifier.

        Example:
            >>> client.folders.delete("folder_abc123")
        """
        self._http.delete(f"/folder/{guid}")

    def move(
        self,
        guid: str,
        parent_guid: Optional[str] = None,
    ) -> FolderInfo:
        """Move a folder to a new parent.

        Args:
            guid: The folder's unique identifier.
            parent_guid: New parent folder GUID, or None for root.

        Returns:
            Updated folder information.

        Example:
            >>> folder = client.folders.move("folder_abc", parent_guid="folder_xyz")
        """
        request = MoveFolderInput(parent_guid=parent_guid)
        data = self._http.patch(f"/folder/{guid}/move", json=self._serialize(request))
        return FolderInfo.model_validate(data)

    def bulk_move(
        self,
        plan_sponsor_guid: str,
        module: str,
        guids: list[str],
        target_folder_guid: Optional[str] = None,
    ) -> BulkOperationResult:
        """Move multiple items to a folder.

        Args:
            plan_sponsor_guid: The plan sponsor's GUID.
            module: Module name.
            guids: List of item GUIDs to move.
            target_folder_guid: Target folder GUID, or None for root.

        Returns:
            Result of the bulk operation.

        Example:
            >>> result = client.folders.bulk_move(
            ...     plan_sponsor_guid="ps_abc",
            ...     module="scenarios",
            ...     guids=["sc_1", "sc_2"],
            ...     target_folder_guid="folder_xyz"
            ... )
        """
        request = BulkMoveInput(guids=guids, target_folder_guid=target_folder_guid)
        data = self._http.post(
            f"/plansponsor/{plan_sponsor_guid}/{module}/bulk/move",
            json=self._serialize(request),
        )
        return BulkOperationResult.model_validate(data)

    def bulk_delete(
        self,
        plan_sponsor_guid: str,
        module: str,
        guids: list[str],
    ) -> BulkOperationResult:
        """Delete multiple items.

        Args:
            plan_sponsor_guid: The plan sponsor's GUID.
            module: Module name.
            guids: List of item GUIDs to delete.

        Returns:
            Result of the bulk operation.

        Example:
            >>> result = client.folders.bulk_delete(
            ...     plan_sponsor_guid="ps_abc",
            ...     module="scenarios",
            ...     guids=["sc_1", "sc_2"]
            ... )
        """
        request = BulkDeleteInput(guids=guids)
        data = self._http.post(
            f"/plansponsor/{plan_sponsor_guid}/{module}/bulk/delete",
            json=self._serialize(request),
        )
        return BulkOperationResult.model_validate(data)

    def bulk_clone(
        self,
        plan_sponsor_guid: str,
        module: str,
        guids: list[str],
    ) -> BulkOperationResult:
        """Clone multiple items.

        Args:
            plan_sponsor_guid: The plan sponsor's GUID.
            module: Module name.
            guids: List of item GUIDs to clone.

        Returns:
            Result of the bulk operation.

        Example:
            >>> result = client.folders.bulk_clone(
            ...     plan_sponsor_guid="ps_abc",
            ...     module="scenarios",
            ...     guids=["sc_1", "sc_2"]
            ... )
        """
        request = BulkCloneInput(guids=guids)
        data = self._http.post(
            f"/plansponsor/{plan_sponsor_guid}/{module}/bulk/clone",
            json=self._serialize(request),
        )
        return BulkOperationResult.model_validate(data)
