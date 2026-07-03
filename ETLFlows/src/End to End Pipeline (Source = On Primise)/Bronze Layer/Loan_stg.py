import dlt 

# Loan Table Expectations

loan_rule = {
    "rule1": "LoanID IS NOT NULL",
    "rule2": "LoanAmount > 0",
    "rule3": "InterestRate > 0"
}

@dlt.table(
    name = "Loan_Stg"
)

@dlt.expect_all_or_fail(loan_rule)

def Loan_Stg():
    return spark.readStream.table("altrahul.rschema.loans")