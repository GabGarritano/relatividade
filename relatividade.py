import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Constante da velocidade da luz (m/s)
c = 3e8

# Entrada: tempo dentro do planeta (em horas)
try:
    tempo_planeta_horas = float(input("Digite o tempo passado no planeta (em horas): "))
except ValueError:
    print("Por favor, insira um número válido.")
    exit()

# Tempo em repouso (no planeta), convertido para segundos
tempo_reposo = tempo_planeta_horas * 3600

# Tempo fora do planeta fixo (Interestelar: 1h = 7 anos)
tempo_dilatado = 7 * tempo_planeta_horas * 365 * 24 * 3600  # segundos

# Fator de Lorentz (γ)
gamma = tempo_dilatado / tempo_reposo

# Velocidade equivalente (em fração de c)
v_rel_frac = np.sqrt(1 - (1 / gamma**2))
v_rel = v_rel_frac * c

# Comprimento base
comprimento_reposo = 100.0  # metros
comprimento_contraido = comprimento_reposo / gamma

print("\n=== Resultados ===")
print(f"Fator de dilatação (γ): {gamma:.2f}")
print(f"Velocidade necessária: {v_rel_frac:.15f} c")
print(f"Comprimento contraído: {comprimento_contraido:.4f} m (de {comprimento_reposo} m)")
print(f"Tempo fora do planeta: {tempo_dilatado / 3600 / 24 / 365:.2f} anos")

# Geração de vetor de velocidades
v = np.linspace(0.01 * c, 0.999999 * c, 1000)
fator_lorentz = 1 / np.sqrt(1 - (v**2 / c**2))
tempo_dilatado_arr = tempo_reposo * fator_lorentz
comprimento_contraido_arr = comprimento_reposo / fator_lorentz

# Gráficos
plt.figure(figsize=(12, 5))

# Dilatação do tempo
plt.subplot(1, 2, 1)
plt.plot(v / c, tempo_dilatado_arr, color='blue', label="Tempo dilatado")
plt.axhline(tempo_reposo, color='red', linestyle='--', label="Tempo no planeta")
plt.axvline(v_rel_frac, color='purple', linestyle=':', label="Velocidade do planeta")

# Adiciona anotação explicando os tempos
tempo_anos = tempo_dilatado / (3600 * 24 * 365)
texto = f"Tempo no planeta: {tempo_planeta_horas:.1f} h\nTempo fora: {tempo_anos:.1f} anos\nv ≈ {v_rel_frac*100:.12f}% da luz"
plt.text(0.05, tempo_dilatado * 0.6, texto, fontsize=10,
         bbox=dict(facecolor='white', alpha=0.7))

plt.title("Dilatação do Tempo")
plt.xlabel("v/c")
plt.ylabel("t'")
plt.grid(True)
plt.legend()

# Contração do comprimento
plt.subplot(1, 2, 2)
plt.plot(v / c, comprimento_contraido_arr, color='green', label="Comprimento contraído")
plt.axhline(comprimento_reposo, color='red', linestyle='--', label="Comprimento em repouso")
plt.axvline(v_rel_frac, color='purple', linestyle=':', label="Velocidade do planeta")
plt.title("Contração do Comprimento")
plt.xlabel("v/c")
plt.ylabel("L'")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
