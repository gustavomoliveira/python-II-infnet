from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import ssl # confiando no site e ignorando a certificação. necessário para macos

URL = 'https://www.tiobe.com/tiobe-index/'

def acessar_url():
    try:
        contexto_ssl = ssl._create_unverified_context() # necessário para macos
        html = urlopen(URL, context=contexto_ssl) # necessário para macos
    except Exception as ex:
        print(ex)
        exit()
    return html

def exibir_cabecalho(bs):    
    print(bs.h1.text)

def obter_tabela(bs):
    tabela_html = bs.find('table', id='top20')
    return tabela_html

def converter_tabela(tabela_html):
    df = pd.read_html(str(tabela_html))[0]
    return df

def limpar_df(df):
    df.drop('Change', axis=1, inplace=True) # alterando o df original
    df.drop('Programming Language', axis=1, inplace=True)
    df.rename(columns={'Programming Language.1': 'Language'}, inplace=True)
    df.rename(columns={'Change.1': 'Change'}, inplace=True)
    df[['Ratings', 'Change']] = df[['Ratings', 'Change']].replace('%', '', regex=True).astype(float)
    return df

def exibir_numero_linguagens(df):
    print('\nNúmero de Linguagens:', df.shape[0]) # shape pega o número de linhas da tabela

def exibir_linguagem_mais_usada(df):
    print('\nLinguagem mais usada:')
    print(df[df['Ratings'] == df['Ratings'].max()].to_string(index=False)) # linguagem mais usada, sem o index

def exibir_linguagem_menos_usada(df):
    print('\nLinguagem menos usada:')
    print(df[df['Ratings'] == df['Ratings'].min()].to_string(index=False)) # linguagem menos usada, sem o index

def linguagens_subiram(df):
    print('\nLinguagens que aumentaram em popularidade:')
    df_subiram = df[df['Mar 2025'] < df['Mar 2024']].to_string(index=False)
    print(df_subiram)

def top_5_linguagens(df_original):
    print('\nTop 5 Linguagens que mais subiram no ranking:')
    df = df_original.copy() # copiando o df original
    df['Diferenca'] = (df['Mar 2024'] - df['Mar 2025'])
    df = df.sort_values(by=['Diferenca'], ascending=False).head(5) # ordenando pela coluna Diferença usando pandas
    print(df[['Language', 'Diferenca']].to_string(index=False))

html = acessar_url()
bs = BeautifulSoup(html, 'html.parser')
tabela_html = obter_tabela(bs)
df = converter_tabela(tabela_html)
df = limpar_df(df)

exibir_cabecalho(bs)
exibir_numero_linguagens(df)
exibir_linguagem_mais_usada(df)
exibir_linguagem_menos_usada(df)
linguagens_subiram(df)
top_5_linguagens(df)