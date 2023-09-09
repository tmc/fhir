# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Immunization:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: Immunization_StatusCode
    status_reason: CodeableConcept
    vaccine_code: CodeableConcept
    patient: Reference
    encounter: Reference
    occurrence: Immunization_OccurrenceX
    recorded: DateTime
    primary_source: Boolean
    report_origin: CodeableConcept
    location: Reference
    manufacturer: Reference
    lot_number: String
    expiration_date: Date
    site: CodeableConcept
    route: CodeableConcept
    dose_quantity: SimpleQuantity
    performer: Immunization_Performer
    note: Annotation
    reason_code: CodeableConcept
    reason_reference: Reference
    is_subpotent: Boolean
    subpotent_reason: CodeableConcept
    education: Immunization_Education
    program_eligibility: CodeableConcept
    funding_source: CodeableConcept
    reaction: Immunization_Reaction
    protocol_applied: Immunization_ProtocolApplied


@dataclass
class Immunization_StatusCode:
    value: ImmunizationStatusCodesValueSet_Value
    id: String
    extension: Extension


@dataclass
class Immunization_OccurrenceX:
    date_time: DateTime
    string_value: String


@dataclass
class Immunization_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    function: CodeableConcept
    actor: Reference


@dataclass
class Immunization_Education:
    id: String
    extension: Extension
    modifier_extension: Extension
    document_type: String
    reference: Uri
    publication_date: DateTime
    presentation_date: DateTime


@dataclass
class Immunization_Reaction:
    id: String
    extension: Extension
    modifier_extension: Extension
    date: DateTime
    detail: Reference
    reported: Boolean


@dataclass
class Immunization_ProtocolApplied:
    id: String
    extension: Extension
    modifier_extension: Extension
    series: String
    authority: Reference
    target_disease: CodeableConcept
    dose_number: Immunization_ProtocolApplied_DoseNumberX
    series_doses: Immunization_ProtocolApplied_SeriesDosesX


@dataclass
class Immunization_ProtocolApplied_DoseNumberX:
    positive_int: PositiveInt
    string_value: String


@dataclass
class Immunization_ProtocolApplied_SeriesDosesX:
    positive_int: PositiveInt
    string_value: String

