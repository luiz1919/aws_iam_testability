# aws_iam_testability
Simple repository to test the security using AWS IAM

Let's prepare an app in python that runs in a docker container. 
Then we will create a github action that compiles the code, builds the container image and pushes it to an Elastic Container Registry in aws.

The app in python just creates a dummy text file and pushes it to a S3 bucket in aws.