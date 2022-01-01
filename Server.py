import cherrypy
import RepositoryInfoService
import Constant
from GithubApiException import GithubApiException
class Server(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self , username):
        try:
            repositoryList = RepositoryInfoService.getRepositoryList(username)
        except GithubApiException as e:
            cherrypy.log(Constant.GITHUB_API_ERROR_MSG, traceback=True)
            raise cherrypy.HTTPError(e.responseCode)
        except BaseException as e:
            cherrypy.log(Constant.INTERNAL_SERVER_ERROR_MSG, traceback=True)
            raise e
        result = [{'name' : repo.name , 'stars':repo.stars } for repo in repositoryList]
        return result

    @cherrypy.expose
    def stars(self , username):
        try:
            repositoryList = RepositoryInfoService.getRepositoryList(username)
            result = RepositoryInfoService.sumStars(repositoryList)
        except GithubApiException as e:
            cherrypy.log(Constant.GITHUB_API_ERROR_MSG, traceback=True)
            raise cherrypy.HTTPError(e.responseCode)
        except BaseException as e:
            cherrypy.log(Constant.INTERNAL_SERVER_ERROR_MSG, traceback=True)
            raise e
        return str(result)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def languages(self , username):
        try:
            result = RepositoryInfoService.getLanguagesInfo(username)
        except GithubApiException as e:
            cherrypy.log(Constant.GITHUB_API_ERROR_MSG, traceback=True)
            raise cherrypy.HTTPError(e.responseCode)
        except BaseException as e:
            cherrypy.log(Constant.INTERNAL_SERVER_ERROR_MSG, traceback=True)
            raise e
        return result