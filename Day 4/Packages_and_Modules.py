# Importing Required Libraries
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Creating a Sales DataFrame
sales_df = pd.DataFrame({'Month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                        'Sales': [1000, 1500, 1200, 1700, 1600, 2000, 1800, 2100, 2300, 1700, 1300, 1500]})

# Creating a Feature Matrix
X = sales_df.iloc[:, [0, 1]].values

# Creating an Instance of KMeans
kmeans = KMeans(n_clusters = 3)

# Fitting the Model
kmeans.fit(X)

# Assigning the Clusters
sales_df['Cluster'] = kmeans.labels_

# Printing the Sales DataFrame with Cluster Labels
print(sales_df)
