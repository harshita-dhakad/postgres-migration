import pandas as pd


def get_record_as_df(table_name, connection):
    cursor = connection.cursor()
    cursor.execute(f"select * from {table_name} LIMIT 3")

    table_rows = cursor.fetchall() # Executes the query and puts the query restult in table_rows
    columns = cursor.description # provides column data (Column1, Column2) 

    print(table_name) #client

    # [('1', 'Acme Corp', 'contact@acmecorp.com'), ('2', 'Tech Innovations', 'support@techinnovations.com'), 
    # ('3', 'Global Enterprises', 'info@globalenterprises.com')]
    # print(table_rows)
    
    # (Column(name='id', type_code=1043), Column(name='client_name', type_code=1043), Column(name='contact_email', type_code=1043))
    # print(columns)

    # print(columns[0]) # Column(name='id', type_code=1043)
    # print(columns[0].name) # id

    list_column = []
    for i in columns:
        list_column.append(i.name)
    # print(list_column)

    df = pd.DataFrame(table_rows, columns = list_column )
    return df

