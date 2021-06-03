def euclids_ggt_algorithm(a,b):                                                                #Euklidischer GGT algorithmus
    m = a; n = b
    last = [0,0]
    while not (n == m):
        if ( m < n ):
            temp = m; m = n
            n = temp
        r = m - n
        m = n; n = r
        if ((last[0] == m and last[1] == n) or (last[0] == n and last[1] == m)): #verhindert infinite looping
            break
        last[0] = m; last[1] = n                                                 #bis hier
    #print("[a,b]=["+str(a)+","+str(b)+"];[GGT]=["+str(m)+" == "+str(n)+"]")
    return m