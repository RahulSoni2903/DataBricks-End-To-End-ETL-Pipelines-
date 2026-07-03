import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="DimCustomer",
    table_properties={"skipChangeCommits": "true"}
)
def DimCustomer():
    df = spark.readStream.table("workspace.destination.customer_transformation")
    return df
