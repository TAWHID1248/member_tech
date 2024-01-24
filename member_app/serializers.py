from rest_framework import serializers
from member_app.models import MemberInfo



class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberInfo
        fields = ['full_name', 'designation', 'company_name', 'company_address', 'residential_address', 'landline_number', 'cellphone_number', 'email', 'company_website', 'business_category', 'company_logo', 'member_picture', 'association_name', 'member_id', 'term', 'company_profile']