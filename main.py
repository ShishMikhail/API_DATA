import api
import pandas as pd

API = api.DB(host='127.0.0.1', username='postgres', password='we010203', database='api_kt')

data = {'fullname': ['Jon Jonovich Jonov', 'Вася пупкин пупкович', 'Ян Янов Янович'], 'age': [111, 222, 0]}
df = pd.DataFrame(data)
API.create_table(df, 'db', 'users')
print(df)

API.delete_from_table('users', 'db', conditions="age = 0")

query = "SELECT * FROM db.users"
result = API.read_sql(query)
print(result)

API.truncate_table('db', 'users')

data = {'fullname': ['Jon Jonovich Jonov', 'Вася пупкин пупкович', 'Ян Янов Янович'], 'age': [111, 222, 0]}
df = pd.DataFrame(data)

API.insert_sql(df, 'db', 'users')

query = "UPDATE db.users SET age = 7 WHERE fullname = 'Ян Янов Янович'"
API.execute(query)

query = "SELECT * FROM db.users"
result = API.read_sql(query)
print(result)
