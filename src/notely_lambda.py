import jsons
from notely.notely import create_note
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Notely_DB')

def lambda_handler(event, context):

    context = event.get('context', {})
    http_method = context.get('http-method', None)

    if http_method is None:
        return {
            'statusCode': 500,
            'body': jsons.dumps('Unable to determine HTTP method')
        }

    newnote = create_note()
    table.put_item(
        Item=jsons.dump(newnote)
    )
    # TODO implement
    return {
        'statusCode': 200,
        'body': jsons.dumps(newnote)
    }