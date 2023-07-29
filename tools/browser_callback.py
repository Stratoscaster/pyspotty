import socketserver
from http.server import SimpleHTTPRequestHandler


class CallbackListener(SimpleHTTPRequestHandler):

    def __init__(self, callback_address=None):
        super().__init__(self)
        if callback_address is not None and len(callback_address) != 2:
            print(f'Callback host address given invalid: {callback_address}. '
                  f'\nMust be tuple (address, port) - either may be null.'
                  f'\nFalling back to default (localhost:8069).')
        self.HOST = 'localhost' if callback_address is None else callback_address[0]
        self.PORT = 8069 if callback_address is None else callback_address[1]
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

