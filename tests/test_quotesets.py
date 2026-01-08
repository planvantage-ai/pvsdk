"""Tests for QuoteSets resource."""

from typing import Any

import pytest
import respx
from httpx import Response

from planvantage import PlanVantageClient
from planvantage.models.quoteset import QuoteSetData


class TestQuoteSetsResource:
    """Tests for QuoteSetsResource."""

    def test_get_quoteset(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_quoteset_data: dict[str, Any],
    ) -> None:
        """Test getting a single quote set."""
        mock_api.get("/quoteset/qs_test123").mock(
            return_value=Response(200, json=sample_quoteset_data)
        )

        quoteset = client.quotesets.get("qs_test123")

        assert isinstance(quoteset, QuoteSetData)
        assert quoteset.guid == "qs_test123"
        assert quoteset.name == "Carrier Quotes"

    def test_create_quoteset(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_quoteset_data: dict[str, Any],
    ) -> None:
        """Test creating a quote set."""
        mock_api.post("/quoteset").mock(
            return_value=Response(201, json=sample_quoteset_data)
        )

        quoteset = client.quotesets.create(
            plan_sponsor_guid="ps_test123",
            name="Carrier Quotes",
        )

        assert isinstance(quoteset, QuoteSetData)
        assert quoteset.name == "Carrier Quotes"

    def test_update_quoteset(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
    ) -> None:
        """Test updating a quote set."""
        updated_data = {
            "guid": "qs_test123",
            "name": "Updated Quotes",
        }
        mock_api.patch("/quoteset/qs_test123").mock(
            return_value=Response(200, json=updated_data)
        )

        quoteset = client.quotesets.update("qs_test123", name="Updated Quotes")

        assert isinstance(quoteset, QuoteSetData)
        assert quoteset.name == "Updated Quotes"

    def test_delete_quoteset(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
    ) -> None:
        """Test deleting a quote set."""
        mock_api.delete("/quoteset/qs_test123").mock(
            return_value=Response(204)
        )

        client.quotesets.delete("qs_test123")

    def test_clone_quoteset(
        self,
        client: PlanVantageClient,
        mock_api: respx.MockRouter,
        sample_quoteset_data: dict[str, Any],
    ) -> None:
        """Test cloning a quote set."""
        cloned_data = {**sample_quoteset_data, "guid": "qs_cloned123"}
        mock_api.post("/quoteset/qs_test123/clone").mock(
            return_value=Response(201, json=cloned_data)
        )

        cloned = client.quotesets.clone("qs_test123")

        assert isinstance(cloned, QuoteSetData)
        assert cloned.guid == "qs_cloned123"
