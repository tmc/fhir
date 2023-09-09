# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicationRequest:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: MedicationRequest_StatusCode
    status_reason: CodeableConcept
    intent: MedicationRequest_IntentCode
    category: CodeableConcept
    priority: MedicationRequest_PriorityCode
    do_not_perform: Boolean
    reported: MedicationRequest_ReportedX
    medication: MedicationRequest_MedicationX
    subject: Reference
    encounter: Reference
    supporting_information: Reference
    authored_on: DateTime
    requester: Reference
    performer: Reference
    performer_type: CodeableConcept
    recorder: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    instantiates_canonical: Canonical
    instantiates_uri: Uri
    based_on: Reference
    group_identifier: Identifier
    course_of_therapy_type: CodeableConcept
    insurance: Reference
    note: Annotation
    dosage_instruction: Dosage
    dispense_request: MedicationRequest_DispenseRequest
    substitution: MedicationRequest_Substitution
    prior_prescription: Reference
    detected_issue: Reference
    event_history: Reference


@dataclass
class MedicationRequest_StatusCode:
    value: MedicationrequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationRequest_IntentCode:
    value: MedicationRequestIntentCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationRequest_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationRequest_ReportedX:
    boolean: Boolean
    reference: Reference


@dataclass
class MedicationRequest_MedicationX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class MedicationRequest_DispenseRequest:
    id: String
    extension: Extension
    modifier_extension: Extension
    initial_fill: MedicationRequest_DispenseRequest_InitialFill
    dispense_interval: Duration
    validity_period: Period
    number_of_repeats_allowed: UnsignedInt
    quantity: SimpleQuantity
    expected_supply_duration: Duration
    performer: Reference


@dataclass
class MedicationRequest_DispenseRequest_InitialFill:
    id: String
    extension: Extension
    modifier_extension: Extension
    quantity: SimpleQuantity
    duration: Duration


@dataclass
class MedicationRequest_Substitution:
    id: String
    extension: Extension
    modifier_extension: Extension
    allowed: MedicationRequest_Substitution_AllowedX
    reason: CodeableConcept


@dataclass
class MedicationRequest_Substitution_AllowedX:
    boolean: Boolean
    codeable_concept: CodeableConcept

