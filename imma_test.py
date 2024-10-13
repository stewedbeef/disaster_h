import gzip
import pandas as pd
import numpy as np
import argparse

# Arguments for tool
parser = argparse.ArgumentParser(description="Stage 1 or data processing")

arguments = parser.add_argument_group("Arguments")
arguments.add_argument("-d", "--data", help="Path to train input data as IMMA", required=True)

args = parser.parse_args()

path = args.data
out_path = path + "_stage1.csv"

print("Loading IMMA...")


country = ["NL", "NO", "US", "UK", "FR", "DK", "IT", "ID", "HK", "NZ", "IE", "PH", "EG", "CA", "BE", "SA", "Australia", "Japan", "Pakistan", "Argentina", "Sweden", "FRG", "Iceland", "Israel", "Malaysia"]

def try_int(i):
    try:
        return int(i)
    except:
        return np.nan

cols = ["YEAR", "MONTH", "DAY", "LAT", "LON", "COUNTRY", "SST", "SLP", "W", "AT", "WW", "W1", "PPP", "WD", "WP", "WH", "SD", "SP", "SH"]

df = pd.DataFrame(columns=cols)

i = 0

with gzip.open(path, "r") as f:
    while line := f.readline().decode('utf-8') != '':
        entry = f.readline().decode('utf-8')

        if i % 100000 == 0:
            print(100000 * i, "processed...")
        i += 1

        year = try_int(entry[0:4])
        month = try_int(entry[4:6])
        day = try_int(entry[6:8])

        lat = try_int(entry[12:17])
        long = try_int(entry[17:23])
        long = 360-long if long > 180 else long

        country = try_int(entry[43:45])

        sst = try_int(entry[85:89])

        slp = try_int(entry[59:64])

        w = try_int(entry[50:53])

        at = try_int(entry[69:73])

        ww = try_int(entry[56:58])

        w1 = try_int(entry[58:59])

        ppp = try_int(entry[65:68])

        wd = try_int(entry[96:98])

        wp = try_int(entry[98:100])
        wh = try_int(entry[100:102])
        sd = try_int(entry[102:104])
        sp = try_int(entry[104:106])
        sh = try_int(entry[106:108])

        df = pd.concat([df, pd.DataFrame([[year, month, day, lat, long, country, sst, slp, w, at, ww, w1, ppp, wd, wp, wh, sd, sp, sh]], columns=cols)])

df.to_csv(path + ".csv")
