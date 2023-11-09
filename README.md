# Data Science - Times Series

## Description

Online shopping is, more than ever, part of people's daily lives.
More than ever, using data to make decisions is the big bet
of companies in the world.

Understanding the profile of the customer portfolio to generate personalized campaigns is
imperative in a competitive world like today.

Furthermore, good sales planning is crucial for the supply sector
chain to power the network and avoid problems such as sold out and overstocking.

Let's take on this challenge to work with a purchasing base via e-commerce that
allows us to build views about customers and projections about future sales.

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

- Prophet: `conda install -c conda-forge fbprophet`
- dependencies: `pip3 install plotly holidays`
