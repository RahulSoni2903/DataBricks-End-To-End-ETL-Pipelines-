import dlt 

@dlt.table(
    name = "FactTransaction"
)
def FactTransaction():
    df = spark.readStream.table("workspace.destination.transaction_tr")
    df_cust = spark.read.table("workspace.destination.dimaccount")
    df_loan = spark.read.table("workspace.destination.dimloan")
    df_join = df.join(
        df_cust,
        on="AccountID",
        how="left"
    )
    df_joinn = df_join.join(
        df_loan,
        on="CustomerID",
        how="left"
    )

    df_select = df_joinn.select(
        "TransactionID",
        "AccountID",
        "CustomerID",
        "LoanID",
        "TransactionType",
        "Amount",
        "TransactionDate",
    )

    return df_select

    
