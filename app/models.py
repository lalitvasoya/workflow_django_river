from django.db import models
from river.models.fields.state import StateField


class DiamondWorkflow(models.Model):
    state_field = StateField()
