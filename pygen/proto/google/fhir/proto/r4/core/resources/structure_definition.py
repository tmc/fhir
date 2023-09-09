# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class StructureDefinition:
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
    status: StructureDefinition_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    keyword: Coding
    fhir_version: StructureDefinition_FhirVersionCode
    mapping: StructureDefinition_Mapping
    kind: StructureDefinition_KindCode
    abstract: Boolean
    context: StructureDefinition_Context
    context_invariant: String
    type: Uri
    base_definition: Canonical
    derivation: StructureDefinition_DerivationCode
    snapshot: StructureDefinition_Snapshot
    differential: StructureDefinition_Differential


@dataclass
class StructureDefinition_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class StructureDefinition_FhirVersionCode:
    value: FHIRVersionCode_Value
    id: String
    extension: Extension


@dataclass
class StructureDefinition_Mapping:
    id: String
    extension: Extension
    modifier_extension: Extension
    identity: Id
    uri: Uri
    name: String
    comment: String


@dataclass
class StructureDefinition_KindCode:
    value: StructureDefinitionKindCode_Value
    id: String
    extension: Extension


@dataclass
class StructureDefinition_Context:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: StructureDefinition_Context_TypeCode
    expression: String


@dataclass
class StructureDefinition_Context_TypeCode:
    value: ExtensionContextTypeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureDefinition_DerivationCode:
    value: TypeDerivationRuleCode_Value
    id: String
    extension: Extension


@dataclass
class StructureDefinition_Snapshot:
    id: String
    extension: Extension
    modifier_extension: Extension
    element: ElementDefinition


@dataclass
class StructureDefinition_Differential:
    id: String
    extension: Extension
    modifier_extension: Extension
    element: ElementDefinition

