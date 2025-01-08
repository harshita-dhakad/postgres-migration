from py2neo import Node
from connection_util import get_neo4j_graph, create_postgres_connection
from postgres_read_table import get_record_as_df

def insert_data_to_neo4j(table_name:str):

    conn = create_postgres_connection()
    record_df = get_record_as_df(table_name, conn)

    record_dict = record_df.to_dict(orient='records')
    
    graph = get_neo4j_graph()
    label = table_name.capitalize()
    for record in record_dict:
        node = Node(label, **record)
        graph.merge(node, label, 'id')

