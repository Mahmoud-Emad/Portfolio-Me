# Generated by Django 3.1.1 on 2020-10-15 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201015_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsmodel',
            name='Live',
            field=models.URLField(blank=True, max_length=500, verbose_name='Live Of Project'),
        ),
    ]
