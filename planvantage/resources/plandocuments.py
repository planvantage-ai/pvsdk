"""Plan documents resource."""

from typing import Any, BinaryIO, Optional

from planvantage.models.plandocument import (
    PlanDocumentData,
    PlanDocumentInfo,
)
from planvantage.resources.base import BaseResource


class PlanDocumentsResource(BaseResource):
    """Resource for managing plan documents."""

    def get(self, guid: str) -> PlanDocumentData:
        """Get a specific plan document by GUID.

        Args:
            guid: The document's unique identifier.

        Returns:
            Full document data including extracted content.

        Example:
            >>> doc = client.plandocuments.get("doc_abc123")
            >>> print(doc.filename)
        """
        data = self._http.get(f"/plandocument/{guid}")
        return PlanDocumentData.model_validate(data)

    def upload(
        self,
        plan_sponsor_guid: str,
        file: BinaryIO,
        filename: Optional[str] = None,
        user_input: Optional[str] = None,
    ) -> PlanDocumentInfo:
        """Upload a plan document.

        Args:
            plan_sponsor_guid: The plan sponsor's GUID.
            file: File-like object to upload.
            filename: Optional filename override.
            user_input: Optional instructions for AI processing.

        Returns:
            Created document info.

        Example:
            >>> with open("plan.pdf", "rb") as f:
            ...     doc = client.plandocuments.upload(
            ...         plan_sponsor_guid="ps_abc123",
            ...         file=f,
            ...         filename="Plan Summary 2024.pdf",
            ...         user_input="Focus on medical plans only"
            ...     )
        """
        files = {"file": (filename or "document", file)}
        data_fields: dict[str, str] = {"planSponsorGuid": plan_sponsor_guid}
        if user_input:
            data_fields["userInput"] = user_input
        data = self._http.post(
            "/plandocument",
            files=files,
            data=data_fields,
        )
        return PlanDocumentInfo.model_validate(data)

    def delete(self, guid: str) -> None:
        """Delete a plan document.

        Args:
            guid: The document's unique identifier.

        Example:
            >>> client.plandocuments.delete("doc_abc123")
        """
        self._http.delete(f"/plandocument/{guid}")

    def download(self, guid: str) -> bytes:
        """Download the document file.

        Args:
            guid: The document's unique identifier.

        Returns:
            File contents as bytes.

        Example:
            >>> content = client.plandocuments.download("doc_abc123")
            >>> with open("plan.pdf", "wb") as f:
            ...     f.write(content)
        """
        return self._http.get(f"/plandocument/{guid}/download")

    def preview(self, guid: str) -> bytes:
        """Get document for inline viewing/preview.

        Args:
            guid: The document's unique identifier.

        Returns:
            File contents as bytes.
        """
        return self._http.get(f"/plandocument/{guid}/preview")

    def reprocess(self, guid: str) -> None:
        """Reprocess document extraction.

        Args:
            guid: The document's unique identifier.

        Example:
            >>> client.plandocuments.reprocess("doc_abc123")
        """
        self._http.post(f"/plandocument/{guid}/reprocess")

    def cancel(self, guid: str) -> None:
        """Cancel document processing.

        Args:
            guid: The document's unique identifier.

        Example:
            >>> client.plandocuments.cancel("doc_abc123")
        """
        self._http.post(f"/plandocument/{guid}/cancel")

    def rename(self, guid: str, filename: str) -> None:
        """Rename a plan document.

        Args:
            guid: The document's unique identifier.
            filename: New filename.

        Example:
            >>> client.plandocuments.rename("doc_abc123", "Updated Plan.pdf")
        """
        self._http.post(f"/plandocument/{guid}/rename", json={"fileName": filename})

    def extract_plan_designs(
        self,
        guid: str,
        user_input: Optional[str] = None,
    ) -> None:
        """Extract plan designs from the document.

        Args:
            guid: The document's unique identifier.
            user_input: Optional instructions for AI extraction.

        Example:
            >>> client.plandocuments.extract_plan_designs("doc_abc123")
        """
        body: dict[str, str] = {}
        if user_input:
            body["userInput"] = user_input
        self._http.post(f"/plandocument/{guid}/extractplandesigns", json=body if body else None)

    def extract_rates(
        self,
        guid: str,
        user_input: Optional[str] = None,
    ) -> None:
        """Extract rates from the document.

        Args:
            guid: The document's unique identifier.
            user_input: Optional instructions for AI extraction.

        Example:
            >>> client.plandocuments.extract_rates("doc_abc123")
        """
        body: dict[str, str] = {}
        if user_input:
            body["userInput"] = user_input
        self._http.post(f"/plandocument/{guid}/extractrates", json=body if body else None)

    def extract_contributions(
        self,
        guid: str,
        user_input: Optional[str] = None,
    ) -> None:
        """Extract contributions from the document.

        Args:
            guid: The document's unique identifier.
            user_input: Optional instructions for AI extraction.

        Example:
            >>> client.plandocuments.extract_contributions("doc_abc123")
        """
        body: dict[str, str] = {}
        if user_input:
            body["userInput"] = user_input
        self._http.post(f"/plandocument/{guid}/extractcontributions", json=body if body else None)

    def delete_extracted_data(self, guid: str, data_type: str) -> None:
        """Delete extracted data of a specific type from a document.

        Args:
            guid: The document's unique identifier.
            data_type: Type of data to delete ("planDesigns", "rates", or "contributions").

        Example:
            >>> client.plandocuments.delete_extracted_data("doc_abc123", "rates")
        """
        self._http.post(f"/plandocument/{guid}/{data_type}/delete")
