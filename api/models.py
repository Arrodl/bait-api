from django.db import models

# Create your models here.

class CommonArea (models.Model):
    name = models.CharField(max_length = 200)
    short_description = models.CharField(max_length = 250)
    long_description = models.TextField()
    is_all_day = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # Relationships

    def __str__(self):
        return "%s: %s" % (self.name, self.short_description)

class DayOfWeek (models.Model):
    identifier = models.CharField(max_length = 15)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # Relationships
    common_area = models.ForeignKey(CommonArea, on_delete = models.CASCADE)

    def __str__(self):
        return "%s" % (self.identifier)

