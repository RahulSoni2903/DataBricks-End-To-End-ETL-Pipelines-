import dlt 

# Transaction Table Expectation 
transactionrule = {
    "rule1": "TransactionID IS NOT NULL",
    "rule2": "AccountID IS NOT NULL",
    "rule3": "Amount > 0",
}

@dlt.table(
    name = "Transaction_Stg"
)

@dlt.expect_all_or_fail(transactionrule)

def Transaction_Stg():
    return spark.readStream.table("altrahul.rschema.transactions")


