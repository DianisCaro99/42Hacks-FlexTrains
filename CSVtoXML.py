import pandas as pd

df = pd.read_csv('./generated_demand/demand_1000.csv', sep=',')

def convert_row(row):
    return """
    <person id="ped%s" type="ped_pedestrian" depart="%s">
        <walk busStop="%s"/>
        <ride busStop="%s" intended="" depart="%s"/>
        <walk busStop="%s"/>
        <ride busStop="%s" intended="" depart="%s"/>
    </person>
    """ % (
    row.index, row.Time, row.id_busStop, row.id_busStop, row.Time, row.id_busStop, row.Time)

print('\n').join(df.apply(convert_row, axis=1))
