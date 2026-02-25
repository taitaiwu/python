import pandas
import seaborn
import numpy
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

# load file
train_feature = pandas.read_csv("train.csv")
train_label = pandas.read_csv("train_gt.csv")
val_feature = pandas.read_csv("val.csv")
val_label = pandas.read_csv("val_gt.csv")
test_feature = pandas.read_csv("test.csv")

# pre-processing
train_feature = train_feature.drop(columns=["RowNumber", "CustomerId", "Surname"])
val_feature = val_feature.drop(columns=["RowNumber", "CustomerId", "Surname"])
test_feature = test_feature.drop(columns=["RowNumber", "CustomerId", "Surname"])

encode_gender = LabelEncoder()
train_feature["Gender"] = encode_gender.fit_transform(train_feature["Gender"])
val_feature["Gender"] = encode_gender.transform(val_feature["Gender"])
test_feature["Gender"] = encode_gender.transform(test_feature["Gender"])

train_feature = pandas.get_dummies(train_feature, columns=["Geography"], drop_first=True)
val_feature = pandas.get_dummies(val_feature, columns=["Geography"], drop_first=True)

val_feature = val_feature.reindex(columns=train_feature.columns, fill_value=0)
test_feature = test_feature.reindex(columns=train_feature.columns, fill_value=0)

y_train = train_label.values.ravel()
y_val = val_label.values.ravel()

# create and train model
scaler = StandardScaler()
train_feat_scaled = scaler.fit_transform(train_feature)
val_feat_scaled = scaler.transform(val_feature)
test_feat_scaled = scaler.transform(test_feature)

param_grid = {
    'C': [0.1, 1, 4, 10],
    'gamma': [0.01, 0.1, 1, 'scale'] 
}

grid = GridSearchCV(
    SVC(kernel='rbf'),
    param_grid,
    cv=5,
    scoring='accuracy'
)

grid.fit(train_feat_scaled, y_train)

# predict
val_pred = grid.predict(val_feat_scaled)
test_pred = grid.predict(test_feat_scaled)

# score(val)
accuracy = grid.score(val_feat_scaled, y_val)

# output files
val_result = pandas.DataFrame({"Exited": val_pred})
val_result.to_csv("val_pred.csv", index=False)
test_result = pandas.DataFrame({"Exited": test_pred})
test_result.to_csv("test_pred.csv", index=False)

# print information
print("Best params:", grid.best_params_)
print("Best CV score:", grid.best_score_)
print("Validation accuracy:", accuracy)