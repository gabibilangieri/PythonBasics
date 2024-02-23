usuarios = {}
print(usuarios)

usuarios = {
    "oliver" : ["Oliver Sykes", "24/12/2017", "Recep_01"],
    "noah" : ["Noah Sebastian", "20/12/2017", "RaioX_03"],
    "normani" : ["Normani Kordei", "21/12/2017", "Consult_06"]
}
print(usuarios)

usuarios["demi"] = ["Demi Lovato", "24/12/2017", "Triagem_01"]
print(usuarios)

print("#####---#####")
print(usuarios.get("noah"))