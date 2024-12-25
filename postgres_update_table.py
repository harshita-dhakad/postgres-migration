from log import logger


def update_table_record(table_name, column, value, condition_column, condition_value, connection):
    cursor = connection.cursor()

    # Create the SQL update query
    query = f"UPDATE {table_name} SET {column} = {value} WHERE {condition_column} = {condition_value};"
    logger.info(f"Executing query: {query} with values ({value}, {condition_value})")

    try:
        cursor.execute(query, (value, condition_value))
        connection.commit()
        logger.info(f"Table '{table_name}' updated successfully.")
    except Exception as e:
        logger.info(f"Failed to update table '{table_name}': {e}")
        connection.rollback() # Rollback changes if error occurs
    finally:
        cursor.close()

