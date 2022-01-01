from Server import Server
import cherrypy

if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    cherrypy.quickstart(Server())
