# Generated by Django 3.1.1 on 2020-10-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201015_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsmodel',
            name='Image10',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='', verbose_name='More Image Size 218 x 243'),
        ),
        migrations.AddField(
            model_name='projectsmodel',
            name='Image7',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='', verbose_name='More Image Size 218 x 243'),
        ),
        migrations.AddField(
            model_name='projectsmodel',
            name='Image8',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='', verbose_name='More Image Size 218 x 243'),
        ),
        migrations.AddField(
            model_name='projectsmodel',
            name='Image9',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='', verbose_name='More Image Size 218 x 243'),
        ),
    ]
