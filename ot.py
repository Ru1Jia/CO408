
# yao garbled circuit evaluation v1. simple version based on smart
# naranker dulay, dept of computing, imperial college, october 2018
import util
import numpy as np
import sys

OBLIVIOUS_TRANSFERS = True


if OBLIVIOUS_TRANSFERS: # __________________________________________________
    primeGroup = util.PrimeGroup()

    # alice's two public keys

    # Two public keys from alice to bob who can choose one of these two
    # two keys array
    TwoKeys_c = np.zeros([7,2])
    for i in range(7):
        for j in range(2):
            TwoKeys_c[i][j] = primeGroup.gen_pow(primeGroup.rand_int())

    # bob' choice
    def bob_select_public_key(socket):
        # step1: bob choose one public key from alice
        print('choose one of two public keys: (0: the first one; 1: the second one)')
        while True:
            value = int(input(''))
            if value == 1 or value == 0:
                print(value)
                break
            else:
                print(value)
                print("please select 0 or 1.")
        print(value)
        socket.send(value)

    # step2: to send the one chosen by bob
    def send_public_key_to_bob(value, socket):
        pass


  # bellare-micali OT with naor and pinkas optimisations, see smart p423

  # << removed >>

else: # ____________________________________________________________________
    print("bob")
  # non oblivious transfers, not even a secure channel is used, for testing

# __________________________________________________________________________


