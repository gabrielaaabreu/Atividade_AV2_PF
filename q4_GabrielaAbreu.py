import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                password="#123456A*")
crs = mydb.cursor()

execSQLCmd = lambda cmd, crs : crs.execute(cmd)
execUseDB = lambda dbname, crs : execSQLCmd("Use " + dbname + ";\n", crs)

execUseDB("dbq3", crs)
execShowColumns = lambda table : execSQLCmd("select distinct(COLUMN_NAME) from information_schema.COLUMNS where TABLE_NAME='" + table + "'", crs)
execCreateTable = lambda table, attrib, crs : execSQLCmd("Create table " + table + "(" + attrib + ");\n", crs)


def get_shared_attributes(table1, table2):
    execShowColumns(table1)
    t1 = crs.fetchall()
    execShowColumns(table2)
    t2 = crs.fetchall()
    sharedAttributes = [e for e in t1 if e in t2]
    sharedAttributesList = [''.join(i) for i in sharedAttributes]
    return sharedAttributesList

def gen_inner_join (t1, t2) :
    commonattrs = get_shared_attributes(t1[0],t2[0])
    code = " INNER JOIN " + t2 [0] + " " + t2 [1] + " ON ("
    for i in range (len (commonattrs)) :
        code += " AND " if i > 0 else ""
        code += t1 [1] + "." + commonattrs [i] + " = " + t2 [1] + "." + commonattrs [i]
    code += ")"
    return code

execInnerJoin = lambda t1, t2 : gen_inner_join(t1, t2)
execSelectFromInnerJoin = lambda attrib, table1, table2, table3, crs : execSQLCmd("Select " + attrib + " from " + table1[0] + " " + table1[1] + " " + execInnerJoin(table1, table2) + " " + execInnerJoin(table2, table3) +  ";\n", crs)

execSelectFromInnerJoin("*", ["games", "g"], ["videogames", "v"], ["company", "c"], crs)
res = crs.fetchall()
print_result = lambda res : [print(e) for e in res]
print_result(res)




