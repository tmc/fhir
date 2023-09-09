# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class SearchParameter:
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
    derived_from: Canonical
    status: SearchParameter_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    code: Code
    base: SearchParameter_BaseCode
    type: SearchParameter_TypeCode
    expression: String
    xpath: String
    xpath_usage: SearchParameter_XpathUsageCode
    target: SearchParameter_TargetCode
    multiple_or: Boolean
    multiple_and: Boolean
    comparator: SearchParameter_ComparatorCode
    modifier: SearchParameter_ModifierCode
    chain: String
    component: SearchParameter_Component


@dataclass
class SearchParameter_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class SearchParameter_BaseCode:
    value: ResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class SearchParameter_TypeCode:
    value: SearchParamTypeCode_Value
    id: String
    extension: Extension


@dataclass
class SearchParameter_XpathUsageCode:
    value: XPathUsageTypeCode_Value
    id: String
    extension: Extension


@dataclass
class SearchParameter_TargetCode:
    value: ResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class SearchParameter_ComparatorCode:
    value: SearchComparatorCode_Value
    id: String
    extension: Extension


@dataclass
class SearchParameter_ModifierCode:
    value: SearchModifierCode_Value
    id: String
    extension: Extension


@dataclass
class SearchParameter_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    definition: Canonical
    expression: String

