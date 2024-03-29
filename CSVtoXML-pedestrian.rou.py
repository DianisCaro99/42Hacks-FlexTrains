import pandas as pd

#Document osm.pedestrian.rou.xml
df = pd.read_csv('./generated_demand/demand_100000.csv', sep=',')
df=df.iloc[:100,:]
def convert_row(row):
    time_dateTime = pd.to_datetime(row.Time)
    time = str(time_dateTime.hour)+"."+str(time_dateTime.minute)
    
    time_dateTime_bus = pd.to_datetime(row.time_for_bus)
    time_bus = str(time_dateTime_bus.hour)+"."+str(time_dateTime_bus.minute)

    if "�" in row.id_busStop:
        id_busStop = row.id_busStop.replace("�", "–")
    else:
        id_busStop = row.id_busStop

    if "�" in row.id_TrainStation:
        id_TrainStation = row.id_TrainStation.replace("�", "–")
    else:
        id_TrainStation = row.id_TrainStation

    return """
    <person id="ped%s" type="ped_pedestrian" depart="%s">
        <walk edges="x" busStop="%s"/>
        <ride intended="%s" depart="%s"/>
    </person>
    """ % (
    int(row.id), time, id_busStop, id_TrainStation, time_bus)

file1 = open("osm.pedestrian.rou.xml","w")
file1.write("""<?xml version="1.0" encoding="UTF-8"?>""")
file1.write("""\n<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">""")
file1.write("""<vType id="ped_pedestrian" vClass="pedestrian"/>""")
file1.write("".join(df.apply(convert_row, axis=1)))
file1.write("</routes>")
file1.close()
