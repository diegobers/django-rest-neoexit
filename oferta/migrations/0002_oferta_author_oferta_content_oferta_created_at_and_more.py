# Generated by Django 4.0.4 on 2022-05-05 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oferta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='oferta',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='oferta',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='oferta',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='oferta',
            name='title',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
