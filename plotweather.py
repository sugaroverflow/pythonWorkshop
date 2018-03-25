# Pandas for managing datasets
import pandas as pd
# Matplotlib for additional customization
from matplotlib import pyplot as plt
# Seaborn for plotting and styling
import seaborn as sns


def main():
  # Read dataset
  temps = pd.read_csv('London.csv')

  sns.pointplot(x="Day", y="Low Temp", data=temps)

  # add some labels
  plt.title("Graph of weekly Low temperature in London, Ontario")
  plt.xlabel("Day")
  plt.ylabel("Low Temp");

  # show the plot
  plt.show()

if __name__ == '__main__':
    main()


