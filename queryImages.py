import keyvalue.sqlitekeyvalue as KeyValue
import keyvalue.parsetriples as ParseTripe
import keyvalue.stemmer as Stemmer


# Make connections to KeyValue
kv_labels = KeyValue.SqliteKeyValue("sqlite_labels.db","labels",sortKey=True)
kv_images = KeyValue.SqliteKeyValue("sqlite_images.db","images")

# Process Logic.
print('Enter Query:')
s = input()
QueryResults = []
Query1 = []
array = s.split(' ', )
for w in array:
    #print('w is ', w)
    word = Stemmer.stem(w)
    Query1 = kv_labels.get(word)
    #print(Query1)
    if Query1:
        #Query1 = Query1.split(' ', 1)
        #print('Query 1 is: ', Query1)
        for item in Query1:
            Query2 = kv_images.get(item[0])
            #print ('RESPONSE FROM THE QUERY',Query2)
            if Query2 is not None:
                QueryResults.append(Query2)
    #else:
        #print('not found')
print(QueryResults)

# Close KeyValues Storages
kv_labels.close()
kv_images.close()







