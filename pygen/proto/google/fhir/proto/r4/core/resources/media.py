# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Media:
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
    status: Media_StatusCode
    type: CodeableConcept
    modality: CodeableConcept
    view: CodeableConcept
    subject: Reference
    encounter: Reference
    created: Media_CreatedX
    issued: Instant
    operator: Reference
    reason_code: CodeableConcept
    body_site: CodeableConcept
    device_name: String
    device: Reference
    height: PositiveInt
    width: PositiveInt
    frames: PositiveInt
    duration: Decimal
    content: Attachment
    note: Annotation


@dataclass
class Media_StatusCode:
    value: EventStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Media_CreatedX:
    date_time: DateTime
    period: Period

