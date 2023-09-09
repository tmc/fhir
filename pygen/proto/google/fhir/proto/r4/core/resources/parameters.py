# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Parameters:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    parameter: Parameters_Parameter


@dataclass
class Parameters_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    value: Parameters_Parameter_ValueX
    resource: Any
    part: Parameters_Parameter


@dataclass
class Parameters_Parameter_ValueX:
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

