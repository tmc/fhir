# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ShareableValueSet:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    status: ShareableValueSet_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    immutable: Boolean
    purpose: Markdown
    copyright: Markdown
    compose: ShareableValueSet_Compose
    expansion: ShareableValueSet_Expansion


@dataclass
class ShareableValueSet_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ShareableValueSet_Compose:
    id: String
    extension: Extension
    modifier_extension: Extension
    locked_date: Date
    inactive: Boolean
    include: ShareableValueSet_Compose_ConceptSet
    exclude: ShareableValueSet_Compose_ConceptSet


@dataclass
class ShareableValueSet_Compose_ConceptSet:
    id: String
    extension: Extension
    modifier_extension: Extension
    system: Uri
    version: String
    concept: ShareableValueSet_Compose_ConceptSet_ConceptReference
    filter: ShareableValueSet_Compose_ConceptSet_Filter
    value_set: Canonical


@dataclass
class ShareableValueSet_Compose_ConceptSet_ConceptReference:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    display: String
    designation: ShareableValueSet_Compose_ConceptSet_ConceptReference_Designation


@dataclass
class ShareableValueSet_Compose_ConceptSet_ConceptReference_Designation:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: Code
    use: Coding
    value: String


@dataclass
class ShareableValueSet_Compose_ConceptSet_Filter:
    id: String
    extension: Extension
    modifier_extension: Extension
    property: Code
    op: ShareableValueSet_Compose_ConceptSet_Filter_OpCode
    value: String


@dataclass
class ShareableValueSet_Compose_ConceptSet_Filter_OpCode:
    value: FilterOperatorCode_Value
    id: String
    extension: Extension


@dataclass
class ShareableValueSet_Expansion:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Uri
    timestamp: DateTime
    total: Integer
    offset: Integer
    parameter: ShareableValueSet_Expansion_Parameter
    contains: ShareableValueSet_Expansion_Contains


@dataclass
class ShareableValueSet_Expansion_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    value: ShareableValueSet_Expansion_Parameter_ValueX


@dataclass
class ShareableValueSet_Expansion_Parameter_ValueX:
    string_value: String
    boolean: Boolean
    integer: Integer
    decimal: Decimal
    uri: Uri
    code: Code
    date_time: DateTime


@dataclass
class ShareableValueSet_Expansion_Contains:
    id: String
    extension: Extension
    modifier_extension: Extension
    system: Uri
    abstract: Boolean
    inactive: Boolean
    version: String
    code: Code
    display: String
    designation: ShareableValueSet_Compose_ConceptSet_ConceptReference_Designation
    contains: ShareableValueSet_Expansion_Contains

