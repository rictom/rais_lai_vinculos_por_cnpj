# rais_lai_vinculos_por_cnpj
Script em python para converter dados públicos disponibilizados pelo Ministério da Economia por um pedido pela Lei de Acesso à Informação. Os arquivos disponibilizados contém quantidade de vínculos ativos (funcionários) por CNPJ, do período de <b>2010 a 2021</b>. O resultado será um arquivo <b>rais_lai.db</b> no formato [SQLITE](https://pt.wikipedia.org/wiki/SQLite). A [RAIS](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/estatisticas-trabalho/o-pdet/o-que-e-rais) (Relação Anual de Informações Sociais) é um registro anual em que as empresas informam dados de seus funcionários para o Governo Federal. 

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
- Ao final, será gerado um arquivo rais_lai.db, no formato sqlite, com cerca de 16GB, que poderá ser aberto no DB Browser for SQLITE (https://sqlitebrowser.org/). <br>
- O arquivo rais_lai.db conterá três tabelas:<br> 
a) _anos_registros: especificando a quantidade de registros (linhas) de cada ano;<br> 
b) rais: contendo os dados dos arquivos CSVs. <br>
c) rais_anocnpj: tabela com quantidade de vínculos por CNPJ (ou código CEI) e por ano.<br>
- Não utilize a aba "Navegar dados" do DB Browser, pois as tabelas são muito grandes (mais de 80 milhões de registros) e podem travar o programa. Use a aba "Executar SQL" e faça uma consulta como <i>SELECT * FROM rais_anocnpj WHERE ano='2020' LIMIT 1000</i><br>
- Para obter dados de empresas, como a Razão Social, utilize o projeto https://github.com/rictom/cnpj-sqlite . O SQLITE permite cruzar dados de arquivos separados pela opção [ATTACH](https://www.sqlite.org/lang_attach.html) ou pelo botão "Anexar banco de dados" no DBBrowser for SQLITE.<br>

## Como obter dados mais recentes:
O Ministério do Trabalho e Emprego tem negado atualização dessas informações sob os seguintes argumentos:<br>
a) os dados foram obtidos pelo Órgão no exercício de supervisão de atividade econômica. A divulgação desses dados poderia representar vantagem competitiva a outros agentes econômicos: <i>"...O MTE, em continuação à resposta acima, reiterou a sua preocupação à violação do sigilo empresarial das empresas que concedem informações de seus empregados e estabelecimentos por meio da RAIS. Isso, porque, o MTE entende que a disponibilização de informações públicas do número de empregados por estabelecimento empresarial poderia oferecer vantagens competitivas, inclusive, para situações de concorrência internacional com empresas não submetidas aos mesmos critérios de transparência. Estes concorrentes, advertiu, poderiam acessar informações do número de empregados utilizados para operar determinadas plantas produtivas, inclusive as que se caracterizem por utilizar processos inovadores, usando essa informação como subsídio para estratégicas competitivas e ferindo o direto ao sigilo empresarial sobre as suas operações e serviços..."</i> [(resposta da CGU)](https://buscaprecedentes.cgu.gov.br/?idAnexo=114068&idAws=AnexosRecurso%2F192351%2Fbfaa3bb4-ca6d-4790-b299-35ed08db8450&fileName=SEI_19955.0778262023-19_Parecer___Recurso_de_3%C2%AA_Instancia_148.pdf&handler=DownloadFile)<br>
b) a partir da QUANTIDADE de funcionários de uma empresa, seria possível inferir QUAIS PESSOAS trabalham nesse local (!!!), portanto haveria violação à [LGPD.](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)<br>

Os argumentos para recusa são criativos, por isso, se desejar atualização dos dados, recomendo utilizar a Lei de Acesso à Informação e fazer o seu pedido em https://falabr.cgu.gov.br/ , no botão "Faça um pedido de acesso à informação". Se o pedido for negado, recorra em cada instância... Se houver vários pedidos semelhantes, eventualmente a Administração vai atender à demanda.

## Histórico de versões

versão 0.1 (setembro/2025)
- primeira versão
