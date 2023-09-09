# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ImagingStudy:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ImagingStudy_StatusCode
    modality: Coding
    subject: Reference
    encounter: Reference
    started: DateTime
    based_on: Reference
    referrer: Reference
    interpreter: Reference
    endpoint: Reference
    number_of_series: UnsignedInt
    number_of_instances: UnsignedInt
    procedure_reference: Reference
    procedure_code: CodeableConcept
    location: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    note: Annotation
    description: String
    series: ImagingStudy_Series


@dataclass
class ImagingStudy_StatusCode:
    value: ImagingStudyStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ImagingStudy_Series:
    id: String
    extension: Extension
    modifier_extension: Extension
    uid: Id
    number: UnsignedInt
    modality: Coding
    description: String
    number_of_instances: UnsignedInt
    endpoint: Reference
    body_site: Coding
    laterality: Coding
    specimen: Reference
    started: DateTime
    performer: ImagingStudy_Series_Performer
    instance: ImagingStudy_Series_Instance


@dataclass
class ImagingStudy_Series_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    function: CodeableConcept
    actor: Reference


@dataclass
class ImagingStudy_Series_Instance:
    id: String
    extension: Extension
    modifier_extension: Extension
    uid: Id
    sop_class: Coding
    number: UnsignedInt
    title: String

