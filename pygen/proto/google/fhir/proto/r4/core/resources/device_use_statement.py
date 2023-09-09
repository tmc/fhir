# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class DeviceUseStatement:
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
    status: DeviceUseStatement_StatusCode
    subject: Reference
    derived_from: Reference
    timing: DeviceUseStatement_TimingX
    recorded_on: DateTime
    source: Reference
    device: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    body_site: CodeableConcept
    note: Annotation


@dataclass
class DeviceUseStatement_StatusCode:
    value: DeviceUseStatementStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceUseStatement_TimingX:
    timing: Timing
    period: Period
    date_time: DateTime

