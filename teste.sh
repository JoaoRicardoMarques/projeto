#!/bin/bash

# Nome do arquivo que conterá o bytecode hexadecimal
BYTECODE_FILE="bytecode.hex"

# Bytecode hexadecimal que você deseja descompilar
BYTECODE="608060405234801561001057600080fd5b5060405161012838038061012883398101604090815281516020909201918252602080832090920151916040518083038186803b15801561004b57600080fd5b505af115801561005f573d6000803e3d6000fd5b5050505061011a806100706000396000f3fe6080604052600080fdfea264697066735822122004bcc6f0005ec3dfe4d2b9d96a6d37e5e8a7eec1e7030b29c1cb1609e83e91e364736f6c63430008010033"

# Cria o arquivo e insere o bytecode hexadecimal
echo $BYTECODE > $BYTECODE_FILE

# Verifica se o evm está instalado
if ! command -v evm &> /dev/null
then
    echo "evm could not be found. Please install it to proceed."
    exit 1
fi

# Descompila o bytecode usando evm disasm
DISASSEMBLY=$(evm disasm < $BYTECODE_FILE)

# Verifica se a descompilação foi bem-sucedida
if [ $? -ne 0 ]; then
    echo "Error disassembling bytecode."
    exit 1
fi

# Exibe o resultado da descompilação
echo "Disassembled Bytecode:"
echo "$DISASSEMBLY"
