import dlt 
from pyspark.sql.functions import *
from pyspark.sql.types import *

@dlt.view(
    name = "Loan_View"
)
def Loan_View():
    df = spark.readStream.table("workspace.destination.Loan_Stg")
    df = df.withColumn("LoanAmount", col("LoanAmount").cast(IntegerType()))
    return df
    
dlt.create_streaming_table(
    name = "Loan_Transformation"
)

dlt.create_auto_cdc_flow(
    target="Loan_Transformation",
    source="Loan_View",
    keys=["LoanID"],
    sequence_by=col("__START_AT"),
    stored_as_scd_type=1,
    except_column_list=["__START_AT", "__END_AT"]
)