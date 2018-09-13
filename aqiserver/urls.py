from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'aqimonth', views.AqimonthdataViewSet)
router.register(r'aqiday', views.AqidaydataViewSet)
router.register(r'getcitiesinfo', views.CityViewSet)
router.register(r'getdailynationaldata', views.getdailynationaldataViewSet, base_name='getdailynationaldata')
router.register(r"getyearaqidata", views.getyearaqidataViewSet, base_name='getyearaqidata')
router.register(r'getcitypollutantsbyyear', views.getcitypollutantsbyyearViewSet, base_name='getcitypollutantsbyyear')
router.register(r'getcitydaysleavelbyyear', views.getcitydaysleavelbyyearViewSet, base_name='getcitydaysleavelbyyear')
router.register(r'getdailydatabymouth', views.getdailydatabymouthViewSet, base_name='getdailydatabymouth')
router.register(r'getdatatimespan', views.getdatatimespanViewSet, base_name='getdatatimespan')
router.register(r'getmonthlevelanddata', views.getmonthlevelanddataViewSet, base_name='getmonthlevelanddata')

urlpatterns = [
    path('', include(router.urls)),
    # path('getdailynationaldata/', views.getdailynationaldata)
]