# Generated by Django 2.2.4 on 2019-10-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
