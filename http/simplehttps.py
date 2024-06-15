import http.server
import ssl
from io import BytesIO


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        print(post_data.decode("utf-8"))

        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b"This is POST request. ")
        response.write(b"Received: ")
        response.write(post_data)
        self.wfile.write(response.getvalue())

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, https world!")


server_address = ("localhost", 5000)
httpd = http.server.HTTPServer(server_address, MyHandler)

ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ctx.load_cert_chain(certfile="./public.pem", keyfile="./private.pem")
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)

httpd.serve_forever()
