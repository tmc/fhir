# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class CDSHooksRequestGroup:
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
    status: CDSHooksRequestGroup_StatusCode
    intent: CDSHooksRequestGroup_IntentCode
    priority: CDSHooksRequestGroup_PriorityCode
    code: CodeableConcept
    subject: Reference
    encounter: Reference
    authored_on: DateTime
    author: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    note: Annotation
    action: CDSHooksRequestGroup_Action


@dataclass
class CDSHooksRequestGroup_StatusCode:
    value: RequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksRequestGroup_IntentCode:
    value: RequestIntentCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksRequestGroup_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksRequestGroup_Action:
    id: String
    extension: Extension
    modifier_extension: Extension
    prefix: String
    title: String
    description: String
    text_equivalent: String
    priority: CDSHooksRequestGroup_Action_PriorityCode
    code: CodeableConcept
    documentation: RelatedArtifact
    condition: CDSHooksRequestGroup_Action_Condition
    related_action: CDSHooksRequestGroup_Action_RelatedAction
    timing: CDSHooksRequestGroup_Action_TimingX
    participant: Reference
    type: CodeableConcept
    grouping_behavior: CDSHooksRequestGroup_Action_GroupingBehaviorCode
    selection_behavior: CDSHooksRequestGroup_Action_SelectionBehaviorCode
    required_behavior: CDSHooksRequestGroup_Action_RequiredBehaviorCode
    precheck_behavior: CDSHooksRequestGroup_Action_PrecheckBehaviorCode
    cardinality_behavior: CDSHooksRequestGroup_Action_CardinalityBehaviorCode
    resource: Reference
    action: CDSHooksRequestGroup_Action


@dataclass
class CDSHooksRequestGroup_Action_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksRequestGroup_Action_Condition:
    id: String
    extension: Extension
    modifier_extension: Extension
    kind: CDSHooksRequestGroup_Action_Condition_KindCode
    expression: Expression


@dataclass
class CDSHooksRequestGroup_Action_Condition_KindCode:
    value: ActionConditionKindCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksRequestGroup_Action_RelatedAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    action_id: Id
    relationship: CDSHooksRequestGroup_Action_RelatedAction_RelationshipCode
    offset: CDSHooksRequestGroup_Action_RelatedAction_OffsetX


@dataclass
class CDSHooksRequestGroup_Action_RelatedAction_RelationshipCode:
    value: ActionRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksRequestGroup_Action_RelatedAction_OffsetX:
    duration: Duration
    range: Range


@dataclass
class CDSHooksRequestGroup_Action_TimingX:
    date_time: DateTime
    age: Age
    period: Period
    duration: Duration
    range: Range
    timing: Timing


@dataclass
class CDSHooksRequestGroup_Action_GroupingBehaviorCode:
    value: ActionGroupingBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksRequestGroup_Action_SelectionBehaviorCode:
    value: ActionSelectionBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksRequestGroup_Action_RequiredBehaviorCode:
    value: ActionRequiredBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksRequestGroup_Action_PrecheckBehaviorCode:
    value: ActionPrecheckBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksRequestGroup_Action_CardinalityBehaviorCode:
    value: ActionCardinalityBehaviorCode_Value
    id: String
    extension: Extension

