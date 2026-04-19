import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], intercept + slope*df['Year'], color='red')

    plt.savefig("sea_level_plot.png")