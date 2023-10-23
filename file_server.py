import http.server
import socketserver
import os
from urllib.parse import parse_qs

# Define the port on which the server will listen.
PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = '''
        <html>
        <body>
            <form method="POST">
                <input name="input_text" type="text" />
                <input type="submit" />
            </form>
        </body>
        </html>
        '''
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = "You submitted: {}".format(data.get('input_text')[0])
        self.wfile.write(bytes(response, "utf8"))
        return

# Create a TCP server instance. This will start a server that listens for
# incoming TCP connections on the specified port. When a connection is
# established, it will use the specified handler to process requests.
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    # This command actually starts the server. It will run forever, waiting
    # for connections and serving files.
    httpd.serve_forever()
