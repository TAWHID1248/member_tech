# Generated by Django 5.0.1 on 2024-01-24 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberinfo',
            name='cellphone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='memberinfo',
            name='landline_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
