from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework.response import Response
from collections import OrderedDict
from django.db.models import Avg, Max, Min, Count, Sum

# Create your views here.

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class AqimonthdataViewSet(viewsets.ModelViewSet):
    queryset = Aqimonthdata.objects.all()
    serializer_class = AqimonthdataSerializer

class AqidaydataViewSet(viewsets.ModelViewSet):
    queryset = Aqidaydata.objects.all()
    serializer_class = AqidaydataSerializer

class getdailynationaldataViewSet(viewsets.ViewSet):

    def list(self, request):
        date = request.GET["date"]
        data = Aqidaydata.objects.filter(time_point="{}".format(date))
        serializer = AqidaydataSerializer(data, many=True)
        return_list = []
        for item in serializer.data:
            in_data = OrderedDict()
            in_data["id"] = item["city"]["id"]
            in_data["name"] = item["city"]["cityname"]
            in_data["date"] = OrderedDict(year=date.split('-')[0], month=date.split('-')[1], day=date.split('-')[2])
            in_data["position"] = [item["city"]["lon"], item["city"]["lat"]]
            in_data["value"] = [
                item["aqi"],
                item["pm25"],
                item["pm10"],
                item["co"],
                item["no2"],
                item["so2"]
            ]
            in_data["level"] = item["quality"]
            return_list.append(in_data)
        return_list.sort(key=lambda x: x["value"][0], reverse=True)
        return Response(return_list)

class getyearaqidataViewSet(viewsets.ViewSet):

    def list(self, request):
        year = request.GET["year"]
        city = request.GET["city"]
        data = City.objects.get(id=city).aqidaydata_set.filter(time_point__startswith = "{}".format(year)).order_by("time_point")
        serializer = AqimonthdataSerializer(data, many=True)
        return_list = []
        for item in serializer.data:
            in_data = [item["time_point"], item["aqi"]]
            return_list.append(in_data)
        return Response(return_list)

class getcitypollutantsbyyearViewSet(viewsets.ViewSet):

    def list(self, request):
        year = request.GET["year"]
        city = request.GET["city"]
        data = City.objects.get(id=city).aqidaydata_set.filter(time_point__startswith="{}".format(year))
        return_list = []
        for item in ['aqi', 'pm25', 'pm10', 'co', 'no2', 'so2']:
            exec("max_{}=data.aggregate(Max('{}'))['{}__max']".format(item, item, item))
            exec("min_{}=data.aggregate(Min('{}'))['{}__min']".format(item, item, item))
            exec("avg_{}=data.aggregate(Avg('{}'))['{}__avg']".format(item, item, item))
        for item in ['max', 'min', 'avg']:
            in_list = []
            for value in ['aqi', 'pm25', 'pm10', 'co', 'no2', 'so2']:
                exec("in_list.append({}_{})".format(item, value))
            return_list.append(in_list)
        return Response(return_list)


class getcitydaysleavelbyyearViewSet(viewsets.ViewSet):

    def list(self, request):
        year = request.GET["year"]
        city = request.GET["city"]
        data = City.objects.get(id=city).aqidaydata_set.filter(time_point__startswith="{}".format(year)).values("quality").annotate(value=Count("quality"))
        return_list = []
        for item in data:
            in_dict = OrderedDict()
            in_dict["value"] = item["value"]
            in_dict["name"] = item["quality"]
            return_list.append(in_dict)
        return Response(return_list)

class getdailydatabymouthViewSet(viewsets.ViewSet):

    def list(self, request):
        year = request.GET["year"]
        city = request.GET["city"]
        month = request.GET["month"]
        month = month.zfill(2)
        yearandmonth = "{}-{}".format(year,month)
        data = City.objects.get(id=city).aqidaydata_set.filter(time_point__startswith="{}".format(yearandmonth)).order_by("time_point")
        serializer = AqidaydataSerializer(data, many=True)
        return_list = []
        for item in serializer.data:
            in_list = []
            day = int(item["time_point"].split("-")[2])
            in_list.append(day)
            in_list.append(item["aqi"])
            in_list.append(item["pm25"])
            in_list.append(item["pm10"])
            in_list.append(item["co"])
            in_list.append(item["no2"])
            in_list.append(item["so2"])
            in_list.append(item["quality"])
            return_list.append(in_list)
        return Response(return_list)

class getdatatimespanViewSet(viewsets.ViewSet):

    def list(self, request):
        city = request.GET["city"]
        min_date = City.objects.get(id=city).aqidaydata_set.aggregate(Min("time_point"))
        max_date = City.objects.get(id=city).aqidaydata_set.aggregate(Max("time_point"))
        return_dict = {
            'min': {
                'year': min_date["time_point__min"].split("-")[0],
                'month': min_date["time_point__min"].split("-")[1],
                'day': min_date["time_point__min"].split("-")[2],
            },
            'max': {
                'year': max_date["time_point__max"].split("-")[0],
                'month': max_date["time_point__max"].split("-")[1],
                'day': max_date["time_point__max"].split("-")[2],
            }
        }
        return Response(return_dict)

