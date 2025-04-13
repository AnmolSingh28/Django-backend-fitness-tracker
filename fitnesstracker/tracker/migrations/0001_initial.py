# Generated by Django 5.1.7 on 2025-04-13 06:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sets', models.IntegerField(default=50)),
                ('reps', models.PositiveBigIntegerField(default=50)),
                ('image', models.ImageField(default='/', upload_to='images/')),
                ('tutorial', models.TextField(default=50, max_length=500)),
                ('history', models.FloatField(default=50, max_length=100)),
                ('weight', models.FloatField(default=2)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveBigIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('reps', models.PositiveBigIntegerField(default=50)),
                ('workoutName', models.CharField(default=50, max_length=10)),
                ('weight', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
