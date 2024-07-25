import os
import duckdb
import sys

def Import(DuckPath, ImputArquive, Table):
    A='hash varchar'
    B='nonce bigint'
    C='block_hash varchar'
    D='block_number bigint'
    E='transaction_index bigint'
    F='from_address varchar'
    G='to_address varchar'
    H='value varchar'
    I='gas bigint'
    J='gas_price bigint'
    K='input varchar'
    L='block_timestamp bigint'
    M='max_fee_per_gas bigint'
    N='max_priority_fee_per_gas bigint'
    O='transaction_type bigint'

    
    
    con=duckdb.connect(database=DuckPath, read_only=False)
    con.sql(f"DROP TABLE IF EXISTS {Table}")
    
    con.sql(f"CREATE TABLE {Table}({A},{B},{C},{D},{E},{F},{G},{H},{I},{J},{K},{L},{M},{N},{O})")
    con.sql(f"COPY {Table} FROM '{ImputArquive}'")

    #con.table(f"{Table}").show()

def QueryEC(DuckPath, QueryArgumentEC, OutputArquiveEC):
    con=duckdb.connect(database=DuckPath, read_only=True)
    con.sql(f"{QueryArgumentEC}").write_csv(f"{OutputArquiveEC}")
    con.close()

def QueryDTC(DuckPath, QueryArgumentDTC, OutputArchiveDTC):
    con=duckdb.connect(database=DuckPath, read_only=True)
    con.sql(f"{QueryArgumentDTC}").write_csv(f"{OutputArchiveDTC}")
    con.close()

def QueryRTC(DuckPath, QueryArgumentRTC, OutputArquiveRTC):
    con=duckdb.connect(database=DuckPath, read_only=True)
    con.sql(f"{QueryArgumentRTC}").write_csv(f"{OutputArquiveRTC}")
    con.close()

def Drop(Table):
    con=duckdb.connect(database=DuckPath, read_only=False)
    con.sql(f"DROP TABLE {Table}")
    con.close()

if __name__ == "__main__":
    argumentos = sys.argv
    valores = argumentos[1:]

    Initial_Block=int(valores[0])
    Final_Block=int(valores[1])

    DuckPath='~/UTFPR-IC/Config/Data_Base_ETH'
    Table=f'transactions'

    ImputArquive=f'~/UTFPR-IC/Data_Extract/Transactions/transactions-of-blocks-{Initial_Block}-{Final_Block}.csv'
    
    OutputArquiveEC=f'~/UTFPR-IC/Data_Analysis/Execution_Contract/EC-{Initial_Block}-{Final_Block}.csv'
    QueryArgumentEC=f'SELECT * FROM transactions WHERE to_address=from_address'
   
    OutputArquiveDTC=f'~/UTFPR-IC/Data_Analysis/Deployment_Transactions_Contracts/DTC-{Initial_Block}-{Final_Block}.csv'
    QueryArgumentDTC=f'SELECT * FROM transactions WHERE to_address IS NULL'

    OutputArquiveRTC=f'~/UTFPR-IC/Data_Analysis/Regular_Transactions_Contracts/RTC-{Initial_Block}-{Final_Block}.csv'
    QueryArgumentRTC=f'SELECT * FROM transactions WHERE to_address!=from_address'

    Import(DuckPath, ImputArquive, Table)

    QueryEC(DuckPath, QueryArgumentEC, OutputArquiveEC)
    QueryDTC(DuckPath, QueryArgumentDTC, OutputArquiveDTC)
    QueryRTC(DuckPath, QueryArgumentRTC, OutputArquiveRTC)

    Drop(Table)
