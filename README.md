# sam-app

This project contains the source code and support files for a serverless application for Slack notifications that you can deploy using SAMCLI.

## Build

```bash
sam build
```

## Local Test

```bash
sam local start-api --env-vars env.json
```

```bash
sam local invoke "HelloWorldFunction" -e events/event.json --env-vars env.json
```

## Deploy

```bash
sam deploy --guided
```

## Cleanup

```bash
# aws cloudformation delete-stack --stack-name <app name> --region <region>
aws cloudformation delete-stack --stack-name sam-app --region ap-northeast-1
```
