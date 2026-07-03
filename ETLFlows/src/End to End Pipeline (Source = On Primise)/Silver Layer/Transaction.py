import dlt 
from pyspark.sql.functions import * 
from pyspark.sql.types import *

@dlt.view(
    name  = "Transaction_View"
)

def Transaction_View():

    df = spark.readStream.table("workspace.destination.Transaction_Stg")
    df = df.withColumn("Amount",col("Amount").cast(IntegerType()))
    return df 

dlt.create_streaming_table(
    name = "Transaction_Tr"
)


dlt.create_auto_cdc_flow(
    target="Transaction_Tr",
    source="Transaction_View",
    keys=["TransactionID"],
    sequence_by=col("__START_AT"),
    stored_as_scd_type=1,
    except_column_list=["__START_AT", "__END_AT"]
)
