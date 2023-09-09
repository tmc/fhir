# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Communication:
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
    part_of: Reference
    in_response_to: Reference
    status: Communication_StatusCode
    status_reason: CodeableConcept
    category: CodeableConcept
    priority: Communication_PriorityCode
    medium: CodeableConcept
    subject: Reference
    topic: CodeableConcept
    about: Reference
    encounter: Reference
    sent: DateTime
    received: DateTime
    recipient: Reference
    sender: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    payload: Communication_Payload
    note: Annotation


@dataclass
class Communication_StatusCode:
    value: EventStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Communication_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class Communication_Payload:
    id: String
    extension: Extension
    modifier_extension: Extension
    content: Communication_Payload_ContentX


@dataclass
class Communication_Payload_ContentX:
    string_value: String
    attachment: Attachment
    reference: Reference

