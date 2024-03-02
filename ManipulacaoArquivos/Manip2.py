import json

dicionario = {
  "NOAH": ["Noah Sebastian", "27/03/1997", "RECEP_01"],
  "OLIVER": ["Oliver Sykes", "16/01/1996", "RAIOX_02"],
  "DEMI": ["Demi Lovato", "03/01/1995", "RECEP_03"],
  "JOE": ["Joe Jonas", "11/02/1997", "RAIOX_01"]

}

with open("bd1.json", "w") as json_file:
    json.dump(dicionario,json_file)