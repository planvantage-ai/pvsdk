"""AV Models resource."""

from typing import Any, Optional

from planvantage.models.avmodel import (
    AVModelData,
    AVModelInput,
)
from planvantage.models.folder import MoveItemToFolderInput
from planvantage.models.plandesign import CopyPlanDesignRequest, PlanDesignData
from planvantage.resources.base import BaseResource


class AVModelsResource(BaseResource):
    """Resource for managing actuarial value models."""

    def get(self, guid: str) -> AVModelData:
        """Get a specific AV model by GUID.

        Args:
            guid: The AV model's unique identifier.

        Returns:
            Full AV model data including plan designs.

        Example:
            >>> model = client.avmodels.get("av_abc123")
            >>> print(model.name)
        """
        data = self._http.get(f"/avmodel/{guid}")
        return AVModelData.model_validate(data)

    def create(
        self,
        plan_sponsor_guid: str,
        name: Optional[str] = None,
    ) -> AVModelData:
        """Create a new AV model for a plan sponsor.

        Args:
            plan_sponsor_guid: The plan sponsor's GUID.
            name: Optional name for the AV model.

        Returns:
            Created AV model data.

        Example:
            >>> model = client.avmodels.create(
            ...     plan_sponsor_guid="ps_abc123",
            ...     name="2024 Plan Analysis"
            ... )
        """
        data = self._http.post(
            f"/plansponsor/{plan_sponsor_guid}/avmodel",
            json={"name": name} if name else {},
        )
        return AVModelData.model_validate(data)

    def update(
        self,
        guid: str,
        name: Optional[str] = None,
        **kwargs: Any,
    ) -> AVModelData:
        """Update an AV model.

        Args:
            guid: The AV model's unique identifier.
            name: New name for the AV model.
            **kwargs: Additional fields to update.

        Returns:
            Updated AV model data.

        Example:
            >>> model = client.avmodels.update("av_abc123", name="Updated Analysis")
        """
        request = AVModelInput(name=name, **kwargs)
        data = self._http.patch(f"/avmodel/{guid}", json=self._serialize(request))
        return AVModelData.model_validate(data)

    def delete(self, guid: str) -> None:
        """Delete an AV model.

        Args:
            guid: The AV model's unique identifier.

        Example:
            >>> client.avmodels.delete("av_abc123")
        """
        self._http.delete(f"/avmodel/{guid}")

    def clone(self, guid: str) -> AVModelData:
        """Clone an AV model.

        Args:
            guid: The AV model's unique identifier.

        Returns:
            Cloned AV model data.

        Example:
            >>> cloned = client.avmodels.clone("av_abc123")
        """
        data = self._http.post(f"/avmodel/{guid}/clone")
        return AVModelData.model_validate(data)

    def move_to_folder(
        self,
        guid: str,
        folder_guid: Optional[str] = None,
    ) -> AVModelData:
        """Move an AV model to a folder.

        Args:
            guid: The AV model's unique identifier.
            folder_guid: Target folder GUID, or None for root.

        Returns:
            Updated AV model data.

        Example:
            >>> client.avmodels.move_to_folder("av_abc123", "folder_xyz")
        """
        request = MoveItemToFolderInput(folder_guid=folder_guid)
        data = self._http.patch(f"/avmodel/{guid}/folder", json=self._serialize(request))
        return AVModelData.model_validate(data)

    def create_plan_design(
        self,
        guid: str,
        **kwargs: Any,
    ) -> PlanDesignData:
        """Create a plan design within an AV model.

        Args:
            guid: The AV model's unique identifier.
            **kwargs: Plan design fields.

        Returns:
            Created plan design data.

        Example:
            >>> plan = client.avmodels.create_plan_design(
            ...     "av_abc123",
            ...     name="Gold PPO"
            ... )
        """
        data = self._http.post(f"/avmodel/{guid}/plandesign", json=kwargs)
        return PlanDesignData.model_validate(data)

    def copy_plan_design(
        self,
        guid: str,
        source_plan_design_guid: str,
    ) -> PlanDesignData:
        """Copy an existing plan design into an AV model.

        Args:
            guid: The AV model's unique identifier.
            source_plan_design_guid: GUID of the plan design to copy.

        Returns:
            Copied plan design data.

        Example:
            >>> plan = client.avmodels.copy_plan_design("av_abc", "pd_xyz")
        """
        request = CopyPlanDesignRequest(source_plan_design_guid=source_plan_design_guid)
        data = self._http.post(
            f"/avmodel/{guid}/plandesign/copy",
            json=self._serialize(request),
        )
        return PlanDesignData.model_validate(data)
