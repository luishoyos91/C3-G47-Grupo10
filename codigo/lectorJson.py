import json
file = open("estudiantes.json","r")
est = json.load(file)
file.close()
print(est)
print(est["nombre"])

