install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
 	
# create deployment packages from lambdas as .zip file in ./build/
package_lambda:
	pynt packagelambda
	# to package individual lambdas instead of all lambdas in ./lambdas/, provide the corresponding name, eg:
	#pynt packagelambda[gluerunner]
	#pynt packagelambda[ons3objectcreated]

# upload Glue Runner lambda .zip package(s) to S3 for pickup by CloudFormation
deploy_lambda:
	pynt deploylambda

# deploy Glue scripts to the S3 path specified in configs
deploy_gluescripts:
	pynt deploygluescripts

# create the project's CloudFormation stacks
create_stack_sfr:
	pynt createstack["step-functions-resources"]
	
# glue-resources stack should only be created AFTER step-functions-resources
create_stack_glr:
	pynt createstack["glue-resources"]

create_stack_glrl:
	pynt createstack["gluerunner-lambda"]
	
create_stacks: create_stack_sfr create_stacks_glr create_stacks_glrl

# build stacks which will stand ready to be triggered upon addition of objects to data s3
build: package_lambda deploy_lambda deploy_gluescripts create_stacks

# delete stacks if no longer needed
delete_stacks:
	pynt deletestack["step-functions-resources"]
	pynt deletestack["glue-resources"]
	pynt deletestack["gluerunner-lambda"]	