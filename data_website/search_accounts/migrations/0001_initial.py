# Generated by Django 4.2.6 on 2023-11-08 04:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.CharField(choices=[('enfaureport', 'enfaureport'), ('enfau2report', 'enfau2report')], default='enfaureport', max_length=100)),
                ('login', models.IntegerField(max_length=500)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 11, 8, 12, 38, 33, 172746))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
