
Carbon Dioxide – What you do today will determine your future
=
A UMSI MADS Capstone Project Report
--

**Prepared by**
* Heewoon Kang 
* Ho Fai Howard Wong
* Koon Leong Ho

Introduction
--

This is a study seeks to understand the causes of carbon dioxide emissions to identify practical approach to control and reduce it.  Much work has been done to understand the causes of the emission.  The responsible candidates are not unexpected and the blame has often been attributed to:

1. Population growth
2. Economic growth
3. Increase in consumption

Unfortunately, it is almost an impossibility for governments to curb or reduce these causal factors. Drawing from the numerous datasets available, this study seeks to identify alternative approaches to reduced Carbon Dioxide Emissions.

Method
--
The strategy is to develop two different approaches to predict the level of CO2 emission.  These approaches are:
1. Panel Regression 
2. Supervised Learning Regression

To generate the input predict the input features for the forecasts, time-series analysis were used.

To improve the accuracy of the time series forecasts, Unsupervised Learning Clustering was used.  The Time Series models were optimized for each cluster and the outputs were used as input parameters for the regression models.

Machine Learning models can produce accurate forecasts but it does not lend itself to intprepretation.  Whilst an analysis of the feature inportance can provide an indication of the relative impact of the features on the dependent variable, it does not provide a quantitative measure of the impact.

Panel regression models is expected to be less accurate in its forecasts compared to Machine Learning models.  The advantage, however, is that the coefficient of the terms do communicate the elasticity of the impart of the feature on the dependent variable.  

With the knowledge of the actual magnitude of the feature on CO2, decisions can then be made to prioritise practical actions that will have the most impact on reducing emissions.

The Machine Learning Regression Model is used a benchmark to validate the accuracy of the Panel Regresssion and hence the validity of the feature elasticity on CO2 emission.

Libraries used:
--
The following are key libraries used int he analysis:
1. pmdaraima - used for automated grid search to identify the optimal hyperparameters tor the time series forecast models.
2. PyCaret - used for automated grid search to identify the beast performaning algorithm for clustering as well as for supervise learning regression.  It will help tune the models for optimal accuracy.
3. PanelOLS - used to developed the Panel Regression models

Pipeline
--
The Jupyter Notebooks are organised and numbered in sequence. The pipeline should be executed in sequence order.

The data is prepaerd off-line and different datasets are merged into a master table using the ISO Country Code.  The following routines are used to manage the data.<br>
<br>
**1. Data Preparation**
* 1.1 **data_upload_manifest** - Uploads xls/xlsx/csv files into the database based on a manifests defined in the manifest spreadshet.
* 1.2 **load_dataset_to_pickle** - Downloads master dataset into a pickle to reduce dataloading time
* 1.3 **identify_data_start_end** - Checks all the dataset to identify start and end of time series <br>

**2. Clustering and Time Series**
* 2.1 **find_clustering_model** - Determines the ideal clustering method and the number of clusters
* 2.2 **create_ts_models** - Optimizes the time series models for forecasting
* 2.3 **generate_ts_forecasts** - creates the forecasts for use in regression predictions<br>

**3. Predictions**
* 3.1 **Panel Regression**
* 3.1.1 **create_panel_model** - Creates the panel regression model to be sued for analysis
* 3.1.2 **panel_regression_model_predict_2017_2020_and_2025** - performs the panel regression prediction based on the inptus from the Time Series forecasts.

* 3.2 **Supervised Learning Regression**
* 3.2.1 **create_regression_prediction_c0** - Identify and optimize the regression model for Cluster 0
* 3.2.2 **create_regression_prediction_c1** - Identify and optimize the regression model for Cluster 1
* 3.2.3 **create_regression_prediction_c2** - Identify and optimize the regression model for Cluster 2
* 3.2.4 **create_regression_prediction_c3** - Identify and optimize the regression model for Global

**4. Reports Support**
* 4.1 **report_appendix_a_charts** - Prepares charts used in Appendix 1 of blog post.
* 4.2 **report_pairwise_cosine similarity** - Performs Cosine Similarity analysis between China and the rest of the world

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- (NOT USED) Makefile with commands like `make data` or `make train`
    ├── README.md          <- (NOT USED) The top-level README for developers using this project.
    ├── data
    │   ├── external       <- (NOT USED) Data from third party sources.
    │   ├── interim        <- (NOT USED) Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- (NOT USED) A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering), and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- (NOT USED) Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- (NOT USED) Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- (NOT USED) makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- (NOT USED) Source code for use in this project.
    │   ├── __init__.py    <- (NOT USED) Makes src a Python module
    │   │
    │   ├── data           <- (NOT USED) Scripts to download or generate data
    │   │   └── (NOT USED) make_dataset.py
    │   │
    │   ├── features       <- (NOT USED) Scripts to turn raw data into features for modeling
    │   │   └── (NOT USED) build_features.py
    │   │
    │   ├── models         <- (NOT USED) Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── (NOT USED) predict_model.py
    │   │   └── (NOT USED) train_model.py
    │   │
    │   └── visualization  <- (NOT USED) Scripts to create exploratory and results oriented visualizations
    │       └── (NOT USED) visualize.py
    │
    └── tox.ini            <- (NOT USED) tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
