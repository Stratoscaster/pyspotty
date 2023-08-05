import socketserver
from http.server import SimpleHTTPRequestHandler
from collections.abc import Callable
from functools import partial
from threading import Thread
from io import StringIO

class CallbackListener(SimpleHTTPRequestHandler):

    def __init__(self, path_callback: callable, *args, **kwargs):
        self.path_callback = path_callback
        self.callback_received = False
        super().__init__(*args, **kwargs)


    @staticmethod
    def start_server(path_callback: Callable, host: str, port: int):
        # Use partial to partially init CallbackListener with our callback function(str) and port
        # Huge shoutout to that one guy who suggested it on Stack Overflow [https://stackoverflow.com/a/58217918/16472278] jfc
        CallbackHandler = partial(CallbackListener, path_callback)

        server_thread = Thread(target=CallbackListener.start_server_instance, args=(CallbackHandler, host, port))
        server_thread.start()

    @staticmethod
    def start_server_instance(tcp_server, host: str, port: int):
        with socketserver.TCPServer((host, port), tcp_server) as httpd:
            httpd.serve_forever()

    def do_GET(self):
        self.callback_received = True

        page_content = self.send_head()
        if page_content:
            self.wfile.write(page_content)
        else:
            print('CallbackListener (non-fatal error): invalid content in self.send_head(). '
                  '\n Please close your browser tab after clicking "login". Login was successful.')

        # Pass itself and the path back to the main program to shut the server down
        # once the path is verified
        self.path_callback(self, self.path)

    def log_message(self, *args):
        # Mute the built-in logger
        pass

    def stop_server(self):
        print('Stopping Server...')
        self.server.shutdown()
        self.server.server_close()

    def send_head(self):
        body = '<html><b>Authentication complete. Please return to pyspotty to continue.</b></html>'.encode('utf-8')
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        return body
