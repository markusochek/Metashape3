from http.server import HTTPServer, SimpleHTTPRequestHandler
from io import BytesIO
from urllib import parse
from requests_toolbelt.multipart import decoder

# for part in multipart_data.parts:
#     print(part.content)  # Alternatively, part.text if you want unicode
#     print(part.headers)

HOST = "localhost"
PORT = 3000


class HTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        body = self.rfile.read(int(self.headers['Content-Length']))
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('qqqqq.jpg', 'wb') as f:
            f.write(body)

        # response = BytesIO()
        # response.write(b'This is POST request. ')
        # response.write(b'Received: ')
        # response.write(body)
        self.wfile.write('{ "response": "true" }'.encode())

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)


server = HTTPServer((HOST, PORT), HTTPRequestHandler)
server.serve_forever()
