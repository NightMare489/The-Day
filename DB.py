import sqlite3

con = sqlite3.connect("DataBase.db")
cursor = con.cursor()



sql_query="""UPDATE 'Subjects' SET Status=1 WHERE Name = 'ESP0'"""


# for i in range(1,25):
#     sql_query = f"""insert into PhysicsI values ({i},{i})"""
cursor.execute(sql_query)
con.commit()