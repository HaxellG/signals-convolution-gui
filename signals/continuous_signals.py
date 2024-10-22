import numpy as np
import plotly.graph_objs as go
from scipy.interpolate import interp1d
from static.styles import (
    LIGHT_BLUE_COLOR, 
    DARK_BLUE_COLOR, 
    DARK_PURPLE_COLOR,
)
import time
import streamlit as st

Delta = 0.001

def generate_continuous_graphique(t, x_t, color, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=x_t, mode="lines", name=title, line=dict(color=color)))

    fig.update_layout(
        xaxis_title="Tiempo",
        yaxis_title="Amplitud",
        showlegend=True,
    )

    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    # Mostrar gráfico en la primera columna
    st.plotly_chart(fig, use_container_width=True)

def generate_double_continuous_graphique(t, x_t, t2, x_t2, color1, color2, title1, title2):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=x_t, mode="lines", name=title1, line=dict(color=color1)))
    fig.add_trace(go.Scatter(x=t2, y=x_t2, mode="lines", name=title2, line=dict(color=color2)))

    fig.update_layout(
        xaxis_title="Tiempo",
        yaxis_title="Amplitud",
        showlegend=True,
    )

    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    # Mostrar gráfico en la primera columna
    st.plotly_chart(fig, use_container_width=True)

def invert_continous_signal(t, x_t):
    return -t[::-1], x_t[::-1]

def generate_continous_conv(t, x_t, h, h_t):
    y_conv = np.convolve(x_t, h_t) * Delta
    t_conv = np.arange(t[0] + h[0], t[0] + h[0] + len(y_conv) * Delta, Delta)

    h, h_t = invert_continous_signal(h, h_t)
    
    interp_func = interp1d(t_conv, y_conv, bounds_error=False, fill_value=0)
    x_min = min(t.min()-5, h.min()-1)
    x_max = max(t.max()+5, h.max()+1)

    col_1, col_2 = st.columns(2)
    plot_placeholder_1 = col_1.empty()
    plot_placeholder_2 = col_2.empty()

    trace_fija = go.Scatter(
        x=t, 
        y=x_t, 
        mode='lines', 
        name='Señal Fija',
        line=dict(color=DARK_BLUE_COLOR),
    )
    trace_movil = go.Scatter(
        x=h, 
        y=h_t, 
        mode='lines', 
        name='Señal en Movimiento',
        line=dict(color=LIGHT_BLUE_COLOR),
    )

    layout_señales = go.Layout(
        xaxis=dict(showgrid=True, range=[x_min, x_max]),
        yaxis=dict(showgrid=True),
        xaxis_title="Tiempo",
        yaxis_title="Amplitud",
        title='Gráfica de la señal fija y la señal en movimiento'
    )

    # Crear la figura con ambas señales en movimiento
    fig_señales = go.Figure(data=[trace_fija, trace_movil], layout=layout_señales)

    # Rango de movimiento de la señal móvil
    shift_min = t[0] - 7 - h[0]
    shift_max = t[-1] + 7 - h[-1]

    x_full = np.arange(shift_min, shift_max, Delta)
    y_full = interp_func(x_full)

    # Crear la traza para la convolución
    trace_convolucion = go.Scatter(
        x=x_full, 
        y=y_full, 
        mode='lines', 
        name='Convolución',
        line=dict(color=DARK_PURPLE_COLOR),
    )
    layout_convolucion = go.Layout(
        xaxis=dict(showgrid=True, autorange=True),
        yaxis=dict(showgrid=True),
        xaxis_title="Tiempo",
        yaxis_title="Amplitud",
        title='Gráfica de Convolución en tiempo real'
    )

    fig_convolucion = go.Figure(data=[trace_convolucion], layout=layout_convolucion)

    plot_placeholder_2.plotly_chart(fig_convolucion, use_container_width=True, key="convolution_chart")

    # Animar la señal en movimiento (h_t)
    for i in range(len(x_full)):
        # Actualizar los valores de X para mover la señal en movimiento
        new_h = h + x_full[i]
        fig_señales.data[1].x = new_h  # Actualizamos solo la señal en movimiento

        # Renderizar la figura actualizada de las señales en movimiento
        fig_convolucion.data[0].y = y_full[:i+1]
        plot_placeholder_1.plotly_chart(fig_señales, use_container_width=True, key=f"signal_chart_{i}")

        # Actualizar la figura de convolución
        plot_placeholder_2.plotly_chart(fig_convolucion, use_container_width=True, key=f"convolution_chart_{i}")
        
        # Agregar un pequeño retardo para la animación final
        time.sleep(0.1)
