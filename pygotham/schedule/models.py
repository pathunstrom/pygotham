"""Talk voting models."""

from pygotham.core import db

__all__ = 'Schedule',


class Schedule(db.Model):

    """
       Schedule is populated from accepted talks.
       It adds time/date and other info, to make schedule generation easy.
    """

    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True)
    talk_datetime = db.Column(
        db.DateTime(timezone="America/New_York"),
        nullable=False
    )
    notes = db.Column(
        db.String(length=500),
        nullable=True,
        default=None
    )
    talk_id = db.Column(
        db.Integer, db.ForeignKey('talks.id'), nullable=False,
    )
    talk = db.relationship('Talk', backref=db.backref('schedule', lazy='dynamic'))

    event_id = db.Column(
        db.Integer, db.ForeignKey('events.id'), nullable=False,
    )
    event = db.relationship(
        'Event', backref=db.backref('schedule', lazy='dynamic'),
    )

    def __str__(self):
        """Return a printable representation."""
        return self.name
