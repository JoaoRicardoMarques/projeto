#!/bin/bash
echo "Insira os Blocos que deseja extrair:"
echo 

#bloco inicial
echo "Initial Block"
read Initial_Block
echo

#bloco final
echo "Final Block"
read Final_Block
echo

#Max-Workers
Max_Workers=1

#Batch_Size
Batch_Size=1

#Qntd de Arquivos
echo "Quantidade de arquivos"
read Qntd_Arquivos
echo

#Primeira API Key
First_ApiKey='f6d071a0f26248eebc05effccad66a5f'
#Segunda API Key
Second_ApiKey='a1396b66469549e8af981d99a0316269'
#Terceira API Key
Trird_ApiKey='447e39ff833043d8a2068ee4b4e45738'
#Quarta API Key
Fourth_ApiKey='4e1694b0b9ad4f19a414df6774617d3f'

for ((i=1; i<=Qntd_Arquivos; i++)) do

    if [ $i -le 5 ]; then

        #extraindo dados da rede ethereum com a Primeira API Key
        ethereumetl export_blocks_and_transactions --start-block $Initial_Block --end-block $Final_Block \
        --max-workers $Max_Workers --batch-size $Batch_Size\
        --provider-uri https://mainnet.infura.io/v3/$First_ApiKey \
        --blocks-output blocks-$Initial_Block-$Final_Block.csv \
        --transactions-output transactions-$Initial_Block-$Final_Block.csv

        mv ~/blocks-$Initial_Block-$Final_Block.csv ~/UTFPR-IC/Data_Extract/Blocks
        mv ~/transactions-$Initial_Block-$Final_Block.csv ~/UTFPR-IC/Data_Extract/Transactions
    
        Initial_Block=$((Initial_Block+10000))
        Final_Block=$((Final_Block+10000))
    fi 

    if [ $i -gt 5 ] && [ $i -le 10 ]; then

        #extraindo dados da rede ethereum com a Segunda API Key
        ethereumetl export_blocks_and_transactions --start-block $Initial_Block --end-block $Final_Block \
        --max-workers $Max_Workers --batch-size $Batch_Size\
        --provider-uri https://mainnet.infura.io/v3/$Second_ApiKey \
        --blocks-output blocks-$Initial_Block-$Final_Block.csv \
        --transactions-output transactions-$Initial_Block-$Final_Block.csv

        mv ~/home/joao/UTFPR-IC/Scripts/blocks-$Initial_Block-$Final_Block.csv ~/home/joao/UTFPR-IC/Data_Extract/Blocks
        mv ~/home/joao/UTFPR-IC/Scripts/transactions-$Initial_Block-$Final_Block.csv ~/home/joao/UTFPR-IC/Data_Extract/Transactions
    
        Initial_Block=$((Initial_Block+10000))
        Final_Block=$((Final_Block+10000))
    fi

    if [ $i -gt 10 ] && [ $i -le 15 ]; then

        #extraindo dados da rede ethereum com a Terceira API Key
        ethereumetl export_blocks_and_transactions --start-block $Initial_Block --end-block $Final_Block \
        --max-workers $Max_Workers --batch-size $Batch_Size\
        --provider-uri https://mainnet.infura.io/v3/$Trird_ApiKey \
        --blocks-output blocks-$Initial_Block-$Final_Block.csv \
        --transactions-output transactions-$Initial_Block-$Final_Block.csv

        mv ~/blocks-$Initial_Block-$Final_Block.csv ~/home/joao/UTFPR-IC/Data_Extract/Blocks
        mv ~/transactions-$Initial_Block-$Final_Block.csv ~/home/joao/UTFPR-IC/Data_Extract/Transactions
    
        Initial_Block=$((Initial_Block+10000))
        Final_Block=$((Final_Block+10000))
    fi

    if [ $i -gt 10 ] && [ $i -le 15 ]; then

        #extraindo dados da rede ethereum com a Quarta API Key
        ethereumetl export_blocks_and_transactions --start-block $Initial_Block --end-block $Final_Block \
        --max-workers $Max_Workers --batch-size $Batch_Size\
        --provider-uri https://mainnet.infura.io/v3/$Fourth_ApiKey \
        --blocks-output blocks-$Initial_Block-$Final_Block.csv \
        --transactions-output transactions-$Initial_Block-$Final_Block.csv

        mv ~/blocks-$Initial_Block-$Final_Block.csv ~/home/joao/UTFPR-IC/Data_Extract/Blocks
        mv ~/transactions-$Initial_Block-$Final_Block.csv ~/home/joao/UTFPR-IC/Data_Extract/Transactions
    
        Initial_Block=$((Initial_Block+10000))
        Final_Block=$((Final_Block+10000))
    fi
done