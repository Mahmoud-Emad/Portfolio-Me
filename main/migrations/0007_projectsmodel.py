# Generated by Django 3.1.1 on 2020-10-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_delete_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='Name Of Project')),
                ('Image', models.ImageField(blank=True, max_length=1000, null=True, upload_to='', verbose_name='Top Image')),
                ('Discraption', models.TextField(max_length=500, verbose_name='Discraption Of Project')),
                ('Category', models.CharField(choices=[('Ecommerce', 'Ecommerce'), ('Job Board', 'Job Board'), ('Doctors community', 'Doctors community'), ('The city of moves', 'The city of moves')], max_length=255)),
            ],
        ),
    ]
