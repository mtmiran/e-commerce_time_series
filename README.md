# Data Science Project - Time Series

## Goals

### Customer segmentation

Construction of customer segmentation with a focus on value pyramid: Recency, Frequency and Value

### Sales projection by segment

- Train a time series forecast model to forecast sales (Sales column) for the segment with the highest sales volume (across the entire history) - daily frequency
- Model validation: December 2014 (daily frequency)
- Use MAPE, SMAPE and RMSLE metrics to calculate the result in Dec 2014.

## Data Environment

```bash
conda create -n e-commerce_time_series
conda activate e-commerce_time_series
conda install pandas ipykernel openpyxl matplotlib seaborn scipy scikit-learn xgboost
```

### Forecasting

- Prophet: `python -m pip install prophet`
