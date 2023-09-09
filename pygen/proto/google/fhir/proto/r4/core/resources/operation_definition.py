# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class OperationDefinition:
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
    status: OperationDefinition_StatusCode
    kind: OperationDefinition_KindCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    affects_state: Boolean
    code: Code
    comment: Markdown
    base: Canonical
    resource: OperationDefinition_ResourceCode
    system: Boolean
    type: Boolean
    instance: Boolean
    input_profile: Canonical
    output_profile: Canonical
    parameter: OperationDefinition_Parameter
    overload: OperationDefinition_Overload


@dataclass
class OperationDefinition_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class OperationDefinition_KindCode:
    value: OperationKindCode_Value
    id: String
    extension: Extension


@dataclass
class OperationDefinition_ResourceCode:
    value: ResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class OperationDefinition_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: Code
    use: OperationDefinition_Parameter_UseCode
    min: Integer
    max: String
    documentation: String
    type: OperationDefinition_Parameter_TypeCode
    target_profile: Canonical
    search_type: OperationDefinition_Parameter_SearchTypeCode
    binding: OperationDefinition_Parameter_Binding
    referenced_from: OperationDefinition_Parameter_ReferencedFrom
    part: OperationDefinition_Parameter


@dataclass
class OperationDefinition_Parameter_UseCode:
    value: OperationParameterUseCode_Value
    id: String
    extension: Extension


@dataclass
class OperationDefinition_Parameter_TypeCode:
    value: FHIRAllTypesValueSet_Value
    id: String
    extension: Extension


@dataclass
class OperationDefinition_Parameter_SearchTypeCode:
    value: SearchParamTypeCode_Value
    id: String
    extension: Extension


@dataclass
class OperationDefinition_Parameter_Binding:
    id: String
    extension: Extension
    modifier_extension: Extension
    strength: OperationDefinition_Parameter_Binding_StrengthCode
    value_set: Canonical


@dataclass
class OperationDefinition_Parameter_Binding_StrengthCode:
    value: BindingStrengthCode_Value
    id: String
    extension: Extension


@dataclass
class OperationDefinition_Parameter_ReferencedFrom:
    id: String
    extension: Extension
    modifier_extension: Extension
    source: String
    source_id: String


@dataclass
class OperationDefinition_Overload:
    id: String
    extension: Extension
    modifier_extension: Extension
    parameter_name: String
    comment: String

