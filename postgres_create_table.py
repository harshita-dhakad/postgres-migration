import json
from log import logger

def  get_table_json():
    logger.info("function get_table_json is getting data from json file")
    file = open('./table.json', 'r')
    file_data = file.read()
    json_data = json.loads(file_data)
    logger.info("data from json is returned in original format")
    return json_data


def create_tables_from_json(tables, connection):
    logger.info("function create_table_from_json is creating table from json data")
    cursor = connection.cursor()
    for table_dict in tables:
        table_name = table_dict['table_name']
        columns = table_dict['columns']

        create_table_query = get_create_table_query(table_name, columns)
        cursor.execute(create_table_query)
        connection.commit()
    logger.info("returned table names and columns in desired format")



def get_create_table_query(table_name, columns):
    logger.info("function get_create_table_query is writing query in postgres for creating a table")
    columns_str = ""

    for column in columns:
        if column != columns[-1]:
            columns_str = columns_str + column + " VARCHAR(150),"
        else:
            columns_str = columns_str + column + " VARCHAR(150)"

    # Add created_at and updated_at columns
    columns_str += ", created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
    columns_str += ", updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"

    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
    print(query)
    logger.info("table is created ")
    return query