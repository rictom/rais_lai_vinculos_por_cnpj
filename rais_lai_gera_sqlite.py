# -*- coding: utf-8 -*-
"""
Created on Thu Sep 4 21:13:44 2025

@author: ricar
"""

import pandas as pd, os, sys, glob, contextlib, sqlite3, time, zipfile
#import sqlalchemy


#%%
arquivosZip = sorted(list( glob.glob('zip/RAIS*.zip')))
print('relação de arquivos:')
print(arquivosZip)

url_download = 'https://www.mediafire.com/folder/cgw7bxi0e53gb/rais_lai'
if not len(arquivosZip):
    print('Os arquivos com as tabelas devem ser baixadas de ' + url_download + ' e copiadas na pasta zip deste projeto.')
    sys.exit()
#%%

camdb = 'rais_lai.db'
if os.path.exists(camdb):
    print('o arquivo ' + camdb + ' já existe. Apague e rode o script novamente.')
    sys.exit()
#con = sqlalchemy.create_engine(f"sqlite:///{cam}")
colunas = ['ano', 'cnpj_raiz', 'cnpj_cei', 'cei_vinculado', 'uf', 'qtd_vinculos_ativos']
for k, arqzip in enumerate(arquivosZip):
    print(time.asctime(), 'Carregando ' + arqzip)
    with contextlib.closing(sqlite3.connect(camdb)) as con, con: #autocommit e autoclose
        try:
            df = pd.read_csv(arqzip, sep=';', encoding='latin1', dtype=str)
        except:
            with zipfile.ZipFile(arqzip, 'r') as z:
                arquivoNoZip = [n for n in z.namelist() if n.endswith('.txt')][0]
                with z.open(arquivoNoZip) as csv_file:
                    df = pd.read_csv(csv_file, sep=';', encoding='latin1', dtype=str)
        df.columns = [c.lower().replace(' / ','_').replace(' ','_').replace('í','i') for c in df.columns]
        if colunas != [x for x in df.columns]:
            print('colunas diferentes do padrão:')
            print(df.columns)
            if '2020' in arqzip:
                if 'ano' not in df.columns:
                    df.insert(0,'ano','2020')
            if '2019' in arqzip:
                df.drop('ano', axis=1, inplace=True)
                df.insert(0,'ano','2019')
        df.columns = [x for x in colunas]
        df.to_sql('rais', con, index=None, if_exists='append')
print(time.asctime(), 'Carregou arquivos em ' + camdb)

#%%
sqls= '''
    ALTER TABLE rais ADD COLUMN qte INTEGER;
    update RAIS
    set qte = cast( qtd_vinculos_ativos as INTEGER);
    --ALTER TABLE rais DROP COLUMN qte_vinculos_ativos;
    update rais
    set cnpj_raiz = SUBSTR('00000000'|| trim(cnpj_raiz), -8, 8);
    update rais
    set cnpj_cei = SUBSTR('00000000000000'|| trim(cnpj_cei), -14, 14);
'''
print(time.asctime(), 'Ajustando colunas da tabela, colocando zeros à esquerda no cnpj_raiz e código ceis...')
with contextlib.closing(sqlite3.connect(camdb)) as con, con: #autocommit e autoclose
    con.executescript(sqls)

#%%
sqls = '''
create table rais_anocnpj AS --está supondo que a coluna cnpj_cei só tem cnpj, o que pode estar errado. Mas como o objetivo é cruzar com cnpj, não há problema
select ano, cnpj_cei as cnpj, count(*) as registros, sum(qte) as qte_total 
from rais 
group by ano, cnpj_cei;
CREATE INDEX "idx_rais_cnpj" ON "rais_anocnpj" ("cnpj");
'''
print(time.asctime(), 'Criando qte de vínculos por ano e cnpj (cnpj_cei)...')
with contextlib.closing(sqlite3.connect(camdb)) as con, con: #autocommit e autoclose
    con.executescript(sqls)

#%%   
print(time.asctime(), 'Fim! O arquivo ' + camdb + ' foi criado. Este é um banco de dados no formato sqlite. Pode ser aberto no DBBrowser for SQLITE')

print('A tabela rais contém o contéudo dos arquivos txts (csvs)')
print('A tabela rais_anocnpj contém a quantidade de vínculos ativos por cnpj e por ano. Observe que a coluna pode ter o código cei ao invés de cnpj.')
