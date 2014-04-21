"""Admin for talk-related models."""

from pygotham.admin.utils import model_view
from pygotham.schedule import models

__all__ = 'ScheduleModelView',


ScheduleModelView = model_view(
    models.Schedule,
    'Schedule',
    'Schedule',
)
