import socketserver
from http.server import SimpleHTTPRequestHandler


class CallbackListener(SimpleHTTPRequestHandler):

    def __init__(self, client_address=None, server=None):
        super().__init__(self)
        self.HOST = 'localhost'
        self.PORT = callback_port
        self.address = (self.HOST, self.PORT)
        self.callback_received = False


# MAY NEED TO SEPARATE HANDLER FROM THE CALLBACK LISTENER
    def start(self):
        with socketserver.TCPServer(self.address, CallbackListener) as httpd:
            print('Listening for callback...')
            httpd.serve_forever()

    def do_GET(self):
        print('Callback POST Received. Path: ' + self.path)
        self.callback_received = True
        self.headers.items()
        self.send_response(200)
        return SimpleHTTPRequestHandler.do_GET(self)

    def get_path(self):
        return self.path

    def stop_server(self):
        self.server.shutdown()


class ListenerHandler():


