from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from finance.models import FinancialRecord
from core.permissions import IsAnalystOrAdmin, IsViewer
from rest_framework.permissions import IsAuthenticated
from django.db.models.functions import TruncMonth

# Create your views here.
class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        records = FinancialRecord.objects.all()

        income = records.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        expense = records.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

        return Response({
            "total_income": income,
            "total_expense" : expense,
            "net_balance": income-expense
        })
    
class CategorySummaryView(APIView):
    permission_classes = [IsAnalystOrAdmin]

    def get(self, request):
        data = (
            FinancialRecord.objects
            .values('category')
            .annotate(total=Sum('amount'))
        )
        return Response(data)
    
class MonthlyTrendsView(APIView):
    permission_classes = [IsAnalystOrAdmin]

    def get(self, request):
        data = (
            FinancialRecord.objects
            .annotate(month=TruncMonth('date'))
            .values('month', 'type')
            .annotate(total=Sum('amount'))
            .order_by('month')
        )

        return Response(data)