class getmonthlevelanddataViewSet(viewsets.ViewSet):

    def list(self, request):
        year = request.GET["year"]
        city = request.GET["city"]
        # month = request.GET["month"]
        # month = month.zfill(2)
        # yearandmonth = "{}-{}".format(year, month)
        return_list = []
        goodday_list=[]
        badday_list=[]
        aqimean_list=[]
        for month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
            yearandmonth = "{}-{}".format(year, month)
            exec("goodday_list.append(City.objects.get(id=city).aqidaydata_set.filter(time_point__startswith='{}'.format(yearandmonth), quality__in=['优', '良']).count())")
            exec("badday_list.append(City.objects.get(id=city).aqidaydata_set.filter(time_point__startswith='{}'.format(yearandmonth), quality__in=['轻度污染', '中度污染', '重度污染', '严重污染']).count())")
            exec("aqimean_list.append(City.objects.get(id=city).aqidaydata_set.filter(time_point__startswith='{}'.format(yearandmonth)).aggregate(Avg('aqi'))['aqi__avg'])")
        return_list.append(goodday_list)
        return_list.append(badday_list)
        return_list.append(aqimean_list)
        return Response(return_list)

class gettop10cityViewSet(viewsets.ViewSet):

    def list(self, request):
        date = request.GET["date"]
        return_dist = []
        aqi_list = []
        cityId_list = []
        city_list = []
        pm25_list = []
        so2_list = []
        latlng_list = []
        aqidata_on_date = Aqidaydata.objects.filter(time_point=date).order_by('-aqi').values()[:10]
        for data in aqidata_on_date:
            cityId = data['city_id']
            cityObject = City.objects.get(id=cityId)
            cityId_list.append(cityId)
            city_list.append(cityObject.cityname)
            aqi_list.append(data['aqi'])
            pm25_list.append(data['pm25'])
            so2_list.append(data['so2'])
            latlng_list.append([cityObject.lat, cityObject.lon])
        sum = 0
        for aqi in aqi_list:
            sum += aqi
        return_dist = {
            'city': city_list,
            'cityId': cityId_list,
            'aqi': aqi_list,
            'pm2.5': pm25_list,
            'so2': so2_list,
            'latlng': latlng_list,
            'average': sum / len(aqi_list)
        }
        # print(str(return_dist))
        return Response(return_dist)

class get3avgindexofcityViewSet(viewsets.ViewSet):

    def list(self, request):
        city = request.GET["city"]
        year = request.GET["year"]
        aqidata_on_date = Aqidaydata.objects.filter(time_point__startswith=year).filter(city__id=city).values('city').annotate(Avg('aqi'), Avg('pm25'), Avg('so2'))[0]
        result = {
            'aqi': aqidata_on_date['aqi__avg'],
            'pm25': aqidata_on_date['pm25__avg'],
            'so2': aqidata_on_date['so2__avg']
        }
        return Response(result)


class getprovincesnamesViewSet(viewsets.ModelViewSet):

    def list(self, request):
        queryset = Province.objects.all().values()
        return_list = []
        for query_item in queryset:
            return_list.append({
                'id': query_item['id'],
                'name': query_item['provincename']
            })
        return Response(return_list)


class getprovincesdataViewSet(viewsets.ModelViewSet):

    def list(self, request):
        provinceId = request.GET['province']
        city_list = City.objects.filter(province__id=provinceId).values()
        year_list = [2014, 2015, 2016, 2017]
        data_list = []
        for city in city_list:
            data = []
            for year in year_list:
                all_month_data = Aqimonthdata.objects.filter(city=city['id'], time_point__startswith=year).values('city').annotate(Avg('aqi'))
                for month_data in all_month_data:
                    data.append(round(month_data['aqi__avg'], 2))
            data_list.append({
                'name': city['cityname'],
                'data': data
            })
        return Response({
            'xaxis': year_list,
            'datalist': data_list
        })

class getmonthnationaldataViewSet(viewsets.ModelViewSet):

    def list(self, request):
        date = request.GET["date"]
        data = Aqimonthdata.objects.filter(time_point="{}".format(date))
        serializer = AqimonthdataSerializer(data, many=True)
        return_list = []
        for item in serializer.data:
            in_data = OrderedDict()
            in_data["id"] = item["city"]["id"]
            in_data["name"] = item["city"]["cityname"]
            in_data["date"] = OrderedDict(year=date.split('-')[0], month=date.split('-')[1])
            in_data["position"] = [item["city"]["lon"], item["city"]["lat"]]
            in_data["value"] = [
                item["aqi"],
                item["pm25"],
                item["pm10"],
                item["co"],
                item["no2"],
                item["so2"]
            ]
            in_data["level"] = item["quality"]
            return_list.append(in_data)
        return_list.sort(key=lambda x: x["value"][0], reverse=True)
        return Response(return_list)
