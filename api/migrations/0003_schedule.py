# Generated by Django 2.1.2 on 2018-10-24 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181024_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('common_area_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CommonAreaDay')),
            ],
        ),
    ]