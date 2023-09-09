# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Endpoint:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: Endpoint_StatusCode
    connection_type: Coding
    name: String
    managing_organization: Reference
    contact: ContactPoint
    period: Period
    payload_type: CodeableConcept
    payload_mime_type: Endpoint_PayloadMimeTypeCode
    address: Url
    header: String


@dataclass
class Endpoint_StatusCode:
    value: EndpointStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Endpoint_PayloadMimeTypeCode:
    id: String
    extension: Extension
    value: str

