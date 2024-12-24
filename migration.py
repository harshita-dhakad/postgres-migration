from log import logger

def get_create_node_queries(table_name, connection):
    logger.info("function get_create_node_queries is quering for node creation")
     
    cursor = connection.cursor()
    cursor.execute(f"select * from {table_name}")

    table_rows = cursor.fetchall()
    col_names = cursor.description
    n = len(col_names)

    queries = []
    for table_row in table_rows:
        query = ""
        for i in range(n):
            query = query + f"{col_names[i].name} : '{table_row[i]}', "
        query = f"CREATE (:{table_name} {{ {query[:-2]} }})"
        queries.append(query)
    logger.info("nodes are created")
    return queries

        
def migrate_data_to_neo4j(connection, driver, table_json):
    logger.info("function migrate_data_to_neo4j is inserting data in neo4j")

    for table_dict in table_json:
        table_name = table_dict['table_name']

        queries = get_create_node_queries(table_name, connection)

        with driver.session() as session:
            for query in queries:
                session.run(query)
    logger.info("data is entered in neo4j")