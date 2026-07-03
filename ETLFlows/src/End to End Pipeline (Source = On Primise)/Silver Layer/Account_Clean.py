import dlt 
from pyspark.sql.functions import *
from pyspark.sql.types import *

@dlt.view(
    name = "Account_View"
)

def Account_View():
  df = spark.readStream.table("workspace.destination.Account_Stg")
  df = df.withColumn("Balance",col("Balance").cast(IntegerType()))\
         .withColumn("Branch",coalesce(col("Branch"),lit("Central Branch")))
  return df 


dlt.create_streaming_table(
    name = "Account_Transformation"
)

dlt.create_auto_cdc_flow(
    target="Account_Transformation",
    source="Account_View",
    keys=["AccountID"],
    sequence_by=col("OpenDate"),
    stored_as_scd_type=1,
    except_column_list=["__START_AT", "__END_AT"]
)