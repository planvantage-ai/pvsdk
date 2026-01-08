"""Dashboard resources."""

from typing import Any, Optional

from planvantage.models.dashboard import (
    AdminFeeData,
    AdminFeeInput,
    DashboardClaimsData,
    DashboardContributionGroupData,
    DashboardContributionGroupInput,
    DashboardCustomValueData,
    DashboardData,
    DashboardDataAvailability,
    DashboardEnrollmentData,
    DashboardInput,
    DashboardLargeClaimData,
    DashboardMembersData,
    DashboardPlanData,
    DashboardPlanInput,
    DashboardPlanTierData,
    DashboardPlanTierInput,
    DashboardSlideData,
    DashboardTierSetInput,
    DashboardVersionData,
    DashboardVersionInput,
    LFComponentColumnData,
    LFComponentColumnInput,
    TierComponentInput,
)
from planvantage.models.folder import MoveItemToFolderInput
from planvantage.resources.base import BaseResource


class DashboardsResource(BaseResource):
    """Resource for managing dashboards."""

    def get(self, guid: str) -> DashboardData:
        """Get a specific dashboard by GUID.

        Args:
            guid: The dashboard's unique identifier.

        Returns:
            Full dashboard data.

        Example:
            >>> dashboard = client.dashboards.get("db_abc123")
            >>> print(dashboard.name)
        """
        data = self._http.get(f"/dashboard/{guid}")
        return DashboardData.model_validate(data)

    def create(
        self,
        plan_sponsor_guid: str,
        name: Optional[str] = None,
    ) -> DashboardData:
        """Create a new dashboard for a plan sponsor.

        Args:
            plan_sponsor_guid: The plan sponsor's GUID.
            name: Optional name for the dashboard.

        Returns:
            Created dashboard data.

        Example:
            >>> dashboard = client.dashboards.create(
            ...     plan_sponsor_guid="ps_abc123",
            ...     name="2024 Experience Dashboard"
            ... )
        """
        request = DashboardInput(plan_sponsor_guid=plan_sponsor_guid, name=name)
        data = self._http.post("/dashboard", json=self._serialize(request))
        return DashboardData.model_validate(data)

    def update(
        self,
        guid: str,
        **kwargs: Any,
    ) -> DashboardData:
        """Update a dashboard.

        Args:
            guid: The dashboard's unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated dashboard data.
        """
        data = self._http.patch(f"/dashboard/{guid}", json=kwargs)
        return DashboardData.model_validate(data)

    def delete(self, guid: str) -> None:
        """Delete a dashboard.

        Args:
            guid: The dashboard's unique identifier.
        """
        self._http.delete(f"/dashboard/{guid}")

    def clone(self, guid: str) -> DashboardData:
        """Clone a dashboard.

        Args:
            guid: The dashboard's unique identifier.

        Returns:
            Cloned dashboard data.
        """
        data = self._http.post(f"/dashboard/{guid}/clone")
        return DashboardData.model_validate(data)

    def move_to_folder(
        self,
        guid: str,
        folder_guid: Optional[str] = None,
    ) -> DashboardData:
        """Move a dashboard to a folder.

        Args:
            guid: The dashboard's unique identifier.
            folder_guid: Target folder GUID, or None for root.

        Returns:
            Updated dashboard data.
        """
        request = MoveItemToFolderInput(folder_guid=folder_guid)
        data = self._http.patch(f"/dashboard/{guid}/folder", json=self._serialize(request))
        return DashboardData.model_validate(data)

    # Plan methods
    def create_plan(
        self,
        guid: str,
        **kwargs: Any,
    ) -> DashboardPlanData:
        """Create a plan in the dashboard.

        Args:
            guid: The dashboard's unique identifier.
            **kwargs: Plan fields (name, carrier, plan_type, etc.).

        Returns:
            Created plan data.
        """
        data = self._http.post(f"/dashboard/{guid}/plan", json=kwargs)
        return DashboardPlanData.model_validate(data)

    def update_plan(
        self,
        guid: str,
        plan_guid: str,
        **kwargs: Any,
    ) -> DashboardPlanData:
        """Update a dashboard plan.

        Args:
            guid: The dashboard's unique identifier.
            plan_guid: The plan's unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated plan data.
        """
        data = self._http.patch(f"/dashboard/{guid}/plan/{plan_guid}", json=kwargs)
        return DashboardPlanData.model_validate(data)

    def delete_plan(self, guid: str, plan_guid: str) -> None:
        """Delete a dashboard plan.

        Args:
            guid: The dashboard's unique identifier.
            plan_guid: The plan's unique identifier.
        """
        self._http.delete(f"/dashboard/{guid}/plan/{plan_guid}")

    # Tier methods
    def create_plan_tier(
        self,
        guid: str,
        plan_guid: str,
        **kwargs: Any,
    ) -> DashboardPlanTierData:
        """Create a tier for a dashboard plan.

        Args:
            guid: The dashboard's unique identifier.
            plan_guid: The plan's unique identifier.
            **kwargs: Tier fields.

        Returns:
            Created tier data.
        """
        data = self._http.post(f"/dashboard/{guid}/plan/{plan_guid}/tier", json=kwargs)
        return DashboardPlanTierData.model_validate(data)

    def update_plan_tier(
        self,
        guid: str,
        plan_guid: str,
        tier_guid: str,
        **kwargs: Any,
    ) -> DashboardPlanTierData:
        """Update a dashboard plan tier.

        Args:
            guid: The dashboard's unique identifier.
            plan_guid: The plan's unique identifier.
            tier_guid: The tier's unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated tier data.
        """
        data = self._http.patch(
            f"/dashboard/{guid}/plan/{plan_guid}/tier/{tier_guid}",
            json=kwargs,
        )
        return DashboardPlanTierData.model_validate(data)

    def delete_plan_tier(
        self,
        guid: str,
        plan_guid: str,
        tier_guid: str,
    ) -> None:
        """Delete a dashboard plan tier.

        Args:
            guid: The dashboard's unique identifier.
            plan_guid: The plan's unique identifier.
            tier_guid: The tier's unique identifier.
        """
        self._http.delete(f"/dashboard/{guid}/plan/{plan_guid}/tier/{tier_guid}")

    def update_tier_lf_components(
        self,
        guid: str,
        plan_guid: str,
        tier_guid: str,
        lf_components: list[dict[str, Any]],
    ) -> None:
        """Update level-funded components for a tier.

        Args:
            guid: The dashboard's unique identifier.
            plan_guid: The plan's unique identifier.
            tier_guid: The tier's unique identifier.
            lf_components: List of LF component values.
        """
        self._http.patch(
            f"/dashboard/{guid}/plan/{plan_guid}/tier/{tier_guid}/lf-components",
            json={"lf_components": lf_components},
        )

    # Tier set
    def apply_tier_set(
        self,
        guid: str,
        tier_name_set_id: int,
    ) -> DashboardData:
        """Apply a tier name set to the dashboard.

        Args:
            guid: The dashboard's unique identifier.
            tier_name_set_id: The tier name set ID.

        Returns:
            Updated dashboard data.
        """
        request = DashboardTierSetInput(tier_name_set_id=tier_name_set_id)
        data = self._http.patch(f"/dashboard/{guid}/tierset", json=self._serialize(request))
        return DashboardData.model_validate(data)

    # Admin fees
    def create_admin_fee(
        self,
        guid: str,
        **kwargs: Any,
    ) -> AdminFeeData:
        """Create an admin fee for the dashboard.

        Args:
            guid: The dashboard's unique identifier.
            **kwargs: Admin fee fields.

        Returns:
            Created admin fee data.
        """
        data = self._http.post(f"/dashboard/{guid}/adminfee", json=kwargs)
        return AdminFeeData.model_validate(data)

    def update_admin_fee(
        self,
        guid: str,
        fee_id: int,
        **kwargs: Any,
    ) -> AdminFeeData:
        """Update a dashboard admin fee.

        Args:
            guid: The dashboard's unique identifier.
            fee_id: The admin fee's ID.
            **kwargs: Fields to update.

        Returns:
            Updated admin fee data.
        """
        data = self._http.patch(f"/dashboard/{guid}/adminfee/{fee_id}", json=kwargs)
        return AdminFeeData.model_validate(data)

    def delete_admin_fee(self, guid: str, fee_id: int) -> None:
        """Delete a dashboard admin fee.

        Args:
            guid: The dashboard's unique identifier.
            fee_id: The admin fee's ID.
        """
        self._http.delete(f"/dashboard/{guid}/adminfee/{fee_id}")

    # LF Columns
    def list_lf_columns(self, guid: str) -> list[LFComponentColumnData]:
        """List level-funded component columns.

        Args:
            guid: The dashboard's unique identifier.

        Returns:
            List of LF columns.
        """
        data = self._http.get(f"/dashboard/{guid}/lf-columns")
        if isinstance(data, list):
            return [LFComponentColumnData.model_validate(item) for item in data]
        return []

    def create_lf_column(
        self,
        guid: str,
        name: str,
        **kwargs: Any,
    ) -> LFComponentColumnData:
        """Create a level-funded component column.

        Args:
            guid: The dashboard's unique identifier.
            name: Column name.
            **kwargs: Additional column fields.

        Returns:
            Created column data.
        """
        request = LFComponentColumnInput(name=name, **kwargs)
        data = self._http.post(f"/dashboard/{guid}/lf-columns", json=self._serialize(request))
        return LFComponentColumnData.model_validate(data)

    def update_lf_column(
        self,
        guid: str,
        column_guid: str,
        **kwargs: Any,
    ) -> LFComponentColumnData:
        """Update a level-funded component column.

        Args:
            guid: The dashboard's unique identifier.
            column_guid: The column's unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated column data.
        """
        data = self._http.patch(f"/dashboard/{guid}/lf-columns/{column_guid}", json=kwargs)
        return LFComponentColumnData.model_validate(data)

    def delete_lf_column(self, guid: str, column_guid: str) -> None:
        """Delete a level-funded component column.

        Args:
            guid: The dashboard's unique identifier.
            column_guid: The column's unique identifier.
        """
        self._http.delete(f"/dashboard/{guid}/lf-columns/{column_guid}")

    # Data availability and slides
    def get_data_availability(self, guid: str) -> DashboardDataAvailability:
        """Get data availability information.

        Args:
            guid: The dashboard's unique identifier.

        Returns:
            Data availability information.
        """
        data = self._http.get(f"/dashboard/{guid}/data-availability")
        return DashboardDataAvailability.model_validate(data)

    def get_slide_data(self, guid: str, slide_key: str) -> DashboardSlideData:
        """Get computed data for a dashboard slide.

        Args:
            guid: The dashboard's unique identifier.
            slide_key: The slide key.

        Returns:
            Slide data.
        """
        data = self._http.get(f"/dashboard/{guid}/slides/{slide_key}")
        return DashboardSlideData.model_validate(data)

    # Contribution groups
    def list_contribution_groups(
        self,
        guid: str,
    ) -> list[DashboardContributionGroupData]:
        """List contribution groups for the dashboard.

        Args:
            guid: The dashboard's unique identifier.

        Returns:
            List of contribution groups.
        """
        data = self._http.get(f"/dashboard/{guid}/contributiongroups")
        if isinstance(data, list):
            return [DashboardContributionGroupData.model_validate(item) for item in data]
        return []

    def create_contribution_group(
        self,
        guid: str,
        **kwargs: Any,
    ) -> DashboardContributionGroupData:
        """Create a contribution group.

        Args:
            guid: The dashboard's unique identifier.
            **kwargs: Group fields.

        Returns:
            Created group data.
        """
        data = self._http.post(f"/dashboard/{guid}/contributiongroups", json=kwargs)
        return DashboardContributionGroupData.model_validate(data)

    def update_contribution_group(
        self,
        guid: str,
        group_guid: str,
        **kwargs: Any,
    ) -> DashboardContributionGroupData:
        """Update a contribution group.

        Args:
            guid: The dashboard's unique identifier.
            group_guid: The group's unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated group data.
        """
        data = self._http.patch(
            f"/dashboard/{guid}/contributiongroup/{group_guid}",
            json=kwargs,
        )
        return DashboardContributionGroupData.model_validate(data)

    def delete_contribution_group(self, guid: str, group_guid: str) -> None:
        """Delete a contribution group.

        Args:
            guid: The dashboard's unique identifier.
            group_guid: The group's unique identifier.
        """
        self._http.delete(f"/dashboard/{guid}/contributiongroup/{group_guid}")


