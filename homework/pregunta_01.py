"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
def pregunta_01():
    import os
    import pandas as pd
    file_path = 'files/input/solicitudes_de_credito.csv' 
    data = pd.read_csv(file_path, sep=';') 
    data.drop(['Unnamed: 0'], axis=1, inplace=True) 
    data.dropna(inplace=True) 
    data.drop_duplicates(inplace=True) 
    data[['día', 'mes', 'año']] = data['fecha_de_beneficio'].str.split('/', expand=True) 
    data.loc[data['año'].str.len() < 4, ['día', 'año']] = data.loc[data['año'].str.len() < 4, ['año', 'día']].values  
    data['fecha_de_beneficio'] = data['año'] + '-' + data['mes'] + '-' + data['día'] 
    data.drop(['día', 'mes', 'año'], axis=1, inplace=True) 
    object_columns = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito'] 
    data[object_columns] = data[object_columns].apply(lambda x: x.str.lower().replace(['-', '_'], ' ', regex=True).str.strip()) 
    data['barrio'] = data['barrio'].str.lower().replace(['-', '_'], ' ', regex=True) 
    data['monto_del_credito'] = data['monto_del_credito'].str.replace("[$, ]", "", regex=True).str.strip() 
    data['monto_del_credito'] = pd.to_numeric(data['monto_del_credito'], errors='coerce')  
    data['monto_del_credito'] = data['monto_del_credito'].fillna(0).astype(int) 
    data['monto_del_credito'] = data['monto_del_credito'].astype(str).str.replace('.00', '')  
    data.drop_duplicates(inplace=True)
    output_dir = 'files/output' 
    os.makedirs(output_dir, exist_ok=True) 
    output_path = f'{output_dir}/solicitudes_de_credito.csv'
    data.to_csv(output_path, sep=';', index=False)
    return data.head()

# def pregunta_01():
#     input_path = r"C:\analiticadescriptiva\2024-2-LAB-06-limpieza-de-datos-de-solicitudes-de-credito-Dieguini15\files\input\solicitudes_de_credito.csv"
#     output_path = r"C:\analiticadescriptiva\2024-2-LAB-06-limpieza-de-datos-de-solicitudes-de-credito-Dieguini15\files\output\solicitudes_de_credito.csv"

#     try:
#         if not os.path.isfile(input_path):
#             raise FileNotFoundError(f"El archivo {input_path} no existe.")

#         print(f"Leyendo archivo: {input_path}")
        
#         try:
#             df = pd.read_csv(input_path, sep=",")
#         except:
#             print("Intentando con delimitador alternativo ';'.")
#             df = pd.read_csv(input_path, sep=";")

#         print("Información inicial del archivo:")
#         print(df.info())
#         print("\nPrimeros registros:")
#         print(df.head())

#         # Eliminar duplicados
#         initial_rows = len(df)
#         df = df.drop_duplicates()
#         print(f"Se eliminaron {initial_rows - len(df)} registros duplicados.")

#         # Eliminar valores nulos
#         initial_rows = len(df)
#         df = df.dropna()
#         print(f"Se eliminaron {initial_rows - len(df)} registros con datos faltantes.")

#         # Normalizar valores de texto
#         for column in df.select_dtypes(include=["object"]).columns:
#             df[column] = df[column].str.strip().str.lower()

#         # Asegurar consistencia en la columna 'sexo'
#         if "sexo" in df.columns:
#             valid_sexo_values = ["masculino", "femenino"]
#             df = df[df["sexo"].isin(valid_sexo_values)]

#         print("\nInformación después de la limpieza:")
#         print(df.info())
#         print("\nPrimeros registros después de la limpieza:")
#         print(df.head())

#         # Crear carpeta de salida si no existe
#         os.makedirs(os.path.dirname(output_path), exist_ok=True)

#         # Guardar archivo limpio
#         df.to_csv(output_path, index=False, sep=";")
#         print(f"Archivo limpio guardado en: {output_path}")

#     except FileNotFoundError as e:
#         print(f"Error: {e}")
#     except PermissionError as e:
#         print(f"Error de permisos: {e}")
#         print("Intenta cerrar programas que usen el archivo o ejecuta el script como administrador.")
#     except Exception as e:
#         print(f"Se produjo un error durante la limpieza: {e}")

# if __name__ == "__main__":
#     pregunta_01()


"""
Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
El archivo tiene problemas como registros duplicados y datos faltantes.
Tenga en cuenta todas las verificaciones discutidas en clase para
realizar la limpieza de los datos.

El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

"""
