# Change Log
All notable changes to this project will be documented in this file.
 
## Feedback from Milestone 1

### Improvements

1. **Feedback**: CODE_OF_CONDUCT.md missing
    - Narration: Added `CODE_OF_CONDUCT.md` file
    - Evidence: [commit dd07888](https://github.com/UBC-MDS/New_Businesses_Survival_Prediction/commit/dd07888a5403a956a70b9e96ea0fab8a97739f48)

2. **Feedback**: CONTRIBUTING.md missing
    - Narration: Added `CONTRIBUTING.md` file
    - Evidence: [commit d09ebd7](https://github.com/UBC-MDS/New_Businesses_Survival_Prediction/commit/d09ebd7539ea7769a731d875a63e614c4e9ff1b6)

3. **Feedback**: data - Raw and processed/intermediate data are mixed in the data directory (they should be in subfolders, or at least clearly labelled)
    - Narration: Separately saved the data in the ‘raw’ and ‘processed’ folders. However, in order to prevent LSF issue, we have ignore `.csv` files in our `.gitignore`. By running the `DataFetch.py` and `DataProcessed.py` via command lines, the folders will be automatically created and data files will save in the user’s local machine.
    - Evidence: [commit 482ccaa](https://github.com/UBC-MDS/New_Businesses_Survival_Prediction/commit/482ccaa4509eee4d17a6e0e0495b296ff3b8a394)
  
4.  **Feedback**: Information in tables are not clearly presented. Some important results are not displayed.
    - Narration: Generating confusion matrix and earlier was using only accuracy. Added F1 score, precision and recall metrics. All changes in evaluation.py script.
    - Evidence: [commit dafd4af](https://github.com/UBC-MDS/New_Businesses_Survival_Prediction/commit/dafd4afce08b42f1b46404e5288604fb488071a6)
      
5. **Feedback**: Broke the golden rule of machine learning.
    - Narration: Data leakage was happening causing bias on the test results. Fixed it in Modeling.py file by using column transformers and subsequent fit.
    - Evidence: [commit dafd4af](https://github.com/UBC-MDS/New_Businesses_Survival_Prediction/commit/dafd4afce08b42f1b46404e5288604fb488071a6)
 
## Feedback from Milestone 2

### Improvements

1. **Feedback**: There is no documentation on how to run the test suite or the instructions are vague.
    - Narration: Included “Running the tests” instructions in the “Developer notes” section to explain how to run the test.
    - Evidence: [commit 68af9b6](https://github.com/UBC-MDS/New_Businesses_Survival_Prediction/commit/68af9b67e5112bc4c96c1d3b8a3f60e2a53b017f)

2. **Feedback**: running into an error when running the notebook. Error: `chart_grid`.
    - Narration: Removed `chart_grid` from the report file to prevent NameError.
    - Evidence: [commit 03976ce](https://github.com/UBC-MDS/New_Businesses_Survival_Prediction/commit/03976cee5a790d480c5a9162275d60890114c11a)

## Feedback from peer review

### Improvements

1. **Feedback**: Lack of DOI link for references, affecting citation accessibility.
    - Narration: Included DOI links for references to enhance citation accessibility and improve writing and explanation.
    - Evidence: [commit 64a6eb4](https://github.com/UBC-MDS/New_Businesses_Survival_Prediction/commit/64a6eb44dacd391c849dbc696cb37e65fc4c47fa)
  
2. **Feedback**: Consider clarifying the rationale behind choosing a two-year window for predicting business survival.
    - Narration: Included the rationale.
    - Evidence: [commit 5ca58a2](https://github.com/UBC-MDS/New_Businesses_Survival_Prediction/commit/5ca58a2c10b89519fce37720637cfb34fa598410)
