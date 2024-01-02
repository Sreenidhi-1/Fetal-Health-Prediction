# Fetal-Insight

The Fetal Insight project aims to classify the health of a fetus based on Cardiotocography (CTG) data. The objective is to predict whether the fetal health is Normal, Suspect, or Pathological, contributing to the prevention of child and maternal mortality.

### Dataset

The dataset used for this project was obtained from Kaggle (https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification). It includes CTG data that has been preprocessed and labeled with the corresponding fetal health categories.

### Model

The classification of fetal health is performed using the Gradient Boosting algorithm. This machine learning model has been trained on the provided dataset to make accurate predictions.


<p float="left">
  <img src="https://github.com/Sreenidhi-1/Fetal-Health-Prediction/assets/91629420/03fb5f28-fe21-4e78-aacb-6f26a100aac1" width="400" />
  <img src="https://github.com/Sreenidhi-1/Fetal-Health-Prediction/assets/91629420/f474dbe8-6a01-45b1-aced-3e3c4495ed5f" width="400"/>

</p>



### Privacy Protection

To ensure the privacy of sensitive data, the project implements two key privacy-preserving techniques: Private Aggregation of Teacher Ensembles (PATE) and Federated Learning.

- PATE : PATE is utilized to train a model without direct access to the individual records. It involves training multiple "teacher" models on disjoint subsets of the data and then aggregating their predictions in a privacy-preserving manner.

- Federated Learning : Federated Learning is implemented to train the model across decentralized devices. This allows the model to learn from distributed data without exposing individual data records.

<img width="624" alt="image" src="https://github.com/Sreenidhi-1/Fetal-Health-Prediction/assets/91629420/22028c91-32b9-4b16-8de1-dd75760a0305">


### Visualization

The project includes visualizations to provide insights into the model's performance, privacy-preserving techniques, and the overall health classification.


<p float="left">
  <img src="https://github.com/Sreenidhi-1/Fetal-Health-Prediction/assets/91629420/64cfcca6-0523-470b-82d6-a69a2e58ea8c" width="300" />
  <img src="https://github.com/Sreenidhi-1/Fetal-Health-Prediction/assets/91629420/e5bc8798-1335-489f-a18c-9784f6df5f83" width="300"/>
  <img src="https://github.com/Sreenidhi-1/Fetal-Health-Prediction/assets/91629420/19ba176f-0cf6-4f2d-b137-e2bb3d2f1a8e" width="300"/>
  <img src="https://github.com/Sreenidhi-1/Fetal-Health-Prediction/assets/91629420/676ae70d-b2e5-4d79-a8cd-1b524b96c8e8" width="300"/>
</p>






