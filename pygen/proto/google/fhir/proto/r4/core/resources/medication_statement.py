# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicationStatement:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    part_of: Reference
    status: MedicationStatement_StatusCode
    status_reason: CodeableConcept
    category: CodeableConcept
    medication: MedicationStatement_MedicationX
    subject: Reference
    context: Reference
    effective: MedicationStatement_EffectiveX
    date_asserted: DateTime
    information_source: Reference
    derived_from: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    note: Annotation
    dosage: Dosage


@dataclass
class MedicationStatement_StatusCode:
    value: MedicationStatementStatusCodes_Value
    id: String
    extension: Extension


@dataclass
class MedicationStatement_MedicationX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class MedicationStatement_EffectiveX:
    date_time: DateTime
    period: Period

