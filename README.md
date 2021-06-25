# Machine Learning Engineer
## Introduction and Foundations
## Project 0: Titanic Survival Exploration

### Run

This notebook is intended to be run from an AI Platform Notebook on the Impower.ai Skynet GCP Project.

### Install

This project requires **Python 3.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [BigQuery Client](https://cloud.google.com/bigquery/docs/reference/libraries)
- [Cloud Storage Client](https://cloud.google.com/storage/docs/reference/libraries)
- [Jupyter Notebook](http://ipython.org/notebook.html)

### Code

Template code is provided in the notebook `titanic_survival_exploration.ipynb` notebook file. You will also be required to use the included `visuals.py` and `data_load.py` Python files to explore the `titanic` dataset file and complete your work. While some code has already been implemented to get you started, you will need to implement additional functionality when requested to successfully complete the project. Note that the code included in `visuals.py` and `data_load.py` is meant to be used out-of-the-box and not intended to be edited. If you are interested in how the visualizations are created or how the data is loaded in the notebook, please feel free to explore these Python files.

### Data

The dataset used in this project contains the following attributes:

**Features**

- `pclass` : Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
- `name` : Name
- `sex` : Sex
- `age` : Age
- `sibsp` : Number of Siblings/Spouses Aboard
- `parch` : Number of Parents/Children Aboard
- `ticket` : Ticket Number
- `fare` : Passenger Fare
- `cabin` : Cabin
- `embarked` : Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

**Target Variable**

- `survival` : Survival (0 = No; 1 = Yes)
