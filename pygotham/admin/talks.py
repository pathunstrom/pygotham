"""Admin for talk-related models."""

from pygotham.admin.utils import model_view
from pygotham.talks import models as talk_models
from pygotham.voting import models as talkvote_models

__all__ = 'CategoryModelView', 'TalkModelView'


CategoryModelView = model_view(
    talk_models.Category,
    'Categories',
    'Talks',
    form_columns=('name', 'slug'),
)

TalkModelView = model_view(
    talk_models.Talk,
    'Talks',
    'Talks',
    column_list=('name', 'status', 'level', 'category'),
    column_searchable_list=('name',),
)

TalkVoteView = model_view(
    talkvote_models.TalkVote,
    'TalkVote',
    'TalkVote',
)
