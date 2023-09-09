# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class StructureMap:
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
    status: StructureMap_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    structure: StructureMap_Structure
    import: Canonical
    group: StructureMap_Group


@dataclass
class StructureMap_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMap_Structure:
    id: String
    extension: Extension
    modifier_extension: Extension
    url: Canonical
    mode: StructureMap_Structure_ModeCode
    alias: String
    documentation: String


@dataclass
class StructureMap_Structure_ModeCode:
    value: StructureMapModelModeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMap_Group:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: Id
    extends: Id
    type_mode: StructureMap_Group_TypeModeCode
    documentation: String
    input: StructureMap_Group_Input
    rule: StructureMap_Group_Rule


@dataclass
class StructureMap_Group_TypeModeCode:
    value: StructureMapGroupTypeModeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMap_Group_Input:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: Id
    type: String
    mode: StructureMap_Group_Input_ModeCode
    documentation: String


@dataclass
class StructureMap_Group_Input_ModeCode:
    value: StructureMapInputModeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMap_Group_Rule:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: Id
    source: StructureMap_Group_Rule_Source
    target: StructureMap_Group_Rule_Target
    rule: StructureMap_Group_Rule
    dependent: StructureMap_Group_Rule_Dependent
    documentation: String


@dataclass
class StructureMap_Group_Rule_Source:
    id: String
    extension: Extension
    modifier_extension: Extension
    context: Id
    min: Integer
    max: String
    type: String
    default_value: StructureMap_Group_Rule_Source_DefaultValueX
    element: String
    list_mode: StructureMap_Group_Rule_Source_ListModeCode
    variable: Id
    condition: String
    check: String
    log_message: String


@dataclass
class StructureMap_Group_Rule_Source_DefaultValueX:
    base64_binary: Base64Binary
    boolean: Boolean
    canonical: Canonical
    code: Code
    date: Date
    date_time: DateTime
    decimal: Decimal
    id: Id
    instant: Instant
    integer: Integer
    markdown: Markdown
    oid: Oid
    positive_int: PositiveInt
    string_value: String
    time: Time
    unsigned_int: UnsignedInt
    uri: Uri
    url: Url
    uuid: Uuid
    address: Address
    age: Age
    annotation: Annotation
    attachment: Attachment
    codeable_concept: CodeableConcept
    coding: Coding
    contact_point: ContactPoint
    count: Count
    distance: Distance
    duration: Duration
    human_name: HumanName
    identifier: Identifier
    money: Money
    period: Period
    quantity: Quantity
    range: Range
    ratio: Ratio
    reference: Reference
    sampled_data: SampledData
    signature: Signature
    timing: Timing
    contact_detail: ContactDetail
    contributor: Contributor
    data_requirement: DataRequirement
    expression: Expression
    parameter_definition: ParameterDefinition
    related_artifact: RelatedArtifact
    trigger_definition: TriggerDefinition
    usage_context: UsageContext
    dosage: Dosage
    meta: Meta


@dataclass
class StructureMap_Group_Rule_Source_ListModeCode:
    value: StructureMapSourceListModeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMap_Group_Rule_Target:
    id: String
    extension: Extension
    modifier_extension: Extension
    context: Id
    context_type: StructureMap_Group_Rule_Target_ContextTypeCode
    element: String
    variable: Id
    list_mode: StructureMap_Group_Rule_Target_ListModeCode
    list_rule_id: Id
    transform: StructureMap_Group_Rule_Target_TransformCode
    parameter: StructureMap_Group_Rule_Target_Parameter


@dataclass
class StructureMap_Group_Rule_Target_ContextTypeCode:
    value: StructureMapContextTypeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMap_Group_Rule_Target_ListModeCode:
    value: StructureMapTargetListModeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMap_Group_Rule_Target_TransformCode:
    value: StructureMapTransformCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMap_Group_Rule_Target_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    value: StructureMap_Group_Rule_Target_Parameter_ValueX


@dataclass
class StructureMap_Group_Rule_Target_Parameter_ValueX:
    id: Id
    string_value: String
    boolean: Boolean
    integer: Integer
    decimal: Decimal


@dataclass
class StructureMap_Group_Rule_Dependent:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: Id
    variable: String

