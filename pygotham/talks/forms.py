"""Talks forms."""

from flask.ext.wtf import Form
from wtforms import HiddenField
from wtforms_alchemy import model_form_factory

from pygotham.talks.models import Talk

__all__ = 'TalkSubmissionForm',

ModelForm = model_form_factory(Form)


class TalkSubmissionForm(ModelForm):

    """Form for editing :class:`~pygotham.models.Talk` instances."""

    id = HiddenField()

    class Meta:
        model = Talk
        exclude = ('status',)
        field_args = {
            'name': {'label': 'Title'},
            'description': {'label': 'Description'},
            'level': {'label': 'Experience Level'},
            'duration': {'label': 'Talk Duration'},
            'talk_type': {'label': 'Talk Type'},
            'abstract': {'label': 'Abstract'},
            'objectives': {'label': 'Objectives'},
            'target_audience': {'label': 'Target Audience'},
            'outline': {'label': 'Outline'},
            'additional_requirements': {'label': 'Additional Requirements'},
            'need_a_TA': {'label': "If you've proposed a class, do you need help finding a TA?"},
            'recording_release': {'label': 'Recording Release'},
        }
