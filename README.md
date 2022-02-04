# Serverless ETL on AWS using Step Functions, Lambda, Glue, and CloudFormation
ETL workflow to grab (two) datasets from an S3 bucket upon uploading, apply transformations to them separalely in parallel, and join the transformed versions after all the separate transformation processes complete. 
![Step Functions DAG](https://github.com/biswas/aws-serverless-etl/blob/main/resources/stepfunctions_graph.png)

## Steps:
1. Clone this repo into an environment with AWS CLI.
2. Make sure user hass full access to CloudFormation, Creating IAM Roles, Step Functions, Lambda, Glue, DynamoDB, S3, CloudWatch and CloudWatch Logs.
3. Create and activate virtual environment, then run `make install`.
4. Update the resource name `"sfn_activity_arn"` in `./lambda/gluerunner/gluerunner-config.json` to include the user region and account ID in the correct format: `arn:aws:states:<region-name>:<account-ID>:activity:GlueRunnerActivity`.
5. Run `make build`.
6. After build success, execute state machine from either the Step Functions console or the CLI. Make sure the data S3 bucket does not exist prior to this execution.
7. To remove cloud resources after ETL run completion and backing up of any necessary outputs, first delete the data S3 bucket and then run `make delete_stacks`.

## References:
- <https://aws.amazon.com/blogs/big-data/orchestrate-multiple-etl-jobs-using-aws-step-functions-and-aws-lambda/>
- <https://github.com/aws-samples/aws-etl-orchestrator>: codes from the tutorial repo modified to exclude Athena and use python3.8 [instead of 2.7](https://aws.amazon.com/blogs/compute/announcing-end-of-support-for-python-2-7-in-aws-lambda/)
