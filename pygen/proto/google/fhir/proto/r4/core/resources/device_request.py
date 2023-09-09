# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class DeviceRequest:
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
    prior_request: Reference
    group_identifier: Identifier
    status: DeviceRequest_StatusCode
    intent: DeviceRequest_IntentCode
    priority: DeviceRequest_PriorityCode
    code: DeviceRequest_CodeX
    parameter: DeviceRequest_Parameter
    subject: Reference
    encounter: Reference
    occurrence: DeviceRequest_OccurrenceX
    authored_on: DateTime
    requester: Reference
    performer_type: CodeableConcept
    performer: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    insurance: Reference
    supporting_info: Reference
    note: Annotation
    relevant_history: Reference


@dataclass
class DeviceRequest_StatusCode:
    value: RequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceRequest_IntentCode:
    value: RequestIntentCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceRequest_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceRequest_CodeX:
    reference: Reference
    codeable_concept: CodeableConcept


@dataclass
class DeviceRequest_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: DeviceRequest_Parameter_ValueX


@dataclass
class DeviceRequest_Parameter_ValueX:
    codeable_concept: CodeableConcept
    quantity: Quantity
    range: Range
    boolean: Boolean


@dataclass
class DeviceRequest_OccurrenceX:
    date_time: DateTime
    period: Period
    timing: Timing

