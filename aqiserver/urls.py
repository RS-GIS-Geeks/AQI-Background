from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'aqimonth', views.AqimonthdataViewSet)
router.register(r'aqiday', views.AqidaydataViewSet)
router.register(r'getcitiesinfo', views.CityViewSet)
router.register(r'getprovincesinfo', views.ProvinceViewSet)
router.register(r'getdailynationaldata', views.getdailynationaldataViewSet, base_name='getdailynationaldata')
router.register(r"getyearaqidata", views.getyearaqidataViewSet, base_name='getyearaqidata')
router.register(r'getcitypollutantsbyyear', views.getcitypollutantsbyyearViewSet, base_name='getcitypollutantsbyyear')
router.register(r'getcitydaysleavelbyyear', views.getcitydaysleavelbyyearViewSet, base_name='getcitydaysleavelbyyear')
router.register(r'getdailydatabymouth', views.getdailydatabymouthViewSet, base_name='getdailydatabymouth')
router.register(r'getdatatimespan', views.getdatatimespanViewSet, base_name='getdatatimespan')
router.register(r'getmonthlevelanddata', views.getmonthlevelanddataViewSet, base_name='getmonthlevelanddata')
# new apis
router.register(r'gettop10city', views.gettop10cityViewSet, base_name='gettop10city')
router.register(r'get3avgindexofcity', views.get3avgindexofcityViewSet, base_name='get3avgindexofcity')
router.register(r'getprovincesnames', views.getprovincesnamesViewSet, base_name='getprovincesnames')
router.register(r'getprovincesdata', views.getprovincesdataViewSet, base_name='getprovincesdata')

urlpatterns = [
    path('', include(router.urls)),
    # path('getdailynationaldata/', views.getdailynationaldata)
]
