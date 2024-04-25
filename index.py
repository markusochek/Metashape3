from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "localhost"
PORT = "3000"


class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html></html>"))


server = HTTPServer((HOST, PORT), NeuralHTTP)
print("RUN!!!")
