# Generated by Django 5.0.1 on 2024-01-24 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=40)),
                ('designation', models.CharField(blank=True, max_length=40)),
                ('company_name', models.CharField(blank=True, max_length=40)),
                ('company_address', models.TextField(blank=True, max_length=264)),
                ('residential_address', models.TextField(blank=True, max_length=264)),
                ('landline_number', models.CharField(blank=True, max_length=10)),
                ('cellphone_number', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('company_website', models.CharField(blank=True, max_length=100)),
                ('business_category', models.CharField(blank=True, max_length=100)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='company_logo')),
                ('member_picture', models.ImageField(blank=True, null=True, upload_to='member_picture')),
                ('association_name', models.CharField(blank=True, max_length=264)),
                ('member_id', models.CharField(blank=True, max_length=100)),
                ('term', models.CharField(blank=True, max_length=50)),
                ('company_profile', models.FileField(blank=True, null=True, upload_to='company_profile')),
            ],
        ),
    ]