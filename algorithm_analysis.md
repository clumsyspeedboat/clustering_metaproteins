# Goal: To cluster points to fit class labels

## Data : Metaprotein abundance for patients with bowel disease

**Rows(Patients) * Variables(Metaproteins):** 48 * 2969

**Class Labels:** C(21), CD(13) and UC(14)

**Original data, their transformations used in experiments**

* df_csv_data - Original dataframe
* df_normalized - PCA of original dataframe
* df_U - dataframe of unnormalized eigen values of original
* df_N - dataframe of normalized eigen values of original

#### Note : All points are plotted on principal component axes
########################################################################################################

### Cluster analysis (number of clusters = 3) for sklearn.cluster.SpectralClustering

![image](https://user-images.githubusercontent.com/57228346/196718278-c9c8c368-9855-4c1d-a271-6844ab0a43de.png)

* Inferior cluster separation for original silhouette values under 0 and adjusted randsignificantly close to 0
* PCA (2 components) was performed on the normalized dataframe and it slightly decreased cluster seperation, which shows it might be a redundant step for spectral analysis

### Spectral Clustering for k = 3 using sklearn.cluster.SpectralClustering, σ = unknown

**Original Data**
  ![image](https://user-images.githubusercontent.com/57228346/196416057-39a6b836-5962-44d8-8921-b0359cbf6ef5.png)
**Normalized(Original) Data**
  ![image](https://user-images.githubusercontent.com/57228346/196416087-52ddd985-1c95-4bdb-a13f-6c64975d244c.png)
**PCA(Normalized) Data**
  ![image](https://user-images.githubusercontent.com/57228346/196723034-74e93d9d-5278-421a-953a-59e14662579b.png)
  
* While Normalized(Original) data provides the best cluster seperation, PCA(normalized) provides best results in separating class labels.



