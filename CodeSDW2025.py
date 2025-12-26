## ETL - Extract, Transform, Load com Python

import pandas as pd

df = pd.read_csv('SDW2025.CSV')
user_ids = df['UserID'].tolist()
print(user_ids)

## Extract o arquivo JSON com os dados dos usuários, pois a API está indisponível. 

import json

with open('Mock.json', 'r', encoding='utf-8') as f:
    all_users = json.load(f)

users = [user for user in all_users if user["id"] in user_ids]
print(json.dumps(users, indent=2, ensure_ascii=False))

## Install e importe a biblioteca OpenAI para Python.
!pip install openai

## Pega a chave da API do OpenAI de forma segura.
openai_api_key = 'A variável foi censurada por motivos de segurança'

## Chama a API do OpenAI para gerar uma mensagem personalizada para cada usuário.
from openai import OpenAI

client = OpenAI(api_key=openai_api_key)

def generate_ai_news(user):
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {
          "role": "system",
          "content": "Você é um especialista em markting bancário."
      },
      {
          "role": "user",
          "content":(
              f"A mensagem deve começar com o nome {user['name']}"
              f"Crie uma mensagem breve sobre as vantagens de criar uma conta banco"
              f"máximo de 100 caracteres"
          )
      }
    ]
  )
  return response.choices[0].message.content.strip('"')

for user in users:
  news = generate_ai_news(user)
  print(news)
  ## Adiciona a notícia gerada ao perfil do usuário. O link foi fornecido nos vídeos ensinando o desafio.
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })

## Salva os dados atualizados em um novo arquivo JSON, pois a API de atualização está indisponível.
import json

def update_user (user, filename = 'mock_completed.json'):
  try:
    with open(filename, 'w', encoding='utf-8') as f:
      json.dump(user, f, ensure_ascii=False, indent=2)
    return True
  except:
    return False

### Atualiza os dados dos usuários no arquivo JSON e gera um relatório de sucesso.
success = update_user(users)
for user in users:
  print(f"User {user['name']} updated? {success}!")

