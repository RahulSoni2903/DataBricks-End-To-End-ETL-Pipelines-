import dlt 

# Expectatoin Of Branch Tables 
branch_rule  = {
    "rule1": "BranchID IS NOT NULL"
}


@dlt.table (
    name  = "Branch_Stg"
)   

@dlt.expect_all_or_fail(branch_rule)

def Branch_Stg():
    return spark.readStream.table("altrahul.rschema.branches")
