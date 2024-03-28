from socketserver import StreamRequestHandler, TCPServer
from functools import partial


class EchoHandler(StreamRequestHandler):

    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT:' + line)


serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
serv.serve_forever()