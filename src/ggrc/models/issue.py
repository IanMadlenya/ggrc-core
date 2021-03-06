# Copyright (C) 2017 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

from ggrc import db
from ggrc.models.mixins.audit_relationship import AuditRelationship
from ggrc.models.mixins import (
    BusinessObject, Timeboxed, CustomAttributable, TestPlanned
)
from ggrc.models.object_document import EvidenceURL
from ggrc.models.object_owner import Ownable
from ggrc.models.object_person import Personable
from ggrc.models.relationship import Relatable
from ggrc.models.track_object_state import HasObjectState


class Issue(HasObjectState, TestPlanned, CustomAttributable, EvidenceURL,
            Personable, Timeboxed, Ownable, Relatable, AuditRelationship,
            BusinessObject, db.Model):

  __tablename__ = 'issues'

  # REST properties
  _publish_attrs = [
  ]

  _aliases = {"url": "Issue URL"}
