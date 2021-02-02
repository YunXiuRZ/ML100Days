import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('titanic')

#1
sns.barplot(x='sex',
            y='survived',
            hue='pclass',
            data=df)

#2
g = sns.FacetGrid(df, col='survived')
g.map(plt.hist, "sex")

#3
survived_counts = pd.crosstab([df.pclass, df.sex],
                              df.survived)
sns.violinplot(data=survived_counts)
plt.show()
