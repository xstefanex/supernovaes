import pandas as pd
import sndata

dataset = sndata.sdss.Sako18()
ids_disponiveis = dataset.get_available_ids()

dfs_completos = []

print("Consolidando dados... Isso pode levar um tempinho.")
for idx, obj_id in enumerate(ids_disponiveis):
    # Carrega o objeto individual
    dados_astropy = dataset.get_data_for_id(obj_id)
    df_temp = dados_astropy.to_pandas()
    
    # Adiciona a coluna com o ID do objeto para não misturar os dados
    df_temp['objid'] = str(obj_id)
    
    dfs_completos.append(df_temp)
    
    # Print de progresso a cada 1000 objetos
    if idx % 1000 == 0 and idx > 0:
        print(f"{idx} supernovas processadas...")

# Concatena todos os DataFrames em um único
df_final = pd.concat(dfs_completos, ignore_index=True)

# Salva em um único arquivo CSV no seu diretório atual
df_final.to_csv('sdss_supernovae_curves.csv', index=False)
print("Pronto! Arquivo 'sdss_supernovae_curves.csv' gerado com sucesso.")