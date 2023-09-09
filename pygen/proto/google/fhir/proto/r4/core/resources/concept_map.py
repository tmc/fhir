# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ConceptMap:
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
    status: ConceptMap_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    source: ConceptMap_SourceX
    target: ConceptMap_TargetX
    group: ConceptMap_Group


@dataclass
class ConceptMap_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ConceptMap_SourceX:
    uri: Uri
    canonical: Canonical


@dataclass
class ConceptMap_TargetX:
    uri: Uri
    canonical: Canonical


@dataclass
class ConceptMap_Group:
    id: String
    extension: Extension
    modifier_extension: Extension
    source: Uri
    source_version: String
    target: Uri
    target_version: String
    element: ConceptMap_Group_SourceElement
    unmapped: ConceptMap_Group_Unmapped


@dataclass
class ConceptMap_Group_SourceElement:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    display: String
    target: ConceptMap_Group_SourceElement_TargetElement


@dataclass
class ConceptMap_Group_SourceElement_TargetElement:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    display: String
    equivalence: ConceptMap_Group_SourceElement_TargetElement_EquivalenceCode
    comment: String
    depends_on: ConceptMap_Group_SourceElement_TargetElement_OtherElement
    product: ConceptMap_Group_SourceElement_TargetElement_OtherElement


@dataclass
class ConceptMap_Group_SourceElement_TargetElement_EquivalenceCode:
    value: ConceptMapEquivalenceCode_Value
    id: String
    extension: Extension


@dataclass
class ConceptMap_Group_SourceElement_TargetElement_OtherElement:
    id: String
    extension: Extension
    modifier_extension: Extension
    property: Uri
    system: Canonical
    value: String
    display: String


@dataclass
class ConceptMap_Group_Unmapped:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: ConceptMap_Group_Unmapped_ModeCode
    code: Code
    display: String
    url: Canonical


@dataclass
class ConceptMap_Group_Unmapped_ModeCode:
    value: ConceptMapGroupUnmappedModeCode_Value
    id: String
    extension: Extension

