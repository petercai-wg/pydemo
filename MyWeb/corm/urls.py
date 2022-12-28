from django.urls import include, path

import corm.views.report_api as report_api
import corm.views.report_rest as report_rest

import corm.views.ProductView as productview

urlpatterns = [

    path('api/list_reports', report_api.api_list_reports,
         name='api_list_reports'),
    path('api/report/<str:pk>', report_api.api_report_detail,
         name='api_report_detail'),


    path('api/report_detail/<str:pk>', report_rest.rest_report_detail,
         name='rest_report_detail'),

    path('api/report_list', report_rest.ReportListView.as_view(),
         name='rest_report_detail'),

    path("report/<slug:slug>", report_api.ReportDetailView.as_view(),
         name="report_detail"),

    path('products/', productview.product_list_view),
    path('product/<int:pk>/', productview.product_detail_view, name="product-detail"),

    path('product/create/', productview.product_create_view, name="product-create"),
    #     path('products/<int:pk>/', product_detail_view),
]
