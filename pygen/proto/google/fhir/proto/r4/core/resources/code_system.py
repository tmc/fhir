# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class CodeSystem:
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
    status: CodeSystem_StatusCode
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
    hierarchy_meaning: CodeSystem_HierarchyMeaningCode
    compositional: Boolean
    version_needed: Boolean
    content: CodeSystem_ContentCode
    supplements: Canonical
    count: UnsignedInt
    filter: CodeSystem_Filter
    property: CodeSystem_Property
    concept: CodeSystem_ConceptDefinition


@dataclass
class CodeSystem_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CodeSystem_HierarchyMeaningCode:
    value: CodeSystemHierarchyMeaningCode_Value
    id: String
    extension: Extension


@dataclass
class CodeSystem_ContentCode:
    value: CodeSystemContentModeCode_Value
    id: String
    extension: Extension


@dataclass
class CodeSystem_Filter:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    description: String
    operator: CodeSystem_Filter_OperatorCode
    value: String


@dataclass
class CodeSystem_Filter_OperatorCode:
    value: FilterOperatorCode_Value
    id: String
    extension: Extension


@dataclass
class CodeSystem_Property:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    uri: Uri
    description: String
    type: CodeSystem_Property_TypeCode


@dataclass
class CodeSystem_Property_TypeCode:
    value: PropertyTypeCode_Value
    id: String
    extension: Extension


@dataclass
class CodeSystem_ConceptDefinition:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    display: String
    definition: String
    designation: CodeSystem_ConceptDefinition_Designation
    property: CodeSystem_ConceptDefinition_ConceptProperty
    concept: CodeSystem_ConceptDefinition


@dataclass
class CodeSystem_ConceptDefinition_Designation:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: Code
    use: Coding
    value: String


@dataclass
class CodeSystem_ConceptDefinition_ConceptProperty:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    value: CodeSystem_ConceptDefinition_ConceptProperty_ValueX


@dataclass
class CodeSystem_ConceptDefinition_ConceptProperty_ValueX:
    code: Code
    coding: Coding
    string_value: String
    integer: Integer
    boolean: Boolean
    date_time: DateTime
    decimal: Decimal

