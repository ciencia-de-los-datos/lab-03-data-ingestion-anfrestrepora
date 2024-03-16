"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

def ingest_data():
    #Lectura DF, renombrar columnas

    df=pd.read_fwf('clusters_report.txt', skiprows=4,index_col=False, names=['cluster','cantidad_de_palabras_clave','porcentaje_de_palabras_clave','principales_palabras_clave'])
    # Llenar valor inf y faltantes, y convertir en entero la columna clauster
    df['cluster']=df['cluster'].ffill().astype(int)
    # Eliminar duplicados la columna clauster
    df=df.drop_duplicates(subset=['cluster'])
    #Convertir cantidad de palabras en entero
    df['cantidad_de_palabras_clave']=df['cantidad_de_palabras_clave'].astype(int)
    #Eliminar procentajes, espacios y convertir la columna porcentaje en float
    df['porcentaje_de_palabras_clave']=df['porcentaje_de_palabras_clave'].str.replace("%","").str.replace(",",".").astype(float)
    #Separar palabras unicamente por espacio y eliminar puntos para que las palabras claves, esten separadas unicamente por ,
    df['principales_palabras_clave']=df.groupby(['cluster'])['principales_palabras_clave'].transform(lambda x: " ".join(x)).str.replace(".","")
    df['principales_palabras_clave']=df['principales_palabras_clave'].replace(r'\s+'," ",regex=True) 
    
    return df
