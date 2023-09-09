# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ShareableCodeSystem:
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
    status: ShareableCodeSystem_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    case_sensitive: Boolean
    value_set: Canonical
    hierarchy_meaning: ShareableCodeSystem_HierarchyMeaningCode
    compositional: Boolean
    version_needed: Boolean
    content: ShareableCodeSystem_ContentCode
    supplements: Canonical
    count: UnsignedInt
    filter: ShareableCodeSystem_Filter
    property: ShareableCodeSystem_Property
    concept: ShareableCodeSystem_ConceptDefinition


@dataclass
class ShareableCodeSystem_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ShareableCodeSystem_HierarchyMeaningCode:
    value: CodeSystemHierarchyMeaningCode_Value
    id: String
    extension: Extension


@dataclass
class ShareableCodeSystem_ContentCode:
    value: CodeSystemContentModeCode_Value
    id: String
    extension: Extension


@dataclass
class ShareableCodeSystem_Filter:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    description: String
    operator: ShareableCodeSystem_Filter_OperatorCode
    value: String


@dataclass
class ShareableCodeSystem_Filter_OperatorCode:
    value: FilterOperatorCode_Value
    id: String
    extension: Extension


@dataclass
class ShareableCodeSystem_Property:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    uri: Uri
    description: String
    type: ShareableCodeSystem_Property_TypeCode


@dataclass
class ShareableCodeSystem_Property_TypeCode:
    value: PropertyTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ShareableCodeSystem_ConceptDefinition:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    display: String
    definition: String
    designation: ShareableCodeSystem_ConceptDefinition_Designation
    property: ShareableCodeSystem_ConceptDefinition_ConceptProperty
    concept: ShareableCodeSystem_ConceptDefinition


@dataclass
class ShareableCodeSystem_ConceptDefinition_Designation:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: Code
    use: Coding
    value: String


@dataclass
class ShareableCodeSystem_ConceptDefinition_ConceptProperty:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    value: ShareableCodeSystem_ConceptDefinition_ConceptProperty_ValueX


@dataclass
class ShareableCodeSystem_ConceptDefinition_ConceptProperty_ValueX:
    code: Code
    coding: Coding
    string_value: String
    integer: Integer
    boolean: Boolean
    date_time: DateTime
    decimal: Decimal

