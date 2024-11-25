from openai import OpenAI 
from dotenv import load_dotenv 
import os 

# Ler todas as chaves de acessos do .env
load_dotenv()

# Criar obj para acessar a openia com a chave de acesso que esta em .env
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resposta = cliente.chat.completions.create(
    messages=[
        {
            # Formata a resposta do sistema, no caso ele só ira apresentar os nome produtos sem descrição
            "role"    : "system",
            "content" : "Listar apenas os nomes dos produtos, sem descrição"
        },
        {
            # Pedido do usuario
            "role"    : "user",
            "content" : "Liste 3 produtos sustentáveis"
        }
    ],
    # Modelo do AI
    model="gpt-4"
)

print(resposta.choices[0].message.content)