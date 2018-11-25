
# yao garbled circuit evaluation v1. simple version based on smart
# naranker dulay, dept of computing, imperial college, october 2018
import util

OBLIVIOUS_TRANSFERS = True


if OBLIVIOUS_TRANSFERS: # __________________________________________________
    primeGroup = util.PrimeGroup()


    # alice
    def generate_public_key(socket):

        c = primeGroup.rand_int()
        pub1 = primeGroup.gen_pow(c)
        socket.send(pub1)

  # << removed >>

else: # ____________________________________________________________________
    print("bob")

  # << removed >>

# __________________________________________________________________________


