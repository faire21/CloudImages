import boto3
import dynamostorage as DynDBStorage
import keyvalue.parsetriples as ParseTripe
import keyvalue.stemmer as Stemmer


dynamodb = boto3.resource('dynamodb')
dynamodb_client = boto3.client('dynamodb')
DynDBStorage.dynamostorage.createTableWtSortKey('kv_labels')
DynDBStorage.dynamostorage.createTableWtSortKey('kv_images')

filename1 = 'images.ttl'
filename2 = 'labels_en.ttl'


iteration = 450
line = []
EveryLine = []
images = []
labels =[]
file = open(filename1,"r",errors='ignore')

#print('**********Images***********')
for i in range(iteration):
    line = ParseTripe.ParseTriples.getNext(file)
    images.append(
        {
         'key': line[0],
         'Skey': i,
         'value': line[2]
        }
        )
    if line[0][38:] not in EveryLine:
        EveryLine.append(line[0][38:])
    #print('Key ',line[0], ' SortKey ', i , ' Value',line[2])

file.close()

file = open(filename2,"r",errors='ignore')
#print('**********Labels***********')
for i in range(iteration):
    line = ParseTripe.ParseTriples.getNext(file)
    if line[0][38:]  in EveryLine:
        arrange= line[2].split(' ',  )
        for w in arrange:
            word = Stemmer.stem(w)
            labels.append({
                'key': word,
                'Skey': int(line[0][38:]) ,
                'value': line[0] })
            #print('Key ', word, ' SortKey ', line[0][38:] , ' Value',line[0])
    else:
        i=i-1
file.close()
#print(EveryLine)

DynDBStorage.dynamostorage.StoreInfo(images, labels, 'kv_images', 'kv_labels')
