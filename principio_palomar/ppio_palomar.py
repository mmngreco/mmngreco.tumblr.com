import numpy as np
import scipy.stats as st

# datos
pob_sevilla = 696676
media_pelos = 100000

# conocido
n = pob_sevilla
ic_inf = 0
xbarra = media_pelos
alfa = 0.0000001
z = st.norm.ppf(alfa / 2)

# desconocido
s1 = -xbarra / (z / np.sqrt(n))
ee = (media_pelos / (st.norm.ppf(1-alfa/2)/np.sqrt(pob_sevilla))) / np.sqrt(pob_sevilla)
dist_pelos_persona = np.random.normal(loc=media_pelos, 
                                      scale=ee, 
                                      size=pob_sevilla)


dist_pelos_persona = np.round(dist_pelos_persona, 0)          # convertir a datos discretos
dp_unique = np.unique(dist_pelos_persona)                     # creamos etiquetas de cada valor
sample = np.random.choice(dp_unique, size=10000, replace=False)  # tomamos una muestra
sample = np.sort(sample)                                      # ordenamos la muestra
count = 0

# print muestra
print('{}\t\t{}\n---–---\t\t----------'.format('NºPelos', 'Frecuencia'))
for e in sample:
    n = len(dist_pelos_persona[dist_pelos_persona == e])
    print('{} = \t'.format(e),'.' * n)
    if n > 1:
        count += 1
print('Tamaño de la muestra =', len(sample))
print('Nº Pelos por persona con frecuencia > 1 =', count)
print('happy python :-)')
print('@mmngreco')
