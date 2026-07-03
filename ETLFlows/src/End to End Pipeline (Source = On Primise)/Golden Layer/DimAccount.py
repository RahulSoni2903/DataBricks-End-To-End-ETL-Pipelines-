import dlt
from pyspark.sql.functions import row_number
from pyspark.sql.window import Window

@dlt.table(
    name="DimAccount"
)

def DimAccount():

    df = spark.readStream.table("workspace.destination.account_transformation")
    return df


