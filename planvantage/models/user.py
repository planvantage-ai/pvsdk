"""User models."""

from datetime import datetime
from typing import Optional

from planvantage.models.base import PlanVantageModel


class LimitedUserInput(PlanVantageModel):
    """Limited user input for invitations."""

    email: str
    name: Optional[str] = None


class ApiKey(PlanVantageModel):
    """API key information (without the actual key)."""

    guid: str
    name: str
    key_prefix: str
    created_at: datetime
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    is_active: bool
    request_count: int


class CreateApiKeyRequest(PlanVantageModel):
    """Request to create a new API key."""

    name: str
    expires_in: Optional[int] = None  # Days until expiration


class CreateApiKeyResponse(PlanVantageModel):
    """Response from creating an API key (includes the actual key)."""

    guid: str
    name: str
    key: str  # Full key, only shown once
    key_prefix: str
    created_at: datetime
    expires_at: Optional[datetime] = None


class ApiKeyListResponse(PlanVantageModel):
    """Response containing a list of API keys."""

    api_keys: list[ApiKey]


class RevokeApiKeyRequest(PlanVantageModel):
    """Request to revoke an API key."""

    guid: str
