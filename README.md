# aws_iam_testability
Simple repository to test the security using AWS IAM

## Description

Python app that creates a dummy txt file and pushes it to an AWS S3 bucket.

We have all the code in [Github](https://github.com/luiz1919/aws_iam_testability) with a GitHub Action that logs in into AWS, builds the docker image and pushes it to AWS ECR (Elastic Container Registry).

### Policies

It is necessary that the user to log in with, has the following permissions:

- S3 permissions to upload files
- ECR permissions to push images

### Secrets

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_S3_BUCKET

### Workflow diagram

![Workflow](./img/assessment%201.png)

## Run locally

If you want to run locally the docker container, execute the following commands:

```cmd
docker build -t my-python-app .

docker run -e AWS_ACCESS_KEY_ID=your_key \
           -e AWS_SECRET_ACCESS_KEY=your_secret \
           -e AWS_S3_BUCKET=your_bucket \
           my-python-app
```