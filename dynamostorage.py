import boto3

dynamodb = boto3.resource('dynamodb')
dynamodb_client = boto3.client('dynamodb')

class dynamostorage():
    def createTable(TablNm):
        if TablNm in dynamodb_client.list_tables()['TableNames']:
            print('La tabla "', TablNm,'" ya existe')
            return
        else:
            table = dynamodb.create_table(
                TableName = TablNm,
                KeySchema = [
                    {
                        'AttributeName': 'key',
                        'KeyType': 'HASH' #Partition Key
                    }
                ],
                AttributeDefinitions = [
                    {
                        'AttributeName': 'key',
                        'AttributeType': 'S'
                    }
            ],
                ProvisionedThroughput={
                        'ReadCapacityUnits': 5,
                        'WriteCapacityUnits': 5
                    }
            )
            print("Table status:", table.table_status)

    def createTableWtSortKey(TablNm):
        if TablNm in dynamodb_client.list_tables()['TableNames']:
            print('La tabla "', TablNm,'" ya existe')
            return
        else:
            table = dynamodb.create_table(
                TableName = TablNm,
                KeySchema = [
                    {
                        'AttributeName': 'key',
                        'KeyType': 'HASH' #Partition Key
                    },
                    {
                        'AttributeName': 'Skey',
                        'KeyType': 'RANGE' #Partition Key
                    }
                ],
                AttributeDefinitions = [
                    {
                        'AttributeName': 'key',
                        'AttributeType': 'S'
                    },
                     {
                        'AttributeName': 'Skey',
                        'AttributeType': 'N'
                    }
            ],
                ProvisionedThroughput={
                        'ReadCapacityUnits': 5,
                        'WriteCapacityUnits': 5
                    }
            )
            print("Table status:", table.table_status)

    def StoreInfo(Images, Labels, TbImages, TbLabels):
        table = dynamodb.Table(TbImages)
        #print(table.creation_date_time)

        with table.batch_writer() as batch:
            for r in Images:
                batch.put_item(Item=r)

        print('Starting second Table')
        table = dynamodb.Table(TbLabels)

        with table.batch_writer() as batch:
            for r in Labels:
                batch.put_item(Item=r)
        print('Data loading complete')
