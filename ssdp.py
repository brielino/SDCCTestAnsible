from ssdpy import SSDPServer

server = SSDPServer("my-service-identifier")
server.serve_forever()
