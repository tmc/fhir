# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class CarePlan:
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
    replaces: Reference
    part_of: Reference
    status: CarePlan_StatusCode
    intent: CarePlan_IntentCode
    category: CodeableConcept
    title: String
    description: String
    subject: Reference
    encounter: Reference
    period: Period
    created: DateTime
    author: Reference
    contributor: Reference
    care_team: Reference
    addresses: Reference
    supporting_info: Reference
    goal: Reference
    activity: CarePlan_Activity
    note: Annotation


@dataclass
class CarePlan_StatusCode:
    value: RequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CarePlan_IntentCode:
    value: CarePlanIntentValueSet_Value
    id: String
    extension: Extension


@dataclass
class CarePlan_Activity:
    id: String
    extension: Extension
    modifier_extension: Extension
    outcome_codeable_concept: CodeableConcept
    outcome_reference: Reference
    progress: Annotation
    reference: Reference
    detail: CarePlan_Activity_Detail


@dataclass
class CarePlan_Activity_Detail:
    id: String
    extension: Extension
    modifier_extension: Extension
    kind: CarePlan_Activity_Detail_KindCode
    instantiates_canonical: Canonical
    instantiates_uri: Uri
    code: CodeableConcept
    reason_code: CodeableConcept
    reason_reference: Reference
    goal: Reference
    status: CarePlan_Activity_Detail_StatusCode
    status_reason: CodeableConcept
    do_not_perform: Boolean
    scheduled: CarePlan_Activity_Detail_ScheduledX
    location: Reference
    performer: Reference
    product: CarePlan_Activity_Detail_ProductX
    daily_amount: SimpleQuantity
    quantity: SimpleQuantity
    description: String


@dataclass
class CarePlan_Activity_Detail_KindCode:
    value: CarePlanActivityKindValueSet_Value
    id: String
    extension: Extension


@dataclass
class CarePlan_Activity_Detail_StatusCode:
    value: CarePlanActivityStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CarePlan_Activity_Detail_ScheduledX:
    timing: Timing
    period: Period
    string_value: String


@dataclass
class CarePlan_Activity_Detail_ProductX:
    codeable_concept: CodeableConcept
    reference: Reference

