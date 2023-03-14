# TL_Team5
Clustering Modern European languages

We want to cluster languages based on their similarities, in order to predict how easy it would be to learn a specific language based on your current knowledge.
Categories: Modern European languages - their standard variation

Features: Grammar - pronunciation - vocabulary

## Basis instructions
### Pre-requisites
Project is implemented as Jupyter notebooks. Anaconda should bring with it all required libraries   but geopandas and shapely. 
`pip install geopandas
`pip install shapely
## Workflow
### 1. languages.ipynb
Notebook reads all languages WALS provides, filters relevant languages (manual approach), and visualize results on a map. Manual filtering is done with a manually curated whitelist which is hard-coded in notebook.
	Input: data/languages.csv	
	Ouput: data/european_languages.csv
### 2. transform.ipynb
Notebook to de-normalize original data, filters relevant languages, and transforms it into a de-normalized dataset.
	Input: data/european_languages.csv, data/values.csv
	Output: data/vals_transformed.csv
### 3. analysis.ipynb
Notebook to filter reevant features and remove the ones which are sparsely populated. Filter parameter are part of the notebook 
	Parameter (defined in notebook):
		threshold_pct_features: feature available for x% of languages in scope; value 0.5 
		threshold_pct_langauges: include only languages that have y% of features populated; value 1.00
	Input:data/vals_transformed.csv
	Output: data/training_set.csv
### 4. learn.ipynb
Notebook to train kModes model, evaluates model performance internally (cohesion and separation), and outputs and visualize clusters.
	Parameter (defined in notebook, description in kmodes_parameter.txt):
		k: The number of clusters to form as well as the number of centroids to generate.
		init: Maximum number of iterations of the k-modes algorithm for a single run.
		n_init: Method for initialization
		verbose: Verbosity mode
		random_state: Seed for random number generator.
	Input: data/training_set.csv
	Output: data/result_cluster.csv
