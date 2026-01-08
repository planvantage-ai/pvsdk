"""Tests for Projections resource."""

from typing import Any

import pytest
import respx
from httpx import Response

from planvantage import PlanVantageClient
from planvantage.models.projection import ProjectionData


class TestProjectionsResource:
    """Tests for ProjectionsResource."""

    def test_get_projection(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_projection_data: dict[str, Any],
    ) -> None:
        """Test getting a single projection."""
        mock_api.get("/projection/proj_test123").mock(
            return_value=Response(200, json=sample_projection_data)
        )

        projection = client.projections.get("proj_test123")

        assert isinstance(projection, ProjectionData)
        assert projection.guid == "proj_test123"
        assert projection.name == "2024 Renewal Projection"

    def test_create_projection(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_projection_data: dict[str, Any],
    ) -> None:
        """Test creating a projection."""
        mock_api.post("/projection").mock(
            return_value=Response(201, json=sample_projection_data)
        )

        projection = client.projections.create(
            plan_sponsor_guid="ps_test123",
            name="2024 Renewal Projection",
        )

        assert isinstance(projection, ProjectionData)
        assert projection.name == "2024 Renewal Projection"

    def test_update_projection(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
    ) -> None:
        """Test updating a projection."""
        updated_data = {
            "guid": "proj_test123",
            "name": "Updated Projection",
        }
        mock_api.patch("/projection/proj_test123").mock(
            return_value=Response(200, json=updated_data)
        )

        projection = client.projections.update("proj_test123", name="Updated Projection")

        assert isinstance(projection, ProjectionData)
        assert projection.name == "Updated Projection"

    def test_delete_projection(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
    ) -> None:
        """Test deleting a projection."""
        mock_api.delete("/projection/proj_test123").mock(
            return_value=Response(204)
        )

        client.projections.delete("proj_test123")

    def test_clone_projection(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_projection_data: dict[str, Any],
    ) -> None:
        """Test cloning a projection."""
        cloned_data = {**sample_projection_data, "guid": "proj_cloned123"}
        mock_api.post("/projection/proj_test123/clone").mock(
            return_value=Response(201, json=cloned_data)
        )

        cloned = client.projections.clone("proj_test123")

        assert isinstance(cloned, ProjectionData)
        assert cloned.guid == "proj_cloned123"

    def test_import_from_dashboard(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_projection_data: dict[str, Any],
    ) -> None:
        """Test importing from dashboard."""
        mock_api.post("/projection/proj_test123/import-dashboard").mock(
            return_value=Response(200, json=sample_projection_data)
        )

        projection = client.projections.import_from_dashboard(
            "proj_test123",
            dashboard_version_guid="dbv_test123",
        )

        assert isinstance(projection, ProjectionData)
