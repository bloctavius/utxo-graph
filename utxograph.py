import subprocess
import json
import electrum

import plotly.graph_objects as go

cmd="electrum --testnet listunspent"

def getProcessOutput(cmd):
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE)
    process.wait()
    data, err = process.communicate()
    if process.returncode is 0:
        return data.decode('utf-8')
    else:
        print("Error:", err)
    return ""

output = getProcessOutput(cmd)
l = json.loads(output)
utxo = []

for i in range(len(l)):
	utxo.append(l[i]['value'])
	
amts = list(map(float, utxo))

print(amts)

addr = []

for j in range(len(l)):
	addr.append(l[j]['address'])
	
print(addr)

import plotly.graph_objects as go

fig = go.Figure(go.Bar(
            x=amts,
            y=addr,
            orientation='h'))

fig.show()

