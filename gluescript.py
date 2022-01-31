import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": [
            "s3://awsglue-datasets/examples/medicare/Medicare_Hospital_Provider.csv"
        ],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("DRG Definition", "string", "DRG Definition", "string"),
        ("Provider Id", "long", "Provider Id", "long"),
        ("Provider Name", "string", "Provider Name", "string"),
        ("Provider Street Address", "string", "Provider Street Address", "string"),
        ("Provider City", "string", "Provider City", "string"),
        ("Provider State", "string", "Provider State", "string"),
        ("Provider Zip Code", "long", "Provider Zip Code", "long"),
        (
            "Hospital Referral Region Description",
            "string",
            "Hospital Referral Region Description",
            "string",
        ),
        ("Total Discharges", "long", "Total Discharges", "long"),
        ("Average Covered Charges", "string", "Average Covered Charges", "string"),
        ("Average Total Payments", "string", "Average Total Payments", "string"),
        ("Average Medicare Payments", "string", "Average Medicare Payments", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=ApplyMapping_node2,
    connection_type="s3",
    format="csv",
    connection_options={"path": "s3://etl-target-1/", "partitionKeys": []},
    transformation_ctx="S3bucket_node3",
)

job.commit()