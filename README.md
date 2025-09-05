# rais_lai_vinculos_por_cnpj
Script em python para converter dados públicos disponibilizados pelo Ministério da Economia por um pedido pela Lei de Acesso à Informação. Os arquivos disponibilizados contém quantidade de vínculos ativos (funcionários) por CNPJ, do período de 2010 a 2021. O resultado será um arquivo <b>rais_lai.db</b> no formato [SQLITE](https://pt.wikipedia.org/wiki/SQLite). A [RAIS](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/estatisticas-trabalho/o-pdet/o-que-e-rais) (Relação Anual de Informações Sociais) é um registro anual em que as empresas informam dados de seus funcionários para o Governo Federal. 

## Dados obtidos pela Lei de Acesso à Informação:
O pedido de informação que liberou os arquivos foi este: https://buscalai.cgu.gov.br/PedidosLai/DetalhePedido?id=4173393 . Os arquivos estavam disponíveis até outubro/2023 em https://drive.google.com/drive/folders/1pn2tW1-SjFmHXy6--qyzad0y_5rVPqC-?usp=sharing <br>
Existe um espelho desses arquivos em https://www.mediafire.com/folder/cgw7bxi0e53gb/rais_lai <br>


## Pré-requisitos:
Python 3.12 ou posterior;<br>
Bibliotecas pandas, sqlite3.<br><br>

## Procedimento:
- Faça um espelho desse repositório no seu computador (utilize o botão verde CODE e selecione download)<br>
- Baixe os arquivos em https://www.mediafire.com/folder/cgw7bxi0e53gb/rais_lai . Se não precisar de todos os períodos, selecione apenas os arquivos dos anos desejados.<br>
- Copie os arquivos do mediafire para a pasta zip.<br>
- Use o Anaconda prompt ou ative um ambiente virtual ( https://docs.python.org/pt-br/3/library/venv.html )<br>
- Rode o script pelo comando:<br>
python rais_lai_gera_sqlite.py<br>
- Ao final, será gerado um arquivo rais_lai.db, no formato sqlite, com cerca de 16GB, que poderá ser aberto no DB Browser for SQLITE (https://sqlitebrowser.org/).<br>
- O arquivo rais_lai.db conterá três tabelas:<br> 
a) _anos_registros: especificando a quantidade de registros (linhas) de cada ano;<br> 
b) rais: contendo os dados dos arquivos CSVs. <br>
c) rais_anocnpj: tabela com quantidade de vínculos por CNPJ (ou código CEI) e por ano.<br><br>

## Como obter dados mais recentes:
O Ministério do Trabalho e Emprego tem negado atualização dessas informações sob os seguintes argumentos:<br>
a) os dados foram obtidos pelo Órgão no exercício de supervisão de atividade econômica. A divulgação desses dados poderia representar vantagem competitiva a outros agentes econômicos. Por exemplo, uma empresa estrangeira hipotética "XXYYZZ Enterprise", sabendo a quantidade de funcionários que trabalham numa empresa nacional "BRAZUZU Alimentos", poderia inferir o método produtivo da empresa nacional e obter uma vantagem econômica.<br>
b) a partir da QUANTIDADE de funcionários de uma empresa, seria possível inferir QUAIS PESSOAS trabalham nesse local (!!!). <br>

Os argumentos para recusa são frágeis, por isso, se desejar atualização dos dados, recomendo utilizar a Lei de Acesso à Informação e fazer o seu pedido em https://falabr.cgu.gov.br/ , no botão "Faça um pedido de acesso à informação". Se o pedido for negado, recorra em cada instância... Se houver vários pedidos semelhantes, eventualmente a Administração vai atender à demanda.

## Histórico de versões

versão 0.1 (setembro/2025)
- primeira versão
