# yao garbled circuit evaluation v1. simple version based on smart
# naranker dulay, dept of computing, imperial college, october 2018

import util

OBLIVIOUS_TRANSFERS = True


if OBLIVIOUS_TRANSFERS: # __________________________________________________
    primeGroup = util.PrimeGroup()

    # alice generates c from G, bob generates x from (Z/qZ)
    def generate_random_int():  return primeGroup.rand_int()

    # bob sends h_b to alice
    def generate_h_b(x, c_from_G, b_chosen_by_bob):
        # x is generated from (Z/qZ) in main
        # bob generates a pair of public keys: h_b and h_1-b
        h_b_0 = primeGroup.gen_pow(x)
        h_b_1 = primeGroup.mul(c_from_G, primeGroup.inv(h_b_0))
        # send the h_b
        h_b = []
        if b_chosen_by_bob == 0:    h_b.append(h_b_0)
        if b_chosen_by_bob == 1:    h_b.append(h_b_1)
        else:
            print("ERROR: bob generates public keys !")

        return h_b

    # alice sends c, e0, e1 to bob
    def send_parameters(c, h0, m_0, m_1):
        # generate h1 by c/h0
        h1 = primeGroup.mul(c, primeGroup.inv(h0))
        # alice generates k from (Z/qZ)
        k = primeGroup.rand_int()
        # alice generate a public key by g^k
        c_1 = primeGroup.gen_pow(k)
        # Calculate e_0 and e_1
        e_0 = util.xor_bytes(m_0, util.ot_hash(primeGroup.pow(h0, k), len(m_0)))
        e_1 = util.xor_bytes(m_1, util.ot_hash(primeGroup.pow(h1, k), len(m_1)))
        #
        parameters_AliceToBob = []
        parameters_AliceToBob.append(c_1)
        parameters_AliceToBob.append(e_0)
        parameters_AliceToBob.append(e_1)

        return parameters_AliceToBob


    def calculate_m_b(x, c_1, e_0, e_1, b_chosen_by_bob):
        # the same x with generate_h_b
        # calculate m_b and m_1-b
        m_b = util.xor_bytes(e_0, util.ot_hash(primeGroup.pow(c_1, x), len(e_0)))
        m_1_b = util.xor_bytes(e_1, util.ot_hash(primeGroup.pow(c_1, x), len(e_1)))

        if b_chosen_by_bob == 0:    return m_b
        if b_chosen_by_bob == 1:    return m_1_b
        else:
            print("ERROR: calculate m_b !")

# non oblivious transfers, not even a secure channel is used, for testing
else: # ____________________________________________________________________
    print("just for testing.")
