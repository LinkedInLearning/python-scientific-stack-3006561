from urllib.request import urlopen

data_url = 'https://nyc-tlc.s3.amazonaws.com/trip+data/yellow_tripdata_2020-08.csv'
with urlopen(data_url) as fp, open('taxi.csv', 'wb') as out:
    for lnum, line in enumerate(fp, 1):
        out.write(line)
        if lnum == 10_001:
            break