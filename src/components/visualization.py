import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from src.exception import CustomException
from src.logger import logging
import sys



# Non outlier customer segmentation in 3d scatterplot with Nonoutlier data
def plot_3d_scatter(Non_Outlier_Data: pd.DataFrame,colors):
    try:

        fig=plt.figure(figsize=(12,12))
        ax=fig.add_subplot(projection='3d')
        scatter=ax.scatter(Non_Outlier_Data['Monetary'],Non_Outlier_Data['Frequency'],Non_Outlier_Data['Recency'],c=colors,s=70)
        ax.set_xlabel("MonetaryValue",fontsize=14)
        ax.set_ylabel("Frequency",fontsize=14)
        ax.set_zlabel("Recency",fontsize=14)
        ax.set_title("Kmeans cluster in 3d plot",fontsize=24)
        ax.tick_params(axis='x', labelsize=12)
        ax.tick_params(axis='y', labelsize=12)
        ax.tick_params(axis='z', labelsize=12)    
        plt.tight_layout()
        logging.info("3d Scatterplot is created")
        return fig
    except Exception as e:
        raise CustomException(e,sys)

# Non outlier Customer Segmentation in violin plot
def violin_plot(Non_Outlier_Data: pd.DataFrame,cluster_colors,RFM_colums):
    try:

        fig2=plt.figure(figsize=(10,10))   
        for index,name in enumerate(RFM_colums):        
            ax=fig2.add_subplot(3,1,index+1)
            sns.violinplot(x=Non_Outlier_Data['Cluster'],y=Non_Outlier_Data[name],palette=cluster_colors,hue=Non_Outlier_Data['Cluster'],ax=ax)
            ax.set_title(f"{name} Violinplot",fontsize=14)
            ax.set_xlabel(f'{name}')
            ax.set_ylabel('Count')
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Cluster')
        plt.tight_layout()
        logging.info("Violin plot is created")
        return fig2
    except Exception as e:
        raise CustomException(e,sys)
    
# full customer segmentation with bar plot
def bar_plot(full_cluster_df:pd.DataFrame):
    try:

        label_name_grouped=full_cluster_df.value_counts('ClusterName')
        full_cluster_df['value_in_hundreds']=full_cluster_df['Monetary']/100
        feature_means=full_cluster_df.groupby(by='ClusterName')[['value_in_hundreds','Frequency','Recency']].mean()
        fig1,ax1=plt.subplots(figsize=(14,8))
        sns.barplot(x=label_name_grouped.index,y=label_name_grouped.values,ax=ax1,palette='Paired',hue=label_name_grouped.index,)
        ax1.set_title("Cluster Counts with Avg RFM",fontsize=24)
        ax1.set_xlabel("Segment Name",fontsize=14)
        ax1.set_ylabel("Customer Count",fontsize=14,color='red')
        ax1.tick_params(axis='x',labelsize=12)
        ax1.tick_params(axis='y',labelsize=12)    
        ax2=ax1.twinx()
        sns.lineplot(data=feature_means,ax=ax2,palette='Set2',marker='o')
        ax2.set_ylabel("Average Value",color='g',fontsize=14)
        ax2.tick_params(axis='y',labelsize=12)
        logging.info("barplot is created on complete semented data")
        return fig1
    except Exception as e:
        raise CustomException(e,sys)
    

