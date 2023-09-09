# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MessageHeader:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    event: MessageHeader_EventX
    destination: MessageHeader_MessageDestination
    sender: Reference
    enterer: Reference
    author: Reference
    source: MessageHeader_MessageSource
    responsible: Reference
    reason: CodeableConcept
    response: MessageHeader_Response
    focus: Reference
    definition: Canonical


@dataclass
class MessageHeader_EventX:
    coding: Coding
    uri: Uri


@dataclass
class MessageHeader_MessageDestination:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    target: Reference
    endpoint: Url
    receiver: Reference


@dataclass
class MessageHeader_MessageSource:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    software: String
    version: String
    contact: ContactPoint
    endpoint: Url


@dataclass
class MessageHeader_Response:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Id
    code: MessageHeader_Response_CodeType
    details: Reference


@dataclass
class MessageHeader_Response_CodeType:
    value: ResponseTypeCode_Value
    id: String
    extension: Extension

