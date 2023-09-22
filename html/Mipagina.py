from functools import cached_property
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse
import re 

class WebRequestHandler(BaseHTTPRequestHandler):
    @cached_property
    def url(self):
        return urlparse(self.path)

    def do_GET(self):
        book_list = re.findall(r'^/Book/(\d+)$', self.url.path)
        if book_list:
            if book_list[0] in books:
                self.get_book( book_list[0])
                return 
            else:
                    print("Not Found")
                    self.error_message_format = "Does not compute!"
                    self.send_error(self, 404, "Not Found") 
        else:
                print("Not Found")
                self.send_error( 404, "Not Found") 

    def get_book(self, book_id):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        response = f"""
         {books[book_id]}
    <p>  Ruta: {self.path}            </p>
    <p>  URL: {self.url}              </p>
    <p>  HEADERS: {self.headers}      </p>
"""
        self.wfile.write(response.encode("utf-8"))

    def get_response(self, book_id):
        return f"""
         {books[book_id]}
    <p>  Ruta: {self.path}         </p>
    <p>  URL: {self.url}         </p>
    <p>  HEADERS: {self.headers}      </p>
"""


books = {
            '1': "\books\book1.html", 
            '2': "\books\book2.html", 
            '3':"\books\book3.html", 
            '4':"\books\book4.html",
            '5':"\books\book5.html",
            '6':"\books\book6.html",
        }

if __name__ == "__main__":
    print("Server starting...")
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
    server.serve_forever()
