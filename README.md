# Fetal-Insight

The Fetal Insight project aims to classify the health of a fetus based on Cardiotocography (CTG) data. The objective is to predict whether the fetal health is Normal, Suspect, or Pathological, contributing to the prevention of child and maternal mortality.

### Dataset

The dataset used for this project was obtained from Kaggle (https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification). It includes CTG data that has been preprocessed and labeled with the corresponding fetal health categories.

### Model

The classification of fetal health is performed using the Gradient Boosting algorithm. This machine learning model has been trained on the provided dataset to make accurate predictions.

### Privacy Protection

To ensure the privacy of sensitive data, the project implements two key privacy-preserving techniques: Private Aggregation of Teacher Ensembles (PATE) and Federated Learning.

-PATE : PATE is utilized to train a model without direct access to the individual records. It involves training multiple "teacher" models on disjoint subsets of the data and then aggregating their predictions in a privacy-preserving manner.

-Federated Learning : Federated Learning is implemented to train the model across decentralized devices. This allows the model to learn from distributed data without exposing individual data records.

### Visualization

The project includes visualizations to provide insights into the model's performance, privacy-preserving techniques, and the overall health classification.
