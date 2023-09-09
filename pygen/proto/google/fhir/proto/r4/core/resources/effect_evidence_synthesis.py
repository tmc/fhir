# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class EffectEvidenceSynthesis:
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
    status: EffectEvidenceSynthesis_StatusCode
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
    exposure_alternative: Reference
    outcome: Reference
    sample_size: EffectEvidenceSynthesis_SampleSize
    results_by_exposure: EffectEvidenceSynthesis_ResultsByExposure
    effect_estimate: EffectEvidenceSynthesis_EffectEstimate
    certainty: EffectEvidenceSynthesis_Certainty


@dataclass
class EffectEvidenceSynthesis_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class EffectEvidenceSynthesis_SampleSize:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    number_of_studies: Integer
    number_of_participants: Integer


@dataclass
class EffectEvidenceSynthesis_ResultsByExposure:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    exposure_state: EffectEvidenceSynthesis_ResultsByExposure_ExposureStateCode
    variant_state: CodeableConcept
    risk_evidence_synthesis: Reference


@dataclass
class EffectEvidenceSynthesis_ResultsByExposure_ExposureStateCode:
    value: ExposureStateCode_Value
    id: String
    extension: Extension


@dataclass
class EffectEvidenceSynthesis_EffectEstimate:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    type: CodeableConcept
    variant_state: CodeableConcept
    value: Decimal
    unit_of_measure: CodeableConcept
    precision_estimate: EffectEvidenceSynthesis_EffectEstimate_PrecisionEstimate


@dataclass
class EffectEvidenceSynthesis_EffectEstimate_PrecisionEstimate:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    level: Decimal
    from: Decimal
    to: Decimal


@dataclass
class EffectEvidenceSynthesis_Certainty:
    id: String
    extension: Extension
    modifier_extension: Extension
    rating: CodeableConcept
    note: Annotation
    certainty_subcomponent: EffectEvidenceSynthesis_Certainty_CertaintySubcomponent


@dataclass
class EffectEvidenceSynthesis_Certainty_CertaintySubcomponent:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    rating: CodeableConcept
    note: Annotation

