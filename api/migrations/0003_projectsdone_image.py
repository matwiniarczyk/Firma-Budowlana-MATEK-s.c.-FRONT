# Generated by Django 5.1.2 on 2024-10-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_projectsdone_description_projectsdone_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsdone',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]