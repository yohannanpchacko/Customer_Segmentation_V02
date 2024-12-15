import pandas as pd
from sklearn.preprocessing import StandardScaler
from typing import List
from src.exception import CustomException
from src.logger import logging
import sys

# data cleaning
def data_cleaning(sale: pd.DataFrame)->pd.DataFrame:
    try:
        logging.info("data cleaning is started")
        sale['Invoice']=sale['Invoice'].astype("str")
        mask=(
        sale['Invoice'].str.match('^\\d{6}$')==True)
        cleaned_df=sale[mask]
        logging.info("invoce column is cleaned")
        cleaned_df['StockCode']=cleaned_df['StockCode'].astype("str")
        mask1=(
        (cleaned_df['StockCode'].str.match('^\\d{5}$')==True)|
        (cleaned_df['StockCode'].str.match('^\\d{5}[a-zA-Z]+$')==True)|
        (cleaned_df['StockCode'].str.match('^PADS$')==True))
        cleaned_df=cleaned_df[mask1]
        logging.info("Stock Code column is cleaned")
        cleaned_df.dropna(subset=['Customer ID'],inplace=True)
        logging.info("Customer ID is removed")
        cleaned_df=cleaned_df[cleaned_df["Price"]>0]
        cleaned_df['Sale_Value']=cleaned_df.Quantity*cleaned_df.Price
        logging.info("positive sale value is calculated")
        logging.info("data cleaning is completed")
        return cleaned_df
    except Exception as e:
        raise CustomException(e,sys)
#RFM Grouping
def RFM_grouping(cleaned_df):
    try:
        logging.info("RFM Grouping is started")
        aggregated_df=cleaned_df.groupby(by='Customer ID',as_index=False).agg(
        Monetary=("Sale_Value","sum"),
        Frequency=("Invoice","nunique"),
        LastInvoiceDate=("InvoiceDate","max"))
        max_date=aggregated_df.LastInvoiceDate.max()
        # Recency calculation
        aggregated_df['Recency']=(max_date-aggregated_df['LastInvoiceDate']).dt.days
        RFM_colums=list(["Monetary","Frequency","Recency"])
        RFM_data=aggregated_df[RFM_colums]
        logging.info("RFM grouping is completed")
        return RFM_data,aggregated_df
    except Exception as e:
        raise CustomException(e,sys)
    
# outlier and non-outlier data separation
def non_outlier_calculation(RFM_data):
    try:
        logging.info("quantile calculation is started")
        limits=[]
        
        for i in RFM_data:
            if i!="Recency":
                Q1=RFM_data[i].quantile(0.25)
                Q3=RFM_data[i].quantile(0.75)
                IQR=Q3-Q1
                lower_bound=Q1-(1.5*IQR)
                upper_bound=Q3+(1.5*IQR)
                limits.append({"RFM_Params":i,"Lower_Bound":lower_bound,"Upper_Bound":upper_bound,"IQR":IQR})
        quantile_cal=pd.DataFrame(limits)
        Monetary_L_Bound=quantile_cal.loc[quantile_cal['RFM_Params']=='Monetary','Lower_Bound']
        Monetary_U_Bound=quantile_cal.loc[quantile_cal['RFM_Params']=='Monetary','Upper_Bound']
        
        Frequency_L_Bound=quantile_cal.loc[quantile_cal['RFM_Params']=='Frequency','Lower_Bound']
        Frequency_U_Bound=quantile_cal.loc[quantile_cal['RFM_Params']=='Frequency','Upper_Bound']
        logging.info("Monetary and Frequency upper and lower bound is calculated")
        M_Outlier_DF=RFM_data[(RFM_data['Monetary']<Monetary_L_Bound[0])|(RFM_data['Monetary']>Monetary_U_Bound[0])]
        F_Outlier_DF=RFM_data[(RFM_data['Frequency']<Frequency_L_Bound[1])|(RFM_data['Frequency']>Frequency_U_Bound[1])]
        Non_Outlier_Data=RFM_data[(~RFM_data.index.isin(M_Outlier_DF.index))&(~RFM_data.index.isin(F_Outlier_DF.index))]
        Overlap_Outlier_Index=M_Outlier_DF.index.intersection(F_Outlier_DF.index)
        M_only_outliers=M_Outlier_DF.drop(Overlap_Outlier_Index)
        F_only_outliers=F_Outlier_DF.drop(Overlap_Outlier_Index)
        M_F_overlap_DF=M_Outlier_DF.loc[Overlap_Outlier_Index]
        logging.info("outlier segregation is completed")
        return Non_Outlier_Data,M_Outlier_DF,F_Outlier_DF,M_only_outliers,F_only_outliers,M_F_overlap_DF
    except Exception as e:
        raise CustomException(e,sys)

# feature scaling 
def feature_scaling(Non_Outlier_Data: pd.DataFrame, feature: List[str]):
    try:
        logging.info("feature scaling is started")
        scalar=StandardScaler()
        scaled_data=scalar.fit_transform(Non_Outlier_Data)
        scaled_data=pd.DataFrame(scaled_data,columns=['Monetary','Frequency','Recency'],index=Non_Outlier_Data.index)
        logging.info("feature scaling is completed")
        return scaled_data
    except Exception as e:
        raise CustomException(e,sys)

def cluster_color_mapping(cluster_labels,Non_Outlier_Data,cluster_colors,cluster_name):
    try:
        Non_Outlier_Data['Cluster']=cluster_labels    
        colors=Non_Outlier_Data['Cluster'].map(cluster_colors)
        Non_Outlier_Data['ClusterName']=Non_Outlier_Data['Cluster'].map(cluster_name)
        logging.info("Cluster color mapping is completed")
        return Non_Outlier_Data,colors
    except Exception as e:
        raise CustomException(e,sys)

def outlier_cluster_mapping(Non_Outlier_Data,M_only_outliers,F_only_outliers,M_F_overlap_DF,cluster_colors,cluster_name):
    try:
        
        M_only_outliers['Cluster']=-1
        F_only_outliers['Cluster']=-2
        M_F_overlap_DF['Cluster']=-3
        logging.info("Assigned values to oulier clusters")
        outlier_DF=pd.concat([M_only_outliers,F_only_outliers,M_F_overlap_DF])
        logging.info("outlier data contactination is completed")
        colors_outlier=outlier_DF['Cluster'].map(cluster_colors)
        logging.info("outlier cluster color mapping is completed")
        outlier_DF['ClusterName']=outlier_DF['Cluster'].map(cluster_name)
        logging.info("cluster name assigned to outlier cluster")
        full_cluster_df=pd.concat([Non_Outlier_Data,outlier_DF])
        logging.info("Non outlier and outlier data concatination is completed")
        return full_cluster_df
    except Exception as e:
        raise CustomException(e,sys)
    
    


