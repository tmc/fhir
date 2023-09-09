# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class CompartmentDefinition:
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
    status: CompartmentDefinition_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    purpose: Markdown
    code: CompartmentDefinition_CodeType
    search: Boolean
    resource: CompartmentDefinition_Resource


@dataclass
class CompartmentDefinition_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CompartmentDefinition_CodeType:
    value: CompartmentTypeCode_Value
    id: String
    extension: Extension


@dataclass
class CompartmentDefinition_Resource:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CompartmentDefinition_Resource_CodeType
    param: String
    documentation: String


@dataclass
class CompartmentDefinition_Resource_CodeType:
    value: ResourceTypeCode_Value
    id: String
    extension: Extension

