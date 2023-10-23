import http.server
import socketserver

# Define the port on which the server will listen.
PORT = 8000

# Define the request handler. This will process incoming requests and
# provide responses. In this case, we're using the simple HTTP request
# handler provided by Python's http.server module.
Handler = http.server.SimpleHTTPRequestHandler

# Create a TCP server instance. This will start a server that listens for
# incoming TCP connections on the specified port. When a connection is
# established, it will use the specified handler to process requests.
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    # This command actually starts the server. It will run forever, waiting
    # for connections and serving files.
    httpd.serve_forever()
