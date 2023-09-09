# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicationAdministration:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    instantiates: Uri
    part_of: Reference
    status: MedicationAdministration_StatusCode
    status_reason: CodeableConcept
    category: CodeableConcept
    medication: MedicationAdministration_MedicationX
    subject: Reference
    context: Reference
    supporting_information: Reference
    effective: MedicationAdministration_EffectiveX
    performer: MedicationAdministration_Performer
    reason_code: CodeableConcept
    reason_reference: Reference
    request: Reference
    device: Reference
    note: Annotation
    dosage: MedicationAdministration_Dosage
    event_history: Reference


@dataclass
class MedicationAdministration_StatusCode:
    value: MedicationAdministrationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationAdministration_MedicationX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class MedicationAdministration_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class MedicationAdministration_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    function: CodeableConcept
    actor: Reference


@dataclass
class MedicationAdministration_Dosage:
    id: String
    extension: Extension
    modifier_extension: Extension
    text: String
    site: CodeableConcept
    route: CodeableConcept
    method: CodeableConcept
    dose: SimpleQuantity
    rate: MedicationAdministration_Dosage_RateX


@dataclass
class MedicationAdministration_Dosage_RateX:
    ratio: Ratio
    quantity: SimpleQuantity

