import http.server
import socketserver
import re

# Definir un mapeo de rutas a controladores
route_handlers = {
    r'/books/1': 'El Cerebro de Silicio',
    r'/books/2': 'Superinteligencia',
    r'/books/3': 'Machine Learning: A Probabilistic Perspective',
    r'/books/4': 'AI: A Very Short Introduction',
    r'/books/5': 'Deep Learning',
    r'/books/6': 'Revolución de la Inteligencia Artificial',
}

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Verificar si la ruta solicitada coincide con una ruta definida
        for pattern, title in route_handlers.items():
            if re.match(pattern, self.path):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(f"<html><head><title>{title}</title></head><body><h1>{title}</h1></body></html>", 'utf-8'))
                return

        # Si la ruta no coincide con ninguna ruta definida, servir el archivo estático
        return super().do_GET()

# Configurar el servidor
port = 8000  # Cambiamos el puerto a 8000
with socketserver.TCPServer(("", port), MyHandler) as httpd:
    print(f"Servidor web en el puerto {port}")
    httpd.serve_forever()
