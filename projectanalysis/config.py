import api_devs
path = "http://localhost"
port = 8080
context = "api/test"
devs_endpoints = api_devs.setPath(path,port,context,"developpeurs")
equipes_endpoints =  api_devs.setPath(path,port,context,"equipes")
projets_endpoints =  api_devs.setPath(path,port,context,"projets")
print(devs_endpoints)