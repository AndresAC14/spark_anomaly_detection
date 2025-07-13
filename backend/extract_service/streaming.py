import pandas as pd
import os
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load the full dataset
df = pd.read_csv("database\\model_data.csv", parse_dates=['FECHA_HORA'])

# Filter data from January 1, 2024 onwards
df_2024 = df[df['FECHA_HORA'] >= '2024-01-01']

# Output directory for hourly CSVs
output_dir = 'database\\streaming_data'
os.makedirs(output_dir, exist_ok=True)

logging.info(f"Starting data streaming starting from 2024-01-01...")

# Group by timestamp (hourly granularity)
for timestamp, group in df_2024.groupby('FECHA_HORA'):
    filename = timestamp.strftime('%Y%m%d_%H%M%S') + '.csv'
    filepath = os.path.join(output_dir, filename)

    group = group.groupby(['FECHA_HORA']).agg({ 
        'INTENSIDAD': 'mean',
        'OCUPACION': 'mean',
        'CARGA': 'mean',
        'VALOR_CONTAMINACION': 'mean'
    }).reset_index()
    
    # Save the current group to CSV
    group.to_csv(filepath, index=False)
    logging.info(f'Saved file: {filepath}')
    
    # Wait for 30 seconds before processing the next file
    time.sleep(30)

logging.info(f'All hourly CSV files have been generated in folder: {output_dir}')
