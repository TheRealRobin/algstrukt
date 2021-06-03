import euclid as ggt #euclid.py enthält Euklidischen Algorithmus für GGT

a = []

for i in range(2, 5):
    for j in range(1,10):
        a += [ [[i],[j],[ggt.euclids_ggt_algorithm(i,j)]] ]
print(str(a))