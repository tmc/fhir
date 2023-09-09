# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class CDSHooksServicePlanDefinition:
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
    type: CodeableConcept
    status: CDSHooksServicePlanDefinition_StatusCode
    experimental: Boolean
    subject: CDSHooksServicePlanDefinition_SubjectX
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
    library: Canonical
    goal: CDSHooksServicePlanDefinition_Goal
    action: CDSHooksServicePlanDefinition_Action
    cds_hooks_endpoint: Uri


@dataclass
class CDSHooksServicePlanDefinition_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksServicePlanDefinition_SubjectX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class CDSHooksServicePlanDefinition_Goal:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    description: CodeableConcept
    priority: CodeableConcept
    start: CodeableConcept
    addresses: CodeableConcept
    documentation: RelatedArtifact
    target: CDSHooksServicePlanDefinition_Goal_Target


@dataclass
class CDSHooksServicePlanDefinition_Goal_Target:
    id: String
    extension: Extension
    modifier_extension: Extension
    measure: CodeableConcept
    detail: CDSHooksServicePlanDefinition_Goal_Target_DetailX
    due: Duration


@dataclass
class CDSHooksServicePlanDefinition_Goal_Target_DetailX:
    quantity: Quantity
    range: Range
    codeable_concept: CodeableConcept


@dataclass
class CDSHooksServicePlanDefinition_Action:
    id: String
    extension: Extension
    modifier_extension: Extension
    prefix: String
    title: String
    description: String
    text_equivalent: String
    priority: CDSHooksServicePlanDefinition_Action_PriorityCode
    code: CodeableConcept
    reason: CodeableConcept
    documentation: RelatedArtifact
    goal_id: Id
    subject: CDSHooksServicePlanDefinition_Action_SubjectX
    trigger: TriggerDefinition
    condition: CDSHooksServicePlanDefinition_Action_Condition
    input: DataRequirement
    output: DataRequirement
    related_action: CDSHooksServicePlanDefinition_Action_RelatedAction
    timing: CDSHooksServicePlanDefinition_Action_TimingX
    participant: CDSHooksServicePlanDefinition_Action_Participant
    type: CodeableConcept
    grouping_behavior: CDSHooksServicePlanDefinition_Action_GroupingBehaviorCode
    selection_behavior: CDSHooksServicePlanDefinition_Action_SelectionBehaviorCode
    required_behavior: CDSHooksServicePlanDefinition_Action_RequiredBehaviorCode
    precheck_behavior: CDSHooksServicePlanDefinition_Action_PrecheckBehaviorCode
    cardinality_behavior: CDSHooksServicePlanDefinition_Action_CardinalityBehaviorCode
    definition: CDSHooksServicePlanDefinition_Action_DefinitionX
    transform: Canonical
    dynamic_value: CDSHooksServicePlanDefinition_Action_DynamicValue
    action: CDSHooksServicePlanDefinition_Action


@dataclass
class CDSHooksServicePlanDefinition_Action_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksServicePlanDefinition_Action_SubjectX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class CDSHooksServicePlanDefinition_Action_Condition:
    id: String
    extension: Extension
    modifier_extension: Extension
    kind: CDSHooksServicePlanDefinition_Action_Condition_KindCode
    expression: Expression


@dataclass
class CDSHooksServicePlanDefinition_Action_Condition_KindCode:
    value: ActionConditionKindCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksServicePlanDefinition_Action_RelatedAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    action_id: Id
    relationship: CDSHooksServicePlanDefinition_Action_RelatedAction_RelationshipCode
    offset: CDSHooksServicePlanDefinition_Action_RelatedAction_OffsetX


@dataclass
class CDSHooksServicePlanDefinition_Action_RelatedAction_RelationshipCode:
    value: ActionRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksServicePlanDefinition_Action_RelatedAction_OffsetX:
    duration: Duration
    range: Range


@dataclass
class CDSHooksServicePlanDefinition_Action_TimingX:
    date_time: DateTime
    age: Age
    period: Period
    duration: Duration
    range: Range
    timing: Timing


@dataclass
class CDSHooksServicePlanDefinition_Action_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CDSHooksServicePlanDefinition_Action_Participant_TypeCode
    role: CodeableConcept


@dataclass
class CDSHooksServicePlanDefinition_Action_Participant_TypeCode:
    value: ActionParticipantTypeCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksServicePlanDefinition_Action_GroupingBehaviorCode:
    value: ActionGroupingBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksServicePlanDefinition_Action_SelectionBehaviorCode:
    value: ActionSelectionBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksServicePlanDefinition_Action_RequiredBehaviorCode:
    value: ActionRequiredBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksServicePlanDefinition_Action_PrecheckBehaviorCode:
    value: ActionPrecheckBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksServicePlanDefinition_Action_CardinalityBehaviorCode:
    value: ActionCardinalityBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class CDSHooksServicePlanDefinition_Action_DefinitionX:
    canonical: Canonical
    uri: Uri


@dataclass
class CDSHooksServicePlanDefinition_Action_DynamicValue:
    id: String
    extension: Extension
    modifier_extension: Extension
    path: String
    expression: Expression

