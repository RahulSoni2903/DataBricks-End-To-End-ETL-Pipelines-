import dlt 

@dlt.table(
    name = "DimBranch"
)

def FactTransaction():

    df = spark.readStream.table("workspace.destination.branch_transformation")
    return df 

