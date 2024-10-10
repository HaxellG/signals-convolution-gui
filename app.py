import numpy as np
import streamlit as st
from static.styles import (
    CSS_STYLES,
    LIGHT_BLUE_COLOR, 
    MEDIUM_BLUE_COLOR, 
    LIGHT_PURPLE_COLOR,
)
from signals.continuous_signals import (
    generate_continuous_graphique, 
    invert_continous_signal, 
    generate_continous_conv,
)
from signals.discrete_signals import (
    generate_discrete_graphique,
    invert_discrete_signal,
    generate_discrete_conv,
)

Delta = 0.01

# Señal Continua A
ta=[0]
ta2 = np.arange(0, 3, Delta)
ta3 = np.arange(3, 5, Delta)
ta4 = [5]
ta_t = np.concatenate((ta, ta2, ta3, ta4))

xa=[0]
xa2 = 2*np.ones(len(ta2))
xa3 = (-2*np.ones(len(ta3)))
xa4=[0]
x_ta = np.concatenate((xa, xa2, xa3, xa))


# Señal Continua B
tb = [-1]
tb2 = np.arange(-1, 1, Delta)
tb3 = [1]
tb_t = np.concatenate((tb, tb2, tb3))

xb = [0]
xb2 = -(tb2*1)
xb3 = [0]
x_tb = np.concatenate((xb, xb2, xb3))


# Señal Continua C
tc = [-1]
tc2 = np.arange(-1, 1, Delta)
tc3 = np.arange(1, 3, Delta)
tc4 = np.arange(3, 5, Delta)
tc5 = [5]
tc_t = np.concatenate((tc, tc2, tc3,tc4,tc5))

xc = [0]
xc2 = 2*np.ones(len(tc2))
xc3 = (-2*tc3+4)
xc4 = -2*np.ones(len(tc4))
xc5 = [0]
x_tc = np.concatenate((xc, xc2, xc3, xc4, xc5))


# Señal Continua D
td = [-3]
td2 = np.arange(-3, 0, Delta)
td3 = np.arange(0, 3, Delta)
td4 = [3]
td_t = np.concatenate((td, td2, td3, td4))

xd=[0]
xd2 = np.exp(td2)
xd3 = np.exp(-td3)
xd4 = [0]
x_td = np.concatenate((xd, xd2, xd3, xd4))


# Señales Discretas
na = np.arange(-5, 5+1)
xn_a = np.zeros(len(na))
for i in range(len(na)):
  xn_a[i] = 6-abs(na[i])

ha = np.arange(-5, 5+1)
hn_a = np.ones(len(ha))

nb = np.arange(-2, 8+1)
xn_b = np.ones(len(nb))

hb = np.arange(-1, 9+1)
hn_b = np.zeros(len(hb))
for i in range(len(hb)):
  hn_b[i] = (9/11)**(hb[i])


MENU_OPTIONS = ["Introducción", "Señales Continuas", "Señales Discretas", "Créditos"]

st.set_page_config(layout="wide")
st.markdown(CSS_STYLES, unsafe_allow_html=True)
st.title("Convolucionador de Señales")
st.sidebar.title("MENU DE INTERACCION")
selected_option = st.sidebar.selectbox("Seleccione una opción", MENU_OPTIONS)

if selected_option == "Introducción":
    st.write("Bienvenido a esta interfaz gráfica de convolución de señales. Esta herramienta le permitirá explorar y entender mejor el proceso de convolución en diferentes tipos de señales.")
    st.write("Utilice el menú de la izquierda para navegar entre las diferentes secciones y funcionalidades de la aplicación.")

