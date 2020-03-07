import keyvalue.sqlitekeyvalue as KeyValue
import keyvalue.parsetriples as ParseTripe
import keyvalue.stemmer as Stemmer



filename1 = 'images.ttl'
filename2 = 'labels_en.ttl'
# Make connections to KeyValue
kv_labels = KeyValue.SqliteKeyValue("sqlite_labels.db","labels",sortKey=True)
kv_images = KeyValue.SqliteKeyValue("sqlite_images.db","images")

# Process Logic.
# iteration is the number of Images that we want stored
# line stores the obtained line from the dataset
# EveryLine stores de ID from the image, to ensure that every label has an image
iteration = 750
line = []
EveryLine = []
file = open(filename1,"r",errors='ignore')

#
#print('**********Images***********')
for i in range(iteration):
    line = ParseTripe.ParseTriples.getNext(file)
    kv_images.put(line[0], line[2])
    if line[0][37:] not in EveryLine:
        EveryLine.append(line[0][37:])
    #print('Key ', line[0], 'Value', line[2])
file.close()

file = open(filename2,"r",errors='ignore')
#print('**********Labels***********')
for i in range(iteration):
    line = ParseTripe.ParseTriples.getNext(file)
    if line[0][37:]  in EveryLine:
        arrange= line[2].split(' ',  )
        for w in arrange:
            word = Stemmer.stem(w)
            kv_labels.putSort(word, line[0][37:] ,line[0])
            #print('Key ', word, 'SortKey ', line[0][37:] , 'Value',line[0])
    else:
        i=i-1
file.close()
#print(EveryLine)
# Close KeyValues Storages
kv_labels.close()
kv_images.close()
print('Loading Complete')







