from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import CalendarPlugin as CalendarPluginModel
from .models import LastEventsPlugin as LastEventsPluginModel
from .models import EventsByPeriodPlugin as EventsByPeriodPluginModel

from datetime import datetime, date, timedelta
import calendar
from django.utils.timezone import utc, make_aware

class LastEventsPlugin(CMSPluginBase):
    module = _('Events')
    model = LastEventsPluginModel
    name = _("Last events")
    render_template = "cmsplugin_schedule/event_list.html"
    
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['events'] = []
        for event in instance.calendar.occurrences_after():
            if instance.event_type:
                if event.event.creator and event.event.creator in instance.event_type.user_set.all():
                    context['events'].append(event)
            else:
                context['events'].append(event)
            
            if len(context['events']) == instance.nb_event:
                break
         
        return context

plugin_pool.register_plugin(LastEventsPlugin)

class EventsByPeriodPlugin(CMSPluginBase):
    module = _('Events')
    model = EventsByPeriodPluginModel
    name = _("Events by period")
    render_template = "cmsplugin_schedule/event_list.html"
    
    def render(self, context, instance, placeholder):
        occurrences = []
        today = date.today()
        min_time = datetime.min.time()
        if instance.period == "D":
            start = datetime.combine(today, min_time)
            end = start + timedelta(days=1)
        elif instance.period == "W":
            start = datetime.combine(today - timedelta(days=today.weekday()), min_time)
            end = start + timedelta(days=7)
        else: #period=="M"
            start = datetime.combine(date(today.year, today.month, 1), min_time)
            end = datetime.combine(date(today.year, (today.month + 1) % 12, 1), min_time)
        
        start = make_aware(start, utc)
        end = make_aware(end, utc)
        
        for event in instance.calendar.event_set.filter(start__gte=start, end__lte=end):
            occurrences.extend(event.get_occurrences(start, end))
        context["events"] = occurrences
        context['instance'] = instance
        return context

plugin_pool.register_plugin(EventsByPeriodPlugin)

class CalendarPlugin(CMSPluginBase):
    module = _('Events')
    model = CalendarPluginModel
    name = _("Calendar")
    render_template = "cmsplugin_schedule/schedule.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(CalendarPlugin)