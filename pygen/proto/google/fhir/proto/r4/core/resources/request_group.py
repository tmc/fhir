# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class RequestGroup:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    instantiates_canonical: Canonical
    instantiates_uri: Uri
    based_on: Reference
    replaces: Reference
    group_identifier: Identifier
    status: RequestGroup_StatusCode
    intent: RequestGroup_IntentCode
    priority: RequestGroup_PriorityCode
    code: CodeableConcept
    subject: Reference
    encounter: Reference
    authored_on: DateTime
    author: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    note: Annotation
    action: RequestGroup_Action


@dataclass
class RequestGroup_StatusCode:
    value: RequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class RequestGroup_IntentCode:
    value: RequestIntentCode_Value
    id: String
    extension: Extension


@dataclass
class RequestGroup_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class RequestGroup_Action:
    id: String
    extension: Extension
    modifier_extension: Extension
    prefix: String
    title: String
    description: String
    text_equivalent: String
    priority: RequestGroup_Action_PriorityCode
    code: CodeableConcept
    documentation: RelatedArtifact
    condition: RequestGroup_Action_Condition
    related_action: RequestGroup_Action_RelatedAction
    timing: RequestGroup_Action_TimingX
    participant: Reference
    type: CodeableConcept
    grouping_behavior: RequestGroup_Action_GroupingBehaviorCode
    selection_behavior: RequestGroup_Action_SelectionBehaviorCode
    required_behavior: RequestGroup_Action_RequiredBehaviorCode
    precheck_behavior: RequestGroup_Action_PrecheckBehaviorCode
    cardinality_behavior: RequestGroup_Action_CardinalityBehaviorCode
    resource: Reference
    action: RequestGroup_Action


@dataclass
class RequestGroup_Action_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class RequestGroup_Action_Condition:
    id: String
    extension: Extension
    modifier_extension: Extension
    kind: RequestGroup_Action_Condition_KindCode
    expression: Expression


@dataclass
class RequestGroup_Action_Condition_KindCode:
    value: ActionConditionKindCode_Value
    id: String
    extension: Extension


@dataclass
class RequestGroup_Action_RelatedAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    action_id: Id
    relationship: RequestGroup_Action_RelatedAction_RelationshipCode
    offset: RequestGroup_Action_RelatedAction_OffsetX


@dataclass
class RequestGroup_Action_RelatedAction_RelationshipCode:
    value: ActionRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class RequestGroup_Action_RelatedAction_OffsetX:
    duration: Duration
    range: Range


@dataclass
class RequestGroup_Action_TimingX:
    date_time: DateTime
    age: Age
    period: Period
    duration: Duration
    range: Range
    timing: Timing


@dataclass
class RequestGroup_Action_GroupingBehaviorCode:
    value: ActionGroupingBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class RequestGroup_Action_SelectionBehaviorCode:
    value: ActionSelectionBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class RequestGroup_Action_RequiredBehaviorCode:
    value: ActionRequiredBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class RequestGroup_Action_PrecheckBehaviorCode:
    value: ActionPrecheckBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class RequestGroup_Action_CardinalityBehaviorCode:
    value: ActionCardinalityBehaviorCode_Value
    id: String
    extension: Extension

