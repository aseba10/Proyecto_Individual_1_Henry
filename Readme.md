<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>


<hr>  

## **Descripción del problema (Contexto y rol a desarrollar)**

## Contexto

Tienes tu modelo de recomendación dando unas buenas métricas :smirk:, y ahora, cómo lo llevas al mundo real? :eyes:

El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.


## Rol a desarrollar

Empezaste a trabajar como **`Data Scientist`** en una start-up que provee servicios de agregación de plataformas de streaming. El mundo es bello y vas a crear tu primer modelo de ML que soluciona un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha! 

Vas a sus datos y te das cuenta que la madurez de los mismos es poca (ok, es nula :sob:): Datos anidados, sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas….  haciendo tu trabajo imposible :weary:. 

Debes empezar desde 0, haciendo un trabajo rápido de **`Data Engineer`** y tener un **`MVP`** (_Minimum Viable Product_) para el cierre del proyecto! Tu cabeza va a explotar 🤯, pero al menos sabes cual es, conceptualmente, el camino que debes de seguir :exclamation:. Así que te espantas los miedos y te pones manos a la obra :muscle:

<p align="center">
<img src="https://github.com/HX-PRomero/PI_ML_OPS/raw/main/src/DiagramaConceptualDelFlujoDeProcesos.png"  height=500>
</p>


## **Propuesta de trabajo**

**`Transformaciones`**:  


+ Se desanidaron las columnasAlgunos campos, como **`belongs_to_collection`**, **`production_companies`**, **`production_countries`**, **`spoken_language`** y **`genres`**.

+ Los valores nulos de los campos **`revenue`**, **`budget`** se rellenaron con el número **`0`**.
  
+ Los valores nulos del campo **`release date`** se eliminaron.

+ Las fechas se pasaron al formato **`AAAA-mm-dd`**, y se creó  la columna **`release_year`** donde se extrae el año de la fecha de estreno.

+ Se creó la columna con el retorno de inversión, llamada **`return`** con los campos **`revenue`** y **`budget`**, dividiendo estas dos últimas **`revenue / budget`**, y cuando no hubo datos disponibles para calcularlo, se tomó el valor **`0`**.

+ Se emilinaron las columnas que no serán utilizadas, **`video`**,**`imdb_id`**,**`adult`**,**`original_title`**,**`poster_path`** y **`homepage`**.

<br/>

**`Análisis exploratorio de los datos`**: _(Exploratory Data Analysis-EDA)_

Para el EDA se buscó outliers con graficos de caja y la correlación entre las variables numéricas. Se realizó un recuento de las películas por genero y por pais y se utilizó una nube de palabras para las columnas **`title`**, **`overview`** y **`tagline`**.

<br/>


**`Desarrollo API`**:   

Se crearon 7 funcoines para los endpoints que se consumen en la API. Se utilizó el framework [***FastApi***](https://fastapi.tiangolo.com/) y para el deployment [***Render***](https://render.com/).
  
+ def **peliculas_idioma( *`Idioma`: str* )**:
    Se ingresa un idioma. Devuelve la cantidad de películas producidas en ese idioma.

        

+ def **peliculas_duracion( *`Pelicula`: str* )**:
    Se ingresa una pelicula. Devuelve la duracion y el año.


+ def **franquicia( *`Franquicia`: str* )**:
    Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
    

+ def **peliculas_pais( *`Pais`: str* )**:
    Se ingresa un país retornando la cantidad de peliculas producidas en el mismo.
    

+ def **productoras_exitosas( *`Productora`: str* )**:
    Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo. 
    

+ def **get_director( *`nombre_director`* )**:
    Se ingresa el nombre de un director que se encuentre dentro de un dataset devolviendo el éxito del mismo medido a través del retorno. Además, entrega el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.

+ def **recomendacion( *`titulo`* )**:
    Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.


Para el sistema de recomendacion el modelo primero filtra el dataframe dejando solamente las peliculas con los mismos generos. Posteriormente se calcula la similitud coseno entre las características TF-IDF de los títulos de las películas y arroja una lista de 5 títulos ordenados de acuerdo a la puntuación de la columna **`vote_average`**.

## **[Link Api](https://proyecto-1-individual-henry.onrender.com/docs#)**



## **[Link Video](https://drive.google.com/file/d/1YRLAmOh1J2uiREE0CvGzcY7uyV5mSWUH/view)**



## **Fuente de datos**

- + [Dataset](https://drive.google.com/drive/folders/1nvSjC2JWUH48o3pb8xlKofi8SNHuNWeu)
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1QkHH5er-74Bpk122tJxy_0D49pJMIwKLurByOfmxzho/edit#gid=0)
<br/>


  
<br/>

