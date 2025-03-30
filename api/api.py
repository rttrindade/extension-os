import google.generativeai as geneai
from api_key import GOOGLE_GEMINI_API_KEY

geneai.configure(api_key=GOOGLE_GEMINI_API_KEY)

# testando modelos

# for m in geneai.list_models():
#    if 'generateContent' in m.supported_generation_methods:
#        print(m.name)

model = geneai.GenerativeModel("gemini-1.5-pro-latest")

response = model.generate_content(
    'olá chat, boa tarde. Este é o meu primeiro teste')
print(response.text)
