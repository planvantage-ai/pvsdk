"""API Keys resource."""

from typing import Optional

from planvantage.models.user import (
    ApiKey,
    CreateApiKeyRequest,
    CreateApiKeyResponse,
    RevokeApiKeyRequest,
)
from planvantage.resources.base import BaseResource


class ApiKeysResource(BaseResource):
    """Resource for managing API keys."""

    def list(self) -> list[ApiKey]:
        """List all API keys for the authenticated user.

        Returns:
            List of API key information (without the actual key values).

        Example:
            >>> keys = client.apikeys.list()
            >>> for key in keys:
            ...     print(f"{key.name}: {key.key_prefix}")
        """
        data = self._http.get("/apikeys")
        if isinstance(data, dict) and "api_keys" in data:
            return [ApiKey.model_validate(item) for item in data["api_keys"]]
        return []

    def create(
        self,
        name: str,
        expires_in: Optional[int] = None,
    ) -> CreateApiKeyResponse:
        """Create a new API key.

        Args:
            name: A descriptive name for the API key.
            expires_in: Optional number of days until the key expires.

        Returns:
            Response containing the new API key (shown only once).

        Example:
            >>> response = client.apikeys.create(
            ...     name="Production API Key",
            ...     expires_in=365
            ... )
            >>> print(f"New key: {response.key}")
        """
        request = CreateApiKeyRequest(name=name, expires_in=expires_in)
        data = self._http.post("/apikeys", json=self._serialize(request))
        return CreateApiKeyResponse.model_validate(data)

    def revoke(self, guid: str) -> None:
        """Revoke an API key.

        The key will immediately stop working but remains in the list
        as inactive for record-keeping purposes.

        Args:
            guid: The API key's unique identifier.

        Example:
            >>> client.apikeys.revoke("key_abc123")
        """
        request = RevokeApiKeyRequest(guid=guid)
        self._http.post("/apikeys/revoke", json=self._serialize(request))

    def delete(self, guid: str) -> None:
        """Permanently delete an API key.

        Args:
            guid: The API key's unique identifier.

        Example:
            >>> client.apikeys.delete("key_abc123")
        """
        self._http.delete(f"/apikeys/{guid}")
