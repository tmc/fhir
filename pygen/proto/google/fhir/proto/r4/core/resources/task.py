# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Task:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    instantiates_canonical: Canonical
    instantiates_uri: Uri
    based_on: Reference
    group_identifier: Identifier
    part_of: Reference
    status: Task_StatusCode
    status_reason: CodeableConcept
    business_status: CodeableConcept
    intent: Task_IntentCode
    priority: Task_PriorityCode
    code: CodeableConcept
    description: String
    focus: Reference
    for_value: Reference
    encounter: Reference
    execution_period: Period
    authored_on: DateTime
    last_modified: DateTime
    requester: Reference
    performer_type: CodeableConcept
    owner: Reference
    location: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    insurance: Reference
    note: Annotation
    relevant_history: Reference
    restriction: Task_Restriction
    input: Task_Parameter
    output: Task_Output


@dataclass
class Task_StatusCode:
    value: TaskStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Task_IntentCode:
    value: TaskIntentValueSet_Value
    id: String
    extension: Extension


@dataclass
class Task_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class Task_Restriction:
    id: String
    extension: Extension
    modifier_extension: Extension
    repetitions: PositiveInt
    period: Period
    recipient: Reference


@dataclass
class Task_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    value: Task_Parameter_ValueX


@dataclass
class Task_Parameter_ValueX:
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
class Task_Output:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    value: Task_Output_ValueX


@dataclass
class Task_Output_ValueX:
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

