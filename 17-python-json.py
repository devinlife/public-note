import json

params = 1
validation_auc = 2
train_auc = 3

metrics_data = {
    "mae": params,
    "r2": validation_auc,
    "rmse": train_auc,
}

# Save the evaluation metrics to the location specified by output_data_dir
metrics_location = "metrics.json"

# Save the model to the location specified by model_dir
with open(metrics_location, "w") as f:
    json.dump(metrics_data, f)