elif selected_option == "Señales Continuas":
    # Mover las selecciones del sidebar a la página principal
    column_1, column_2 = st.columns(2)
    
    with column_1:
        st.markdown("**Señal x(t)**")
        x_t = st.selectbox("Señal x(t)", ["Seleccione la señal a graficar", "A", "B", "C", "D"])
    with column_2:
        st.markdown("**Señal h(t)**")
        h_t = st.selectbox("Señal h(t)", ["Seleccione la señal a graficar", "A", "B", "C", "D"])

    if x_t == "Seleccione la señal a graficar" or h_t == "Seleccione la señal a graficar":
        st.error("Seleccione ambas señales para continuar")
    else:
        if x_t == "A":
            x = ta_t
            y = x_ta
        elif x_t == "B":
            x = tb_t
            y = x_tb
        elif x_t == "C":
            x = tc_t
            y = x_tc
        elif x_t == "D":
            x = td_t
            y = x_td

        if h_t == "A":
            h = ta_t
            z = x_ta
        elif h_t == "B":
            h = tb_t
            z = x_tb
        elif h_t == "C":
            h = tc_t
            z = x_tc
        elif h_t == "D":
            h = td_t
            z = x_td

        st.markdown("**Señal a invertir**")
        signal_to_invert = st.selectbox("", ["Seleccione la señal a invertir", "x(t)", "h(t)"])

        column_1, column_2 = st.columns(2)
        with column_1:
            st.markdown("**Gráfica de x(t)**")
            generate_continuous_graphique(x, y, MEDIUM_BLUE_COLOR, "x(t)")
        with column_2:
            st.markdown("**Gráfica de h(t)**")
            generate_continuous_graphique(h, z, LIGHT_PURPLE_COLOR, "h(t)")

        if signal_to_invert == "Seleccione la señal a invertir":
            st.error("Seleccione la señal a invertir")
        else:
            if signal_to_invert == "x(t)":
                st.markdown("**Gráfica de la señal invertida**")
                t_inv, x_inv = invert_continous_signal(x, y)
                generate_continuous_graphique(t_inv, x_inv, LIGHT_BLUE_COLOR, "x(t) invertida")
                st.markdown("### Proceso de convolución ###")
                generate_continous_conv(h, z, x, y)
            elif signal_to_invert == "h(t)":
                st.markdown("**Gráfica de la señal invertida**")
                t_inv, x_inv = invert_continous_signal(h, z)
                generate_continuous_graphique(t_inv, x_inv, LIGHT_BLUE_COLOR, "h(t) invertida")
                st.markdown("### Proceso de convolución ###")
                generate_continous_conv(x, y, h, z)

elif selected_option == "Señales Discretas":
    st.markdown("**Seleccione la señal a graficar**")
    selected_signal = st.selectbox("Señal x[n]", ["Seleccione la señal a graficar", "A", "B"])

    if selected_signal == "Seleccione la señal a graficar":
        st.error("Debe seleccionar las señal a graficar para continuar")
    else:
        if selected_signal == "A":
            column_1, column_2 = st.columns(2)
            with column_1:
                x = na
                y = xn_a
                graf = generate_discrete_graphique(na, xn_a, "x[n]", MEDIUM_BLUE_COLOR)
                st.plotly_chart(graf, use_container_width=True)
            with column_2:
                h = ha
                z = hn_a
                graf = generate_discrete_graphique(ha, hn_a, "h[n]", LIGHT_PURPLE_COLOR)
                st.plotly_chart(graf, use_container_width=True)

        elif selected_signal == "B":
            column_1, column_2 = st.columns(2)
            with column_1:
                x = nb
                y = xn_b
                graf = generate_discrete_graphique(nb, xn_b, "x[n]", MEDIUM_BLUE_COLOR)
                st.plotly_chart(graf, use_container_width=True)
            with column_2:
                h = hb
                z = hn_b
                graf = generate_discrete_graphique(hb, hn_b, "h[n]", LIGHT_PURPLE_COLOR)
                st.plotly_chart(graf, use_container_width=True)

        st.markdown("**Seleccione la señal a invertir**")
        signal_to_invert = st.selectbox("Cual señal desea invertir", ["Seleccione la señal a invertir", "x[n]", "h[n]"])
        
        if signal_to_invert == "Seleccione la señal a invertir":
            st.error("Debe seleccionar la señal a invertir para continuar")
        else:
            if signal_to_invert == "x[n]":
                x_inv, y_inv = invert_discrete_signal(x, y)
                inv = generate_discrete_graphique(x_inv, y_inv, "x[n] invertida", LIGHT_BLUE_COLOR)
                st.plotly_chart(inv, use_container_width=True)

                generate_discrete_conv(h, x, z, y)
            elif signal_to_invert == "h[n]":
                h_inv, z_inv = invert_discrete_signal(h, z)
                inv = generate_discrete_graphique(h_inv, z_inv, "h[n] invertida", LIGHT_BLUE_COLOR)
                st.plotly_chart(inv, use_container_width=True)
                generate_discrete_conv(x, h, y, z)

elif selected_option == "Créditos":
    st.markdown("Aca va el texto de créditos")
    st.markdown(".....")