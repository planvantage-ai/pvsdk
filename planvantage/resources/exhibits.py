"""Exhibit resources."""

from __future__ import annotations

from typing import Any, Optional

from planvantage.models.exhibit import (
    ContributionOptionInfo,
    ExhibitApplyContributionInput,
    ExhibitData,
    ExhibitFixedCostReorderInput,
    ExhibitFixedCostRowInput,
    ExhibitInfo,
    ExhibitInput,
    ExhibitPEPMInput,
    ExhibitScenarioConfigData,
    ExhibitScenarioInput,
    ExhibitSettingsData,
    ExhibitTableData,
)
from planvantage.resources.base import BaseResource


class ExhibitsResource(BaseResource):
    """Resource for managing exhibits."""

    def list(self, plan_sponsor_guid: str) -> list[ExhibitInfo]:
        """List exhibits for a plan sponsor.

        Args:
            plan_sponsor_guid: The plan sponsor's GUID.

        Returns:
            List of exhibit summaries.
        """
        data = self._http.get(f"/plansponsor/{plan_sponsor_guid}/exhibits")
        return [ExhibitInfo.model_validate(item) for item in data]

    def get(self, guid: str) -> ExhibitData:
        """Get a specific exhibit by GUID.

        Args:
            guid: The exhibit's unique identifier.

        Returns:
            Full exhibit data.
        """
        data = self._http.get(f"/exhibit/{guid}")
        return ExhibitData.model_validate(data)

    def create(
        self,
        plan_sponsor_guid: str,
        name: str,
        **kwargs: Any,
    ) -> ExhibitData:
        """Create a new exhibit.

        Args:
            plan_sponsor_guid: The plan sponsor's GUID.
            name: Name for the exhibit.
            **kwargs: Additional fields (show_contributions, diff_vs_current, etc.).

        Returns:
            Created exhibit data.
        """
        request = ExhibitInput(name=name, **kwargs)
        data = self._http.post(
            f"/plansponsor/{plan_sponsor_guid}/exhibit",
            json=self._serialize(request),
        )
        return ExhibitData.model_validate(data)

    def update(self, guid: str, **kwargs: Any) -> ExhibitData:
        """Update an exhibit.

        Args:
            guid: The exhibit's unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated exhibit data.
        """
        data = self._http.patch(f"/exhibit/{guid}", json=kwargs)
        return ExhibitData.model_validate(data)

    def delete(self, guid: str) -> None:
        """Delete an exhibit.

        Args:
            guid: The exhibit's unique identifier.
        """
        self._http.delete(f"/exhibit/{guid}")

    def clone(self, guid: str) -> ExhibitData:
        """Clone an exhibit.

        Args:
            guid: The exhibit's unique identifier.

        Returns:
            Cloned exhibit data.
        """
        data = self._http.post(f"/exhibit/{guid}/clone")
        return ExhibitData.model_validate(data)

    def get_table(self, guid: str) -> ExhibitTableData:
        """Get the calculated exhibit table data.

        Args:
            guid: The exhibit's unique identifier.

        Returns:
            Full calculated exhibit table.
        """
        data = self._http.get(f"/exhibit/{guid}/table")
        return ExhibitTableData.model_validate(data)

    def export(self, guid: str) -> bytes:
        """Export exhibit as Excel file.

        Args:
            guid: The exhibit's unique identifier.

        Returns:
            Excel file bytes.
        """
        return self._http.get(f"/exhibit/{guid}/export")

    def add_scenario(
        self,
        guid: str,
        scenario_guid: str,
        **kwargs: Any,
    ) -> ExhibitScenarioConfigData:
        """Add a scenario to an exhibit.

        Args:
            guid: The exhibit's unique identifier.
            scenario_guid: The scenario's GUID.
            **kwargs: Additional fields (order, display_name, color, etc.).

        Returns:
            Created scenario config data.
        """
        request = ExhibitScenarioInput(scenario_guid=scenario_guid, **kwargs)
        data = self._http.post(
            f"/exhibit/{guid}/scenario",
            json=self._serialize(request),
        )
        return ExhibitScenarioConfigData.model_validate(data)

    def update_scenario(
        self,
        guid: str,
        config_guid: str,
        **kwargs: Any,
    ) -> ExhibitScenarioConfigData:
        """Update a scenario config in an exhibit.

        Args:
            guid: The exhibit's unique identifier.
            config_guid: The scenario config's GUID.
            **kwargs: Fields to update.

        Returns:
            Updated scenario config data.
        """
        data = self._http.patch(f"/exhibit/{guid}/scenario/{config_guid}", json=kwargs)
        return ExhibitScenarioConfigData.model_validate(data)

    def remove_scenario(self, guid: str, config_guid: str) -> None:
        """Remove a scenario from an exhibit.

        Args:
            guid: The exhibit's unique identifier.
            config_guid: The scenario config's GUID.
        """
        self._http.delete(f"/exhibit/{guid}/scenario/{config_guid}")

    def apply_contribution(
        self,
        guid: str,
        contribution_option_guid: str,
    ) -> Any:
        """Apply a contribution option to all scenarios.

        Args:
            guid: The exhibit's unique identifier.
            contribution_option_guid: The contribution option's GUID.

        Returns:
            Response data.
        """
        request = ExhibitApplyContributionInput(
            contribution_option_guid=contribution_option_guid,
        )
        return self._http.post(
            f"/exhibit/{guid}/applycontribution",
            json=self._serialize(request),
        )

    def add_fixed_cost_row(self, guid: str, name: str) -> Any:
        """Add a fixed cost row to the exhibit.

        Args:
            guid: The exhibit's unique identifier.
            name: The row name.

        Returns:
            Response data.
        """
        request = ExhibitFixedCostRowInput(name=name)
        return self._http.post(
            f"/exhibit/{guid}/fixedcost",
            json=self._serialize(request),
        )

    def reorder_fixed_cost_rows(self, guid: str, names: list[str]) -> Any:
        """Reorder fixed cost rows.

        Args:
            guid: The exhibit's unique identifier.
            names: Ordered list of row names.

        Returns:
            Response data.
        """
        request = ExhibitFixedCostReorderInput(names=names)
        return self._http.post(
            f"/exhibit/{guid}/fixedcost/reorder",
            json=self._serialize(request),
        )

    def delete_fixed_cost_row(self, guid: str, name: str) -> None:
        """Delete a fixed cost row.

        Args:
            guid: The exhibit's unique identifier.
            name: The row name.
        """
        self._http.delete(f"/exhibit/{guid}/fixedcost/{name}")

    def apply_pepm(
        self,
        guid: str,
        name: str,
        current_pepm: Optional[float] = None,
        proposed_pepm: Optional[float] = None,
    ) -> Any:
        """Apply PEPM to a fixed cost row across all scenarios.

        Args:
            guid: The exhibit's unique identifier.
            name: The row name.
            current_pepm: Current PEPM value.
            proposed_pepm: Proposed PEPM value.

        Returns:
            Response data.
        """
        request = ExhibitPEPMInput(
            name=name,
            current_pepm=current_pepm,
            proposed_pepm=proposed_pepm,
        )
        return self._http.post(
            f"/exhibit/{guid}/fixedcost/pepm",
            json=self._serialize(request),
        )


class ExhibitSettingsResource(BaseResource):
    """Resource for managing exhibit settings."""

    def get(self, guid: str) -> ExhibitSettingsData:
        """Get exhibit settings.

        Args:
            guid: The exhibit settings' unique identifier.

        Returns:
            Exhibit settings data.
        """
        data = self._http.get(f"/exhibitsettings/{guid}")
        return ExhibitSettingsData.model_validate(data)

    def update(self, guid: str, **kwargs: Any) -> ExhibitSettingsData:
        """Update exhibit settings.

        Args:
            guid: The exhibit settings' unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated exhibit settings data.
        """
        data = self._http.patch(f"/exhibitsettings/{guid}", json=kwargs)
        return ExhibitSettingsData.model_validate(data)
