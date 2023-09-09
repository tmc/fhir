# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class EvidenceVariable:
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
    short_title: String
    subtitle: String
    status: EvidenceVariable_StatusCode
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    note: Annotation
    use_context: UsageContext
    jurisdiction: CodeableConcept
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
    type: EvidenceVariable_TypeCode
    characteristic: EvidenceVariable_Characteristic


@dataclass
class EvidenceVariable_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class EvidenceVariable_TypeCode:
    value: EvidenceVariableTypeCode_Value
    id: String
    extension: Extension


@dataclass
class EvidenceVariable_Characteristic:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    definition: EvidenceVariable_Characteristic_DefinitionX
    usage_context: UsageContext
    exclude: Boolean
    participant_effective: EvidenceVariable_Characteristic_ParticipantEffectiveX
    time_from_start: Duration
    group_measure: EvidenceVariable_Characteristic_GroupMeasureCode


@dataclass
class EvidenceVariable_Characteristic_DefinitionX:
    reference: Reference
    canonical: Canonical
    codeable_concept: CodeableConcept
    expression: Expression
    data_requirement: DataRequirement
    trigger_definition: TriggerDefinition


@dataclass
class EvidenceVariable_Characteristic_ParticipantEffectiveX:
    date_time: DateTime
    period: Period
    duration: Duration
    timing: Timing


@dataclass
class EvidenceVariable_Characteristic_GroupMeasureCode:
    value: GroupMeasureCode_Value
    id: String
    extension: Extension

