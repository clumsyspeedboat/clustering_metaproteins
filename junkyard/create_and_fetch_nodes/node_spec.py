import pandas as pd
from neo4j import GraphDatabase

df = pd.read_csv(r"..\NodeClust\data\Dataset_Metaprotein.csv")
    
    

class Data_Loader():
    
    def __init__(self, edge_path, node_path):
        self.edge_path = edge_path
        self.node_path = node_path


    def create_edge_list(self):
        edge_list = pd.read_csv(self.edge_path, header=None, names=["target", "source"],)
        edge_list["label"] = "cites"
        return edge_list

        
    def create_node_list(self):
        self.feature_names = ["w_{}".format(i) for i in range(1433)]
        column_names = self.feature_names + ["subject"]
        node_list = pd.read_csv(self.node_path, sep="\t", header=None, names=column_names)
        node_list.insert(0, 'edge_index', range(0, len(node_list)))
        return node_list

    
    def preprocess_node_list(self, n_list):
        n_list["feature"] = n_list[self.feature_names].values.tolist()
        n_list = n_list.drop(columns=self.feature_names)
        n_list["id"] = n_list.index
        return n_list