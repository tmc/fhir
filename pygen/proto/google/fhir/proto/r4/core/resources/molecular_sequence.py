# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MolecularSequence:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    type: MolecularSequence_TypeCode
    coordinate_system: Integer
    patient: Reference
    specimen: Reference
    device: Reference
    performer: Reference
    quantity: Quantity
    reference_seq: MolecularSequence_ReferenceSeq
    variant: MolecularSequence_Variant
    observed_seq: String
    quality: MolecularSequence_Quality
    read_coverage: Integer
    repository: MolecularSequence_Repository
    pointer: Reference
    structure_variant: MolecularSequence_StructureVariant


@dataclass
class MolecularSequence_TypeCode:
    value: SequenceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class MolecularSequence_ReferenceSeq:
    id: String
    extension: Extension
    modifier_extension: Extension
    chromosome: CodeableConcept
    genome_build: String
    orientation: MolecularSequence_ReferenceSeq_OrientationCode
    reference_seq_id: CodeableConcept
    reference_seq_pointer: Reference
    reference_seq_string: String
    strand: MolecularSequence_ReferenceSeq_StrandCode
    window_start: Integer
    window_end: Integer


@dataclass
class MolecularSequence_ReferenceSeq_OrientationCode:
    value: OrientationTypeCode_Value
    id: String
    extension: Extension


@dataclass
class MolecularSequence_ReferenceSeq_StrandCode:
    value: StrandTypeCode_Value
    id: String
    extension: Extension


@dataclass
class MolecularSequence_Variant:
    id: String
    extension: Extension
    modifier_extension: Extension
    start: Integer
    end: Integer
    observed_allele: String
    reference_allele: String
    cigar: String
    variant_pointer: Reference


@dataclass
class MolecularSequence_Quality:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: MolecularSequence_Quality_TypeCode
    standard_sequence: CodeableConcept
    start: Integer
    end: Integer
    score: Quantity
    method: CodeableConcept
    truth_tp: Decimal
    query_tp: Decimal
    truth_fn: Decimal
    query_fp: Decimal
    gt_fp: Decimal
    precision: Decimal
    recall: Decimal
    f_score: Decimal
    roc: MolecularSequence_Quality_Roc


@dataclass
class MolecularSequence_Quality_TypeCode:
    value: QualityTypeCode_Value
    id: String
    extension: Extension


@dataclass
class MolecularSequence_Quality_Roc:
    id: String
    extension: Extension
    modifier_extension: Extension
    score: Integer
    num_tp: Integer
    num_fp: Integer
    num_fn: Integer
    precision: Decimal
    sensitivity: Decimal
    f_measure: Decimal


@dataclass
class MolecularSequence_Repository:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: MolecularSequence_Repository_TypeCode
    url: Uri
    name: String
    dataset_id: String
    variantset_id: String
    readset_id: String


@dataclass
class MolecularSequence_Repository_TypeCode:
    value: RepositoryTypeCode_Value
    id: String
    extension: Extension


@dataclass
class MolecularSequence_StructureVariant:
    id: String
    extension: Extension
    modifier_extension: Extension
    variant_type: CodeableConcept
    exact: Boolean
    length: Integer
    outer: MolecularSequence_StructureVariant_Outer
    inner: MolecularSequence_StructureVariant_Inner


@dataclass
class MolecularSequence_StructureVariant_Outer:
    id: String
    extension: Extension
    modifier_extension: Extension
    start: Integer
    end: Integer


@dataclass
class MolecularSequence_StructureVariant_Inner:
    id: String
    extension: Extension
    modifier_extension: Extension
    start: Integer
    end: Integer

