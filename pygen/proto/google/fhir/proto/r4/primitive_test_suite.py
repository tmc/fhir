# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.testing
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class PrimitiveProtoUnion:
    base64_binary: Base64Binary
    boolean: Boolean
    canonical: Canonical
    code: Code
    date: Date
    date_time: DateTime
    decimal: Decimal
    id: Id
    instant: Instant
    integer: Integer
    markdown: Markdown
    oid: Oid
    positive_int: PositiveInt
    string_proto: String
    time: Time
    unsigned_int: UnsignedInt
    uri: Uri
    url: Url
    uuid: Uuid
    xhtml: Xhtml
    reference: Reference


@dataclass
class ValidPair:
    json_string: str
    proto: PrimitiveProtoUnion


@dataclass
class PrimitiveTestSuite:
    valid_pairs: ValidPair
    invalid_json: str
    invalid_protos: PrimitiveProtoUnion
    no_invalid_protos_reason: str

