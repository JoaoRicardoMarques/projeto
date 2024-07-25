import duckdb

def code(duckdb_path):
    con=duckdb.connect(database=duckdb_path,read_only=False)
    
    con.sql("DROP TABLE IF EXISTS code;")

    con.sql("CREATE TABLE code(id bigint PRIMARY KEY,hash VARCHAR,input VARCHAR);")

    con.close()

def code_instructions(duckdb_path):
    con=duckdb.connect(database=duckdb_path,read_only=False)

    con.sql("DROP TABLE IF EXISTS code_instructions")

    con.sql("CREATE TABLE code_instructions(id_code BIGINT PRIMARY KEY,id_instruction INT,FOREIGN KEY(id_code) REFERENCES code(id),FOREIGN KEY(id_instruction) REFERENCES instructions(id));")
    
    con.close()

if __name__ == "__main__":
    duckpath = "~/UTFPR-IC/Config/Dataset"
    code(duckpath)
    code_instructions(duckpath)