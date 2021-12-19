
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
The stragegy is to develop two different approaches to predict the level of CO2 emission.  These approaches are:
1. Panel Regression 
2. Supervised Learning Regression

To generate the input predict the input features for the forecats, time-series analysis were used.

To improve the accuracy of the time series forecasts, Unsupervised Learnign Clustering was used.  The Time Series models were optimized for each cluster and the outputs were used as input parameters for the regression models.

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




Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
