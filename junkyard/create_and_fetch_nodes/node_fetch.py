from neo4j_connections import Neo4jConnection
import pandas as pd
import yaml
import sys
import sys
sys.path.append('../')

config = dict()

def load_config(configuration): 
    """Function to load configuration settings from yaml file

    Args:
        configuration (_type_): _description_
    """
    global config
    with open(configuration) as config_file: 
        config = yaml.load(config_file, Loader = yaml.FullLoader)
        
def main():
    configure = './config.yaml'
    load_config(configure)
    
    connection = Neo4jConnection(
        config
    )

    query = """MATCH (n:mp_samples)-[r:HAS_METAPROTEIN]-(m:mp_demographic) RETURN n.sid as sid,r.val as values,m.class as class,m.did as did,m.family as family,m.order as order,m.genus as genus,m.phylum as phylum,m.kingdom as kingdom,m.metaprotein as metaprotein,m.species as species,m.superkingdom as superkingdom"""

    df = connection.query(query)
    df.to_csv("graph.csv")

    print(df.columns)
    print(df.shape)

    
    
if __name__ == "__main__":
    main()