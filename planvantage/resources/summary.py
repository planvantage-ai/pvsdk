"""Summary settings and fixed cost resources."""

from typing import Any

from planvantage.models.summary import (
    FixedCostLineItemData,
    FixedCostLineItemInput,
    ImportFixedCostLineItemsInput,
    SummarySettingsData,
    ToggleAutoCalcInput,
)
from planvantage.resources.base import BaseResource


class SummarySettingsResource(BaseResource):
    """Resource for managing summary settings."""

    def get(self, guid: str) -> SummarySettingsData:
        """Get summary settings.

        Args:
            guid: The summary settings' unique identifier.

        Returns:
            Summary settings data.
        """
        data = self._http.get(f"/summarysettings/{guid}")
        return SummarySettingsData.model_validate(data)

    def update(self, guid: str, **kwargs: Any) -> SummarySettingsData:
        """Update summary settings.

        Args:
            guid: The summary settings' unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated summary settings data.
        """
        data = self._http.patch(f"/summarysettings/{guid}", json=kwargs)
        return SummarySettingsData.model_validate(data)


class FixedCostsResource(BaseResource):
    """Resource for managing scenario fixed cost line items."""

    def create(
        self,
        scenario_guid: str,
        name: str,
        **kwargs: Any,
    ) -> FixedCostLineItemData:
        """Create a fixed cost line item.

        Args:
            scenario_guid: The scenario's GUID.
            name: Name of the line item.
            **kwargs: Additional fields.

        Returns:
            Created line item data.
        """
        request = FixedCostLineItemInput(name=name, **kwargs)
        data = self._http.post(
            f"/scenario/{scenario_guid}/fixedcost",
            json=self._serialize(request),
        )
        return FixedCostLineItemData.model_validate(data)

    def update(
        self,
        scenario_guid: str,
        line_item_guid: str,
        **kwargs: Any,
    ) -> FixedCostLineItemData:
        """Update a fixed cost line item.

        Args:
            scenario_guid: The scenario's GUID.
            line_item_guid: The line item's GUID.
            **kwargs: Fields to update.

        Returns:
            Updated line item data.
        """
        data = self._http.patch(
            f"/scenario/{scenario_guid}/fixedcost/{line_item_guid}",
            json=kwargs,
        )
        return FixedCostLineItemData.model_validate(data)

    def delete(self, scenario_guid: str, line_item_guid: str) -> None:
        """Delete a fixed cost line item.

        Args:
            scenario_guid: The scenario's GUID.
            line_item_guid: The line item's GUID.
        """
        self._http.delete(f"/scenario/{scenario_guid}/fixedcost/{line_item_guid}")

    def toggle_auto_calc(self, scenario_guid: str, line_item_guid: str) -> Any:
        """Toggle auto-calc on a fixed cost line item.

        Args:
            scenario_guid: The scenario's GUID.
            line_item_guid: The line item's GUID.

        Returns:
            Response data.
        """
        request = ToggleAutoCalcInput(line_item_guid=line_item_guid)
        return self._http.post(
            f"/scenario/{scenario_guid}/fixedcost/toggleauto",
            json=self._serialize(request),
        )

    def import_from(self, scenario_guid: str, line_item_guids: list[str]) -> Any:
        """Import fixed costs from other scenarios.

        Args:
            scenario_guid: The destination scenario's GUID.
            line_item_guids: List of line item GUIDs to import.

        Returns:
            Response data.
        """
        request = ImportFixedCostLineItemsInput(line_item_guids=line_item_guids)
        return self._http.post(
            f"/scenario/{scenario_guid}/importfixedcosts",
            json=self._serialize(request),
        )
