'''
Created on 22 janv. 2014

@author: alban
'''
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404

from schedule.models import Calendar
from datetime import datetime
import json
from django.utils.timezone import utc

class EventListView(View):

    def get(self, request, calendar_slug, **kwargs):
        calendar = get_object_or_404(Calendar, slug=calendar_slug)
        start = datetime.fromtimestamp(int(request.GET.get('start')), tz=utc)
        end = datetime.fromtimestamp(int(request.GET.get('end')), tz=utc)
        occurrences = []
        for event in calendar.event_set.all():
            
            for occurrence in event.get_occurrences(start, end):
                occurrences.append({
                    'title' : occurrence.title,
                    'start' : occurrence.start.strftime('%Y-%m-%d %H:%M:%S'),
                    'end' : occurrence.end.strftime('%Y-%m-%d %H:%M:%S')
                })
        
        return HttpResponse(json.dumps(occurrences))
