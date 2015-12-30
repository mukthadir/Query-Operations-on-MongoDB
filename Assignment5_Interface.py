#!/usr/bin/python2.7
#
# Assignment3 Interface
# Name: 
#

from pymongo import MongoClient
import os
import sys
import json
from math import cos, sin, sqrt, atan2, radians

#R = 3959


def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
    query_name = 'name'
    query_address = 'full_address'
    query_city = 'city'
    query_state = 'state'
    cursor = collection.find()
    file = open(saveLocation1, 'w')
    for document in cursor:
        city_document = document[query_city]
        if is_equal(cityToSearch, city_document):
            name = document[query_name]
            full_address = document[query_address]
            new_full_address = full_address.replace("\n", ", ")
            city = document[query_city]
            state = document[query_state]
            result = name + str('$') + new_full_address + str('$') + city + str('$') + state + str('.\n')
            file.write(result)
    file.close()


def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    lat1 = float(myLocation[0])
    lon1 = float(myLocation[1])
    query_latitude = 'latitude'
    query_longitude = 'longitude'
    query_categories = 'categories'
    query_name = 'name'

    file = open(saveLocation2, 'w')
    cursor = collection.find()
    for document in cursor:
        lat2 = document[query_latitude]
        lon2 = document[query_longitude]
        if distance(lat2, lon2, lat1, lon1) < maxDistance:
            categories = document[query_categories]
            for category in categoriesToSearch:
                if category in categories:
                    result = document[query_name] + str('\n')
                    file.write(result.encode("utf-8"))
                    break
    file.close()


def distance(lat2, lon2, lat1, lon1):
    R = 3959
    radian1 = radians(lat1)
    radian2 = radians(lat2)
    theta = radians(lat2-lat1)
    lamda = radians(lon2 - lon1)

    a = sin(theta/2)*sin(theta/2) + cos(radian1)*cos(radian2)*sin(lamda/2)*sin(lamda/2)

    c = 2*atan2(sqrt(a), sqrt(1-a))
    d = R*c
    return d
    
#    dlon = lon2 - lon1
#    dlat = lat2 - lat1
#    a = (sin(dlat/2)) ** 2 + cos(lat1)*cos(lat2)*(sin(dlon/2)) ** 2
#    c = 2*atan2(sqrt(a), sqrt(1-a))
#    dist = R * c
#    return dist


def is_equal(a, b):
    try:
        return a.upper() == b.upper()
    except AttributeError:
        return a == b
