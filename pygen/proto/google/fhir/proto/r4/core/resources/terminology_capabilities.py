# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class TerminologyCapabilities:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    url: Uri
    version: String
    name: String
    title: String
    status: TerminologyCapabilities_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    kind: TerminologyCapabilities_KindCode
    software: TerminologyCapabilities_Software
    implementation: TerminologyCapabilities_Implementation
    locked_date: Boolean
    code_system: TerminologyCapabilities_CodeSystem
    expansion: TerminologyCapabilities_Expansion
    code_search: TerminologyCapabilities_CodeSearchCode
    validate_code: TerminologyCapabilities_ValidateCode
    translation: TerminologyCapabilities_Translation
    closure: TerminologyCapabilities_Closure


@dataclass
class TerminologyCapabilities_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class TerminologyCapabilities_KindCode:
    value: CapabilityStatementKindCode_Value
    id: String
    extension: Extension


@dataclass
class TerminologyCapabilities_Software:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    version: String


@dataclass
class TerminologyCapabilities_Implementation:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    url: Url


@dataclass
class TerminologyCapabilities_CodeSystem:
    id: String
    extension: Extension
    modifier_extension: Extension
    uri: Canonical
    version: TerminologyCapabilities_CodeSystem_Version
    subsumption: Boolean


@dataclass
class TerminologyCapabilities_CodeSystem_Version:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: String
    is_default: Boolean
    compositional: Boolean
    language: Code
    filter: TerminologyCapabilities_CodeSystem_Version_Filter
    property: Code


@dataclass
class TerminologyCapabilities_CodeSystem_Version_Filter:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    op: Code


@dataclass
class TerminologyCapabilities_Expansion:
    id: String
    extension: Extension
    modifier_extension: Extension
    hierarchical: Boolean
    paging: Boolean
    incomplete: Boolean
    parameter: TerminologyCapabilities_Expansion_Parameter
    text_filter: Markdown


@dataclass
class TerminologyCapabilities_Expansion_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: Code
    documentation: String


@dataclass
class TerminologyCapabilities_CodeSearchCode:
    value: CodeSearchSupportCode_Value
    id: String
    extension: Extension


@dataclass
class TerminologyCapabilities_ValidateCode:
    id: String
    extension: Extension
    modifier_extension: Extension
    translations: Boolean


@dataclass
class TerminologyCapabilities_Translation:
    id: String
    extension: Extension
    modifier_extension: Extension
    needs_map: Boolean


@dataclass
class TerminologyCapabilities_Closure:
    id: String
    extension: Extension
    modifier_extension: Extension
    translation: Boolean

