"""Talks forms."""

from flask.ext.wtf import Form
from wtforms import HiddenField
from wtforms_alchemy import model_form_factory

from pygotham.talks.models import Talk

__all__ = 'TalkVoteForm',

ModelForm = model_form_factory(Form)


class TalkVoteForm(ModelForm):

    """Form for editing :class:`~pygotham.models.Talk` instances."""

    id = HiddenField()

    class Meta:
        model = TalkVote
        exclude = ('talk_id','event_id','event')
        field_args = {
            'name': {'label': 'Talk Title'},
            'description': {'label': 'Talk Description'},
            'the_vote': {'label': 'Your Vote'},
        }
