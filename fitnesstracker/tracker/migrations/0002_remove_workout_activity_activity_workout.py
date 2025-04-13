# Generated by Django 5.1.7 on 2025-04-13 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='activity',
        ),
        migrations.AddField(
            model_name='activity',
            name='workout',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='tracker.workout'),
            preserve_default=False,
        ),
    ]