class DashboardVersionsResource(BaseResource):
    """Resource for managing dashboard versions."""

    def get(self, guid: str) -> DashboardVersionData:
        """Get a specific dashboard version.

        Args:
            guid: The version's unique identifier.

        Returns:
            Version data.
        """
        data = self._http.get(f"/dashboardversion/{guid}")
        return DashboardVersionData.model_validate(data)

    def create(
        self,
        dashboard_guid: str,
        name: str,
        data_end_date: Optional[str] = None,
    ) -> DashboardVersionData:
        """Create a new dashboard version.

        Args:
            dashboard_guid: The parent dashboard's GUID.
            name: Version name.
            data_end_date: Optional data end date.

        Returns:
            Created version data.
        """
        request = {
            "dashboard_guid": dashboard_guid,
            "name": name,
        }
        if data_end_date:
            request["data_end_date"] = data_end_date
        data = self._http.post("/dashboardversion", json=request)
        return DashboardVersionData.model_validate(data)

    def update(
        self,
        guid: str,
        **kwargs: Any,
    ) -> DashboardVersionData:
        """Update a dashboard version.

        Args:
            guid: The version's unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated version data.
        """
        data = self._http.patch(f"/dashboardversion/{guid}", json=kwargs)
        return DashboardVersionData.model_validate(data)

    def delete(self, guid: str) -> None:
        """Delete a dashboard version.

        Args:
            guid: The version's unique identifier.
        """
        self._http.delete(f"/dashboardversion/{guid}")

    def update_enrollment(
        self,
        guid: str,
        enrollment_data: list[dict[str, Any]],
    ) -> None:
        """Bulk update enrollment data.

        Args:
            guid: The version's unique identifier.
            enrollment_data: List of enrollment records.
        """
        self._http.post(f"/dashboardversion/{guid}/enrollment", json=enrollment_data)

    def update_members(
        self,
        guid: str,
        members_data: list[dict[str, Any]],
    ) -> None:
        """Bulk update members data.

        Args:
            guid: The version's unique identifier.
            members_data: List of members records.
        """
        self._http.post(f"/dashboardversion/{guid}/members", json=members_data)

    def update_claims(
        self,
        guid: str,
        claims_data: list[dict[str, Any]],
    ) -> None:
        """Bulk update claims data.

        Args:
            guid: The version's unique identifier.
            claims_data: List of claims records.
        """
        self._http.post(f"/dashboardversion/{guid}/claims", json=claims_data)

    def update_custom_values(
        self,
        guid: str,
        custom_values: list[dict[str, Any]],
    ) -> None:
        """Bulk update custom field values.

        Args:
            guid: The version's unique identifier.
            custom_values: List of custom value records.
        """
        self._http.post(f"/dashboardversion/{guid}/customvalues", json=custom_values)

    def update_large_claims(
        self,
        guid: str,
        large_claims: list[dict[str, Any]],
    ) -> None:
        """Bulk update large claims data.

        Args:
            guid: The version's unique identifier.
            large_claims: List of large claim records.
        """
        self._http.post(f"/dashboardversion/{guid}/largeclaims", json=large_claims)
