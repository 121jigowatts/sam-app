import json
import os
import requests

SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']

def lambda_handler(event, context):
    print(SLACK_WEBHOOK_URL)

    payload = {
        'attachments': [
            {
                'color': '#00a1c6',
                'pretext': "test",
                'text': "It's works!!"
            }
        ]
    }

    try:
        response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload))
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e
    else:
        print(response.status_code)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "success",
        }),
    }
