# Serverless ETL on AWS using Step Functions, Lambda, Glue, and CloudFormation

## Steps:
1. Clone this repo into an environment with AWS CLI.
2. Make sure user hass full access to CloudFormation, Creating IAM Roles, Step Functions, Lambda, Glue, DynamoDB, S3, CloudWatch and CloudWatch Logs.
3. Create and activate virtual environment, then run `make install`.
3. Run `make build`.
4. After build success, execute state machine from either the Step Functions console or the CLI. Make sure the data S3 bucket does not exist prior to this execution.
5. To remove cloud resources after ETL run completion and backing up of any necessary outputs, first delete the data S3 bucket and then run `make delete_stacks`.

## References:
    - <https://aws.amazon.com/blogs/big-data/orchestrate-multiple-etl-jobs-using-aws-step-functions-and-aws-lambda/>