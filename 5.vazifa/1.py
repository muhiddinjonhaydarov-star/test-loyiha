import numpy as np
s1 = [12, 45, 7, 23, 89, 34, 56, 3, 78, 19]
m = np.array(s1)
ortacha  = np.mean(m)
eng_katta = np.max(m)
eng_kichik = np.min(m)
print("O'fshi:",s1)
print("O'rtacha:",ortacha)
print("Eng kattasi:",eng_katta)
print("Eng kichigi:",eng_kichik)
