# IMPORT MODULES
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# READ THE CSV
df = pd.read_csv("upgrade.csv")

radius_list = df["radius"].tolist()
radius_list.pop(0)




mass_list = df["mass"].tolist()
mass_list.pop(0)


x = []

for data in radius_list:
    x.append(data)

for data in mass_list:
    x.append(data)

print(x)

wcss = []

for i in range(1,11):
  kmeans = KMeans(n_clusters = i,init = 'k-means++',random_state = 42)
  kmeans.fit(x)

  # INERTIA METHOD RETURNS WCSS FOR THAT MODEL
  wcss.append(kmeans.inertia_)

plt.figure(figsize = (10,5))
sns.lineplot(range(1,11),wcss,marker = 'o',color = 'red')
plt.title('THE ELBOW METHOD')
plt.xlabel('number of clusters')
plt.ylabel('wcss')
plt.show()




