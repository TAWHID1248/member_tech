from django.shortcuts import render

#model
from member_app.models import MemberInfo

#serializer
from member_app.serializers import MemberSerializer

#drf
from rest_framework.generics import ListAPIView

# Create your views here.
def home(request):
    return render(request, 'member_app/home.html')


class MemberListView(ListAPIView):
    queryset = MemberInfo.objects.all()
    serializer_class = MemberSerializer