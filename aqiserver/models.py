# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aqidaydata(models.Model):
    city = models.ForeignKey('City', models.DO_NOTHING, db_column='city')
    aqi = models.FloatField(blank=True, null=True)
    pm25 = models.FloatField(blank=True, null=True)
    pm10 = models.FloatField(blank=True, null=True)
    so2 = models.FloatField(blank=True, null=True)
    co = models.FloatField(blank=True, null=True)
    no2 = models.FloatField(blank=True, null=True)
    o3 = models.FloatField(blank=True, null=True)
    max_aqi = models.FloatField(blank=True, null=True)
    min_aqi = models.FloatField(blank=True, null=True)
    rank = models.FloatField(blank=True, null=True)
    quality = models.CharField(max_length=40, blank=True, null=True)
    time_point = models.CharField(max_length=20, blank=True, null=True)
    objects = models.Manager()

    class Meta:
        db_table = 'aqidaydata'


class Aqimonthdata(models.Model):
    city = models.ForeignKey('City', models.DO_NOTHING, db_column='city')
    aqi = models.FloatField(blank=True, null=True)
    pm25 = models.FloatField(blank=True, null=True)
    pm10 = models.FloatField(blank=True, null=True)
    so2 = models.FloatField(blank=True, null=True)
    co = models.FloatField(blank=True, null=True)
    no2 = models.FloatField(blank=True, null=True)
    o3 = models.FloatField(blank=True, null=True)
    max_aqi = models.FloatField(blank=True, null=True)
    min_aqi = models.FloatField(blank=True, null=True)
    rank = models.FloatField(blank=True, null=True)
    quality = models.CharField(max_length=40, blank=True, null=True)
    time_point = models.CharField(max_length=20, blank=True, null=True)
    objects = models.Manager()

    class Meta:
        db_table = 'aqimonthdata'


class City(models.Model):
    cityname = models.CharField(max_length=40)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    gdp = models.FloatField(blank=True, null=True)
    pop = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    # province = models.ForeignKey('Province', models.DO_NOTHING, db_column='province')
    objects = models.Manager()

    class Meta:
        db_table = 'city'


class Province(models.Model):
    provincename = models.CharField(max_length=40)
    objects = models.Manager()

    class Meta:
        db_table = 'province'
