

StringZatuchka = ["Наиболее предпочтительные точки: ",
"Точка 4: lat48.6971 lon44.5008",
"Ссылка : https://www.openstreetmap.org/#map=16/48.6971/44.5008",
"Точка 17: lat48.7076 lon44.5193",
"Ссылка : https://www.openstreetmap.org/#map=16/48.7076/44.5193",
" ",
"Точки с удовлетворительным уровнем оценки:",
"Точка 3: lat48.6888 lon44.4916",
"Ссылка : https://www.openstreetmap.org/#map=16/48.6888/44.4916",
"Точка 9: lat48.6981 lon44.4971",
"Ссылка : https://www.openstreetmap.org/#map=16/48.6981/44.4971",
"Точка 16: lat48.6958 lon44.4918",
"Ссылка : https://www.openstreetmap.org/#map=16/48.6958/44.4918",
"Точка 2: lat48.6940 lon44.4956",
"Ссылка : https://www.openstreetmap.org/#map=16/48.6940/44.4956",
"Точка 1: lat48.7124 lon44.5267",
"Ссылка : https://www.openstreetmap.org/#map=16/48.7124/44.5267",
" ",
"Варианты, не прошедшие самый низкий уровень проверки:",
"Точка 5: lat48.7023 lon44.4806",
"Ссылка : https://www.openstreetmap.org/#map=16/48.7023/44.4806",
"Точка 7: lat48.6967 lon44.4785",
"Ссылка : https://www.openstreetmap.org/#map=16/48.6967/44.4785",
"Точка 14: lat48.6876 lon44.4845",
"Ссылка : https://www.openstreetmap.org/#map=16/48.6876/44.4845",
"Точка 15: lat48.6991 lon44.4950",
"Ссылка : https://www.openstreetmap.org/#map=16/48.6991/44.4950",
"Точка 10: lat48.7148 lon44.5077",
"Ссылка : https://www.openstreetmap.org/#map=16/48.7148/44.5077",
"Точка 8: lat48.7265 lon44.5192",
"Ссылка : https://www.openstreetmap.org/#map=16/48.7265/44.5192",
"Точка 12: lat48.7826 lon44.5580",
"Ссылка : https://www.openstreetmap.org/#map=16/48.7826/44.5580",
"Точка 13: lat48.7921 lon44.5860",
"Ссылка : https://www.openstreetmap.org/#map=16/48.7921/44.5860",
"Точка 11: lat48.7965 lon44.5972",
"Ссылка : https://www.openstreetmap.org/#map=16/48.7965/44.5972",
"Точка 6: lat48.7863 lon44.5580",
"Ссылка : https://www.openstreetmap.org/#map=16/48.7863/44.5580"]







pointsList = [[48.72205, 44.533836],[48.700027, 44.505806]]
try:
    from mapsWork import make_net
except:
    from .mapsWork import make_net




def compute(listOfPoints, param1,param2,param3):
    computedReturn = ["wow","uou","yoy"]
    if listOfPoints == "Магазин розничной торговли":
        return StringZatuchka
    else:
        try:
            for each in pointsList:
                a = each[0]
                o = each[1]
                net = make_net(a, o, circles=1)
                print(net)

                # и вот на этом этапе у меня есть сетка из центров точек. нужно вокруг каждой определить квадраты. как уже сделал  юпитерноутбуке
                # передать эти квадраты в базу данных с помощью
                # len(getOrgsSquare(48.6812, 48.7279, 44.4557, 44.5905))
                # для каждой организации в квадрате при условии наличия инн
                # нужно спарсить данные из
                # profit, gain, compPrice = getProfData(INN)
                # обновляя бд
                # update_org(INN, compPrice, gain, profit)
                # потом все данные нормализуются и передаются в electre
                # где в проводятся расчеты. потом полученные три списка возвращаются пользователю вместо затычки

                return computedReturn







        except Exception as e:
            print("ошибка : ",e)
            return StringZatuchka

    #print(listOfPoints)


    #return listOfPoints




if __name__ == '__main__':
    pass
    compute(pointsList, "s","s2","s3")
    # timestart = get_time
    # print(timestart)