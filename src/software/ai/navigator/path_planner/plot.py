import pandas as pd

original = pd.read_csv("paths.csv")
df = original.groupby(['sub_dest_x', 'sub_dest_y'])['total_duration'].idxmin()
new = original.loc[df]

dest_x = new.loc[new['connection_time(s)'] != 0.2]
dest_y = new.loc[new['connection_time(s)'] != 0.2]
