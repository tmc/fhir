# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ProfileForHLAGenotypingResults:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    status: ProfileForHLAGenotypingResults_StatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    encounter: Reference
    effective: ProfileForHLAGenotypingResults_EffectiveX
    issued: Instant
    performer: Reference
    results_interpreter: Reference
    specimen: Reference
    result: Reference
    imaging_study: Reference
    media: ProfileForHLAGenotypingResults_Media
    conclusion: String
    conclusion_code: CodeableConcept
    presented_form: Attachment
    allele_database: CodeableConcept
    glstring: DiagnosticReportGlstring
    haploid: DiagnosticReportHaploid
    method: CodeableConcept


@dataclass
class ProfileForHLAGenotypingResults_StatusCode:
    value: DiagnosticReportStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ProfileForHLAGenotypingResults_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class ProfileForHLAGenotypingResults_Media:
    id: String
    extension: Extension
    modifier_extension: Extension
    comment: String
    link: Reference

