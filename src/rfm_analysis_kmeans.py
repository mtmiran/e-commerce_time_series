# -----------------------------------------------------------------------------
# RFM Analysis with Kmeans

# -----------------------------------------------------------------------------

from datetime import datetime
import pandas as pd

# Import DateSet -----------------------------------------------------------------------------------------------------------------------------

# especify data types - NOT NEEDED
# dtype_dict = {
#     'Order ID': str,
#     'Country': str,
# }

date_format = '%d-%m-%Y'

desafio_dataset = pd.read_excel('../data/dataset_desafio_datascience.xlsx',  parse_dates=['Order Date', 'Ship Date'], date_format=date_format )

df = desafio_dataset.copy()

# print(df.dtypes)

# RFM Analysis -----------------------------------------------------------------------------------------------------------------------------
columns = ['Order ID', 'Order Date', 'customer ID', 'Profit']
df_rfm = df[columns]

recency_date = df['Order Date'].max()
print(recency_date) 