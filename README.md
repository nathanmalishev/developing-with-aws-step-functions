# Developing with AWS Step Functions

## Senario

University students caught plagiarising on exams and assignments are required to take exams to test their knowledge of the universities referencing standard. Students get three attempts to pass the exam before administrative action is taken.

This demo uses exposes an <a href="https://aws.amazon.com/step-functions/">AWS Step Function</a>  via an <a href="https://aws.amazon.com/api-gateway/">Amazon API Gateway</a>. The step-function definition invokes tasks via <a href="https://aws.amazon.com/lambda/">AWS Lambda</a> (Python 3.6), that store results in <a href="https://aws.amazon.com/dynamodb">Amazon DynamoDB</a>. Notifications are implemented via <a href="https://aws.amazon.com/dynamodb">Amazon SNS</a> and <a href="https://aws.amazon.com/xray/">AWS X-Ray</a> provides distributed tracing capability.

