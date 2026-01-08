"""Projections resource."""

from typing import Any, Optional

from planvantage.models.folder import MoveItemToFolderInput
from planvantage.models.projection import (
    BenefitAdjustmentEnableInput,
    BenefitAdjustmentSourceData,
    ProjectionAdminFeeData,
    ProjectionAdminFeeInput,
    ProjectionData,
    ProjectionExperienceBulkInput,
    ProjectionFixedCostsData,
    ProjectionFixedCostsInput,
    ProjectionImportDashboardInput,
    ProjectionImportProjectionInput,
    ProjectionInput,
    ProjectionLFComponentColumnData,
    ProjectionLFComponentColumnInput,
    ProjectionLFTierComponentsInput,
    ProjectionPlanData,
    ProjectionPlanInput,
    ProjectionPlanRateInput,
    ProjectionPlanTierInput,
    ProjectionUpdateInput,
)
from planvantage.resources.base import BaseResource


class ProjectionsResource(BaseResource):
    """Resource for managing renewal projections."""

    def get(self, guid: str) -> ProjectionData:
        """Get a specific projection by GUID.

        Args:
            guid: The projection's unique identifier.

        Returns:
            Full projection data.

        Example:
            >>> projection = client.projections.get("proj_abc123")
            >>> print(projection.name)
        """
        data = self._http.get(f"/projection/{guid}")
        return ProjectionData.model_validate(data)

    def create(
        self,
        plan_sponsor_guid: str,
        name: Optional[str] = None,
    ) -> ProjectionData:
        """Create a new projection for a plan sponsor.

        Args:
            plan_sponsor_guid: The plan sponsor's GUID.
            name: Optional name for the projection.

        Returns:
            Created projection data.

        Example:
            >>> projection = client.projections.create(
            ...     plan_sponsor_guid="ps_abc123",
            ...     name="2024 Renewal Projection"
            ... )
        """
        request = ProjectionInput(plan_sponsor_guid=plan_sponsor_guid, name=name)
        data = self._http.post("/projection", json=self._serialize(request))
        return ProjectionData.model_validate(data)

    def update(
        self,
        guid: str,
        **kwargs: Any,
    ) -> ProjectionData:
        """Update a projection.

        Args:
            guid: The projection's unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated projection data.
        """
        data = self._http.patch(f"/projection/{guid}", json=kwargs)
        return ProjectionData.model_validate(data)

    def delete(self, guid: str) -> None:
        """Delete a projection.

        Args:
            guid: The projection's unique identifier.
        """
        self._http.delete(f"/projection/{guid}")

    def clone(self, guid: str) -> ProjectionData:
        """Clone a projection.

        Args:
            guid: The projection's unique identifier.

        Returns:
            Cloned projection data.
        """
        data = self._http.post(f"/projection/{guid}/clone")
        return ProjectionData.model_validate(data)

    def move_to_folder(
        self,
        guid: str,
        folder_guid: Optional[str] = None,
    ) -> ProjectionData:
        """Move a projection to a folder.

        Args:
            guid: The projection's unique identifier.
            folder_guid: Target folder GUID, or None for root.

        Returns:
            Updated projection data.
        """
        data = self._http.patch(
            f"/projection/{guid}/folder",
            json={"folder_guid": folder_guid},
        )
        return ProjectionData.model_validate(data)

    def import_from_dashboard(
        self,
        guid: str,
        dashboard_version_guid: str,
    ) -> ProjectionData:
        """Import data from a dashboard.

        Args:
            guid: The projection's unique identifier.
            dashboard_version_guid: The dashboard version's GUID.

        Returns:
            Updated projection data.
        """
        request = ProjectionImportDashboardInput(dashboard_version_guid=dashboard_version_guid)
        data = self._http.post(
            f"/projection/{guid}/import-dashboard",
            json=self._serialize(request),
        )
        return ProjectionData.model_validate(data)

    def import_from_projection(
        self,
        guid: str,
        source_projection_guid: str,
    ) -> ProjectionData:
        """Import data from another projection.

        Args:
            guid: The projection's unique identifier.
            source_projection_guid: The source projection's GUID.

        Returns:
            Updated projection data.
        """
        request = ProjectionImportProjectionInput(source_projection_guid=source_projection_guid)
        data = self._http.post(
            f"/projection/{guid}/import-projection",
            json=self._serialize(request),
        )
        return ProjectionData.model_validate(data)

    # Plan methods
    def create_plan(
        self,
        guid: str,
        **kwargs: Any,
    ) -> ProjectionPlanData:
        """Create a plan in the projection.

        Args:
            guid: The projection's unique identifier.
            **kwargs: Plan fields.

        Returns:
            Created plan data.
        """
        data = self._http.post(f"/projection/{guid}/plan", json=kwargs)
        return ProjectionPlanData.model_validate(data)

    def update_plan(
        self,
        guid: str,
        plan_guid: str,
        **kwargs: Any,
    ) -> ProjectionPlanData:
        """Update a projection plan.

        Args:
            guid: The projection's unique identifier.
            plan_guid: The plan's unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated plan data.
        """
        data = self._http.patch(f"/projection/{guid}/plan/{plan_guid}", json=kwargs)
        return ProjectionPlanData.model_validate(data)

    def delete_plan(self, guid: str, plan_guid: str) -> None:
        """Delete a projection plan.

        Args:
            guid: The projection's unique identifier.
            plan_guid: The plan's unique identifier.
        """
        self._http.delete(f"/projection/{guid}/plan/{plan_guid}")

    def update_plan_tiers(
        self,
        guid: str,
        plan_guid: str,
        tiers: list[dict[str, Any]],
    ) -> None:
        """Bulk update tiers for a projection plan.

        Args:
            guid: The projection's unique identifier.
            plan_guid: The plan's unique identifier.
            tiers: List of tier updates.
        """
        self._http.post(f"/projection/{guid}/plan/{plan_guid}/tiers", json=tiers)

    def update_tier_lf_components(
        self,
        guid: str,
        plan_guid: str,
        tier_guid: str,
        **kwargs: Any,
    ) -> None:
        """Update level-funded components for a tier.

        Args:
            guid: The projection's unique identifier.
            plan_guid: The plan's unique identifier.
            tier_guid: The tier's unique identifier.
            **kwargs: LF component values.
        """
        self._http.patch(
            f"/projection/{guid}/plan/{plan_guid}/tier/{tier_guid}/lf-components",
            json=kwargs,
        )

    def update_plan_rates(
        self,
        guid: str,
        plan_guid: str,
        rates: list[dict[str, Any]],
    ) -> None:
        """Bulk update rates for a projection plan.

        Args:
            guid: The projection's unique identifier.
            plan_guid: The plan's unique identifier.
            rates: List of rate updates.
        """
        self._http.post(f"/projection/{guid}/plan/{plan_guid}/rates", json=rates)

    # Experience methods
    def update_experience(
        self,
        guid: str,
        months: list[dict[str, Any]],
    ) -> None:
        """Bulk update experience months.

        Args:
            guid: The projection's unique identifier.
            months: List of experience month data.
        """
        self._http.post(f"/projection/{guid}/experience", json={"months": months})

    # Fixed costs
    def update_fixed_costs(
        self,
        guid: str,
        **kwargs: Any,
    ) -> ProjectionFixedCostsData:
        """Update fixed costs for the projection.

        Args:
            guid: The projection's unique identifier.
            **kwargs: Fixed cost fields.

        Returns:
            Updated fixed costs data.
        """
        data = self._http.patch(f"/projection/{guid}/fixedcosts", json=kwargs)
        return ProjectionFixedCostsData.model_validate(data)

    # Admin fees
    def create_admin_fee(
        self,
        guid: str,
        **kwargs: Any,
    ) -> ProjectionAdminFeeData:
        """Create an admin fee for the projection.

        Args:
            guid: The projection's unique identifier.
            **kwargs: Admin fee fields.

        Returns:
            Created admin fee data.
        """
        data = self._http.post(f"/projection/{guid}/adminfee", json=kwargs)
        return ProjectionAdminFeeData.model_validate(data)

    def update_admin_fee(
        self,
        guid: str,
        fee_guid: str,
        **kwargs: Any,
    ) -> ProjectionAdminFeeData:
        """Update a projection admin fee.

        Args:
            guid: The projection's unique identifier.
            fee_guid: The admin fee's unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated admin fee data.
        """
        data = self._http.patch(f"/projection/{guid}/adminfee/{fee_guid}", json=kwargs)
        return ProjectionAdminFeeData.model_validate(data)

    def delete_admin_fee(self, guid: str, fee_guid: str) -> None:
        """Delete a projection admin fee.

        Args:
            guid: The projection's unique identifier.
            fee_guid: The admin fee's unique identifier.
        """
        self._http.delete(f"/projection/{guid}/adminfee/{fee_guid}")

    # LF Columns
    def list_lf_columns(self, guid: str) -> list[ProjectionLFComponentColumnData]:
        """List level-funded component columns.

        Args:
            guid: The projection's unique identifier.

        Returns:
            List of LF columns.
        """
        data = self._http.get(f"/projection/{guid}/lf-columns")
        if isinstance(data, list):
            return [ProjectionLFComponentColumnData.model_validate(item) for item in data]
        return []

    def create_lf_column(
        self,
        guid: str,
        name: str,
        **kwargs: Any,
    ) -> ProjectionLFComponentColumnData:
        """Create a level-funded component column.

        Args:
            guid: The projection's unique identifier.
            name: Column name.
            **kwargs: Additional column fields.

        Returns:
            Created column data.
        """
        request = ProjectionLFComponentColumnInput(name=name, **kwargs)
        data = self._http.post(f"/projection/{guid}/lf-columns", json=self._serialize(request))
        return ProjectionLFComponentColumnData.model_validate(data)

    def update_lf_column(
        self,
        guid: str,
        column_guid: str,
        **kwargs: Any,
    ) -> ProjectionLFComponentColumnData:
        """Update a level-funded component column.

        Args:
            guid: The projection's unique identifier.
            column_guid: The column's unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated column data.
        """
        data = self._http.patch(f"/projection/{guid}/lf-columns/{column_guid}", json=kwargs)
        return ProjectionLFComponentColumnData.model_validate(data)

    def delete_lf_column(self, guid: str, column_guid: str) -> None:
        """Delete a level-funded component column.

        Args:
            guid: The projection's unique identifier.
            column_guid: The column's unique identifier.
        """
        self._http.delete(f"/projection/{guid}/lf-columns/{column_guid}")

    # Benefit adjustment
    def get_benefit_adjustment_sources(self, guid: str) -> BenefitAdjustmentSourceData:
        """Get available sources for benefit adjustment.

        Args:
            guid: The projection's unique identifier.

        Returns:
            Available dashboards and versions.
        """
        data = self._http.get(f"/projection/{guid}/benefit-adjustment/sources")
        return BenefitAdjustmentSourceData.model_validate(data)

    def enable_benefit_adjustment(
        self,
        guid: str,
        dashboard_version_guid: str,
    ) -> ProjectionData:
        """Enable benefit adjustment.

        Args:
            guid: The projection's unique identifier.
            dashboard_version_guid: The dashboard version to use.

        Returns:
            Updated projection data.
        """
        request = BenefitAdjustmentEnableInput(dashboard_version_guid=dashboard_version_guid)
        data = self._http.post(
            f"/projection/{guid}/benefit-adjustment/enable",
            json=self._serialize(request),
        )
        return ProjectionData.model_validate(data)

    def disable_benefit_adjustment(self, guid: str) -> ProjectionData:
        """Disable benefit adjustment.

        Args:
            guid: The projection's unique identifier.

        Returns:
            Updated projection data.
        """
        data = self._http.post(f"/projection/{guid}/benefit-adjustment/disable")
        return ProjectionData.model_validate(data)

    # Family size adjustment
    def enable_family_size_adjustment(self, guid: str) -> ProjectionData:
        """Enable family size adjustment.

        Args:
            guid: The projection's unique identifier.

        Returns:
            Updated projection data.
        """
        data = self._http.post(f"/projection/{guid}/family-size-adjustment/enable")
        return ProjectionData.model_validate(data)

    def disable_family_size_adjustment(self, guid: str) -> ProjectionData:
        """Disable family size adjustment.

        Args:
            guid: The projection's unique identifier.

        Returns:
            Updated projection data.
        """
        data = self._http.post(f"/projection/{guid}/family-size-adjustment/disable")
        return ProjectionData.model_validate(data)
