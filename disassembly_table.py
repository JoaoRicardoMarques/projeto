import os
import duckdb
import sys

def tabela_DTC(duckpatch,inputArquive,dtc_table):
    
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

    con=duckdb.connect(database=duckpatch,read_only=False)
    con.sql(f"DROP TABLE IF EXISTS {dtc_table}")
    con.sql(f"CREATE TABLE {dtc_table} ({A},{B},{C},{D},{E},{F},{G},{H},{I},{J},{K},{L},{M},{N},{O})")
    con.sql(f"COPY {dtc_table} FROM '{inputArquive}'")
    
    #cria a primeira table para a importação do arquivo base 


def table_disassembly(duckpatch):


    con=duckdb.connect(database=duckpatch,read_only=False)

    con.sql(f"DROP TABLE IF EXISTS HashInput")
    #cria a table para inserir a hash e input de cada tupla do arquivo base 
    con.sql(f"CREATE TABLE HashInput (hash varchar,input varchar)")
    
    con.execute(f"INSERT INTO HashInput VALUES ()")
    con.table(f"HashInput").show()


    
if __name__ == "__main__":
    #argumentos = sys.argv
    #valores = argumentos[1:]

    #Initial_Block=int(valores[0])
    #Final_Block=int(valores[1])

    duckpatch='~/UTFPR-IC/Config/Data_Base_ETH'
    dtc_table=f'dtc_table'

    inputArquive=f'~/UTFPR-IC/Data_Analysis/Deployment_Transactions_Contracts/DTC-60000-69999.csv'
    
    tabela_DTC(duckpatch,inputArquive,dtc_table)
    table_disassembly(duckpatch)
