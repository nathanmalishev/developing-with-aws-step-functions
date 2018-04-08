# Developing with AWS Step Functions

## Senario

University students caught plagiarising on exams and assignments are required to take exams to test their knowledge of the universities referencing standard. Students get three attempts to pass the exam before administrative action is taken.

This demo uses exposes an <a href="https://aws.amazon.com/step-functions/">AWS Step Function</a>  via an <a href="https://aws.amazon.com/api-gateway/">Amazon API Gateway</a>. The step-function definition invokes tasks via <a href="https://aws.amazon.com/lambda/">AWS Lambda</a> (Python 3.6), that store results in <a href="https://aws.amazon.com/dynamodb">Amazon DynamoDB</a>. Notifications are implemented via <a href="https://aws.amazon.com/dynamodb">Amazon SNS</a> and <a href="https://aws.amazon.com/xray/">AWS X-Ray</a> provides distributed tracing capability.

## Architecture

TODO: add  diagram

# Credits
* [heitorlessa/cookiecutter-aws-sam-python](href="https://github.com/heitorlessa/cookiecutter-aws-sam-python)
Cookiecutter SAM for Python Lambda - 
A cookiecutter template to create a Serverless App based on Serverless Application Model (SAM) and Python 3.6.

# Resources

## Step Functions

* [AWS Step Functions](https://aws.amazon.com/step-functions/)
* [AWS Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
* [statelint](https://github.com/awslabs/statelint)
* [Amazon States Language](https://states-language.net/spec.html)

## Reference Architectures

* [Serverless Reference Architecture: Image Recognition and Processing Backend](https://github.com/awslabs/lambda-refarch-imagerecognition)
* [Serverless Reference Architecture: Snapshot Management](https://github.com/awslabs/aws-step-functions-ebs-snapshot-mgmt)
* [Batch Architecture for Life Sciences Workloads](https://github.com/awslabs/aws-batch-genomics)
* [S3 Bucket Sync Reference](https://github.com/awslabs/sync-buckets-state-machine)
* [Step Functions Plug-In for Serverless Framework](https://github.com/horike37/serverless-step-functions)

## AWS Developer Resources

* [Serverless Application Model](https://github.com/awslabs/serverless-application-model)
* [DevOps and AWS](https://aws.amazon.com/devops/)
* [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/)