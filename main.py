import connection_util
import create_table
import insert_data
import migration
from log import logger
import update_table


logger.info("Establishing connection to PostgreSQL.")
conn = connection_util.create_postgres_connection()
logger.info("PostgreSQL connection established successfully.")

logger.info("Fetching table JSON for table creation.")
table_json = create_table.get_table_json()
logger.info("Table JSON fetched successfully.")

logger.info("Creating tables in PostgreSQL from JSON schema.")
create_table.create_tables_from_json(table_json, conn)
logger.info("Tables created successfully in PostgreSQL.")

logger.info("Inserting data into PostgreSQL tables.")
insert_data.insert_data_in_postgres(conn)
logger.info("Data inserted successfully into PostgreSQL.")

# logger.info("Updating records in PostgreSQL table.")
# update_table.update_table_record(
#     table_name="your_table_name",  # Replace with your actual table name
#     column="your_column_name",    # Replace with the column to update
#     value="new_value",            # Replace with the new value
#     condition_column="condition_column_name",  # Replace with condition column
#     condition_value="condition_value",        # Replace with condition value
#     connection=conn
# )
# logger.info("Table records updated successfully.")


logger.info("Establishing connection to Neo4j.")
driver = connection_util.create_neo4j_connection()
logger.info("Neo4j connection established successfully.")

logger.info("Migrating data from PostgreSQL to Neo4j.")
migration.migrate_data_to_neo4j(conn, driver, table_json)
logger.info("Data migration to Neo4j completed successfully.")

logger.info("Closing connections.")
if conn:
    conn.close()
    logger.info("PostgreSQL connection closed.")
if driver:
    driver.close()
    logger.info("Neo4j connection closed.")


