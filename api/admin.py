from django.contrib import admin
from .models import DayOfWeek
from .models import Motive
from .models import Place
from .models import Event
from .models import CommonArea
from .models import CommonAreaDay
from .models import Schedule
from .models import Announcement

admin.site.site_header = "Bait"
admin.site.site_title = "Bait"

# Register your models here.
admin.site.register(CommonAreaDay)
admin.site.register(CommonArea)
admin.site.register(DayOfWeek)
admin.site.register(Motive)
admin.site.register(Place)
admin.site.register(Event)
admin.site.register(Schedule)
admin.site.register(Announcement)
