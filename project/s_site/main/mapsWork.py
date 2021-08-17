from bs4 import BeautifulSoup
try:
    from helpTools import dump, get_right, log, get_html
except:
    from .helpTools import dump, get_right, log, get_html
import requests
import json
from geopy.distance import geodesic
from bs4 import BeautifulSoup




def make_net(lat, lon, circles=1):
    # возвращает список
    l1 = []
    need_len = 0.00177
    start_lat = lat
    start_lon = lon
    for i in range(circles):
        start_lat = start_lat+need_len
        start_lon = start_lon+need_len

    for k in range(circles*2):
        start_lat=start_lat-need_len
        l1.append([float('{:.6f}'.format(start_lat)), float('{:.6f}'.format(start_lon))])

    for k in range(circles*2):
        start_lon=start_lon-need_len
        l1.append([float('{:.6f}'.format(start_lat)), float('{:.6f}'.format(start_lon))])

    for k in range(circles * 2):
        start_lat = start_lat + need_len
        l1.append([float('{:.6f}'.format(start_lat)), float('{:.6f}'.format(start_lon))])

    for k in range(circles * 2):
        start_lon = start_lon + need_len
        l1.append([float('{:.6f}'.format(start_lat)), float('{:.6f}'.format(start_lon))])
    return l1


# round = make_net(48.713109,  44.501474, circles=3)





def defGetNearest(lat, lon, key=None):
    if key==None:
        key = "6FA82531-7162F2EC-F2DDD496-9B899ACB-75D41B07-F0B29EB3-CD773D51-EED27343"
    stringPattern =  "http://api.wikimapia.org/?function=place.getnearest&key={}&lat={}&lon={}"

    getString = stringPattern.format(key, lat, lon)

    rqst = get_html(getString)
    # print("response_code",rqst)
    rqst = rqst.content

    soup1 = BeautifulSoup(rqst, "xml")
    soup1 = soup1.prettify()
    dump("wikimapia", getString, soup1)

    return getString






def make_net(lat, lon, circles=1):
    l1 = []
    need_len = 0.00177
    start_lat = lat
    start_lon = lon
    for i in range(circles):
        start_lat = start_lat+need_len
        start_lon = start_lon+need_len

    for k in range(circles*2):
        start_lat=start_lat-need_len
        l1.append([float('{:.6f}'.format(start_lat)), float('{:.6f}'.format(start_lon))])

    for k in range(circles*2):
        start_lon=start_lon-need_len
        l1.append([float('{:.6f}'.format(start_lat)), float('{:.6f}'.format(start_lon))])

    for k in range(circles * 2):
        start_lat = start_lat + need_len
        l1.append([float('{:.6f}'.format(start_lat)), float('{:.6f}'.format(start_lon))])

    for k in range(circles * 2):
        start_lon = start_lon + need_len
        l1.append([float('{:.6f}'.format(start_lat)), float('{:.6f}'.format(start_lon))])
    return l1


# round = make_net(48.713109,  44.501474, circles=1)
# print(round)




def defGetNearest(lat, lon, key=None):
    if key==None:
        key = "6FA82531-7162F2EC-F2DDD496-9B899ACB-75D41B07-F0B29EB3-CD773D51-EED27343"
    stringPattern =  "http://api.wikimapia.org/?function=place.getnearest&key={}&lat={}&lon={}"
    getString = stringPattern.format(key, lat, lon)
    rqst = get_html(getString)
    # print("response_code",rqst)
    rqst = rqst.content
    soup1 = BeautifulSoup(rqst, "xml")
    soup1 = soup1.prettify()
    dump("wikimapia", getString, soup1)
    return getString


def getDistance(lonFrom, latFrom, lonTo, LatTo):
    point_from = (lonFrom, latFrom)
    point_to = (lonTo, LatTo)
    distance = None
    try:
        results = requests.get("https://graphhopper.com/api/1/route?point={},{}&point={},{}&vehicle=foot&calc_points=false&key=5061955b-14b8-4f76-80e8-9e10821f5e85".format(lonFrom, latFrom, lonTo, LatTo ))
        resultstxt = results.text
        resultsdict = json.loads(resultstxt)
        # dump("dumpFolder", "dumpFile", resultsdict)
        # resultsdict = get_right("dumpFolder", "dumpFile","DICT")
        distance = float(resultsdict['paths'][0]['distance'])
        print("trueDistance",distance)
    except:
        distance = float(geodesic(point_from, point_to).meters)
        print("wrongDistance", distance)
    return distance




# distance = getDistance(48.70287, 44.57678, 48.70081, 44.57935)
# print(distance)

