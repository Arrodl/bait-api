"""bait_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.resources import DayOfWeekResource, CommonAreaDayResource, CommonAreaResource, ScheduleResource

day_of_week_resource = DayOfWeekResource()
common_area_resource = CommonAreaResource()
common_area_day_resource = CommonAreaDayResource()
schedule_resource = ScheduleResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(day_of_week_resource.urls)),
    path('api/v1/', include(common_area_resource.urls)),
    path('api/v1/', include(common_area_day_resource.urls)),
    path('api/v1/', include(schedule_resource.urls))
]
