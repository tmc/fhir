# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class CommunicationRequest:
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
    replaces: Reference
    group_identifier: Identifier
    status: CommunicationRequest_StatusCode
    status_reason: CodeableConcept
    category: CodeableConcept
    priority: CommunicationRequest_PriorityCode
    do_not_perform: Boolean
    medium: CodeableConcept
    subject: Reference
    about: Reference
    encounter: Reference
    payload: CommunicationRequest_Payload
    occurrence: CommunicationRequest_OccurrenceX
    authored_on: DateTime
    requester: Reference
    recipient: Reference
    sender: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    note: Annotation


@dataclass
class CommunicationRequest_StatusCode:
    value: RequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CommunicationRequest_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class CommunicationRequest_Payload:
    id: String
    extension: Extension
    modifier_extension: Extension
    content: CommunicationRequest_Payload_ContentX


@dataclass
class CommunicationRequest_Payload_ContentX:
    string_value: String
    attachment: Attachment
    reference: Reference


@dataclass
class CommunicationRequest_OccurrenceX:
    date_time: DateTime
    period: Period

