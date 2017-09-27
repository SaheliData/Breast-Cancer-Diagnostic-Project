# Creating connection to the database:-

drv <- dbDriver("PostgreSQL")

con <- dbConnect(drv, user="postgres", password="saheli",
                 host="localhost", port=5433, dbname="postgres")

#Data imported from the database

cancer data <- dbReadTable(con, "RestData")

#Ignoring the SCN and C attributes we got cleaned_cancer_Data

cleaned_cancer_data <- cancer data[,2 : 10]

#Replacing the missing value with the mean of the "nuclei_chromatin" column:-


cleaned_cancer_data$nuclei_chromatin[cleaned_cancer_data$nuclei_chromatin == 0] <- round(mean(cancer_data$nuclei_chromatin))

#Plotting all the attributes and C

hist(cleaned_cancer_data$clump_thickness)

hist(cleaned_cancer_data$cell_size)

hist(cleaned_cancer_data$cell_shape)

hist(cleaned_cancer_data$adhesion)

hist(cleaned_cancer_data$epithelial_cell_size)

hist(cleaned_cancer_data$nuclei_chromatin)

hist(cleaned_cancer_data$chromatin)

hist(cleaned_cancer_data$normal_nucleoli)

hist(cleaned_cancer_data$mitoses_class)

hist(cleaned_cancer_data$class)

#Mean, meadian, mode and variance calculation:-


> mean(cancer_data$clump_thickness)
[1] 4.41774

> median(cancer_data$clump_thickness)
[1] 4

> getmode(cancer_data$clump_thickness)
[1] 1

> var(cancer_data$clump_thickness)
[1] 7.928395

> mean(cancer_data$cell_size)
[1] 3.134478

> median(cancer_data$cell_size)
[1] 1

> getmode(cancer_data$cell_size)
[1] 1

> var(cancer_data$cell_size)
[1] 9.311403

> mean(cancer_data$cell_shape)
[1] 3.207439

> median(cancer_data$cell_shape)
[1] 1

> getmode(cancer_data$cell_shape)
[1] 1

> var(cancer_data$cell_shape)
[1] 8.832265

> mean(cancer_data$adhesion)
[1] 2.806867

> median(cancer_data$adhesion)
[1] 1

> getmode(cancer_data$adhesion)
[1] 1

> var(cancer_data$adhesion)
[1] 8.153191

> mean(cancer_data$epithelial_cell_size)
[1] 3.216023
> median(cancer_data$epithelial_cell_size)
[1] 2
> getmode(cancer_data$epithelial_cell_size)
[1] 2
> var(cancer_data$epithelial_cell_size)
[1] 4.903124

> mean(cancer_data$nuclei_chromatin)
[1] 3.463519
> median(cancer_data$nuclei_chromatin)
[1] 1
> getmode(cancer_data$nuclei_chromatin)
[1] 1
> var(cancer_data$nuclei_chromatin)
[1] 13.25476

> mean(cancer_data$chromatin)
[1] 3.437768
> median(cancer_data$chromatin)
[1] 3
> getmode(cancer_data$chromatin)
[1] 2
> var(cancer_data$chromatin)
[1] 5.94562

> mean(cancer_data$normal_nucleoli)
[1] 2.866953
> median(cancer_data$normal_nucleoli)
[1] 1
> getmode(cancer_data$normal_nucleoli)
[1] 1
> var(cancer_data$normal_nucleoli)
[1] 9.32468

> mean(cancer_data$mitoses_class)
[1] 1.589413
> median(cancer_data$mitoses_class)
[1] 1
> getmode(cancer_data$mitoses_class)
[1] 1
> var(cancer_data$mitoses_class)
[1] 2.941492

> mean(cancer_data$class)
[1] 2.689557
> median(cancer_data$class)
[1] 2
> getmode(cancer_data$class)
[1] 2
> var(cancer_data$class)
[1] 0.9049194

# Pearson Co-Variance Calculation:-

correlated values   cor(cleaned cancer data; method = "pearson")

#Updated the value in the csv file:-

write:csv(corr values; file = "Pearson Corr:csv")

# The strongly related attributes are replaced by 0

delta_2_clean <- replace(x = correlated values; correlated values == 1; 0)

# With the final data I made another csv file (Delta 2 clean Pearson:csv):- 

write:csv(delta 2 clean; file   "Delta 2 clean Pearson:csv")


