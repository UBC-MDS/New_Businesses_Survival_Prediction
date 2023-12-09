# Predicting the Survival of New Businesses in Vancouver

- author: Prabhjit Thind, Beth Ou Yang, Arturo Boquin, Weiran Zhao

[View the rendered HTML report here](https://ubc-mds.github.io/New_Businesses_Survival_Prediction/report_business_survival_prediction.html)


## About
This analysis aims to predict the survival of new businesses in Vancouver by examining various economic and demographic factors. Using datasets from the City business license registry and other external sources, we explore the influence of location, industry, and economic indicators on business survival.

## Report

The final report can be found [here](https://ubc-mds.github.io/New_Businesses_Survival_Prediction/report_business_survival_prediction.html).


## Dependencies

- [Docker](https://www.docker.com/) is a container solution 
used to manage the software dependencies for this project.
The Docker image used for this project is based on the
`quay.io/jupyter/minimal-notebook:notebook-7.0.6` image.
Additioanal dependencies are specified int the [`Dockerfile`](Dockerfile).

### Usage via Docker

1. **Cloning:** First clone the repository using the below command:
```
git clone https://github.com/UBC-MDS/New_Businesses_Survival_Prediction.git
```
2. **Docker Compose:** Inside the cloned repository, use the below command to run the docker container in your terminal:
```
docker-compose up
```
3. **Open Jupyterlab:** After running the container, you will get a URL in your terminal. Copy that URL and paste it in your browswer. Change the port mentioned in URL from 8888 to 8889. Jupyter Lab/Notebook will open.

4. **Change Directory:** Change directory by clicking on "DSCI_522_group1".

### Usage via GNU Makefile
1. Inside the docker container, open up a terminal. Go to the project root directory. This directory has a makefile for running our analysis end to end.

2. Initially run the below command to remove existing directories and files for results:

   ```make clean```
   
4. To run the analysis end to end use below command:

   ```make all```

#### Running the analysis

1. Navigate to the root of this project on your computer using the
   command line and enter the following command:

``` 
docker compose up
```

2. In the terminal, look for a URL that starts with 
`http://127.0.0.1:8888/lab?token=` 
(for an example, see the highlighted text in the terminal below). 
Copy and paste that URL into your browser.

<img src="img/jupyter-container-web-app-launch-url.png" width=400>

3. To run the analysis,
enter the following commands in the terminal in the project root:

```
# Data Fetch (to save raw data into csv files)
python src/DataFetch.py --raw_business_path=data/raw/business.csv \
      --raw_econ_path=data/raw/econ.csv

# Data Preprocess (to save clean data into csv files)
python src/DataPreprocess.py --raw_business_path=data/raw/business.csv \
   --processed_business_path=data/processed/business.csv \
   --raw_econ_path=data/raw/econ.csv \
   --merged_data_output_path=data/processed/business_econ.csv

# EDA (to save png files)
python  src/EDA.py --merged_data_path=data/processed/business_econ.csv

# Modeling (to train\fit the model)
python src/Modeling.py --business-data data/processed/business_econ.csv --seed 123 --pipeline-to results/models/ --test-data-to data/processed/

# Evaluation (to check model performance on test data)
python src/evaluation.py --test-data data/processed --pipeline-from results/models --results-to results/tables

```

### Potential issue with data
1. As the data/raw/business-license.csv is too large to upload to Github, please run the script to download all the necessary data files, rather than only look at the data folder.
2. Make sure the connection is great when loading the data by the script. If there raises any error message like: No such file 'temp.zip', please try to re-run the script again because this may be caused by connection problems during the download process.
The script should be run in the repo's folder (working directory should be New_Businesses_Survival_Prediction ).

#### Clean up

1. To shut down the container and clean up the resources, 
type `Cntrl` + `C` in the terminal
where you launched the container, and then type `docker compose rm`

## Developer notes

#### Adding a new dependency

1. Add the dependency to the `Dockerfile` file on a new branch.

2. Re-build the Docker image locally to ensure it builds and runs properly.

3. Push the changes to GitHub. A new Docker
   image will be built and pushed to Docker Hub automatically.
   It will be tagged with the SHA for the commit that changed the file.

4. Update the `docker-compose.yml` file on your branch to use the new
   container image (make sure to update the tag specifically).

5. Send a pull request to merge the changes into the `main` branch. 

#### Running the tests
Tests are run using the `pytest` command in the root of the project.
More details about the test suite can be found in the 
[`tests`](tests) directory.

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
