# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Goal:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    lifecycle_status: Goal_LifecycleStatusCode
    achievement_status: CodeableConcept
    category: CodeableConcept
    priority: CodeableConcept
    description: CodeableConcept
    subject: Reference
    start: Goal_StartX
    target: Goal_Target
    status_date: Date
    status_reason: String
    expressed_by: Reference
    addresses: Reference
    note: Annotation
    outcome_code: CodeableConcept
    outcome_reference: Reference


@dataclass
class Goal_LifecycleStatusCode:
    value: GoalLifecycleStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Goal_StartX:
    date: Date
    codeable_concept: CodeableConcept


@dataclass
class Goal_Target:
    id: String
    extension: Extension
    modifier_extension: Extension
    measure: CodeableConcept
    detail: Goal_Target_DetailX
    due: Goal_Target_DueX


@dataclass
class Goal_Target_DetailX:
    quantity: Quantity
    range: Range
    codeable_concept: CodeableConcept
    string_value: String
    boolean: Boolean
    integer: Integer
    ratio: Ratio


@dataclass
class Goal_Target_DueX:
    date: Date
    duration: Duration

