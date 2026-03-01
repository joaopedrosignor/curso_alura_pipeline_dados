from scripts.processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extract

dados_empresaA = Dados.leitura_dados(path_json, 'json')
print("Nome das colunas da empresa A:")
print(dados_empresaA.nome_colunas)
print("Quantidade de linhas da empresa A:")
print(dados_empresaA.qtd_linhas)

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print("Nome das colunas da empresa B:")
print(dados_empresaB.nome_colunas)
print("Quantidade de linhas da empresa B:")
print(dados_empresaB.qtd_linhas)

# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print("Nome das colunas da fusão:")
print(dados_fusao.nome_colunas)
print("Quantidade de linhas da fusão:")
print(dados_fusao.qtd_linhas)

#Load

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f"Dados combinados salvos em: {path_dados_combinados}")