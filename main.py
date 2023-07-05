#importo librerías

import pandas as pd
from fastapi import FastAPI
import ast
import numpy as np



df = pd.read_csv("Dataset/df.csv")

app = FastAPI()

#http://127.0.0.1:8000/

@app.get("/")
def index():
    return "Bienvenidos"


@app.get("/idioma/{idioma}")
def peliculas_idioma(idioma: str ):
    # Filtrar el DataFrame por idioma
    peliculas_filtradas = df[df['original_language'] == idioma]
        
    # Obtener la cantidad de películas
    cantidad_peliculas = len(peliculas_filtradas)
    
    return f"{cantidad_peliculas} cantidad de peliculas fueron estrenadas en idioma {idioma}"

@app.get("/duracion/{pelicula}")
def peliculas_duracion( pelicula: str):
    
    # Filtrar el DataFrame por la película deseada
    pelicula_filtrada = df[df['title'] == pelicula]
    
    # Obtener la duración y el año de la película
    d = pelicula_filtrada['runtime'].values[0]
    a = pelicula_filtrada['release_year'].values[0]
    
    return f"{pelicula} Duración: {d} Año: {a}"

@app.get("/franquicia/{franquicia}")
def franquicia( franquicia: str):

    # Filtrar el DataFrame por franquicia
    peliculas_franquicia = df[df['belongs_to_collection'] == franquicia]
    
    # Obtener la cantidad de películas
    cantidad_peliculas = len(peliculas_franquicia)
    
    # Calcular la ganancia total y promedio
    ganancia_total = peliculas_franquicia['revenue'].sum()
    ganancia_promedio = ganancia_total / cantidad_peliculas
    
    # Retornar los resultados
    return f"La franquicia {franquicia} posee {cantidad_peliculas} películas, una ganancia total de {ganancia_total} y una ganancia promedio de {ganancia_promedio}"

@app.get("/pais/{pais}")
def peliculas_pais( pais: str):
    
    peliculas_filtradas = df[df["production_countries"].str.contains(pais, na=False)]
    
    cant = len(peliculas_filtradas)

    return f"Se produjeron {cant} películas en el país {pais}"

@app.get("/productoras_exitosas/{productora}")
def productoras_exitosas( productora: str ):

    peliculas_filtradas = df[df["production_companies"].str.contains(productora, na=False)]
    revenue = peliculas_filtradas["revenue"].sum()


    return f"La productora {productora} ha tenido un revenue de {revenue}"

@app.get("/get_director/{nombre_director}")
def get_director(nombre_director):
    peliculas_director = df[df["crew"].apply(lambda x: nombre_director in x)]

    if peliculas_director.empty:
        return None

    promedio_retorno = peliculas_director["return"].mean()

    informacion_peliculas = []
    for _, row in peliculas_director.iterrows():
        pelicula = {
            "Pelicula": row["title"],
            "Fecha de lanzamiento": row["release_date"],
            "Retorno individual": row["return"],
            "Costo": row["budget"],
            "Ganancia": row["revenue"]
        }
        informacion_peliculas.append(pelicula)

    return promedio_retorno, informacion_peliculas


