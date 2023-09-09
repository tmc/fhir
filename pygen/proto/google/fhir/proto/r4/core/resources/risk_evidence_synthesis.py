# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class RiskEvidenceSynthesis:
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
    status: RiskEvidenceSynthesis_StatusCode
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
    synthesis_type: CodeableConcept
    study_type: CodeableConcept
    population: Reference
    exposure: Reference
    outcome: Reference
    sample_size: RiskEvidenceSynthesis_SampleSize
    risk_estimate: RiskEvidenceSynthesis_RiskEstimate
    certainty: RiskEvidenceSynthesis_Certainty


@dataclass
class RiskEvidenceSynthesis_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class RiskEvidenceSynthesis_SampleSize:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    number_of_studies: Integer
    number_of_participants: Integer


@dataclass
class RiskEvidenceSynthesis_RiskEstimate:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    type: CodeableConcept
    value: Decimal
    unit_of_measure: CodeableConcept
    denominator_count: Integer
    numerator_count: Integer
    precision_estimate: RiskEvidenceSynthesis_RiskEstimate_PrecisionEstimate


@dataclass
class RiskEvidenceSynthesis_RiskEstimate_PrecisionEstimate:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    level: Decimal
    from: Decimal
    to: Decimal


@dataclass
class RiskEvidenceSynthesis_Certainty:
    id: String
    extension: Extension
    modifier_extension: Extension
    rating: CodeableConcept
    note: Annotation
    certainty_subcomponent: RiskEvidenceSynthesis_Certainty_CertaintySubcomponent


@dataclass
class RiskEvidenceSynthesis_Certainty_CertaintySubcomponent:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    rating: CodeableConcept
    note: Annotation

