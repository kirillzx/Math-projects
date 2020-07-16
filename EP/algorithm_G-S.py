def gale_sh(mPref, wPref):
    match, cont = [], []
    free_m = list(mPref.keys())

    while free_m:
        for man in free_m:
            w = mPref[man][0]

            if w not in cont:
                match.append([man, w])
                cont.append(w)
                free_m.remove(man)
                mPref[man].remove(w)

            else:
                m0 = match[cont.index(w)][0]
                if wPref[w].index(man) < wPref[w].index(m0):
                    free_m.append(m0)
                    free_m.remove(man)
                    match.remove([m0, w])
                    match.append([man, w])
                else:
                    mPref[man].remove(w)
    return match

mPref = {'m1': ['w2', 'w3', 'w1'],
         'm2': ['w1', 'w3', 'w2'],
         'm3': ['w3', 'w1', 'w2']}

wPref = {'w1': ['w1', 'w2', 'w3'],
         'w2': ['w2', 'w1', 'w3'],
         'w3': ['w3', 'w1', 'w2']}

print(gale_sh(mPref, wPref))
