from json.tool import main
import yaml
import pandas as pd
import sys
from enum import Enum
import sys
sys.path.append('../')
from neo4j_connections import Neo4jConnection
import coloredlogs, logging
import os 


config = dict()

def load_config(configuration): 
    """Function to load configuration settings from yaml file

    Args:
        configuration (dictionary): _description_
    """
    global config
    with open(configuration) as config_file: 
        config = yaml.load(config_file, Loader = yaml.FullLoader)
        
        
def upload_metaprotein_nodes(connection, node_list):
    """Function to upload metaproteins as nodes from csv file

    Args:
        connection (object of class Neo4jConnection): _description_
        node_list (dataframe): dataframe with each row/instance being one metaprotein node with the variables being node attributes
    """
    upload_query = """
       UNWIND $node_list as node 
       CREATE (dm: mp_demographic{
          metaprotein: node.Metaprotein,
          did: toInteger(node.mp_id),
          superkingdom: node.Superkingdom,
          kingdom: node.Kingdom,
          phylum: node.Phylum,
          class: node.Class,
          order: node.Order, 
          family: node.Family, 
          genus: node.Genus,
          species: node.Species 
       })
    """
    
    batch_len = 500 
    for batch_start in range(0, len(node_list), batch_len):
        batch_end = batch_start + batch_len
        records = node_list.iloc[batch_start: batch_end].to_dict("records")
        connection.query(upload_query, {"node_list": records})
        
        
def upload_patient_nodes(connection, node_list):
    """"Function to upload patients as nodes from csv file

    Args:
        connection (_type_): _description_
        node_list (dataframe): dataframe with each row/instance being one metaprotein node with the variables being node attributes
    """
    upload_patient_query = """
       UNWIND $node_list as node 
       CREATE (dm: mp_samples{
          patient: toInteger(node.patient),
          sid: node.p_id
       })
    """
    
    batch_len = 500 
    for batch_start in range(0, len(node_list), batch_len):
        batch_end = batch_start + batch_len
        records = node_list.iloc[batch_start: batch_end].to_dict("records")
        connection.query(upload_patient_query, {"node_list": records})
        
def upload_edges(connection, edge_list):
    edge_query = """
        UNWIND $edge_list as edge
        MATCH(source: mp_samples {sid: toInteger(edge.p_id)})
        MATCH(target: mp_demographic {did: toInteger(edge.mp_id)})
        
        MERGE (source)-[r:HAS_METAPROTEIN{val: toInteger(edge.values)}]->(target)
    """
    
    batch_len = 500 
    
    for batch_start in range(0, len(edge_list), batch_len):
        batch_end = batch_start + batch_len
        records = edge_list.iloc[batch_start: batch_end].to_dict("records")
        connection.query(edge_query, {"edge_list": records})
        
        
        
def preprocess_patient(df):
    sample_series = df.iloc[:, 0:2]
    return sample_series 
    
        
def main():
    configure = './config.yaml'
    load_config(configure)
    
    connection = Neo4jConnection(
        config
    )
    
    df_demographic = pd.read_csv(r'C:\Users\49171\Desktop\NodeClust\data\mp_demographic.csv');
    df_samples = pd.read_csv(r'C:\Users\49171\Desktop\NodeClust\data\mp_samples.csv');
    df_edges = pd.read_csv(r'C:\Users\49171\Desktop\NodeClust\data\mp_edges.csv');
    
    upload_metaprotein_nodes(connection, df_demographic)
    
    sample_df = preprocess_patient(df_samples)
    upload_patient_nodes(connection, sample_df)
    
    upload_edges(connection, df_edges)
    
    
    
if __name__ == "__main__":
    main()
    