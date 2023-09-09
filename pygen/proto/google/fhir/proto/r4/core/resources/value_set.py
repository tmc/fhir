# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ValueSet:
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
    status: ValueSet_StatusCode
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
    compose: ValueSet_Compose
    expansion: ValueSet_Expansion


@dataclass
class ValueSet_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ValueSet_Compose:
    id: String
    extension: Extension
    modifier_extension: Extension
    locked_date: Date
    inactive: Boolean
    include: ValueSet_Compose_ConceptSet
    exclude: ValueSet_Compose_ConceptSet


@dataclass
class ValueSet_Compose_ConceptSet:
    id: String
    extension: Extension
    modifier_extension: Extension
    system: Uri
    version: String
    concept: ValueSet_Compose_ConceptSet_ConceptReference
    filter: ValueSet_Compose_ConceptSet_Filter
    value_set: Canonical


@dataclass
class ValueSet_Compose_ConceptSet_ConceptReference:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    display: String
    designation: ValueSet_Compose_ConceptSet_ConceptReference_Designation


@dataclass
class ValueSet_Compose_ConceptSet_ConceptReference_Designation:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: Code
    use: Coding
    value: String


@dataclass
class ValueSet_Compose_ConceptSet_Filter:
    id: String
    extension: Extension
    modifier_extension: Extension
    property: Code
    op: ValueSet_Compose_ConceptSet_Filter_OpCode
    value: String


@dataclass
class ValueSet_Compose_ConceptSet_Filter_OpCode:
    value: FilterOperatorCode_Value
    id: String
    extension: Extension


@dataclass
class ValueSet_Expansion:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Uri
    timestamp: DateTime
    total: Integer
    offset: Integer
    parameter: ValueSet_Expansion_Parameter
    contains: ValueSet_Expansion_Contains


@dataclass
class ValueSet_Expansion_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    value: ValueSet_Expansion_Parameter_ValueX


@dataclass
class ValueSet_Expansion_Parameter_ValueX:
    string_value: String
    boolean: Boolean
    integer: Integer
    decimal: Decimal
    uri: Uri
    code: Code
    date_time: DateTime


@dataclass
class ValueSet_Expansion_Contains:
    id: String
    extension: Extension
    modifier_extension: Extension
    system: Uri
    abstract: Boolean
    inactive: Boolean
    version: String
    code: Code
    display: String
    designation: ValueSet_Compose_ConceptSet_ConceptReference_Designation
    contains: ValueSet_Expansion_Contains

