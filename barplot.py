import matplotlib.pyplot as plt

# Dados – população do Brasil (em milhões) para anos selecionados
# Fonte: IBGE estimativas e projeções
anos = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025]
populacao = [
    149.0,   # 1990 (aproximado)
    161.8,   # 1995 (aproximado)
    174.4,   # 2000 (aproximado)
    186.8,   # 2005 (aproximado)
    195.7,   # 2010 (aproximado)
    204.4,   # 2015 (aproximado)
    212.6,   # 2020 (aproximado)
    218.5    # 2025 (projeção aproximada)
]

# Gera o gráfico
plt.figure(figsize=(10, 6))
cores = ['red']
barras = plt.bar(anos, populacao, color=cores)

plt.title('Crescimento Populacional no Brasil (1990-2025)', fontsize=16, fontweight='bold')
plt.xlabel('Ano', fontsize=12)
plt.ylabel('População (em milhões)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Adiciona os valores acima das barras
for barra, valor in zip(barras, populacao):
    plt.text(barra.get_x() + barra.get_width()/2,
             barra.get_height() + 0.5,
             f'{valor:.1f}',
             ha='center',
             va='bottom',
             fontsize=10,
             color='black')

plt.tight_layout()

# Salva em formato PDF
plt.savefig('crescimento_populacional_brasil_1990_2025.pdf', format='pdf')

# Mostrar o gráfico
plt.show()
