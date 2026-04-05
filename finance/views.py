from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from core.permissions import IsAdmin, IsAnalystOrAdmin
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class FinancialRecordViewSet(ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer
    filterset_fields = ['type', 'category', 'date']

    def get_permissions(self):
        if self.request.user.role == "viewer":
            return [IsAdmin()]
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        elif self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAnalystOrAdmin()]