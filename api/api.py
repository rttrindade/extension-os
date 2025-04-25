import google.generativeai as geneai
from api_key import GOOGLE_GEMINI_API_KEY
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

geneai.configure(api_key=GOOGLE_GEMINI_API_KEY)

# testando modelos

# for m in geneai.list_models():
#    if 'generateContent' in m.supported_generation_methods:
#        print(m.name)


# parte que importa a IA
# model = geneai.GenerativeModel("gemini-1.5-pro-latest")

# response = model.generate_content(
#    'olá chat, boa tarde. Este é o meu primeiro teste')
# print(response.text)

# Bloco da api que gera o servidor

class GeradorDeOs(BaseHTTPRequestHandler):
    def do_POST(self):
        conteudo_length = int(self.headers['Conteudo-Lenght'])
        post_data = self.rfile.read(conteudo_length)

        try:
            msg = json.loads(post_data.decode('utf-8'))
            print('Recebido:', msg)

            # resposta da IA
            resposta = {"mensagem": f"Recebi seu texto: {msg['texto']}"}
            self.send_response(200)
        except Exception as e:
            resposta = {"erro": str(e)}
            self.send_response(400)

        self.send_header("Conteudo-Lenght", "application/json")
        self.end_headers()
        self.wfile.write(json.dump(resposta).encode('utf-8'))


host = 'localhost'
porta = 8000

servidor = HTTPServer((host, porta), GeradorDeOs)
print(f"Servidor rodando em http://{host}:{porta}")
servidor.serve_forever()
