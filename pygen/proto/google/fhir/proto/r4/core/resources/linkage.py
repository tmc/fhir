# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Linkage:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    active: Boolean
    author: Reference
    item: Linkage_Item


@dataclass
class Linkage_Item:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: Linkage_Item_TypeCode
    resource: Reference


@dataclass
class Linkage_Item_TypeCode:
    value: LinkageTypeCode_Value
    id: String
    extension: Extension

