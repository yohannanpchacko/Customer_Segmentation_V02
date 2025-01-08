import streamlit as st
import pandas as pd
import numpy as np
import time
from src.components.data_ingestion import load_data
from src.components.data_transformation import data_cleaning,RFM_grouping,non_outlier_calculation,feature_scaling,cluster_color_mapping,outlier_cluster_mapping
from src.components.model_training import perform_clustering
from src.utils import color_selection,final_cluster_naming
from src.components.visualization import plot_3d_scatter,violin_plot,bar_plot,plot_3d_scatter_new
from src.components.data_ingestion import final_output_data

st.markdown("<h1 style='text-align: center; color: blue; font-size: 24px;'>RFM Customer Segmentation with Kmeans Cluster</h1>",unsafe_allow_html=True)
st.divider()
sale=load_data()


RFM_colums=list(["Monetary","Frequency","Recency"])
n_clusters=st.slider(min_value=2,max_value=11,label="Select Number of Cluster",value=4)

# data cleaning
cleaned_df=data_cleaning(sale=sale)
RFM_data,aggregated_df=RFM_grouping(cleaned_df=cleaned_df)
Non_Outlier_Data,M_Outlier_DF,F_Outlier_DF,M_only_outliers,F_only_outliers,M_F_overlap_DF=non_outlier_calculation(RFM_data=RFM_data)
scaled_data=feature_scaling(Non_Outlier_Data=Non_Outlier_Data,feature=RFM_colums)
cluster_labels=perform_clustering(scaled_data=scaled_data,n_clusters=n_clusters)
cluster_colors=color_selection()
cluster_name=final_cluster_naming()
Non_Outlier_Data,colors=cluster_color_mapping(Non_Outlier_Data=Non_Outlier_Data,cluster_labels=cluster_labels,cluster_colors=cluster_colors,cluster_name=cluster_name)
# fig=plot_3d_scatter(Non_Outlier_Data=Non_Outlier_Data,colors=colors)
# st.pyplot(fig=fig)
# fig_3d=plot_3d_scatter_new(Non_Outlier_Data=Non_Outlier_Data,colors=colors)
# st.plotly_chart(fig_3d)


fig_3d = plot_3d_scatter_new(Non_Outlier_Data,colors=colors)
# Display the plot
st.plotly_chart(fig_3d,use_container_width=True)
# st.write(Non_Outlier_Data)
st.markdown("<br><br>", unsafe_allow_html=True)

fig2=violin_plot(Non_Outlier_Data=Non_Outlier_Data,cluster_colors=cluster_colors,RFM_colums=RFM_colums)
st.pyplot(fig2)
full_cluster_df=outlier_cluster_mapping(Non_Outlier_Data=Non_Outlier_Data,M_only_outliers=M_only_outliers,F_only_outliers=F_only_outliers,M_F_overlap_DF=M_F_overlap_DF,cluster_colors=cluster_colors,cluster_name=cluster_name)
final_output=final_output_data(aggregated_df,full_cluster_df)

fig3=bar_plot(full_cluster_df=full_cluster_df)
st.pyplot(fig3)
# st.write(final_output.head())
csv_data=final_output.to_csv(index=False)
st.download_button(data=csv_data,label="Download Final Segmented Data",file_name="Final_Segmented_Data.csv",mime="text/csv",key="download-button",help="click to download the clustered data")
st.sidebar.markdown("**Developed by Yohannan P Chacko**\n yohannanpchacko0814@gmail.com")
