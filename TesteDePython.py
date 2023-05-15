#Teste feito por Murilo Vieira Pizzamiglio

from http.server import BaseHTTPRequestHandler, HTTPServer

blist = []

with open("blacklist.txt", "r") as filetxt:
    lines = filetxt.readlines()

    for line in lines:
        blist.append(line.replace('\n', ''))

class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><link rel="icon" href="data:,"></head></html>', "utf8"))

        cpf = self.path
        
        cpf = cpf.replace("/", "")

        if cpf in blist:
            print("BLOCK")
            message = "BLOCK"
            self.wfile.write(bytes(message, "utf8"))
        elif cpf == '':
            print("RUNNING")
            message = "RUNNING"
            self.wfile.write(bytes(message, "utf8"))   
        else:
            print("FREE")
            message = "FREE"
            self.wfile.write(bytes(message, "utf8"))
    
server = HTTPServer(('', 5000), Request)
server.serve_forever()

