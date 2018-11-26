
# yao garbled circuit evaluation v1. simple version based on smart
# naranker dulay, dept of computing, imperial college, october 2018

import json	# load

import sys	# argv
import ot	# alice, bob
import util	# ClientSocket, log, ServerSocket
import yao	# Circuit

# Alice is the circuit generator (client) __________________________________

def alice(filename):
  socket = util.ClientSocket()
  util.log(f'Bob: Listening ...')

  # step1: send c to bob and waiting for h_0
  c = ot.generate_random_int()
  socket.send(c)
  print("Successfully! alice sends c to bob, c is: ", c)


  # step3: receive h_0 from bob
  #           send c_1, e_0, e_1 to bob
  h_0 = socket.receive()
  print("Successfully! alice receives h_0 from bob, h_0 is: ", h_0)
  socket.send(ot.send_parameters(c, h_0, m_0, m_1))
  print("Successfully! alice sends parameters:c, h_0, m_0, m_1", c, h_0, m_0, m_1)

  with open(filename) as json_file:
    json_circuits = json.load(json_file)

  for json_circuit in json_circuits['circuits']:
    print("alice")



# Bob is the circuit evaluator (server) ____________________________________

def bob():
  socket = util.ServerSocket()
  util.log(f'Bob: Listening ...')

  while True:

    # step2: bob receives c from alice
    #          generates x from (Z/qZ)
    #            chooses one public key from alice
    #             and waiting for c_1, e_0, e_1
    c = socket.receive()
    x = ot.generate_random_int()
    print("Successfully! bob receives c from alice, c is: ", c)
    print('please choose one of two public keys: (0: the first one; 1: the second one)')
    b = int(input(''))
    h_0 = ot.generate_h_b(x, c, b)

    #socket.send(h_0)
    #print("Successfully! bob sends h_0 to alice, h_0 is: ", h_0)

    # step4: bob receives c_1, e_0, e_1 from alice
    #          calculate m_b
    parameters = socket.receive()
    c_1 = parameters[0]
    e_0 = parameters[1]
    e_1 = parameters[2]
    print("Successfully! bob receives c_1, e_0, e_1 from alice, ", c_1, e_0, e_1)
    m_b = ot.calculate_m_b(x, c_1, e_0, e_1, b)



# local test of circuit generation and evaluation, no transfers_____________

def local_test(filename):
  with open(filename) as json_file:
    json_circuits = json.load(json_file)

  for json_circuit in json_circuits['circuits']:
    print("local test")
    # << removed >>

# main _____________________________________________________________________

def main():
  behaviour = sys.argv[1]
  if   behaviour == 'alice': alice(filename=sys.argv[2])
  elif behaviour == 'bob':   bob()
  elif behaviour == 'local': local_test(filename=sys.argv[2])

if __name__ == '__main__':
  main()

# __________________________________________________________________________


