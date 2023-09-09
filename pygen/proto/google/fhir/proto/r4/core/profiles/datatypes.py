# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class DataElementConstraintOnElementDefinitionDataType:
    id: String
    extension: Extension
    modifier_extension: Extension
    path: String
    slice_name: String
    slice_is_constraining: Boolean
    label: String
    code: Coding
    definition: Markdown
    comment: Markdown
    requirements: Markdown
    alias: String
    min: UnsignedInt
    max: String
    base: DataElementConstraintOnElementDefinitionDataType_Base
    type: DataElementConstraintOnElementDefinitionDataType_TypeRef
    default_value: DataElementConstraintOnElementDefinitionDataType_DefaultValueX
    meaning_when_missing: Markdown
    order_meaning: String
    example: DataElementConstraintOnElementDefinitionDataType_Example
    min_value: DataElementConstraintOnElementDefinitionDataType_MinValueX
    max_value: DataElementConstraintOnElementDefinitionDataType_MaxValueX
    max_length: Integer
    condition: Id
    constraint: DataElementConstraintOnElementDefinitionDataType_Constraint
    must_support: Boolean
    is_modifier_reason: String
    binding: DataElementConstraintOnElementDefinitionDataType_ElementDefinitionBinding
    mapping: DataElementConstraintOnElementDefinitionDataType_Mapping
    question: String
    allowed_units: ElementDefinitionAllowedUnits_ValueX


@dataclass
class DataElementConstraintOnElementDefinitionDataType_Base:
    id: String
    extension: Extension
    path: String
    min: UnsignedInt
    max: String


@dataclass
class DataElementConstraintOnElementDefinitionDataType_TypeRef:
    id: String
    extension: Extension
    code: Uri
    target_profile: Canonical
    versioning: DataElementConstraintOnElementDefinitionDataType_TypeRef_VersioningCode


@dataclass
class DataElementConstraintOnElementDefinitionDataType_TypeRef_VersioningCode:
    value: ReferenceVersionRulesCode_Value
    id: String
    extension: Extension


@dataclass
class DataElementConstraintOnElementDefinitionDataType_DefaultValueX:
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


@dataclass
class DataElementConstraintOnElementDefinitionDataType_Example:
    id: String
    extension: Extension
    label: String
    value: DataElementConstraintOnElementDefinitionDataType_Example_ValueX


@dataclass
class DataElementConstraintOnElementDefinitionDataType_Example_ValueX:
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


@dataclass
class DataElementConstraintOnElementDefinitionDataType_MinValueX:
    date: Date
    date_time: DateTime
    instant: Instant
    time: Time
    decimal: Decimal
    integer: Integer
    positive_int: PositiveInt
    unsigned_int: UnsignedInt
    quantity: Quantity


@dataclass
class DataElementConstraintOnElementDefinitionDataType_MaxValueX:
    date: Date
    date_time: DateTime
    instant: Instant
    time: Time
    decimal: Decimal
    integer: Integer
    positive_int: PositiveInt
    unsigned_int: UnsignedInt
    quantity: Quantity


@dataclass
class DataElementConstraintOnElementDefinitionDataType_Constraint:
    id: String
    extension: Extension
    key: Id
    requirements: String
    severity: DataElementConstraintOnElementDefinitionDataType_Constraint_SeverityCode
    human: String
    expression: String
    xpath: String
    source: Canonical


@dataclass
class DataElementConstraintOnElementDefinitionDataType_Constraint_SeverityCode:
    value: ConstraintSeverityCode_Value
    id: String
    extension: Extension


@dataclass
class DataElementConstraintOnElementDefinitionDataType_ElementDefinitionBinding:
    id: String
    extension: Extension
    strength: DataElementConstraintOnElementDefinitionDataType_ElementDefinitionBinding_StrengthCode
    description: String
    value_set: Canonical


@dataclass
class DataElementConstraintOnElementDefinitionDataType_ElementDefinitionBinding_StrengthCode:
    value: BindingStrengthCode_Value
    id: String
    extension: Extension


@dataclass
class DataElementConstraintOnElementDefinitionDataType_Mapping:
    id: String
    extension: Extension
    identity: Id
    language: DataElementConstraintOnElementDefinitionDataType_Mapping_LanguageCode
    map: String
    comment: String


@dataclass
class DataElementConstraintOnElementDefinitionDataType_Mapping_LanguageCode:
    id: String
    extension: Extension
    value: str

