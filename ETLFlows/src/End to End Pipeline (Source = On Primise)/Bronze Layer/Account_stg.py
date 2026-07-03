import dlt 

# Account Expectations 
Account_rule = {
    "rule1": "AccountID IS NOT NULL",
    "rule2": "Balance > 0",
    "rule3": "CustomerID IS NOT NULL"
}


@dlt.table(
    name = "Account_Stg"
)

@dlt.expect_all_or_drop(Account_rule)

def Account_Stg():
    return spark.readStream.table("altrahul.rschema.accounts")
