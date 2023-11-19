# Predicting the Survival of New Businesses in Vancouver

- author: Prabhjit Thind, Beth Ou Yang, Arturo Boquin, Weiran Zhao

## About
This analysis aims to predict the survival of new businesses in Vancouver by examining various economic and demographic factors. Using datasets from the City business license registry and other external sources, we explore the influence of location, industry, and economic indicators on business survival.

## Usage

First time running the project, run the following from the root of this repository:
```
conda env create --file environment.yaml
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

## External Datasets:

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
