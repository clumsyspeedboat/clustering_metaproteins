# Goal: To cluster points to fit class labels

## Data : Metaprotein abundance for patients with bowel disease

**Rows(Patients) * Variables(Metaproteins):** 48 * 2969

**Class Labels:** C(21), CD(13) and UC(14)

**Original data, their transformations used in experiments**

* df_csv_data - Original dataframe
* df_normalized - PCA of original dataframe
* df_U - dataframe of unnormalized eigen values of original
* df_N - dataframe of normalized eigen values of original

**Note : All points are plotted on principal component axes**


## Cluster analysis (number of clusters = 3)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
### Original data

##### Spectral clustering on original, normalized(original) and PCA(normalized) data, k = 3, sigma = NA (kNN graph)
<img src = "https://user-images.githubusercontent.com/57228346/196718278-c9c8c368-9855-4c1d-a271-6844ab0a43de.png" width = "600">

**Original Data**
  ![image](https://user-images.githubusercontent.com/57228346/196416057-39a6b836-5962-44d8-8921-b0359cbf6ef5.png)
**Normalized(Original) Data**
  ![image](https://user-images.githubusercontent.com/57228346/196416087-52ddd985-1c95-4bdb-a13f-6c64975d244c.png)
**PCA(Normalized) Data**
  ![image](https://user-images.githubusercontent.com/57228346/196723034-74e93d9d-5278-421a-953a-59e14662579b.png)
  
* Normalized(Original) data provides the best cluster seperation, as well as class label separation.
* Inferior cluster separation for original silhouette values under 0 and adjusted randsignificantly close to 0
* PCA (2 components) was performed on the normalized dataframe and it slightly decreased cluster seperation, which shows it might be a redundant step for spectral analysis

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

### Eigen(Original data)

#### Optimal sigma for adjacency matrix in NJW algorithm
* Sigma for highest rand index = 91
<img src = "https://user-images.githubusercontent.com/57228346/197412509-b4f373be-c4e6-43ea-949d-6547a89d88a3.png" width = "600"> 

* Sigma for highest rand index = 99
<img src = "https://user-images.githubusercontent.com/57228346/197413400-6619c689-1df3-476b-b54c-2d74491ff0c1.png" width = "600">

##### KMeans on unnormalized and normalized eigen (NJW algorithm) of original data, k = 3, sigma = 99
<img src = "https://user-images.githubusercontent.com/57228346/197419477-4304ba05-baf9-4fdc-b4b8-ec56edbe16fc.png" width = "600">

**Unnormalized Eigen (Original data)**
  ![image](https://user-images.githubusercontent.com/57228346/197419830-8b3195e4-3f91-49b2-8a13-1d07bbe4353e.png)


**Normalized Eigen (Original data)**
  ![image](https://user-images.githubusercontent.com/57228346/197419840-dfe6c889-25b5-4aa7-8b32-7eea088cb487.png)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

### Eigen(Normalized data)

#### Optimal sigma for adjacency matrix in NJW algorithm
* Sigma for highest rand index = 0.5
<img src = "https://user-images.githubusercontent.com/57228346/197419253-ebbf4d87-7a98-454d-8a21-be22dcd2936a.png" width = "600"> 

* Sigma for highest rand index = 0.3
<img src = "https://user-images.githubusercontent.com/57228346/197419179-f9fa7c0b-9fea-4ad4-8bbb-0239adc30898.png" width = "600">

##### KMeans on unnormalized and normalized eigen (NJW algorithm) of normalized data, k = 3, sigma = 0.5 (unnormalized) and 0.3 (normalized)
<img src = "https://user-images.githubusercontent.com/57228346/197420297-e84c5cac-755a-436c-99eb-545b69e1a127.png" width = "600">

**Unnormalized Eigen (Unnormalized data), sigma = 0.5**
  ![image](https://user-images.githubusercontent.com/57228346/197420531-57302fc6-a062-4d9c-9588-ee90ea875aea.png)

**Normalized Eigen (Normalized data), sigma = 0.3**
  ![image](https://user-images.githubusercontent.com/57228346/197420546-59b515d5-b495-48b0-99ea-cb9e2e59879b.png)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

### Eigen(PCA data)

#### Optimal sigma for adjacency matrix in NJW algorithm
* Sigma for highest rand index = 0.35
<img src = "https://user-images.githubusercontent.com/57228346/197421404-695aa420-232e-4de5-ba9d-2754fd0b50c3.png" width = "600"> 

* Sigma for highest rand index = 0.20
<img src = "https://user-images.githubusercontent.com/57228346/197421418-112b6d14-7990-4621-bb99-299bd5ea1507.png" width = "600">


##### KMeans on unnormalized and normalized eigen (NJW algorithm) of pca data, k = 3, sigma = 0.75 (unnormalized) and 0.05 (normalized)
<img src = "https://user-images.githubusercontent.com/57228346/197421866-88f33018-624c-4544-ad81-8a44e86c779f.png" width = "600">


**Unnormalized Eigen (PCA data), sigma = 0.35**
  ![image](https://user-images.githubusercontent.com/57228346/197421906-4b004603-9e04-4847-b9a7-a2c596553cc2.png)
  
**Normalized Eigen (PCA data), sigma = 0.20**
  ![image](https://user-images.githubusercontent.com/57228346/197421916-51a08520-24df-4da7-a702-79951bcae34b.png)




