data/raw : 
	python src/DataFetch.py --raw_business_path=data/raw/business.csv \
      --raw_econ_path=data/raw/econ.csv

data/processed/business_econ.csv: data/raw/business.csv data/raw/econ.csv
	python src/DataPreprocess.py --raw_business_path=data/raw/business.csv \
		--processed_business_path=data/processed/business.csv \
		--raw_econ_path=data/raw/econ.csv \
		--merged_data_output_path=data/processed/business_econ.csv

data/processed : data/processed/business_econ.csv
	python src/Modeling.py --business-data data/processed/business_econ.csv --seed 123 --pipeline-to results/models/ --test-data-to data/processed/

results/figures : data/processed/business_econ.csv
	python  src/EDA.py --merged_data_path=data/processed/business_econ.csv

results/models : data/processed/business_econ.csv
	python src/Modeling.py --business-data data/processed/business_econ.csv --seed 123 --pipeline-to results/models/ --test-data-to data/processed/

results/tables : data/processed results/models
	python src/evaluation.py --test-data data/processed --pipeline-from results/models --results-to results/tables

report/_build/html/index.html: report/report_business_survival_prediction.ipynb report/_toc.yml report/_config.yml data/raw results/figures results/models results/tables 
	jupyter-book build report
	cp -r report/_build/html/* docs/

clean:
	rm -rf results/figures
	rm -rf results/models
	rm -rf results/tables
	rm -rf data/processed
	rm -rf data/raw
	rm -rf report/_build

all: report/_build/html/index.html
