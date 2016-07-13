import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", host="db", port="5432")
query_cu = conn.cursor()

query_cu.execute('SELECT link FROM interviews_post')
tuple_list = query_cu.fetchall()
