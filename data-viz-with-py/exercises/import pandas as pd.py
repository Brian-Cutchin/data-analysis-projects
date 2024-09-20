import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
import seaborn as seaborn

df = pd.read_csv(r'C:\Users\bccut\OneDrive\Desktop\LaunchCode\data-analysis-projects\data-viz-with-py\exercises\Popular_Spotify_Songs.csv', index_col='track_name')
print(df)

df.isna()
print(df.isna())


df.dropna(how='all')

print(df)