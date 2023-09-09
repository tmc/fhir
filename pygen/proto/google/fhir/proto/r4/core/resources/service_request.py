# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ServiceRequest:
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
    replaces: Reference
    requisition: Identifier
    status: ServiceRequest_StatusCode
    intent: ServiceRequest_IntentCode
    category: CodeableConcept
    priority: ServiceRequest_PriorityCode
    do_not_perform: Boolean
    code: CodeableConcept
    order_detail: CodeableConcept
    quantity: ServiceRequest_QuantityX
    subject: Reference
    encounter: Reference
    occurrence: ServiceRequest_OccurrenceX
    as_needed: ServiceRequest_AsNeededX
    authored_on: DateTime
    requester: Reference
    performer_type: CodeableConcept
    performer: Reference
    location_code: CodeableConcept
    location_reference: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    insurance: Reference
    supporting_info: Reference
    specimen: Reference
    body_site: CodeableConcept
    note: Annotation
    patient_instruction: String
    relevant_history: Reference


@dataclass
class ServiceRequest_StatusCode:
    value: RequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ServiceRequest_IntentCode:
    value: RequestIntentCode_Value
    id: String
    extension: Extension


@dataclass
class ServiceRequest_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class ServiceRequest_QuantityX:
    quantity: Quantity
    ratio: Ratio
    range: Range


@dataclass
class ServiceRequest_OccurrenceX:
    date_time: DateTime
    period: Period
    timing: Timing


@dataclass
class ServiceRequest_AsNeededX:
    boolean: Boolean
    codeable_concept: CodeableConcept

