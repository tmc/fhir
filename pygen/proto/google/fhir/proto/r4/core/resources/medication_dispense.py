# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicationDispense:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    part_of: Reference
    status: MedicationDispense_StatusCode
    status_reason: MedicationDispense_StatusReasonX
    category: CodeableConcept
    medication: MedicationDispense_MedicationX
    subject: Reference
    context: Reference
    supporting_information: Reference
    performer: MedicationDispense_Performer
    location: Reference
    authorizing_prescription: Reference
    type: CodeableConcept
    quantity: SimpleQuantity
    days_supply: SimpleQuantity
    when_prepared: DateTime
    when_handed_over: DateTime
    destination: Reference
    receiver: Reference
    note: Annotation
    dosage_instruction: Dosage
    substitution: MedicationDispense_Substitution
    detected_issue: Reference
    event_history: Reference


@dataclass
class MedicationDispense_StatusCode:
    value: MedicationDispenseStatusCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationDispense_StatusReasonX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class MedicationDispense_MedicationX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class MedicationDispense_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    function: CodeableConcept
    actor: Reference


@dataclass
class MedicationDispense_Substitution:
    id: String
    extension: Extension
    modifier_extension: Extension
    was_substituted: Boolean
    type: CodeableConcept
    reason: CodeableConcept
    responsible_party: Reference

