# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ResearchStudy:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    title: String
    protocol: Reference
    part_of: Reference
    status: ResearchStudy_StatusCode
    primary_purpose_type: CodeableConcept
    phase: CodeableConcept
    category: CodeableConcept
    focus: CodeableConcept
    condition: CodeableConcept
    contact: ContactDetail
    related_artifact: RelatedArtifact
    keyword: CodeableConcept
    location: CodeableConcept
    description: Markdown
    enrollment: Reference
    period: Period
    sponsor: Reference
    principal_investigator: Reference
    site: Reference
    reason_stopped: CodeableConcept
    note: Annotation
    arm: ResearchStudy_Arm
    objective: ResearchStudy_Objective


@dataclass
class ResearchStudy_StatusCode:
    value: ResearchStudyStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ResearchStudy_Arm:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    type: CodeableConcept
    description: String


@dataclass
class ResearchStudy_Objective:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    type: CodeableConcept

