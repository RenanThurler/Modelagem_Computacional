#Teste com diferentes valores de mu (penalidade) e alpha (passo) para ver como cada elemento afeta o resultado da otimizacao do tanque.

import math
from codigo_principal import metodo_do_gradiente, VOLUME_MINIMO

r0, h0 = 3.5, 12.0

valores_mu = [1e2, 1e4, 1e6]
valores_alpha = [1e-8, 1e-9, 1e-10]

print("=" * 70)
print("Teste variando mu (alpha fixo em 1e-9)")
print("=" * 70)

for mu in valores_mu:
    r, h, c, hist = metodo_do_gradiente(r0, h0, mu, 1e-9, max_iteracoes=500000, tolerancia=1e-10)
    v = math.pi * r**2 * h
    print(f"mu={mu:.0e} -> r={r:.4f} h={h:.4f} V={v:.2f} custo=R$ {c:.2f}")

print("=" * 70)
print("Teste variando alpha (mu fixo em 1e4)")
print("=" * 70)
for alpha in valores_alpha:
    r, h, c, hist = metodo_do_gradiente(r0, h0, 1e4, alpha, max_iteracoes=500000, tolerancia=1e-10)
    v = math.pi * r**2 * h
    print(f"alpha={alpha:.0e} -> r={r:.4f} h={h:.4f} V={v:.2f} custo=R$ {c:.2f} iters={len(hist)-1}")
