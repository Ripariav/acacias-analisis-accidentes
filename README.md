# Análisis de Accidentes de Tránsito — Acacías, Meta

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white)

Análisis exploratorio de datos sobre accidentalidad vial en el municipio de **Acacías, Meta (Colombia)**. El proyecto incluye limpieza de datos, visualizaciones interactivas y un reporte automático en PDF con KPIs de mortalidad.

---

## Demo

> Ejecuta el dashboard localmente con:
> ```bash
> streamlit run app.py
> ```

---

## Estructura del proyecto

```
.
├── app.py                        # Dashboard interactivo (Streamlit + Plotly)
├── src/
│   └── clean_data.py             # Pipeline de limpieza de datos
├── notebooks/
│   └── explicacion.ipynb         # Notebook exploratorio paso a paso
├── data/
│   ├── accidentes.csv            # Dataset original
│   └── accidentesLimpio.csv      # Dataset procesado
├── Informe_Accidentes.pdf        # Reporte PDF generado automáticamente
└── requirements.txt
```

---

## Funcionalidades

- **Limpieza de datos**: corrección de encoding latin-1, normalización de barrios, parseo de fechas, columnas derivadas (año, mes, mortalidad)
- **Dashboard interactivo**: filtros dinámicos por año y barrio, KPIs en tiempo real
- **Visualizaciones**: tendencia temporal, distribución por tipo de accidente, top 15 barrios críticos
- **Reporte PDF automático**: portada, gráficas y tabla de KPIs generada con Matplotlib

## KPIs incluidos

| Indicador | Descripción |
|---|---|
| Total de accidentes | Conteo filtrado por año/barrio |
| Total de muertes | Suma de víctimas fatales |
| Tasa de mortalidad | % de accidentes con al menos una muerte |
| Total de heridos | Suma de heridos en el período |

---

## Stack tecnológico

| Herramienta | Uso |
|---|---|
| `pandas` | Limpieza y transformación de datos |
| `streamlit` | Dashboard web interactivo |
| `plotly` | Gráficas interactivas |
| `matplotlib` | Generación del reporte PDF |

---

## Instalación

```bash
git clone https://github.com/Ripariav/Analisis-accidentes-transito.git
cd Analisis-accidentes-transito
pip install -r requirements.txt
```

**Limpiar los datos** (si modificas el CSV original):
```bash
python src/clean_data.py
```

**Lanzar el dashboard:**
```bash
streamlit run app.py
```

**Regenerar el reporte PDF:**
Ejecuta todas las celdas del notebook `notebooks/explicacion.ipynb`

---

## Dataset

Datos de accidentalidad vial del municipio de Acacías, Meta. Fuente: registros públicos municipales.
512 registros · 2024 · 13 variables

---

*Proyecto de análisis de datos con fines educativos y de portafolio — Daniel Rivera ([@Ripariav](https://github.com/Ripariav))*
