from django.contrib import admin
from member_app.models import MemberInfo

# Register your models here.


@admin.register(MemberInfo)
class MemberInfoAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'designation', 'company_name', 'company_address', 'residential_address', 'landline_number', 'cellphone_number', 'email', 'company_website', 'business_category', 'company_logo', 'member_picture', 'association_name', 'member_id', 'term', 'company_profile']