from os import getcwd
from http.server import HTTPServer, BaseHTTPRequestHandler
from logging import getLogger
import urllib.request
import subprocess


class AgentServer(BaseHTTPRequestHandler):
    logger = getLogger(__name__)

    '''
    member of BaseHTTPRequestHandler class
    
    client_address = client's address (host, port)
    server = contain the server instance
    close_connection = boolean.
    requestline = HTTP request strings. NOT include CRLF.
    command = HTTP command(request type) for ex. 'GET'
    path = request path for ex. '/', '/test/hoge'
    request_version = request HTTP version strings 'HTTP/1.0'
    headers
    rfile = input file
    wfile = response file ex. 'index.html'
    '''


    # HTTP GET
    def do_GET(self):
        # HTTP status code 200
        self.send_response(200)

        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()

        print('client ip: ' + self.client_address[0])

        if self.path == '/download':
            file_name = 'agent.py'
            client_port = 8000
            # ex) url = "http://192.168.0.105/agent.py"
            url = "http://" + self.client_address[0] + ":" + str(client_port) + '/' + file_name
            print("download from: " + url)
            urllib.request.urlretrieve(url, file_name)
            print('file downloaded')
            agent = subprocess.Popen(['python3.7', file_name])
            self.wfile.write('downloaded'.encode('utf-8'))
            return

        elif self.path == '/launch':
            url = 'http://192.168.1.241:8000/download'
            command = "download"
            # url = "http://" + peer_ip[0] + "/" + command
            print(url)
            result = urllib.request.urlopen(url)
            if result == 'downloaded':
                print('a')
            return

        file_path = getcwd() + self.path
        print(file_path)

        with open(file_path, 'rb') as f:
            agent = f.read()
            self.wfile.write(agent)

    # HTTP POST
    def do_POST(self):
        print('http:', self.path)
        print(self.requestline)

    def set_app_port(self, port):
        self.app_port = port


class AgentPlatform:
    host_address = ''
    APP_DEFAULT_PORT = 8000

    host_port = APP_DEFAULT_PORT
    logger = None
    agent_server = None

    def __init__(self, *port):
        self.logger = getLogger(__name__)

        if port:
            self.host_port = port[0]

        self.agent_server = HTTPServer((self.host_address, self.host_port), AgentServer)
        # self.agent_server.set_app_port(self.APP_DEFAULT_PORT)

        print('AgentPlatform started by ' + str(self.host_port) + ' port.')

    def run(self):
        try:
            print('start listen HTTP Request')
            self.agent_server.serve_forever()
        except KeyboardInterrupt:
            pass

    def kill(self):
        self.agent_server.server_close()
        print('server closed')

    def get_server_port(self):
        return self.host_port

    def get_server_ip(self):
        return self.host_address


if __name__ == '__main__':
    ap = AgentPlatform()
    ap.run()
