"""Tests for Folders resource."""

from typing import Any

import pytest
import respx
from httpx import Response

from planvantage import PlanVantageClient
from planvantage.models.folder import FolderContents, FolderInfo


class TestFoldersResource:
    """Tests for FoldersResource."""

    def test_get_folder(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_folder_data: dict[str, Any],
    ) -> None:
        """Test getting a single folder."""
        mock_api.get("/folder/folder_test123").mock(
            return_value=Response(200, json=sample_folder_data)
        )

        folder = client.folders.get("folder_test123")

        assert isinstance(folder, FolderInfo)
        assert folder.guid == "folder_test123"
        assert folder.name == "2024 Renewals"

    def test_list_contents(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
    ) -> None:
        """Test listing folder contents."""
        contents_data = {
            "folder": None,
            "breadcrumbs": [],
            "subfolders": [],
            "items": [],
            "total_items": 0,
            "page": 1,
            "page_size": 50,
        }
        mock_api.get("/plansponsor/ps_test123/scenarios/folder").mock(
            return_value=Response(200, json=contents_data)
        )

        contents = client.folders.list_contents(
            plan_sponsor_guid="ps_test123",
            module="scenarios",
        )

        assert isinstance(contents, FolderContents)

    def test_create_folder(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_folder_data: dict[str, Any],
    ) -> None:
        """Test creating a folder."""
        mock_api.post("/folder").mock(
            return_value=Response(201, json=sample_folder_data)
        )

        folder = client.folders.create(
            plan_sponsor_guid="ps_test123",
            module="scenarios",
            name="2024 Renewals",
        )

        assert isinstance(folder, FolderInfo)
        assert folder.name == "2024 Renewals"

    def test_update_folder(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
    ) -> None:
        """Test updating a folder."""
        updated_data = {
            "guid": "folder_test123",
            "name": "Archived",
        }
        mock_api.patch("/folder/folder_test123").mock(
            return_value=Response(200, json=updated_data)
        )

        folder = client.folders.update("folder_test123", name="Archived")

        assert isinstance(folder, FolderInfo)
        assert folder.name == "Archived"

    def test_delete_folder(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
    ) -> None:
        """Test deleting a folder."""
        mock_api.delete("/folder/folder_test123").mock(
            return_value=Response(204)
        )

        client.folders.delete("folder_test123")

    def test_move_folder(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_folder_data: dict[str, Any],
    ) -> None:
        """Test moving a folder."""
        mock_api.patch("/folder/folder_test123/move").mock(
            return_value=Response(200, json=sample_folder_data)
        )

        folder = client.folders.move("folder_test123", parent_guid="folder_parent")

        assert isinstance(folder, FolderInfo)
