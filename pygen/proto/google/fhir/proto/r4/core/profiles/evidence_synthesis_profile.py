# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class EvidenceSynthesisProfile:
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
    status: EvidenceSynthesisProfile_StatusCode
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
    exposure_background: Reference
    exposure_variant: Reference
    outcome: Reference


@dataclass
class EvidenceSynthesisProfile_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension

