from tastypie.resources import ModelResource
from api.models import DayOfWeek, CommonArea, CommonAreaDay, Schedule

class DayOfWeekResource(ModelResource):
    class Meta:
        queryset = DayOfWeek.objects.all()
        resource_name = 'day_of_week'
        excludes = ['created_at', 'updated_at']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']

class CommonAreaResource(ModelResource):
    class Meta: 
        queryset = CommonArea.objects.all()
        resource_name = "common_area"
        excludes = ['created_at', 'updated_at']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']

class CommonAreaDayResource(ModelResource):
    class Meta:
        queryset = CommonAreaDay.objects.all()
        resource_name = "common_area_day"
        excludes = ['created_at', 'updated_at']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']

class ScheduleResource(ModelResource):
    class Meta:
        queryset = Schedule.objects.all()
        resource_name = "schedule"
        excludes = ['created_at', 'updated_at']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']