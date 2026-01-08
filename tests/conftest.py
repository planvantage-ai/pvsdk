"""Test fixtures for PlanVantage SDK tests."""

from typing import Any, Generator
from unittest.mock import MagicMock

import pytest
import respx
from httpx import Response

from planvantage import PlanVantageClient
from planvantage.auth import AuthConfig
from planvantage.http import HTTPClient


@pytest.fixture
def api_key() -> str:
    """Test API key."""
    return "pk_test_12345"


@pytest.fixture
def base_url() -> str:
    """Test base URL."""
    return "https://api.test.planvantage.ai"


@pytest.fixture
def auth_config(api_key: str, base_url: str) -> AuthConfig:
    """Test auth configuration."""
    return AuthConfig(api_key=api_key, base_url=base_url)


@pytest.fixture
def http_client(auth_config: AuthConfig) -> Generator[HTTPClient, None, None]:
    """Test HTTP client."""
    client = HTTPClient(auth=auth_config)
    yield client
    client.close()


@pytest.fixture
def client(api_key: str, base_url: str) -> Generator[PlanVantageClient, None, None]:
    """Test PlanVantage client."""
    client = PlanVantageClient(api_key=api_key, base_url=base_url)
    yield client
    client.close()


@pytest.fixture
def mock_api(base_url: str) -> Generator[respx.MockRouter, None, None]:
    """Mock API responses using respx."""
    with respx.mock(base_url=base_url, assert_all_called=False) as mock:
        yield mock


# Sample test data fixtures

@pytest.fixture
def sample_plansponsor_data() -> dict[str, Any]:
    """Sample plan sponsor data."""
    return {
        "guid": "ps_test123",
        "name": "Acme Corporation",
        "scenarios": [],
        "plan_documents": [],
    }


@pytest.fixture
def sample_plansponsor_list() -> list[dict[str, Any]]:
    """Sample list of plan sponsors."""
    return [
        {
            "guid": "ps_test123",
            "name": "Acme Corporation",
            "updated_at": "2024-01-15T10:30:00Z",
        },
        {
            "guid": "ps_test456",
            "name": "Tech Startup Inc",
            "updated_at": "2024-01-14T09:00:00Z",
        },
    ]


@pytest.fixture
def sample_scenario_data() -> dict[str, Any]:
    """Sample scenario data."""
    return {
        "guid": "sc_test123",
        "name": "2024 Renewal Analysis",
        "order": 1.0,
    }


@pytest.fixture
def sample_plandesign_data() -> dict[str, Any]:
    """Sample plan design data."""
    return {
        "guid": "pd_test123",
        "scenario_guid": "sc_test123",
        "name": "Gold PPO",
        "carrier": "Blue Cross",
        "order": 1.0,
        "tiers": [
            {
                "guid": "pdt_test1",
                "plan_design_guid": "pd_test123",
                "name": "Employee Only",
                "ind_ded": 500.0,
                "fam_ded": 1000.0,
            },
        ],
    }


@pytest.fixture
def sample_rateplan_data() -> dict[str, Any]:
    """Sample rate plan data."""
    return {
        "guid": "rp_test123",
        "scenario_guid": "sc_test123",
        "plan_design_guid": "pd_test123",
        "name": "Gold PPO Rates",
        "rate_method": "tierRates",
        "tiers": [
            {
                "guid": "rpt_test1",
                "rate_plan_guid": "rp_test123",
                "name": "Employee Only",
                "rate": 450.00,
                "enrollment": 50,
            },
        ],
    }


@pytest.fixture
def sample_dashboard_data() -> dict[str, Any]:
    """Sample dashboard data."""
    return {
        "guid": "db_test123",
        "name": "Experience Dashboard",
        "plan_sponsor_guid": "ps_test123",
        "plans": [],
        "versions": [],
    }


@pytest.fixture
def sample_projection_data() -> dict[str, Any]:
    """Sample projection data."""
    return {
        "guid": "proj_test123",
        "name": "2024 Renewal Projection",
        "plan_sponsor_guid": "ps_test123",
        "plans": [],
    }


@pytest.fixture
def sample_quoteset_data() -> dict[str, Any]:
    """Sample quote set data."""
    return {
        "guid": "qs_test123",
        "name": "Carrier Quotes",
        "plan_sponsor_guid": "ps_test123",
        "quotes": [],
        "documents": [],
    }


@pytest.fixture
def sample_avmodel_data() -> dict[str, Any]:
    """Sample AV model data."""
    return {
        "guid": "av_test123",
        "name": "Plan Analysis",
        "plan_sponsor_guid": "ps_test123",
        "plan_designs": [],
    }


@pytest.fixture
def sample_folder_data() -> dict[str, Any]:
    """Sample folder data."""
    return {
        "guid": "folder_test123",
        "name": "2024 Renewals",
        "parent_guid": None,
        "module": "scenarios",
    }
