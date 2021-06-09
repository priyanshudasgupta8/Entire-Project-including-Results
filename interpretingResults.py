# IMPORT MODULES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# READ THE CSV
df = pd.read_csv("upgrade.csv")

# MAKE LISTS OF GRAPH DATA FROM CSV
star_names = df["star_names"].tolist()
star_names.pop(0)

star_mass = df["mass"].tolist()
star_mass.pop(0)

star_radius = df["radius"].tolist()
star_radius.pop(0)

star_distance = df["distance"].tolist()
star_distance.pop(0)

star_gravity = df["star_gravity"].tolist()
star_gravity.pop(0)


## USING MATPLOTliB IT GIVES ERROR THAT IT CANNOT TAKE STAR NAMES AS IT IS A STRING

#plt.figure()
#sns.barplot(x = star_names,y = star_mass)
#plt.title("STAR NAMES VS MASS")
#plt.xlabel('NAMES')
#plt.ylabel('MASS')
#plt.show()

#plt.figure()
#sns.barplot(x = star_names,y = star_radius)
##plt.title("STAR NAMES VS RADIUS")
#plt.xlabel('NAMES')
#plt.ylabel('RADIUS')
#plt.show()

##plt.figure()
#sns.barplot(x = star_names,y = star_distance)
#plt.title("STAR NAMES VS DISTANCE")
#plt.xlabel('NAMES')
#plt.ylabel('DISTANCE')
#plt.show()

##plt.figure()
#sns.barplot(x = star_names,y = star_gravity)
#plt.title("STAR NAMES VS GRAVITY")
#plt.xlabel('NAMES')
##plt.ylabel('GRAVITY')
#plt.show()

# PLOT THE GRAPHS
fig1 = px.bar(x = star_names,y = star_mass,title="NAMES VS MASS")
fig1.show()

fig2 = px.bar(x = star_names,y = star_distance,title="NAMES VS DISTANCE")
fig2.show()

fig3 = px.bar(x = star_names,y = star_gravity,title="NAMES VS GRAVITY")
fig3.show()

fig4 = px.bar(x = star_names,y = star_radius,title="NAMES VS RADIUS")
fig4.show()


