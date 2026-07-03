import dlt 
from pyspark.sql.functions import *
from pyspark.sql.types import *

@dlt.view(
    name = "Branch_View"
)

def Branch_View():
  df = spark.readStream.table("workspace.destination.Branch_Stg")
  df = df.withColumn("ManagerName",coalesce(col("ManagerName"),lit("Director")))
  return df

dlt.create_streaming_table(
    name = "Branch_Transformation"
)

dlt.create_auto_cdc_flow(
    target="Branch_Transformation",
    source="Branch_View",
    keys=["BranchID"],
    sequence_by=col("__START_AT"),
    stored_as_scd_type=1,
    except_column_list=["__START_AT", "__END_AT"]
)
