import pandas as pd
import glob,os

#Load the original Safety data CSV files from Grab
path=r'../safety/features'
all_files = glob.glob(os.path.join(path, "*.csv"))
rawdata = pd.concat((pd.read_csv(f) for f in all_files),ignore_index=True)
print(rawdata.describe())
