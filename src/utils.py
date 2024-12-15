import pandas as pd

def color_selection():
        
    cluster_colors = {
    0: '#1f77b4',  # Blue
    1: '#ff7f0e',  # Orange
    2: '#2ca02c',  # Green
    3: '#d62728',  # Red
    4: '#8A2BE2',  # Violet
    5: '#9467bd',  # Purple for Cluster_6
    6: '#17becf',  # Teal for Cluster_7
    7: '#bcbd22',  # Yellow-Green for Cluster_8
    8: '#e377c2',  # Pink for Cluster_9
    9: '#7f7f7f',  # Gray for Cluster_10
    10: '#c49c94', # Beige for Cluster_11
    -1: '#E5E4E2', # Platinum for Platinum
    -2: '#FFD700', # Gold for Gold
    -3: '#C0C0C0'  # Silver for Super Platinum
    }
    return cluster_colors

def final_cluster_naming():
    cluster_name={
    0:"Low_Recent",
    1:"Inactive",
    2:"Premium",
    3:"Moderate",
    4:"Cluster_5",
    5:"Cluster_6",
    6:"Cluster_7",
    7:"Cluster_8",
    8:"Cluster_9",
    9:"Cluster_10",
    10:"Cluster_11",
    -1:"Platinum",
    -2:"Gold",
    -3:"Super Platinum"
}
    return cluster_name
    
    