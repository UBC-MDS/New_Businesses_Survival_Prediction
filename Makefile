data/raw : 
	python src/DataFetch.py --raw_business_path=data/raw/business.csv \
      --raw_econ_path=data/raw/econ.csv

data/processed/business_econ.csv: data/raw
	python src/DataPreprocess.py --raw_business_path=data/raw/business.csv \
		--processed_business_path=data/processed/business.csv \
		--raw_econ_path=data/raw/econ.csv \
		--merged_data_output_path=data/processed/business_econ.csv

results/figures : data/processed/business_econ.csv
	python  src/EDA.py --merged_data_path=data/processed/business_econ.csv

results/models : data/processed/business_econ.csv
	python src/Modeling.py --business-data data/processed/business_econ.csv --seed 123 --pipeline-to results/models/ --test-data-to data/processed/

data/processed : data/processed/business_econ.csv
	python src/Modeling.py --business-data data/processed/business_econ.csv --seed 123 --pipeline-to results/models/ --test-data-to data/processed/

results/tables : data/processed results/models
	python src/evaluation.py --test-data data/processed --pipeline-from results/models --results-to results/tables


clean:
	rm -rf results/figures
	rm -rf results/models
	rm -rf results/tables
	rm -rf data/processed
	rm -rf data/raw

all: results/tables results/models results/figures
