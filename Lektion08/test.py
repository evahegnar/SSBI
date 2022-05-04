import zipfile
import pandas as pd
unzipped_file = zipfile.ZipFile("Master.zip", "r")

print(unzipped_file)

with unzipped_file.open("Teams.csv") as file:
    data = pd.read_csv(file)
    print(data)
#print(pd.read_csv)