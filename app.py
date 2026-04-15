import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Accidentes Acacías",
    page_icon="🚗",
    layout="wide"
)

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv('data/accidentesLimpio.csv')
    return df

df = load_data()

# --- SIDEBAR (Filtros) ---
st.sidebar.header("Filtros de Análisis")
st.sidebar.markdown("### Acacías, Meta 🗺️")

años = sorted(df['Año'].unique())
año_seleccionado = st.sidebar.selectbox("Seleccionar Año", ["Todos"] + list(años))

barrios = sorted(df['Barrio'].unique())
barrio_seleccionado = st.sidebar.selectbox("Seleccionar Barrio", ["Todos"] + list(barrios))

# Aplicar filtros
df_filtrado = df.copy()
if año_seleccionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado['Año'] == año_seleccionado]
if barrio_seleccionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado['Barrio'] == barrio_seleccionado]

# --- MAIN CONTENT ---
st.title("📊 Análisis de Accidentes de Tránsito - Acacías")
st.markdown("""
Esta aplicación permite explorar los datos de accidentalidad en el municipio de Acacías, 
identificando patrones, zonas críticas e indicadores clave de mortalidad.
""")

# --- KPIs ---
col1, col2, col3, col4 = st.columns(4)

total_accidentes = len(df_filtrado)
total_muertes = df_filtrado['Muertes'].sum()
tasa_mortalidad = (df_filtrado['Mortalidad'].sum() / total_accidentes) * 100 if total_accidentes > 0 else 0
total_heridos = df_filtrado['Heridos'].sum()

col1.metric("Total Accidentes", f"{total_accidentes}")
col2.metric("Total Muertes", f"{total_muertes}")
col3.metric("Tasa Mortalidad", f"{tasa_mortalidad:.1f}%")
col4.metric("Total Heridos", f"{total_heridos}")

st.divider()

# --- GRAFICOS ---
c1, c2 = st.columns(2)

with c1:
    st.subheader("Tendencia Temporal")
    if año_seleccionado == "Todos":
        # Por año
        fig_trend = px.line(df.groupby('Año').size().reset_index(name='Accidentes'), 
                           x='Año', y='Accidentes', markers=True, 
                           title="Accidentes por Año")
    else:
        # Por mes
        orden_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
                      'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        resumen_mes = df_filtrado.groupby('Mes_Nombre').size().reindex(orden_meses).reset_index(name='Accidentes')
        fig_trend = px.bar(resumen_mes, x='Mes_Nombre', y='Accidentes', 
                          title=f"Accidentes por Mes en {año_seleccionado}",
                          color_discrete_sequence=['#ff4b4b'])
    
    st.plotly_chart(fig_trend, use_container_width=True)

with c2:
    st.subheader("Clase de Accidente")
    fig_pie = px.pie(df_filtrado, names='Clase de Accidente', hole=0.4,
                     title="Distribución por Tipo")
    fig_pie.update_traces(textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

# --- MAPA O BARRIOS ---
st.subheader("Análisis Geográfico: Top 15 Barrios Críticos")
top_barrios = df_filtrado[df_filtrado['Barrio'] != 'NO REGISTRA']['Barrio'].value_counts().head(15).reset_index()
top_barrios.columns = ['Barrio', 'Accidentes']

fig_barrios = px.bar(top_barrios, x='Accidentes', y='Barrio', orientation='h',
                    color='Accidentes', color_continuous_scale='Reds',
                    title="Barrios con mayor accidentalidad")
fig_barrios.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig_barrios, use_container_width=True)

# --- TABLA DE DATOS ---
with st.expander("Ver datos detallados"):
    st.dataframe(df_filtrado[['Fecha_Ocurrencia', 'Direccion', 'Barrio', 'Vehiculos Involucrados', 'Heridos', 'Muertes', 'Clase de Accidente']], use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.info("Proyecto desarrollado para CV/Portafolio")
