# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Library:
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
    status: Library_StatusCode
    experimental: Boolean
    type: CodeableConcept
    subject: Library_SubjectX
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
    parameter: ParameterDefinition
    data_requirement: DataRequirement
    content: Attachment


@dataclass
class Library_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Library_SubjectX:
    codeable_concept: CodeableConcept
    reference: Reference

