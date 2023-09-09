# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ShareableMeasure:
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
    status: ShareableMeasure_StatusCode
    experimental: Boolean
    subject: ShareableMeasure_SubjectX
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
    disclaimer: Markdown
    scoring: CodeableConcept
    composite_scoring: CodeableConcept
    type: CodeableConcept
    risk_adjustment: String
    rate_aggregation: String
    rationale: Markdown
    clinical_recommendation_statement: Markdown
    improvement_notation: CodeableConcept
    definition: Markdown
    guidance: Markdown
    group: ShareableMeasure_Group
    supplemental_data: ShareableMeasure_SupplementalData


@dataclass
class ShareableMeasure_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ShareableMeasure_SubjectX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ShareableMeasure_Group:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    description: String
    population: ShareableMeasure_Group_Population
    stratifier: ShareableMeasure_Group_Stratifier


@dataclass
class ShareableMeasure_Group_Population:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    description: String
    criteria: Expression


@dataclass
class ShareableMeasure_Group_Stratifier:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    description: String
    criteria: Expression
    component: ShareableMeasure_Group_Stratifier_Component


@dataclass
class ShareableMeasure_Group_Stratifier_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    description: String
    criteria: Expression


@dataclass
class ShareableMeasure_SupplementalData:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    usage: CodeableConcept
    description: String
    criteria: Expression

