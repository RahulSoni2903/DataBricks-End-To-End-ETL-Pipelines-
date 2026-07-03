import dlt
from pyspark.sql.functions import *

# Create View
@dlt.view(
    name="Customer_view"
)
def Customer_view():

    df = spark.readStream.table("workspace.destination.Customer_Stg")

    df = (
        df.withColumn("FirstName", trim(col("FirstName")))\
          .withColumn("LastName", trim(col("LastName")))\
          .withColumn(
              "Email",
              coalesce(
                  col("Email"),
                  concat(col("FirstName"), lit("@gmail.com"))
              )
          )\
          .withColumn("City", upper(col("City")))\
          .dropDuplicates(["customerID", "CreatedDate"])
    )

    return df


# Create Target Streaming Table
dlt.create_streaming_table(
    name="Customer_transformation"
)


# Apply SCD Type 1
dlt.create_auto_cdc_flow(
    target="Customer_transformation",
    source="Customer_view",
    keys=["customerID"],
    sequence_by=col("CreatedDate"),
    stored_as_scd_type=1,
    except_column_list=["__START_AT", "__END_AT"]
)