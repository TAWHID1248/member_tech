from django.db import models

# Create your models here.


class MemberInfo(models.Model):
    full_name = models.CharField(max_length=40, blank=True)
    designation = models.CharField(max_length=40, blank=True)
    company_name = models.CharField(max_length=40, blank=True)
    company_address = models.TextField(max_length=264, blank=True)
    residential_address = models.TextField(max_length=264, blank=True)
    landline_number = models.CharField(max_length=15, blank=True)
    cellphone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    company_website = models.CharField(max_length=100, blank=True)
    business_category = models.CharField(max_length=100, blank=True)
    company_logo = models.ImageField(upload_to='company_logo', blank=True, null=True)
    member_picture = models.ImageField(upload_to='member_picture', blank=True, null=True)
    association_name = models.CharField(max_length=264, blank=True)
    member_id = models.CharField(max_length=100, blank=True)
    term = models.CharField(max_length=50, blank=True)
    company_profile = models.FileField(upload_to='company_profile', blank=True, null=True)

# 1.	Full name*
# 2.	Company name
# 3.	Designation
# 4.	Company Address
# 5.	Residential Address
# 6.	Phone number(land)
# 7.	Cellphone number*
# 8.	Email
# 9.	Company website
# 10.	Business category
# 11.	Picture*
# 12.	Company logo
# 13.	Association / Chamber
# 14.	Member ID
# 15.	Term
# 16.	Company Profile(pdf)
