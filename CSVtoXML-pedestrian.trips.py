import pandas as pd

#Document osm.pedestrian.rou.xml
df = pd.read_csv('./generated_demand/demand_10000.csv', sep=',')
df=df.iloc[:100,:]
def convert_row(row):
    time_dateTime = pd.to_datetime(row.Time)
    time = str(time_dateTime.hour)+"."+str(time_dateTime.minute)

    if "�" in row.id_busStop:
        id_busStop = row.id_busStop.replace("�", "–")
    else:
        id_busStop = row.id_busStop

    if "�" in row.id_TrainStation:
        id_TrainStation = row.id_TrainStation.replace("�", "–")
    else:
        id_TrainStation = row.id_TrainStation

    return """
    <person id="ped%s" depart="%s" type="ped_pedestrian">
        <personTrip from="%s" to="%s" modes="public"/>
    </person>
    """ % (
    int(row.id), time, id_busStop, id_TrainStation)

file1 = open("osm.pedestrian.trips.xml","w")
file1.write("""<?xml version="1.0" encoding="UTF-8"?>""")
file1.write("""<!-- generated on 2021-10-22 19:59:28.281209 by $Id$ v1_10_0+0000-83496a5972
  options: 
-->""")
file1.write("""\n<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">""")
file1.write("""<vType id="ped_pedestrian" vClass="pedestrian"/>""")
file1.write("".join(df.apply(convert_row, axis=1)))
file1.close()
