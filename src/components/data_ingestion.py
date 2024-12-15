import pandas as pd
from src.logger import logging
from src.exception import CustomException
import sys
import os


def load_data():
    try:
        # Get the absolute path of the current script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the file path relative to the repository root
        file_path = os.path.join(base_dir, '..', '..', 'notebook', 'data', 'sale_data.csv')

        # Load the CSV file
        sale = pd.read_csv(file_path, encoding='iso-8859-1')
        sale['InvoiceDate'] = pd.to_datetime(sale['InvoiceDate'], format='%d-%m-%Y %H:%M', errors='coerce')

        logging.info("Data loading is completed")
        return sale
    except Exception as e:
        raise CustomException(e, sys)
    
def final_output_data(aggregated_df,full_cluster_df)->pd.DataFrame:
    try:
        output=aggregated_df.drop('LastInvoiceDate',axis=1)
        logging.info("LastInvoiceDate is removed from data")
        full_cluster_select=full_cluster_df[['Cluster','ClusterName']]
        logging.info("selected required fields from full clustered data")
        final_output=pd.merge(output,full_cluster_select,left_index=True,right_index=True,how='left')
        logging.info("Customer Segmentation is completed and data is ready for download")
        return final_output
    except Exception as e:
        raise CustomException(e,sys)


