from cms.models.pluginmodel import CMSPlugin

from django.db import models
from schedule.models.calendars import Calendar
from schedule.models.events import Occurrence
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _


class CalendarPlugin(CMSPlugin):
    calendar = models.ForeignKey(Calendar)
    

class LastEventsPlugin(CMSPlugin):
    calendar = models.ForeignKey(Calendar)
    nb_event = models.PositiveSmallIntegerField(default=5, verbose_name=_("Nb events"))
    event_type = models.ForeignKey(Group, null=True, blank=True,
                                   verbose_name=_("Group"),
                                   help_text=_("To dissociate event type"))


class EventsByPeriodPlugin(CMSPlugin):
    calendar = models.ForeignKey(Calendar)
    period = models.CharField(max_length=1, 
                              verbose_name=_("Period"),
                              default='W',
                              choices=(('D', _('Today')),
                                       ('W', _('This week')),
                                       ('M', _('This month'))))
    event_type = models.ForeignKey(Group, null=True, blank=True,
                               verbose_name=_("Group"),
                               help_text=_("To dissociate event type"))
    

@property
def is_past_due(self):
    from datetime import date
    if date.today() > self.end.date():
        return True
    return False

setattr(Occurrence, "is_past_due", is_past_due)
