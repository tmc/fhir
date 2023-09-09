# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Binary:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    content_type: Binary_ContentTypeCode
    security_context: Reference
    data: Base64Binary


@dataclass
class Binary_ContentTypeCode:
    id: String
    extension: Extension
    value: str

