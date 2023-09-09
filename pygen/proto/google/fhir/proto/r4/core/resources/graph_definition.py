# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class GraphDefinition:
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
    status: GraphDefinition_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    start: GraphDefinition_StartCode
    profile: Canonical
    link: GraphDefinition_Link


@dataclass
class GraphDefinition_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class GraphDefinition_StartCode:
    value: ResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class GraphDefinition_Link:
    id: String
    extension: Extension
    modifier_extension: Extension
    path: String
    slice_name: String
    min: Integer
    max: String
    description: String
    target: GraphDefinition_Link_Target


@dataclass
class GraphDefinition_Link_Target:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: GraphDefinition_Link_Target_TypeCode
    params: String
    profile: Canonical
    compartment: GraphDefinition_Link_Target_Compartment
    link: GraphDefinition_Link


@dataclass
class GraphDefinition_Link_Target_TypeCode:
    value: ResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class GraphDefinition_Link_Target_Compartment:
    id: String
    extension: Extension
    modifier_extension: Extension
    use: GraphDefinition_Link_Target_Compartment_UseCode
    code: GraphDefinition_Link_Target_Compartment_CodeType
    rule: GraphDefinition_Link_Target_Compartment_RuleCode
    expression: String
    description: String


@dataclass
class GraphDefinition_Link_Target_Compartment_UseCode:
    value: GraphCompartmentUseCode_Value
    id: String
    extension: Extension


@dataclass
class GraphDefinition_Link_Target_Compartment_CodeType:
    value: CompartmentTypeCode_Value
    id: String
    extension: Extension


@dataclass
class GraphDefinition_Link_Target_Compartment_RuleCode:
    value: GraphCompartmentRuleCode_Value
    id: String
    extension: Extension

