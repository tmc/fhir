# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class SubstanceNucleicAcid:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    sequence_type: CodeableConcept
    number_of_subunits: Integer
    area_of_hybridisation: String
    oligo_nucleotide_type: CodeableConcept
    subunit: SubstanceNucleicAcid_Subunit


@dataclass
class SubstanceNucleicAcid_Subunit:
    id: String
    extension: Extension
    modifier_extension: Extension
    subunit: Integer
    sequence: String
    length: Integer
    sequence_attachment: Attachment
    five_prime: CodeableConcept
    three_prime: CodeableConcept
    linkage: SubstanceNucleicAcid_Subunit_Linkage
    sugar: SubstanceNucleicAcid_Subunit_Sugar


@dataclass
class SubstanceNucleicAcid_Subunit_Linkage:
    id: String
    extension: Extension
    modifier_extension: Extension
    connectivity: String
    identifier: Identifier
    name: String
    residue_site: String


@dataclass
class SubstanceNucleicAcid_Subunit_Sugar:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    name: String
    residue_site: String

