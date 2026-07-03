import dlt 

@dlt.table(
    name = "DimLoan"
)

def FactTransaction():

    df = spark.readStream.table("workspace.destination.loan_transformation")
    return df 
