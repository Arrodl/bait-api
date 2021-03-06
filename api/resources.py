from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from api.models import DayOfWeek, CommonArea, CommonAreaDay, Schedule
from .models import Announcement

class AnnouncementResource(ModelResource): 
    class Meta:
        queryset = Announcement.objects.all()
        resource_name = 'announcement'
        excludes = ['created_at', 'updated_at']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']

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
        detail_allowed_methods = ['get', 'post', 'put', 'delete'],
        authorization = Authorization()
        filtering = {
            'day_of_week': ALL_WITH_RELATIONS,
            'schedule': ALL_WITH_RELATIONS,
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }

class ScheduleResource(ModelResource):
    class Meta:
        queryset = Schedule.objects.all()
        resource_name = "schedule"
        excludes = ['created_at', 'updated_at']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']