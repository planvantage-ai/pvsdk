"""QuoteSet resources."""

from typing import Any, BinaryIO, Optional

from planvantage.models.quoteset import (
    QuoteData,
    QuoteDocumentData,
    QuoteDocumentInfo,
    QuoteInput,
    QuoteLinkDocumentInput,
    QuoteRowDefData,
    QuoteRowInput,
    QuoteRowsReorderInput,
    QuoteRowUpdateInput,
    QuoteSetData,
    QuoteSetInput,
    QuoteSetMoveInput,
    QuoteSetUpdateInput,
    QuotesReorderInput,
    QuoteUpdateInput,
)
from planvantage.resources.base import BaseResource


class QuoteSetsResource(BaseResource):
    """Resource for managing quote sets."""

    def get(self, guid: str) -> QuoteSetData:
        """Get a specific quote set by GUID.

        Args:
            guid: The quote set's unique identifier.

        Returns:
            Full quote set data.

        Example:
            >>> quoteset = client.quotesets.get("qs_abc123")
            >>> print(quoteset.name)
        """
        data = self._http.get(f"/quoteset/{guid}")
        return QuoteSetData.model_validate(data)

    def create(
        self,
        plan_sponsor_guid: str,
        name: Optional[str] = None,
    ) -> QuoteSetData:
        """Create a new quote set for a plan sponsor.

        Args:
            plan_sponsor_guid: The plan sponsor's GUID.
            name: Optional name for the quote set.

        Returns:
            Created quote set data.

        Example:
            >>> quoteset = client.quotesets.create(
            ...     plan_sponsor_guid="ps_abc123",
            ...     name="2024 Carrier Quotes"
            ... )
        """
        request = QuoteSetInput(plan_sponsor_guid=plan_sponsor_guid, name=name)
        data = self._http.post("/quoteset", json=self._serialize(request))
        return QuoteSetData.model_validate(data)

    def update(
        self,
        guid: str,
        **kwargs: Any,
    ) -> QuoteSetData:
        """Update a quote set.

        Args:
            guid: The quote set's unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated quote set data.
        """
        data = self._http.patch(f"/quoteset/{guid}", json=kwargs)
        return QuoteSetData.model_validate(data)

    def delete(self, guid: str) -> None:
        """Delete a quote set.

        Args:
            guid: The quote set's unique identifier.
        """
        self._http.delete(f"/quoteset/{guid}")

    def clone(self, guid: str) -> QuoteSetData:
        """Clone a quote set.

        Args:
            guid: The quote set's unique identifier.

        Returns:
            Cloned quote set data.
        """
        data = self._http.post(f"/quoteset/{guid}/clone")
        return QuoteSetData.model_validate(data)

    def move_to_folder(
        self,
        guid: str,
        folder_guid: Optional[str] = None,
    ) -> QuoteSetData:
        """Move a quote set to a folder.

        Args:
            guid: The quote set's unique identifier.
            folder_guid: Target folder GUID, or None for root.

        Returns:
            Updated quote set data.
        """
        request = QuoteSetMoveInput(folder_guid=folder_guid)
        data = self._http.patch(f"/quoteset/{guid}/folder", json=self._serialize(request))
        return QuoteSetData.model_validate(data)

    # Quote methods
    def create_quote(
        self,
        guid: str,
        **kwargs: Any,
    ) -> QuoteData:
        """Create a quote in the quote set.

        Args:
            guid: The quote set's unique identifier.
            **kwargs: Quote fields (carrier, plan_type, etc.).

        Returns:
            Created quote data.
        """
        data = self._http.post(f"/quoteset/{guid}/quote", json=kwargs)
        return QuoteData.model_validate(data)

    def update_quote(
        self,
        guid: str,
        quote_guid: str,
        **kwargs: Any,
    ) -> QuoteData:
        """Update a quote.

        Args:
            guid: The quote set's unique identifier.
            quote_guid: The quote's unique identifier.
            **kwargs: Fields to update.

        Returns:
            Updated quote data.
        """
        data = self._http.patch(f"/quoteset/{guid}/quote/{quote_guid}", json=kwargs)
        return QuoteData.model_validate(data)

    def delete_quote(self, guid: str, quote_guid: str) -> None:
        """Delete a quote.

        Args:
            guid: The quote set's unique identifier.
            quote_guid: The quote's unique identifier.
        """
        self._http.delete(f"/quoteset/{guid}/quote/{quote_guid}")

    def link_document_to_quote(
        self,
        guid: str,
        quote_guid: str,
        document_guid: str,
    ) -> QuoteData:
        """Link a document to a quote.

        Args:
            guid: The quote set's unique identifier.
            quote_guid: The quote's unique identifier.
            document_guid: The document's unique identifier.

        Returns:
            Updated quote data.
        """
        request = QuoteLinkDocumentInput(document_guid=document_guid)
        data = self._http.patch(
            f"/quoteset/{guid}/quote/{quote_guid}/link-document",
            json=self._serialize(request),
        )
        return QuoteData.model_validate(data)

    def reorder_quotes(
        self,
        guid: str,
        quote_guids: list[str],
    ) -> None:
        """Reorder quotes in the quote set.

        Args:
            guid: The quote set's unique identifier.
            quote_guids: Ordered list of quote GUIDs.
        """
        request = QuotesReorderInput(quote_guids=quote_guids)
        self._http.patch(f"/quoteset/{guid}/quotes/reorder", json=self._serialize(request))

    # Row definition methods
    def create_row(
        self,
        guid: str,
        label: str,
        **kwargs: Any,
    ) -> QuoteRowDefData:
        """Create a row definition for the quote template.

        Args:
            guid: The quote set's unique identifier.
            label: Row label.
            **kwargs: Additional row fields.

        Returns:
            Created row definition data.
        """
        request = QuoteRowInput(label=label, **kwargs)
        data = self._http.post(f"/quoteset/{guid}/row", json=self._serialize(request))
        return QuoteRowDefData.model_validate(data)

    def update_row(
        self,
        guid: str,
        row_key: str,
        **kwargs: Any,
    ) -> QuoteRowDefData:
        """Update a row definition.

        Args:
            guid: The quote set's unique identifier.
            row_key: The row key.
            **kwargs: Fields to update.

        Returns:
            Updated row definition data.
        """
        data = self._http.patch(f"/quoteset/{guid}/row/{row_key}", json=kwargs)
        return QuoteRowDefData.model_validate(data)

    def delete_row(self, guid: str, row_key: str) -> None:
        """Delete a row definition.

        Args:
            guid: The quote set's unique identifier.
            row_key: The row key.
        """
        self._http.delete(f"/quoteset/{guid}/row/{row_key}")

    def reorder_rows(
        self,
        guid: str,
        row_keys: list[str],
    ) -> None:
        """Reorder row definitions.

        Args:
            guid: The quote set's unique identifier.
            row_keys: Ordered list of row keys.
        """
        request = QuoteRowsReorderInput(row_keys=row_keys)
        self._http.patch(f"/quoteset/{guid}/rows/reorder", json=self._serialize(request))

    # Document upload
    def upload_document(
        self,
        guid: str,
        file: BinaryIO,
        filename: Optional[str] = None,
    ) -> QuoteDocumentInfo:
        """Upload a quote document.

        Args:
            guid: The quote set's unique identifier.
            file: File-like object to upload.
            filename: Optional filename override.

        Returns:
            Created document info.

        Example:
            >>> with open("quote.pdf", "rb") as f:
            ...     doc = client.quotesets.upload_document(
            ...         guid="qs_abc123",
            ...         file=f,
            ...         filename="Blue Cross Quote.pdf"
            ...     )
        """
        files = {"file": (filename or "document", file)}
        data = self._http.post(f"/quoteset/{guid}/document", files=files)
        return QuoteDocumentInfo.model_validate(data)


class QuoteDocumentsResource(BaseResource):
    """Resource for managing quote documents."""

    def get(self, guid: str) -> QuoteDocumentData:
        """Get a specific quote document.

        Args:
            guid: The document's unique identifier.

        Returns:
            Full document data including extracted content.
        """
        data = self._http.get(f"/quotedoc/{guid}")
        return QuoteDocumentData.model_validate(data)

    def delete(self, guid: str) -> None:
        """Delete a quote document.

        Args:
            guid: The document's unique identifier.
        """
        self._http.delete(f"/quotedoc/{guid}")

    def download(self, guid: str) -> bytes:
        """Download the document file.

        Args:
            guid: The document's unique identifier.

        Returns:
            File contents as bytes.
        """
        return self._http.get(f"/quotedoc/{guid}/download")

    def view(self, guid: str) -> bytes:
        """Get document for inline viewing.

        Args:
            guid: The document's unique identifier.

        Returns:
            File contents as bytes.
        """
        return self._http.get(f"/quotedoc/{guid}/view")

    def reprocess(self, guid: str) -> None:
        """Reprocess document extraction.

        Args:
            guid: The document's unique identifier.
        """
        self._http.post(f"/quotedoc/{guid}/reprocess")
