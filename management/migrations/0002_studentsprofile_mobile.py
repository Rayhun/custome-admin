# Generated by Django 3.1.3 on 2020-11-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsprofile',
            name='mobile',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
