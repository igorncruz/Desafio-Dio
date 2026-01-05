import pandas as pd

# 0. SETUP: Criando um arquivo CSV de exemplo (apenas para teste)
# Em produção, este arquivo já existiria.
with open('UserID.csv', 'w') as f:
    f.write("UserID,Nome,Conta,Cartao\n1,Maria,0001,Silver\n2,João,0002,Gold\n3,Ana,0003,Platinum\n")

# --- INÍCIO DO ETL ---

# 1. EXTRACT: Leitura do arquivo (Ingestão de Dados)
# O pandas detecta automaticamente cabeçalhos e tipos de dados.
df = pd.read_csv('UserID.csv')

# 2. TRANSFORM: Lógica de Negócio (Enriquecimento)
# Utilizamos 'apply' para processar todas as linhas de forma vetorizada (escalável).
def generate_ai_msg(row):
    return f"💳 Olá {row['Nome']}! 💳 O seu cartão {row['Cartao']} tem ofertas novas. 💳"

df['Mensagem_IA'] = df.apply(generate_ai_msg, axis=1)

# 3. LOAD: Persistência (Escrita do Resultado)
# Salva o resultado processado em um novo arquivo, sem o índice numérico do Pandas.
df.to_csv('Processado.csv', index=False)

print("Processo concluído! Verifique o arquivo 'Processado.csv'.")