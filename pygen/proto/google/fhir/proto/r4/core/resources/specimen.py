# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Specimen:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    accession_identifier: Identifier
    status: Specimen_StatusCode
    type: CodeableConcept
    subject: Reference
    received_time: DateTime
    parent: Reference
    request: Reference
    collection: Specimen_Collection
    processing: Specimen_Processing
    container: Specimen_Container
    condition: CodeableConcept
    note: Annotation


@dataclass
class Specimen_StatusCode:
    value: SpecimenStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Specimen_Collection:
    id: String
    extension: Extension
    modifier_extension: Extension
    collector: Reference
    collected: Specimen_Collection_CollectedX
    duration: Duration
    quantity: SimpleQuantity
    method: CodeableConcept
    body_site: CodeableConcept
    fasting_status: Specimen_Collection_FastingStatusX


@dataclass
class Specimen_Collection_CollectedX:
    date_time: DateTime
    period: Period


@dataclass
class Specimen_Collection_FastingStatusX:
    codeable_concept: CodeableConcept
    duration: Duration


@dataclass
class Specimen_Processing:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    procedure: CodeableConcept
    additive: Reference
    time: Specimen_Processing_TimeX


@dataclass
class Specimen_Processing_TimeX:
    date_time: DateTime
    period: Period


@dataclass
class Specimen_Container:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    description: String
    type: CodeableConcept
    capacity: SimpleQuantity
    specimen_quantity: SimpleQuantity
    additive: Specimen_Container_AdditiveX


@dataclass
class Specimen_Container_AdditiveX:
    codeable_concept: CodeableConcept
    reference: Reference

