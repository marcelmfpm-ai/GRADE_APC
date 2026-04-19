import http.server
import socketserver
import webbrowser
import os

PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))

os.chdir(DIR)

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    url = f"http://localhost:{PORT}/index.html"
    print(f"Servidor rodando em: {url}")
    print("Pressione Ctrl+C para parar.")
    webbrowser.open(url)
    httpd.serve_forever()
