# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ServiceRequestGenetics:
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
    status: ServiceRequestGenetics_StatusCode
    intent: ServiceRequestGenetics_IntentCode
    category: CodeableConcept
    priority: ServiceRequestGenetics_PriorityCode
    do_not_perform: Boolean
    code: CodeableConcept
    order_detail: CodeableConcept
    quantity: ServiceRequestGenetics_QuantityX
    subject: Reference
    encounter: Reference
    occurrence: ServiceRequestGenetics_OccurrenceX
    as_needed: ServiceRequestGenetics_AsNeededX
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
    item: DiagnosticReportItem


@dataclass
class ServiceRequestGenetics_StatusCode:
    value: RequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ServiceRequestGenetics_IntentCode:
    value: RequestIntentCode_Value
    id: String
    extension: Extension


@dataclass
class ServiceRequestGenetics_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class ServiceRequestGenetics_QuantityX:
    quantity: Quantity
    ratio: Ratio
    range: Range


@dataclass
class ServiceRequestGenetics_OccurrenceX:
    date_time: DateTime
    period: Period
    timing: Timing


@dataclass
class ServiceRequestGenetics_AsNeededX:
    boolean: Boolean
    codeable_concept: CodeableConcept

