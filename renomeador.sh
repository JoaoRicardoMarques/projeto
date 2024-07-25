echo 
echo "Quantidade de Arquivos a serem analisados:"
echo
read Qntd_Arquivos

for
    rename 's/00(\d+)-00(\d+)/$1-$2/' transactions-of-blocks-*.csv