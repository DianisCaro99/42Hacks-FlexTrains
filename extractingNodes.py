import pandas as pd
from scipy.spatial import distance
import sys

fp = open("osm_bbox.osm.txt", encoding="utf8")
file1 = open("extracted_nodes_test.txt","w")

line = fp.readline()
cnt = 1
while line:
    if "<node" in line:
        file1.write(line)
    line = fp.readline()
    cnt += 1

fp.close()
file1.close()
def checkCloseNode(x):
    file = open("extracted_nodes_test.txt","r")
    line = file.readline()
    numDistancia = sys.float_info.max
    lineInfo = ""
    while line:
        information = line.split("\"")
        lat = float(x.Lat)
        lon = float(x.Lon)
        temDis = distance.euclidean([float(information[3]), float(information[5])], [lat, lon])
        if min(temDis, numDistancia) == temDis:
            numDistancia = temDis
            lineInfo = information[1]
        line = file.readline()
    file.close()
    resp = str(x.id) + " " + lineInfo + "\n"
    print(resp)
    return resp

fileFinalData = open("nodeForData_test.txt", "w")
df = pd.read_csv('./generated_demand/demand_100000.csv', sep=',')
df=df.iloc[:100,:]
fileFinalData.write("".join(df.apply(checkCloseNode, axis=1)))
fileFinalData.close()

