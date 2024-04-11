import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                password="#123456A*")
crs = mydb.cursor()

execSQLCmd = lambda cmd, crs : crs.execute(cmd)

#Comandos relacionados ao banco
execCreateDB = lambda dbname, crs : execSQLCmd("Create database " + dbname + ";\n", crs)
execUseDB = lambda dbname, crs : execSQLCmd("Use " + dbname + ";\n", crs)
execDropDB = lambda dbname, crs : execSQLCmd("Drop database " + dbname + ";\n", crs)

#Comandos relacionados às tabelas
execCreateTable = lambda table, attrib, crs : execSQLCmd("Create table " + table + "(" + attrib + ");\n", crs)
execDropTable = lambda table, crs : execSQLCmd("Drop table " + table + ";\n", crs)

#Comando para inserção de dados na tabela
execInsertInto = lambda table, attrib, values, crs: execSQLCmd("Insert into " + table + "( " + attrib + ") values ( " + values + ");\n", crs)

#Comando para realizar seleção
execSelectFrom = lambda attrib, table, crs : execSQLCmd("Select " + attrib + " from " + table + ";\n", crs)

#Comando para deletar informações
execDeleteFrom = lambda attrib, table, value, crs : execSQLCmd("Delete from " + table + " where " + attrib + " = " + value + ";\n", crs)

#Criar bd
execCreateDB("dbq3", crs)

#Usar db
execUseDB("dbq3", crs)

#Criar tabelas users, videogames, games, company
execCreateTable("users", "id_user varchar(80), name_user varchar(80), country varchar(80), id_console varchar(80)", crs)
execCreateTable("videogames", "id_console varchar(80), name varchar(80), id_company varchar(80), release_date_vg varchar(80)", crs)
execCreateTable("games", "id_game varchar(80), title varchar(80), genre varchar(80), release_date_game varchar(80), id_console varchar(80)", crs)
execCreateTable("company", "id_company varchar(80), name_company varchar(80), country varchar(80)", crs)

#Inserir dados nas tabelas
execInsertInto("users", "id_user, name_user, country, id_console", "'1', 'John', 'USA', '15'", crs)
execInsertInto("users", "id_user, name_user, country, id_console", "'2', 'Clara', 'USA', '21'", crs)
execInsertInto("users", "id_user, name_user, country, id_console", "'3', 'Maria', 'Argentina', '30'", crs)

execInsertInto("videogames", "id_console, name, id_Company, release_date_vg", "'15', 'Console 1', '1', '15/11/2015'", crs)
execInsertInto("videogames", "id_console, name, id_Company, release_date_vg", "'21', 'Console 2', '2', '01/03/2020'", crs)
execInsertInto("videogames", "id_console, name, id_Company, release_date_vg", "'30', 'Console 3', '3', '31/10/2010'", crs)

execInsertInto("games", "id_game, title, genre, release_date_game, id_console", "'1', 'Game 1', 'Adventure', '04/04/1999', '15'", crs)
execInsertInto("games", "id_game, title, genre, release_date_game, id_console", "'2', 'Game 2', 'Horror', '09/10/2023', '21'", crs)
execInsertInto("games", "id_game, title, genre, release_date_game, id_console", "'3', 'Game 3', 'Adventure', '02/06/2018', '30'", crs)

execInsertInto("company", "id_company, name_company, country", "'1', 'Company 1', 'USA'", crs)
execInsertInto("company", "id_company, name_company, country", "'2', 'Company 2', 'Italy'", crs)
execInsertInto("company", "id_company, name_company, country", "'3', 'Company 3', 'Japan'", crs)

mydb.commit()

#Realizar consultas
print_result = lambda res : [print(e) for e in res]

execSelectFrom("name_user, country", "users", crs)
res1 = crs.fetchall()
print_result(res1)
print("\n")

#Deletar informação em uma tabela
execSelectFrom("*", "company", crs)
res = crs.fetchall()
print_result(res)

execDeleteFrom("country", "company", "'Japan'", crs)

execSelectFrom("*", "company", crs)
res = crs.fetchall()
print("\n")
print_result(res)











