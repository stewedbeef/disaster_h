import IMMA
import pandas as pd
import argparse 

# Arguments for tool
parser = argparse.ArgumentParser(description="Stage 1 or data processing")

arguments = parser.add_argument_group("Arguments")
arguments.add_argument("-d", "--data", help="Path to train input data as IMMA", required=True)

args = parser.parse_args()

path = args.data
out_path = path + "_stage1.csv"

print("Loading IMMA...")
imma_data = IMMA.read(path)
print("Loaded IMMA data")

print("Filtering...")

desired_stats = ["C1", "YR", "MO", "DY", "LAT", "LON", "SST", "SLP", "W", "AT", "WW", "W1", "PPP", "WD", "WP", "WH", "SD", "SP", "SH"]

processed = pd.DataFrame(columns=desired_stats)

def lon_fix(x):
    return x-360 if x > 180 else x

for i, entry in enumerate(imma_data):
    lat = entry["LAT"]
    lon = lon_fix(entry["LON"])
    
    if i % (len(imma_data) / 50000):
        print("1/50000th through the set.", i/len(imma_data))

    if lat < 10.5 and lat > 46.8:
        continue

    if lon < -95 or lon > -22.75:
        continue

    processed = pd.concat([processed, pd.DataFrame([[entry[key] for key in desired_stats]], columns=processed.columns)])

print("Writing csv...")

processed.to_csv("out_path")
