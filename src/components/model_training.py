import pandas as pd
from sklearn.cluster import KMeans
from src.exception import CustomException
from src.logger import logging
import sys

# performs kmeans clustering
def perform_clustering(scaled_data: pd.DataFrame,n_clusters: int=4)->pd.DataFrame:
    try:
        kmeans=KMeans(n_clusters=n_clusters,random_state=42,max_iter=1000)
        cluster_labels=kmeans.fit_predict(scaled_data)
        logging.info("Clustering is completed")
        return cluster_labels
    except Exception as e:
        raise CustomException(e,sys)