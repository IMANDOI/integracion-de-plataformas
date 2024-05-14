# Generated by Django 5.0.6 on 2024-05-13 07:55

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
            name='Bodeguero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_cel_bod', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bodeguero', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_cel', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_cel_cont', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
