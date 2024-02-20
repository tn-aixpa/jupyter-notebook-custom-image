import mlrun
import pandas as pd

@mlrun.handler(outputs=["dataset"])
def downloader(context, url: mlrun.DataItem):
    # read and rewrite to normalize and export as data
    df = url.as_df(format='parquet')
    return df


@mlrun.handler(outputs=["dataset-measures"])
def measure(context, di: mlrun.DataItem):
    
    KEYS = ['00:00-01:00', '01:00-02:00', '02:00-03:00', '03:00-04:00', '04:00-05:00', '05:00-06:00', '06:00-07:00', '07:00-08:00', '08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00', '17:00-18:00', '18:00-19:00', '19:00-20:00', '20:00-21:00', '21:00-22:00', '22:00-23:00', '23:00-24:00']
    COLUMNS=['data','codice spira']
    
    df = di.as_df()
    rdf = df[COLUMNS+KEYS]
    ls = []
    for key in KEYS:
        k = key.split("-")[0]
        xdf = rdf[COLUMNS + [key]]
        xdf['time'] = xdf.data.apply(lambda x: x+' ' +k)
        xdf['value'] = xdf[key]
        ls.append(xdf[['time','codice spira','value']])
    edf = pd.concat(ls)
    return edf



@mlrun.handler(outputs=["dataset-spire"])
def process(context, di: mlrun.DataItem):
    
    KEYS=['codice spira','longitudine','latitudine','Livello','tipologia','codice','codice arco','codice via','Nome via', 'stato','direzione','angolo','geopoint']
    df = di.as_df()
    sdf= df.groupby(['codice spira']).first().reset_index()[KEYS]

    return sdf