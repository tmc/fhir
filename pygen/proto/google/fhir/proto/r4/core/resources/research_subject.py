# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ResearchSubject:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ResearchSubject_StatusCode
    period: Period
    study: Reference
    individual: Reference
    assigned_arm: String
    actual_arm: String
    consent: Reference


@dataclass
class ResearchSubject_StatusCode:
    value: ResearchSubjectStatusCode_Value
    id: String
    extension: Extension

