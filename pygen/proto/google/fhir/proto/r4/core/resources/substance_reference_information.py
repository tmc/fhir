# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class SubstanceReferenceInformation:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    comment: String
    gene: SubstanceReferenceInformation_Gene
    gene_element: SubstanceReferenceInformation_GeneElement
    classification: SubstanceReferenceInformation_Classification
    target: SubstanceReferenceInformation_Target


@dataclass
class SubstanceReferenceInformation_Gene:
    id: String
    extension: Extension
    modifier_extension: Extension
    gene_sequence_origin: CodeableConcept
    gene: CodeableConcept
    source: Reference


@dataclass
class SubstanceReferenceInformation_GeneElement:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    element: Identifier
    source: Reference


@dataclass
class SubstanceReferenceInformation_Classification:
    id: String
    extension: Extension
    modifier_extension: Extension
    domain: CodeableConcept
    classification: CodeableConcept
    subtype: CodeableConcept
    source: Reference


@dataclass
class SubstanceReferenceInformation_Target:
    id: String
    extension: Extension
    modifier_extension: Extension
    target: Identifier
    type: CodeableConcept
    interaction: CodeableConcept
    organism: CodeableConcept
    organism_type: CodeableConcept
    amount: SubstanceReferenceInformation_Target_AmountX
    amount_type: CodeableConcept
    source: Reference


@dataclass
class SubstanceReferenceInformation_Target_AmountX:
    quantity: Quantity
    range: Range
    string_value: String

