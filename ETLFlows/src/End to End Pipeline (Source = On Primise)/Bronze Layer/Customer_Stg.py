import dlt 

### Adding All Tables Expectation Basically It is One Types Of Constarint 
# ----------------- Customer Expectations ---------------------------
Customer_rule  = {
    "rule1": "customerID IS NOT NULL",
}

# Adding Staging Customer Table To Destination 
@dlt.table(
    name = "Customer_Stg"
)

@dlt.expect_all(Customer_rule)

def Customer_Stg():
    df =  spark.readStream.table("altrahul.rschema.customers")
    return df
