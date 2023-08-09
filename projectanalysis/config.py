import api_devs
path = "http://localhost"
port = 8080
context = "api"
membres_endpoints = api_devs.setPath(path,port,context,"utilisateurs")
equipes_endpoints =  api_devs.setPath(path,port,context,"equipes")
projets_endpoints =  api_devs.setPath(path,port,context,"projets")