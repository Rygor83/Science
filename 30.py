from settings import *

# Load Dataset
titanic = sns.load_dataset("titanic")

# Plot
fig = sns.catplot(x="age", y="embark_town",
            hue="sex", col="class",
            data=titanic[titanic.embark_town.notnull()],
            orient="h", height=5, aspect=1, palette="tab10",
            kind="violin", dodge=True, cut=0, bw=.2)

fig.subtitle('sf')
plt.show()
