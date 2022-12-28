from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from corm.models import Report


class ReportDetailView(DetailView):
    model = Report
    template_name = "corm/report_detail.html"


def api_list_reports(request):
    # type django.db.models.query.QuerySet
    reports = Report.objects.all()

    data = {"reports": list(reports.values())}
    # not use django rest framework,  default python Native datatype
    return JsonResponse(data)


def api_report_detail(request, pk):
    # type corm.models.Report
    report = Report.objects.get(pk=pk)
    data = {
        "name": report.name,
        "ref_table": report.ref_table,
        "category": str(report.category),
        "active": report.active
    }

    return JsonResponse(data)
