# import connection_util
# import postgres_read_table

# conn = connection_util.create_postgres_connection()
# df = postgres_read_table.get_record_as_df("project", conn)

# d = df.to_dict(orient="records")
# print(d)
# dt = {'sep': '-separator-', 'end': '-- line end --'}

dt1 = {'name': 'harshi' , 'age' : 23}
print(**dt1)




# ls = [1, 2, 3, 4, 5]

# print(*ls)

# dic = dict(
#     name = "ritik",
#     age = 25
# )
# print(**dic)

# c = {'name': 'ritik', 'age': 25}


# def find_a(**c) :
#     print() 

# find_a(c)
