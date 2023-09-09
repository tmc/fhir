# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ActivityDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    subtitle: String
    status: ActivityDefinition_StatusCode
    experimental: Boolean
    subject: ActivityDefinition_SubjectX
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    usage: String
    copyright: Markdown
    approval_date: Date
    last_review_date: Date
    effective_period: Period
    topic: CodeableConcept
    author: ContactDetail
    editor: ContactDetail
    reviewer: ContactDetail
    endorser: ContactDetail
    related_artifact: RelatedArtifact
    library: Canonical
    kind: ActivityDefinition_KindCode
    profile: Canonical
    code: CodeableConcept
    intent: ActivityDefinition_IntentCode
    priority: ActivityDefinition_PriorityCode
    do_not_perform: Boolean
    timing: ActivityDefinition_TimingX
    location: Reference
    participant: ActivityDefinition_Participant
    product: ActivityDefinition_ProductX
    quantity: SimpleQuantity
    dosage: Dosage
    body_site: CodeableConcept
    specimen_requirement: Reference
    observation_requirement: Reference
    observation_result_requirement: Reference
    transform: Canonical
    dynamic_value: ActivityDefinition_DynamicValue


@dataclass
class ActivityDefinition_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ActivityDefinition_SubjectX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ActivityDefinition_KindCode:
    value: RequestResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ActivityDefinition_IntentCode:
    value: RequestIntentCode_Value
    id: String
    extension: Extension


@dataclass
class ActivityDefinition_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class ActivityDefinition_TimingX:
    timing: Timing
    date_time: DateTime
    age: Age
    period: Period
    range: Range
    duration: Duration


@dataclass
class ActivityDefinition_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ActivityDefinition_Participant_TypeCode
    role: CodeableConcept


@dataclass
class ActivityDefinition_Participant_TypeCode:
    value: ActionParticipantTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ActivityDefinition_ProductX:
    reference: Reference
    codeable_concept: CodeableConcept


@dataclass
class ActivityDefinition_DynamicValue:
    id: String
    extension: Extension
    modifier_extension: Extension
    path: String
    expression: Expression

