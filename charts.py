# IMPORT MODULES
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# READ THE CSV
df = pd.read_csv("upgrade.csv")

mass_list = df["mass"].tolist()
mass_list.pop(0)

radius_list = df["radius"].tolist()
radius_list.pop(0)

gravity_list = df["star_gravity"].tolist()
gravity_list.pop(0)


# PLOT THE CHART OF MASS AND RADIUS
plt.figure()
sns.scatterplot(x = mass_list,y = radius_list)
plt.title("STAR MASS AND RADIUS")
plt.xlabel('MASS')
plt.ylabel('RADIUS')
plt.show()

# PLOT THE CHART OF MASS AND GRAVITY
plt.figure()
sns.scatterplot(x = mass_list,y = gravity_list)
plt.title("STAR MASS AND GRAVITY")
plt.xlabel('MASS')
plt.ylabel('GRAVITY')
plt.show()