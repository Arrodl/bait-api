# Generated by Django 2.1.2 on 2018-10-24 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonAreaDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('common_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CommonArea')),
            ],
        ),
        migrations.RemoveField(
            model_name='dayofweek',
            name='common_area',
        ),
        migrations.AddField(
            model_name='commonareaday',
            name='day_of_week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DayOfWeek'),
        ),
    ]