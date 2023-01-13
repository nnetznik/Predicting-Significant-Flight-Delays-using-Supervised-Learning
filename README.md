# Predicting-Significant-Flight-Delays-using-Supervised-Learning

In this notebook I present my work in predicting flight delays by use of supervised learning.

My goal is to predict whether a given flight will be significantly delayed or cancelled given several known factors about the flight such as time of year, airline, time of departure, and other significant factors.

I began with a random sample of data from a dataset available to the public domain from https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022. The data is saved in the file sample.csv. The code for obtaining the random sample can be found in obtain_data_sample.py. I then selected several pertinent features such as time of year, airline, origin/destination airports, departure/arrival time blocks, and distance, among others. Upon one-hot encoding the categorical features, I built and tuned several supervised learning models on this data including basic decision trees, a random forest model, and a logistic regression model. I found that the random forest model was the highest performing, with its results presented below:

Train accuracy:  0.6293466666666667
Test accuracy:  0.61344

TN: 12023    FP:7453
FN: 2211     TP: 3313

% Predicted delays/cancellations that were delayed/cancelled: 30.772803269552295%
% Predicted non-delays/cancellations that were not delayed/cancelled: 84.46676970633693%

Our model could not accurately predict delays/cancellations, but could accurately predict non-delays/cancellations.

The slide deck can be found in the GitHub repository: https://github.com/nnetznik/Predicting-Significant-Flight-Delays-using-Supervised-Learning