# Generated by Django 4.0.5 on 2022-06-03 14:01

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
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileNum', models.CharField(blank=True, max_length=10, null=True)),
                ('homeNum', models.CharField(blank=True, max_length=10, null=True)),
                ('workNum', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]