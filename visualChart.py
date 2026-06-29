import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

matplotlib.use('Agg') 
sns.set_theme(style="whitegrid")

df = pd.read_csv('sdss_supernovae_curves.csv')
df_sn1000 = df[df['objid'].astype(str) == '1000'].copy()

if df_sn1000.empty:
    print("Aviso: Nenhum dado foi encontrado para o ID 1000. Verifique o arquivo CSV.")
    exit()

df_sn1000['days'] = df_sn1000['time'] - df_sn1000['time'].min()
df_sn1000['days'] = pd.to_numeric(df_sn1000['days'], errors='coerce')
df_sn1000['flux'] = pd.to_numeric(df_sn1000['flux'], errors='coerce')
df_sn1000['fluxerr'] = pd.to_numeric(df_sn1000['fluxerr'], errors='coerce')

cores = {
    'sdss_sako18_u6': '#1f77b4',  # Azul (Ultravioleta)
    'sdss_sako18_g6': '#2ca02c',  # Verde
    'sdss_sako18_r6': '#d62728',  # Vermelho
    'sdss_sako18_i6': '#9467bd',  # Roxo
    'sdss_sako18_z6': '#8c564b'   # Marrom (Infravermelho profundo)
}

fig, ax = plt.subplots(figsize=(10, 6))

df_filtrado = df_sn1000[df_sn1000['band'].isin(cores.keys())]

for banda, grupo in df_filtrado.groupby('band'):
        grupo_ordenado = grupo.sort_values(by='days')
        ax.errorbar(
            grupo['days'], 
            grupo['flux'], 
            yerr=grupo['fluxerr'], 
            fmt='o',
            alpha=0.7,
            label=f"Banda {banda.split('_')[-1]}",
            color=cores[banda],
            capsize=3,
            markersize=8
        )

plt.title("Curva de Luz da Supernova ID 1000 (SDSS)", fontsize=14, fontweight='bold')
plt.xlabel("Tempo Decorrido (Dias)", fontsize=12)
plt.ylabel("Fluxo de Brilho", fontsize=12)
plt.legend(title="Filtros Opticos")
plt.tight_layout()

# Exibe o gráfico na tela
plt.savefig('curva_de_luz_sn1000.png', dpi=300, bbox_inches='tight')
print("Sucesso! Abra o arquivo 'curva_de_luz_sn1000.png' para visualizar a curva de luz.")