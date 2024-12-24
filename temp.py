import connection_util
import read_table

conn = connection_util.create_postgres_connection()
df = read_table.get_record_as_df("project", conn)
print(df.head(5))