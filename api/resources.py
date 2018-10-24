from tastypie.resources import ModelResource
from api.models import DayOfWeek, CommonArea, CommonAreaDay, Schedule

class DayOfWeekResource(ModelResource):
    class Meta:
        queryset = DayOfWeek.objects.all()
        resource_name = 'day_of_week'