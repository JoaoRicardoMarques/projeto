import subprocess
import duckdb


def writer(arquivo, imput):
    with open(arquivo, 'w') as file:
        file.write(imput)

def disassembly(arquivo):
    try:
        result = subprocess.run(['evm', 'disasm', arquivo], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error disassembling bytecode: {result.stderr}")
        else:
            print("Disassembled Bytecode:")
            print(result.stdout)
    except FileNotFoundError:
        print("Error: `evm` command not found. Please install it to proceed.")

if __name__ == "__main__":
    ##DuckPath='~/UTFPR-IC/Config/Data_Base_ETH'
    ##con=duckdb.connect(database=DuckPath, read_only=False)

    arquivo = 'bytecode.asm'
    imput = (
        "608060405234801561001057600080fd5b5060405161012838038061012883398101604090815281516020909201918252602080832090920151916040518083038186803b15801561004b57600080fd5b505af115801561005f573d6000803e3d6000fd5b5050505061011a806100706000396000f3fe6080604052600080fdfea264697066735822122004bcc6f0005ec3dfe4d2b9d96a6d37e5e8a7eec1e7030b29c1cb1609e83e91e364736f6c63430008010033"
    )

    writer(arquivo, imput )
    disassembly(arquivo)