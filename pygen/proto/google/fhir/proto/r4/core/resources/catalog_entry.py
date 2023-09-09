# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class CatalogEntry:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    type: CodeableConcept
    orderable: Boolean
    referenced_item: Reference
    additional_identifier: Identifier
    classification: CodeableConcept
    status: CatalogEntry_StatusCode
    validity_period: Period
    valid_to: DateTime
    last_updated: DateTime
    additional_characteristic: CodeableConcept
    additional_classification: CodeableConcept
    related_entry: CatalogEntry_RelatedEntry


@dataclass
class CatalogEntry_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CatalogEntry_RelatedEntry:
    id: String
    extension: Extension
    modifier_extension: Extension
    relationtype: CatalogEntry_RelatedEntry_RelationtypeCode
    item: Reference


@dataclass
class CatalogEntry_RelatedEntry_RelationtypeCode:
    value: CatalogEntryRelationTypeCode_Value
    id: String
    extension: Extension

