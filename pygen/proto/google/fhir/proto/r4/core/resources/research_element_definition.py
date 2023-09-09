# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ResearchElementDefinition:
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
    status: ResearchElementDefinition_StatusCode
    experimental: Boolean
    subject: ResearchElementDefinition_SubjectX
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    comment: String
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
    type: ResearchElementDefinition_TypeCode
    variable_type: ResearchElementDefinition_VariableTypeCode
    characteristic: ResearchElementDefinition_Characteristic


@dataclass
class ResearchElementDefinition_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ResearchElementDefinition_SubjectX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ResearchElementDefinition_TypeCode:
    value: ResearchElementTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ResearchElementDefinition_VariableTypeCode:
    value: EvidenceVariableTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ResearchElementDefinition_Characteristic:
    id: String
    extension: Extension
    modifier_extension: Extension
    definition: ResearchElementDefinition_Characteristic_DefinitionX
    usage_context: UsageContext
    exclude: Boolean
    unit_of_measure: CodeableConcept
    study_effective_description: String
    study_effective: ResearchElementDefinition_Characteristic_StudyEffectiveX
    study_effective_time_from_start: Duration
    study_effective_group_measure: ResearchElementDefinition_Characteristic_StudyEffectiveGroupMeasureCode
    participant_effective_description: String
    participant_effective: ResearchElementDefinition_Characteristic_ParticipantEffectiveX
    participant_effective_time_from_start: Duration
    participant_effective_group_measure: ResearchElementDefinition_Characteristic_ParticipantEffectiveGroupMeasureCode


@dataclass
class ResearchElementDefinition_Characteristic_DefinitionX:
    codeable_concept: CodeableConcept
    canonical: Canonical
    expression: Expression
    data_requirement: DataRequirement


@dataclass
class ResearchElementDefinition_Characteristic_StudyEffectiveX:
    date_time: DateTime
    period: Period
    duration: Duration
    timing: Timing


@dataclass
class ResearchElementDefinition_Characteristic_StudyEffectiveGroupMeasureCode:
    value: GroupMeasureCode_Value
    id: String
    extension: Extension


@dataclass
class ResearchElementDefinition_Characteristic_ParticipantEffectiveX:
    date_time: DateTime
    period: Period
    duration: Duration
    timing: Timing


@dataclass
class ResearchElementDefinition_Characteristic_ParticipantEffectiveGroupMeasureCode:
    value: GroupMeasureCode_Value
    id: String
    extension: Extension

