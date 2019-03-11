from app import  app

class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        ver = "%s"%(222)
        path = "/static"+path+"?ver="+ver
        return UrlManager.buildUrl( path )