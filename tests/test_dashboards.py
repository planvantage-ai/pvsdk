"""Tests for Dashboards resource."""

from typing import Any

import pytest
import respx
from httpx import Response

from planvantage import PlanVantageClient
from planvantage.models.dashboard import DashboardData


class TestDashboardsResource:
    """Tests for DashboardsResource."""

    def test_get_dashboard(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_dashboard_data: dict[str, Any],
    ) -> None:
        """Test getting a single dashboard."""
        mock_api.get("/dashboard/db_test123").mock(
            return_value=Response(200, json=sample_dashboard_data)
        )

        dashboard = client.dashboards.get("db_test123")

        assert isinstance(dashboard, DashboardData)
        assert dashboard.guid == "db_test123"
        assert dashboard.name == "Experience Dashboard"

    def test_create_dashboard(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_dashboard_data: dict[str, Any],
    ) -> None:
        """Test creating a dashboard."""
        mock_api.post("/dashboard").mock(
            return_value=Response(201, json=sample_dashboard_data)
        )

        dashboard = client.dashboards.create(
            plan_sponsor_guid="ps_test123",
            name="Experience Dashboard",
        )

        assert isinstance(dashboard, DashboardData)
        assert dashboard.name == "Experience Dashboard"

    def test_update_dashboard(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
    ) -> None:
        """Test updating a dashboard."""
        updated_data = {
            "guid": "db_test123",
            "name": "Updated Dashboard",
        }
        mock_api.patch("/dashboard/db_test123").mock(
            return_value=Response(200, json=updated_data)
        )

        dashboard = client.dashboards.update("db_test123", name="Updated Dashboard")

        assert isinstance(dashboard, DashboardData)
        assert dashboard.name == "Updated Dashboard"

    def test_delete_dashboard(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
    ) -> None:
        """Test deleting a dashboard."""
        mock_api.delete("/dashboard/db_test123").mock(
            return_value=Response(204)
        )

        client.dashboards.delete("db_test123")

    def test_clone_dashboard(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_dashboard_data: dict[str, Any],
    ) -> None:
        """Test cloning a dashboard."""
        cloned_data = {**sample_dashboard_data, "guid": "db_cloned123"}
        mock_api.post("/dashboard/db_test123/clone").mock(
            return_value=Response(201, json=cloned_data)
        )

        cloned = client.dashboards.clone("db_test123")

        assert isinstance(cloned, DashboardData)
        assert cloned.guid == "db_cloned123"
