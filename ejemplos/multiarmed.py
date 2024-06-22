import random

def multi_armed_bandit(lllIlllIllllIIllll):
    lIIIllllIIIIllllIl = [lambda : 2 * random.random() + 1, lambda : 3 * random.random() + 2, lambda : random.gauss(1, 0.5), lambda : random.gauss(2, 1.0), lambda : 5]
    lIIlllIlIlIllIIIll = lIIIllllIIIIllllIl[lllIlllIllllIIllll]()
    return lIIlllIlIlIllIIIll

