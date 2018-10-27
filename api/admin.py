from django.contrib import admin
from .models import DayOfWeek
from .models import Motive
from .models import Place
from .models import Event

admin.site.register(DayOfWeek)
admin.site.register(Motive)
admin.site.register(Place)
admin.site.register(Event)
# Register your models here.
