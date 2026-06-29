import sndata

dataset = sndata.sdss.Sako18()

print("Tabelas disponíveis:", dataset.get_available_tables())


ids_disponiveis = dataset.get_available_ids()
print(f"Total de supernovas encontradas: {len(ids_disponiveis)}")
print("Exemplo de alguns IDs:", ids_disponiveis[:5])


primeiro_id = ids_disponiveis[0]
dados_supernova = dataset.get_data_for_id(primeiro_id)

df_supernova = dados_supernova.to_pandas()
print(f"\nDados da Supernova ID {primeiro_id}:")
print(df_supernova.head())

master_table = dataset.load_table(table_id='master')
df_master = master_table.to_pandas()

df_master.to_csv('sdss_supernovae_master.csv', index=False)
print("Tabela master salva como 'sdss_supernovae_master.csv'")

#dataset.download_module_data()

#data_table = dataset.load_table(table_id='light_curve')

#df = data_table.to_pandas()

#print(df.head())