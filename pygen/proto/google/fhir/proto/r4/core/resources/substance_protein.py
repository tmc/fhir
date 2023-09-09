# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class SubstanceProtein:
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
    disulfide_linkage: String
    subunit: SubstanceProtein_Subunit


@dataclass
class SubstanceProtein_Subunit:
    id: String
    extension: Extension
    modifier_extension: Extension
    subunit: Integer
    sequence: String
    length: Integer
    sequence_attachment: Attachment
    n_terminal_modification_id: Identifier
    n_terminal_modification: String
    c_terminal_modification_id: Identifier
    c_terminal_modification: String

