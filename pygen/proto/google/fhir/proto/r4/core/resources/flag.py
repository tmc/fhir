# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Flag:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: Flag_StatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    period: Period
    encounter: Reference
    author: Reference


@dataclass
class Flag_StatusCode:
    value: FlagStatusCode_Value
    id: String
    extension: Extension

