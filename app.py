import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Función para mostrar los datos del archivo
def mostrar_datos(df):
    st.write("### Datos Cargados")
    st.write(df)

    # Estadísticas descriptivas
    st.write("### Estadísticas Descriptivas")
    st.write(df.describe())

    # Visualización
    st.write("### Gráfico de Dispersión")
    fig, ax = plt.subplots()
    ax = sns.scatterplot(x=df.columns[0], y=df.columns[1], data=df)
    st.pyplot(fig)

    # Correlaciones
    st.write("### Matriz de Correlación")
    fig, ax = plt.subplots()
    ax = sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    st.pyplot(fig)

# Sección Acerca de
def acerca_de():
    st.title("Acerca de")
    st.write("""
    Esta aplicación permite compartir contenido personal, como el perfil del desarrollador y los proyectos realizados.
    Además, te permite cargar y visualizar datos de archivos en formato `.xlsx`, `.xls` y `.csv` utilizando herramientas de análisis de datos como Pandas, Numpy, Matplotlib y Seaborn.
    """)

# Sección Perfil del Desarrollador
def perfil():
    st.title("Perfil del Desarrollador")
    st.write("""
    Soy un desarrollador apasionado por el análisis de datos, el desarrollo web y la creación de aplicaciones interactivas.
    Me encanta explorar nuevas tecnologías y desarrollar soluciones que ayuden a los usuarios a tomar decisiones informadas.
    """)

# Sección Proyectos
def proyectos():
    st.title("Proyectos")
    st.write("""
    Aquí algunos de mis proyectos recientes:
    - **Análisis de datos financieros**: Creación de una plataforma para analizar datos de mercado en tiempo real.
    - **Aplicación de predicción**: Desarrollo de una app para predecir tendencias de ventas usando algoritmos de aprendizaje automático.
    - **Visualización interactiva de datos**: Aplicación web que permite a los usuarios cargar datos y generar visualizaciones dinámicas.
    """)

# Función principal de la aplicación
def app():
    st.sidebar.title("Menú")
    opciones = ["Inicio", "Acerca de", "Perfil del Desarrollador", "Proyectos", "Cargar Datos"]
    seleccion = st.sidebar.radio("Selecciona una opción", opciones)

    if seleccion == "Inicio":
        st.title("Bienvenido a mi Aplicación Web")
        st.write("Aquí podrás encontrar mi perfil, proyectos y analizar tus datos.")

    elif seleccion == "Acerca de":
        acerca_de()

    elif seleccion == "Perfil del Desarrollador":
        perfil()

    elif seleccion == "Proyectos":
        proyectos()

    elif seleccion == "Cargar Datos":
        st.title("Cargar Datos")
        archivo = st.file_uploader("Sube tu archivo", type=["xlsx", "xls", "csv"])

        if archivo is not None:
            if archivo.name.endswith(('xlsx', 'xls')):
                df = pd.read_excel(archivo)
            elif archivo.name.endswith('csv'):
                df = pd.read_csv(archivo)

            # Mostrar los datos cargados y generar visualizaciones
            mostrar_datos(df)

# Ejecuta la aplicación
if __name__ == "__main__":
    app()
