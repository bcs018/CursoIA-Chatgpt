# Categoriza os produtos

from openai import OpenAI 
from dotenv import load_dotenv 
import os 

# Ler todas as chaves de acessos do .env
load_dotenv()

# Criar obj para acessar a openia com a chave de acesso que esta em .env
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

modelo = 'gpt-4'

prompt_sistema = """
    Você é um categorizador de produtos.
    Você deve assumir as categorias presentes na lista abaixo.

    # Lista de Categorias Válidas
        - Moda Sustentável
        - Produtos para o Lar
        - Beleza Natural
        - Eletrônicos Verdes
        - Higiene Pessoal

    # Formato da Saída
    Produto: Nome do Produto
    Categoria: apresente a categoria do produto

    # Exemplo de Saída
    Produto: Escova elétrica com recarga solar
    Categoria: Eletrônicos Verdes
"""

prompt_usuario = input("Apresente o nome de um produto: ")

resposta = cliente.chat.completions.create(
    messages=[
        {
            # Formata a resposta do sistema, no caso ele só ira apresentar os nome produtos sem descrição
            "role"    : "system",
            "content" : prompt_sistema
        },
        {
            # Pedido do usuario
            "role"    : "user",
            "content" : prompt_usuario
        }
    ],
    # Modelo do AI
    model=modelo,
    # Temperatura (o quao criativa vai ser a resposta)
    temperature = 0,
    # Numero max de tokens nessa resposta
    max_tokens = 200,
    # Quantidade de respostas (deixar sem esse parametro para retornar uma resposta)
    n=1
)

# pega todas as 3 respostas da api
# for contador in range(0,3):
#    print(resposta.choices[contador].message.content)

print(resposta.choices[0].message.content)
