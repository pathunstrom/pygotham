"""Talk voting models."""

import sqlalchemy.types as types
from pygotham.core import db

__all__ = 'VoteChoiceType','TalkVote',


class VoteChoiceType(types.TypeDecorator):

    impl = types.Integer

    def __init__(self, **kw):
        self.choices = {
           'Down':-1,
           'No Vote':0,
           'Up':1
            }
        super(VoteChoiceType, self).__init__(**kw)

    def process_bind_param(self, value, dialect):
        return [k for k, v in self.choices.iteritems() if v == value][0]

    def process_result_value(self, value, dialect):
        return self.choices[value]


class TalkVote(db.Model):

    """
       Talk vote: we don't look to see who voted for what. But we store this
       info so attendees can change their minds. 
       Voting is double-blind: attendees can't see speaker info, speaker can't see who voted how.
    """

    __tablename__ = 'talk_vote'

    id = db.Column(db.Integer, primary_key=True)
    the_vote = db.Column(
        VoteChoiceType(),
        default='No Vote',
        nullable=False,
    )

    talk_id = db.Column(
        db.Integer, db.ForeignKey('talks.id'), nullable=False,
    )
    talk = db.relationship('Talk', backref=db.backref('talk_vote', lazy='dynamic'))

    event_id = db.Column(
        db.Integer, db.ForeignKey('events.id'), nullable=False,
    )
    event = db.relationship(
        'Event', backref=db.backref('talk_vote', lazy='dynamic'),
    )

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('talk_vote', lazy='dynamic'))

    def __str__(self):
        """Return a printable representation."""
        return self.name
