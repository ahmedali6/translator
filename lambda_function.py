import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    data = json.loads(event['body'])
    print(data)
    client = boto3.client('translate')
    response = client.translate_text(
    Text=data['text'],
    SourceLanguageCode=data['source'],
    TargetLanguageCode=data['target'],
)
    if len(response['TranslatedText']) < 2:
        return "The language could not be translated please check that you choosed the right source", 404
    return response['TranslatedText'], 200
