# yao garbled circuit evaluation v1. simple version based on smart
# naranker dulay, dept of computing, imperial college, october 2018

# << removed >>

import numpy as np


class Circuit:
    def __init__(self):
        self.Name  = ""
        self.Alice = []
        self.Bob   = []
        self.Out   = []
        self.Gates = []
        self.Wires = []

    def createCircuit(self, json_circuit):
        self.Name = json_circuit["name"]
        if ("alice" in json_circuit):
            self.Alice = json_circuit["alice"]
            self.Wires.extend(self.Alice)
        if ("bob" in json_circuit):
            self.Bob = json_circuit["bob"]
            self.Wires.extend(self.Bob)
        self.Out = json_circuit["out"]

        for json_circuit_gates in json_circuit["gates"]:
            gate = Gate()
            gate.createGate(json_circuit_gates)
            self.Gates.append(gate)
            self.Wires.append(gate.Id)


# product the p[]
rand = np.random.randint(0, 2, (3, 1))
p = np.zeros([3, 1])
for i in range(3):
    p[i] = rand[i]
    print("p[i] = ", p[i])

gate = np.zeros([3, 2])
gate[0][0] = 0
gate[0][1] = 0
gate[0][2] = 1
gate[0][3] = 1

gate[1][0] = 0
gate[1][1] = 1
gate[1][2] = 0
gate[1][3] = 1

ANDgate = np.zeros([3, 3])

Garbled_Circuit_ANDgate = np.zeros([3, 3])
for i in range(3):
    for j in range(3):
        Garbled_Circuit_ANDgate[j][i] = ANDgate[j][i] ^ p[i]



