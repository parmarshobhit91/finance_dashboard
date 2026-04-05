from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.
# @api_view(['GET'])
# @permission_classes([AllowAny])   # 👈 THIS IS THE FIX
# def api_root(request):
#     return Response({
#         "message": "Finance Dashboard API is running",
#         "users": "/api/users/",
#         "records": "/api/records",
#         "dashboard": "/api/dashboard/",
#         "category_summary": "/api/category-summary/",
#         "monthly_trends": "/api/monthly-trends/"
#     })

def home(request):
    return render(request, 'home.html')