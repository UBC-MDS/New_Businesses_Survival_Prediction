# Predicting the Survival of New Businesses in Vancouver

- author: Prabhjit Thind, Beth Ou Yang, Arturo Boquin, Weiran Zhao
[View the rendered HTML report here](https://ubc-mds.github.io/New_Businesses_Survival_Prediction/milestone1_report.html)


## About
This analysis aims to predict the survival of new businesses in Vancouver by examining various economic and demographic factors. Using datasets from the City business license registry and other external sources, we explore the influence of location, industry, and economic indicators on business survival.

## Usage via Docker

1. **Cloning:** First clone the repository using the below command:
```
git clone https://github.com/UBC-MDS/New_Businesses_Survival_Prediction.git
```
2. **Docker Compose:** Inside the cloned repository, use the below command to run the docker container in your terminal:
```
docker-compose up
```
3. **Open Jupyterlab:** After running the container, you will get a URL in your terminal. Copy that URL and paste it in your browswer. Change the port mentioned in URL from 8888 to 8889. Jupyter Lab/Notebook will open.

4. **Change Directory:** Now we need to open our main project report (.ipynb) file. Change directory by clicking on "DSCI_522_group1" and then next open "src" directory. Click on "milestone1_report.ipynb" to open the desired notebook.

5. **Run Notebook:** You can reproduces our analysis by doing "Run All" from the Run tab in jupyter.

## Usage via Conda

First time running the project, run the following from the root of this repository:
```
conda env create --file environment.yml
```
To run the analysis, run the following from the root of this repository:

```
conda activate 522_group1
jupyter lab
```

## Dependencies
- ```conda``` (version 23.9.0 or higher)
- ```nb_conda_kernels``` (version 2.3.1 or higher)
- Python and packages listed in environment.yaml

## License
The Business Survival Status Predictor materials here are licensed under the Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If re-using/re-mixing please provide attribution and link to this webpage.

## References

#### External Datasets:

Employment by Industry:
Description: This dataset from Statistics Canada provides detailed information on employment across various industries. It includes data on employment figures, categorized by different industry sectors as defined by the North American Industry Classification System (NAICS).
URL: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410035501&pickMembers%5B0%5D=1.11&pickMembers%5B1%5D=3.1&pickMembers%5B2%5D=4.1&cubeTimeFrame.startMonth=01&cubeTimeFrame.startYear=1997&cubeTimeFrame.endMonth=10&cubeTimeFrame.endYear=2023&referencePeriods=19970101%2C20231001

GDP by Industry:
Description: This dataset presents the Gross Domestic Product (GDP) by industry in Canada. It offers insights into the economic performance of different industry sectors, providing a valuable measure of economic activity and health.
URL: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610043401

Investment in Building Construction:
Description: This dataset includes data on investment in building construction. It covers various types of structures and work, offering a comprehensive view of the construction investment landscape in Canada.
URL: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410017501

Consumer Price Index:
Description: The Consumer Price Index (CPI) dataset provides information on the changes in the price level of a basket of consumer goods and services purchased by households. It is a key indicator of inflation and purchasing power.
URL: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810025601


Statistics Canada. 2023. https://www150.statcan.gc.ca/n1/en/type/data?MM=1
