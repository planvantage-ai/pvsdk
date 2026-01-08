"""Tests for AVModels resource."""

from typing import Any

import pytest
import respx
from httpx import Response

from planvantage import PlanVantageClient
from planvantage.models.avmodel import AVModelData


class TestAVModelsResource:
    """Tests for AVModelsResource."""

    def test_get_avmodel(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_avmodel_data: dict[str, Any],
    ) -> None:
        """Test getting a single AV model."""
        mock_api.get("/avmodel/av_test123").mock(
            return_value=Response(200, json=sample_avmodel_data)
        )

        avmodel = client.avmodels.get("av_test123")

        assert isinstance(avmodel, AVModelData)
        assert avmodel.guid == "av_test123"
        assert avmodel.name == "Plan Analysis"

    def test_create_avmodel(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_avmodel_data: dict[str, Any],
    ) -> None:
        """Test creating an AV model."""
        mock_api.post("/plansponsor/ps_test123/avmodel").mock(
            return_value=Response(201, json=sample_avmodel_data)
        )

        avmodel = client.avmodels.create(
            plan_sponsor_guid="ps_test123",
            name="Plan Analysis",
        )

        assert isinstance(avmodel, AVModelData)
        assert avmodel.name == "Plan Analysis"

    def test_update_avmodel(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
    ) -> None:
        """Test updating an AV model."""
        updated_data = {
            "guid": "av_test123",
            "name": "Updated Analysis",
        }
        mock_api.patch("/avmodel/av_test123").mock(
            return_value=Response(200, json=updated_data)
        )

        avmodel = client.avmodels.update("av_test123", name="Updated Analysis")

        assert isinstance(avmodel, AVModelData)
        assert avmodel.name == "Updated Analysis"

    def test_delete_avmodel(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
    ) -> None:
        """Test deleting an AV model."""
        mock_api.delete("/avmodel/av_test123").mock(
            return_value=Response(204)
        )

        client.avmodels.delete("av_test123")

    def test_clone_avmodel(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_avmodel_data: dict[str, Any],
    ) -> None:
        """Test cloning an AV model."""
        cloned_data = {**sample_avmodel_data, "guid": "av_cloned123"}
        mock_api.post("/avmodel/av_test123/clone").mock(
            return_value=Response(201, json=cloned_data)
        )

        cloned = client.avmodels.clone("av_test123")

        assert isinstance(cloned, AVModelData)
        assert cloned.guid == "av_cloned123"
