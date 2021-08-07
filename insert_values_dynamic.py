#load data into a DataFrame object:
df = pd.DataFrame(data)


valueslists = []

row1 = [column for column in df.columns]
tupleRow = tuple(row1)

tuplelist = []



lastindex = len(row1) - 1
query = "INSERT INTO Customers " + str(tupleRow) +  " VALUES "
for i, row in df.iterrows():
    loopindex = 0
    query += "("
    for j, column in row.iteritems():
        if lastindex != loopindex:
            query += "'%s', "
        else:
            query += "'%s'"
        tuplelist.append(column)
        loopindex += 1
    query += "), "

query = query[0:len(query)-2]
query += ";"


tupleTuple = tuple(tuplelist)
query = query%tupleTuple
print(query)
