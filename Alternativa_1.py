# 1. EXTRACT: Fonte de dados manual (Substituindo a API)
# Simula a resposta que viria da API (List of Dictionaries)
users = [
    {"id": 1, "name": "Maria Silva", "account": "0001", "card": "Silver", "news": []},
    {"id": 2, "name": "João Santos", "account": "0002", "card": "Gold", "news": []},
    {"id": 3, "name": "Ana Costa", "account": "0003", "card": "Platinum", "news": []}
]

# 2. TRANSFORM: Geração de mensagens (Simulando a IA)
# Aqui entraria a chamada para a OpenAI. Para "Alternativa 1", usamos uma f-string.
def generate_ai_news(user):
    # Logic: Personalização baseada no tipo de cartão
    return f"💳 Olá {user['name']}! 💳 Aproveite os benefícios exclusivos do seu cartão {user['card']}. 💳"

for user in users:
    news_message = generate_ai_news(user)
    user['news'].append({
        "icon": "💳", 
        "description": news_message
    })

# 3. LOAD: Atualização/Saída dos dados
# Exibe o resultado final do pipeline
print(f"{'USER':<15} | {'GENERATED MESSAGE'}")
print("-" * 60)
for user in users:
    print(f"{user['name']:<15} | {user['news'][0]['description']}")