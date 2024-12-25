from py2neo import Node
from connection_util import get_neo4j_graph
from log import logger

def update_node(label:str, properties, id):
    label = label.capitalize()

    try:
        graph = get_neo4j_graph()
        node = Node(label, id=id, **properties)
        graph.merge(node, label, 'id')
    except Exception as e:
        logger.error(f"Error during node update - {e}")


update_node('employee', {"name" : "Test Employee", "age" : 16, "email" : "test@gmail.com"}, 20)