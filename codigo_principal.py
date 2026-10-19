import math
import matplotlib.pyplot as plt

CUSTO_BASE = 150.0     # R$ por m^2
CUSTO_LATERAL = 100.0  # R$ por m^2
CUSTO_TETO = 200.0     # R$ por m^2
VOLUME_MINIMO = 500.0  # R$ por m^3

def custo(r, h):
    area_base = math.pi * r**2
    area_lateral = 2 * math.pi * r * h
    area_teto = math.pi * r**2
    return CUSTO_BASE * area_base + CUSTO_LATERAL * area_lateral + CUSTO_TETO * area_teto


def restricao(r, h):
    volume = math.pi * r**2 * h
    return VOLUME_MINIMO - volume

def penalizacao(r, h, mu):
    g = restricao(r, h)
    return custo(r, h) + mu * (max(0.0, g)) ** 2

def derivadas_numericas(r, h, mu, delta=1e-5):
    P_atual = penalizacao(r, h, mu)
    dP_dr = (penalizacao(r + delta, h, mu) - P_atual) / delta
    dP_dh = (penalizacao(r, h + delta, mu) - P_atual) / delta
    return dP_dr, dP_dh

def metodo_do_gradiente(r0, h0, mu, alpha, delta=1e-5, max_iteracoes=20000, tolerancia=1e-8):

    r, h = r0, h0
    historico_P = [penalizacao(r, h, mu)]
    for _ in range(max_iteracoes):
        dP_dr, dP_dh = derivadas_numericas(r, h, mu, delta)
        r_novo = r - alpha * dP_dr
        h_novo = h - alpha * dP_dh
        r_novo = max(r_novo, 1e-6)
        h_novo = max(h_novo, 1e-6)
        variacao = abs(r_novo - r) + abs(h_novo - h)
        r, h = r_novo, h_novo
        historico_P.append(penalizacao(r, h, mu))
        if variacao < tolerancia:
            break
    return r, h, custo(r, h), historico_P

if __name__ == "__main__":
    r0, h0 = 3.5, 12.0
    mu = 1e4
    alpha = 1e-9
    r_otimo, h_otimo, custo_otimo, historico = metodo_do_gradiente(
        r0, h0, mu, alpha, max_iteracoes=500000, tolerancia=1e-10
    )
    volume_final = math.pi * r_otimo**2 * h_otimo
    print("=" * 50)
    print("Resultado da otimizacao")
    print("=" * 50)
    print(f"mu = {mu:.0e}, alpha = {alpha:.0e}")
    print(f"Numero de iteracoes ate convergir: {len(historico) - 1}")
    print(f"Raio otimo (r):   {r_otimo:.4f} m")
    print(f"Altura otima (h): {h_otimo:.4f} m")
    print(f"Volume final:     {volume_final:.4f} m^3 (minimo exigido: {VOLUME_MINIMO} m^3)")
    print(f"Custo minimo:     R$ {custo_otimo:.2f}")

plt.figure(figsize=(8, 5))
plt.plot(historico[1:])
plt.xlabel("Iteracao")
plt.ylabel("Valor da funcao P(r,h)")
plt.title("Convergencia do Metodo do Gradiente")
plt.grid(True)
plt.tight_layout()
plt.savefig("convergencia.png", dpi=150)
print("\nGrafico de convergencia salvo em convergencia.png")