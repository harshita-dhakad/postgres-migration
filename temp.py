import connection_util
import postgres_read_table

conn = connection_util.create_postgres_connection()
df = postgres_read_table.get_record_as_df("project", conn)
print(df.head(5))