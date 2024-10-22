import numpy as np
import streamlit as st
from static.styles import (
    CSS_TOPBAR_STYLES,
    CSS_SIDEBARD_STYLES,
    CSS_CREDITS_STYLES,
    LIGHT_BLUE_COLOR, 
    MEDIUM_BLUE_COLOR, 
    LIGHT_PURPLE_COLOR,
    DARK_BLUE_COLOR,
    DARK_PURPLE_COLOR,
    build_custom_error,
)
from signals.continuous_signals import (
    generate_continuous_graphique, 
    invert_continous_signal, 
    generate_continous_conv,
    generate_double_continuous_graphique,
)
from signals.discrete_signals import (
    generate_discrete_graphique,
    invert_discrete_signal,
    generate_discrete_conv,
)

Delta = 0.01

# Señal Continua A
ta = [0]
ta2 = np.arange(0, 3, Delta)
ta3 = np.arange(3, 5, Delta)
ta4 = [5]
ta_t = np.concatenate((ta, ta2, ta3, ta4))

xa=[0]
xa2 = 2*np.ones(len(ta2))
xa3 = (-2*np.ones(len(ta3)))
xa4 = [0]
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


MENU_OPTIONS = ["Introducción", "Señales Continuas", "Señales Discretas", "Bonus", "Créditos"]

st.set_page_config(layout="wide")
st.markdown(CSS_TOPBAR_STYLES, unsafe_allow_html=True)
st.markdown(CSS_SIDEBARD_STYLES, unsafe_allow_html=True)
st.markdown(f"""
    <h1 style='text-align: center; color: {DARK_BLUE_COLOR};'>Interfaz de Convolución de Señales</h1>
""", unsafe_allow_html=True)
st.sidebar.title("MENU DE INTERACCION")
selected_option = st.sidebar.selectbox("Seleccione una opción", MENU_OPTIONS)

if selected_option == "Introducción":
    st.subheader("🌟 Bienvenido a la Interfaz Gráfica de Convolución de Señales")
    st.markdown("""
    En esta aplicación interactiva, **explorarás y entenderás** el proceso de **convolución** en señales 
    tanto en el **dominio del tiempo continuo** como en el **dominio del tiempo discreto**. 
    ¡Profundicemos más en estos conceptos y aprendamos cómo las señales se combinan mediante la convolución! 🎯
    """)
    
    column_1, column_2 = st.columns(2)

    with column_1:
        st.markdown(f"""
            <h3 style='text-align: center; color: {DARK_PURPLE_COLOR};'>📈 ¿Qué es una señal?</h3>
        """, unsafe_allow_html=True)

        st.write("""
        Las señales son representaciones matemáticas que **varían en el tiempo** o el espacio, 
        transportando información.
        """)
        with st.expander("Tipos de señales"):

            st.write("""
            Existen dos tipos fundamentales:
            - **Señales de tiempo continuo**: Definidas para cada valor en un rango continuo de tiempo.
            - **Señales de tiempo discreto**: Definidas solo en momentos específicos o discretos de tiempo.
            Estas señales pueden representar diferentes fenómenos, como sonido, luz o datos de sensores.
            """)

    with column_2:
        st.markdown(f"""
            <h3 style='text-align: center; color: {DARK_PURPLE_COLOR};'>🔄 ¿Qué es la convolución?</h3>
        """, unsafe_allow_html=True)
        st.write("""
        En ingeniería, la **convolución** es clave para analizar cómo un sistema modifica una señal de entrada.
        Se utiliza cuando conocemos la **señal de entrada** y la **respuesta al impulso** de un sistema, 
        permitiéndonos calcular su **señal de salida**
        """)
        st.write("**Dominios**:")
        st.markdown("""
        - En el **dominio continuo**, la convolución se representa como una **integral** de productos de las señales a lo largo del tiempo.
        - En el **dominio discreto**, la convolución se representa como una **suma** de productos de las señales en diferentes momentos.
        """)

    st.markdown("""
    Utilice el **menú de la izquierda** para navegar entre las diferentes secciones y explorar todas las funcionalidades de esta aplicación. 
    ¡Sumérgete en el fascinante mundo de las señales y la convolución! 🚀
    """)

elif selected_option == "Señales Continuas":
    st.markdown("<br><br>", unsafe_allow_html=True)
    column_1, column_2 = st.columns(2)
    
    with column_1:
        st.markdown(f"""
            <h3 style='color: {DARK_BLUE_COLOR};'>Señal x(t)</h3>
        """, unsafe_allow_html=True)
        x_t = st.selectbox("Señal x(t)", ["Seleccione la señal a graficar", "A", "B", "C", "D"])
    with column_2:
        st.markdown(f"""
            <h3 style='color: {DARK_BLUE_COLOR};'>Señal h(t)</h3>
        """, unsafe_allow_html=True)
        h_t = st.selectbox("Señal h(t)", ["Seleccione la señal a graficar", "A", "B", "C", "D"])

    if x_t == "Seleccione la señal a graficar" or h_t == "Seleccione la señal a graficar":
        CSS_CUSTOM_ERROR_STYLES = build_custom_error('⚠️ Seleccione ambas señales para continuar')
        st.markdown(CSS_CUSTOM_ERROR_STYLES, unsafe_allow_html=True)
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

        column_1, column_2 = st.columns(2)
        with column_1:
            generate_continuous_graphique(x, y, MEDIUM_BLUE_COLOR, "x(t)")
        with column_2:
            generate_continuous_graphique(h, z, LIGHT_PURPLE_COLOR, "h(t)")

        st.markdown(f"""
            <h3 style='text-align: center;color: {DARK_PURPLE_COLOR};'>Señal a invertir</h3>
        """, unsafe_allow_html=True)
        signal_to_invert = st.selectbox("", ["Seleccione la señal a invertir", "x(t)", "h(t)"])

        if signal_to_invert == "Seleccione la señal a invertir":
            CSS_CUSTOM_ERROR_STYLES = build_custom_error('⚠️ Seleccione la señal a invertir')
            st.markdown(CSS_CUSTOM_ERROR_STYLES, unsafe_allow_html=True)
        else:
            if signal_to_invert == "x(t)":
                st.markdown("<br><br>", unsafe_allow_html=True)
                st.markdown(f"""
                    <h5 style='color: {DARK_BLUE_COLOR};'>Gráfica de la señal invertida</h3>
                """, unsafe_allow_html=True)
                t_inv, x_inv = invert_continous_signal(x, y)
                generate_continuous_graphique(t_inv, x_inv, LIGHT_BLUE_COLOR, "x(t) invertida")
                st.markdown(f"""
                    <h2 style='text-align: center; color: {DARK_BLUE_COLOR};'>Proceso de convolución</h3>
                """, unsafe_allow_html=True)
                generate_continous_conv(h, z, x, y)
            elif signal_to_invert == "h(t)":
                st.markdown("<br><br>", unsafe_allow_html=True)
                st.markdown(f"""
                    <h5 style='color: {DARK_BLUE_COLOR};'>Gráfica de la señal invertida</h3>
                """, unsafe_allow_html=True)
                t_inv, x_inv = invert_continous_signal(h, z)
                generate_continuous_graphique(t_inv, x_inv, LIGHT_BLUE_COLOR, "h(t) invertida")
                st.markdown(f"""
                    <h2 style='text-align: center; color: {DARK_BLUE_COLOR};'>Proceso de convolución</h3>
                """, unsafe_allow_html=True)
                generate_continous_conv(x, y, h, z)

elif selected_option == "Señales Discretas":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
            <h3 style='color: {DARK_PURPLE_COLOR};'>Seleccione el par de señales a grafica</h3>
        """, unsafe_allow_html=True)
    selected_signal = st.selectbox("Señal x[n]", ["Seleccione la señal a graficar", "A", "B"])

    if selected_signal == "Seleccione la señal a graficar":
        CSS_CUSTOM_ERROR_STYLES = build_custom_error('⚠️ Debe seleccionar las señal a graficar para continuar')
        st.markdown(CSS_CUSTOM_ERROR_STYLES, unsafe_allow_html=True)
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

        st.markdown(f"""
            <h3 style='text-align: center;color: {DARK_PURPLE_COLOR};'>Seleccione la señal a invertir</h3>
        """, unsafe_allow_html=True)
        signal_to_invert = st.selectbox("Cual señal desea invertir", ["Seleccione la señal a invertir", "x[n]", "h[n]"])
        
        if signal_to_invert == "Seleccione la señal a invertir":
            CSS_CUSTOM_ERROR_STYLES = build_custom_error('⚠️ Debe seleccionar la señal a invertir para continuar')
            st.markdown(CSS_CUSTOM_ERROR_STYLES, unsafe_allow_html=True)
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

elif selected_option == "Bonus":
    def u(t):
        return np.where(t >= 0, 1, 0)
    Delta = 0.01

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
            <h3 style='color: {DARK_PURPLE_COLOR};'>Seleccione el par de señales a graficar</h3>
        """, unsafe_allow_html=True)
    selected_signal = st.selectbox("Señal x[n]", ["Seleccione la señal a graficar", "A", "B", "C"])

    if selected_signal == "Seleccione la señal a graficar":
        CSS_CUSTOM_ERROR_STYLES = build_custom_error('⚠️ Debe seleccionar las señal a graficar para continuar')
        st.markdown(CSS_CUSTOM_ERROR_STYLES, unsafe_allow_html=True)
    else:
        if selected_signal == "A":
            column_1, column_2 = st.columns(2)
            with column_1:
                tx1 = np.arange(-1-Delta, 5 + Delta, Delta)
                cont2_x1 = np.exp(-3/4 * tx1) * (u(tx1 + 1) - u(tx1 - 5))
                x = tx1
                y = cont2_x1
                generate_continuous_graphique(x, y, MEDIUM_BLUE_COLOR, "x(t)")
                
            with column_2:
                th1 = np.arange(0-Delta, 5 + Delta, Delta)
                cont2_h1 = np.exp(4/5 * th1) * u(th1)
                h = th1
                z = cont2_h1
                generate_continuous_graphique(h, z, LIGHT_PURPLE_COLOR, "h(t)")
            
            st.markdown(f"""
            <h3 style='text-align: center;color: {DARK_PURPLE_COLOR};'>Resultado de la Convolución</h3>
            """, unsafe_allow_html=True)

            ya = np.convolve(cont2_h1, cont2_x1) * Delta
            tmin = np.min(tx1) + np.min(th1)
            tmax = np.max(tx1) + np.max(th1)
            ta = np.arange(tmin, tmax + Delta, Delta)

            tx1 = np.arange(-1, 5+Delta, Delta)
            tx2 = np.arange(5, 6+Delta, Delta)
            tx = np.concatenate((tx1,tx2))
            x_tx1 = (20/31)*np.exp((4/5)*tx1)*(np.exp(31/20) - np.exp(-31/20*tx1))
            x_tx2 = (20/31)*np.exp((4/5)*tx2)*(np.exp(31/20)-np.exp(-31/4))
            x_t = np.concatenate((x_tx1,x_tx2))
            
            generate_double_continuous_graphique(ta[:len(ya)], ya, tx, x_t, DARK_PURPLE_COLOR, LIGHT_BLUE_COLOR, "Python", "Analitico")
        elif selected_signal == "B":
            column_1, column_2 = st.columns(2)
            with column_1:
                tx2 = np.arange(-4, 4 + Delta, Delta)
                cont2_x2 = np.exp(tx2) * (u(-tx2) - u(-tx2 - 3)) + np.exp(-tx2) * (u(tx2) - u(tx2 - 3))
                x = tx2
                y = cont2_x2
                generate_continuous_graphique(x, y, MEDIUM_BLUE_COLOR, "x(t)")
                
            with column_2:
                th2 = np.arange(-2, 6 + Delta, Delta)
                cont2_h2 = np.exp(-5/7 * th2) * u(th2 + 1)
                h = th2
                z = cont2_h2
                generate_continuous_graphique(h, z, LIGHT_PURPLE_COLOR, "h(t)")
            
            st.markdown(f"""
            <h3 style='text-align: center;color: {DARK_PURPLE_COLOR};'>Resultado de la Convolución</h3>
            """, unsafe_allow_html=True)

            y = np.convolve(cont2_x2, cont2_h2) * Delta
            tmin = np.min(tx2) + np.min(th2)
            tmax = np.max(tx2) + np.max(th2)

            t = np.arange(tmin, tmax + Delta, Delta)
            tx1 = np.arange(-4, -1+Delta, Delta)
            tx2 = np.arange(-1, 2+Delta, Delta)
            tx3 = np.arange(2, 8+Delta, Delta)
            tx = np.concatenate((tx1,tx2,tx3))
            x_tx1 = (7/12)*np.exp((-5/7)*tx1)*(np.exp(((12/7)*tx1) + (12/7)) - np.exp(-36/7))
            x_tx2 = ((7/12)*np.exp((-5/7)*tx2)*(1-np.exp(-36/7)))-((7/2)*np.exp((-5/7)*tx2)*(np.exp(((-2/7)*(tx2+1))) - 1) )
            x_tx3 = (7/12)*np.exp((-5/7)*tx3)*((1-np.exp((-36/7))))-(7/2)*np.exp((-5/7)*tx3)*(np.exp(-6/7)-1)
            x_t = np.concatenate((x_tx1,x_tx2,x_tx3))
            generate_double_continuous_graphique(t[:len(y)], y, tx, x_t, DARK_PURPLE_COLOR, LIGHT_BLUE_COLOR, "Python", "Analitico")
        
        elif selected_signal == "C":
            column_1, column_2 = st.columns(2)
            with column_1:
                tx3 = np.arange(-2, 5 + Delta, Delta)
                cont2_x3 = u(tx3 + 1) - u(tx3 - 3)
                x = tx3
                y = cont2_x3
                generate_continuous_graphique(x, y, MEDIUM_BLUE_COLOR, "x(t)")
                
            with column_2:
                th3 = np.arange(-4, 3 + Delta, Delta)
                cont2_h3 = np.exp(th3) * u(1 - th3)
                h = th3
                z = cont2_h3
                generate_continuous_graphique(h, z, LIGHT_PURPLE_COLOR, "h(t)")
            
            st.markdown(f"""
            <h3 style='text-align: center;color: {DARK_PURPLE_COLOR};'>Resultado de la Convolución</h3>
            """, unsafe_allow_html=True)

            y = np.convolve(cont2_x3, cont2_h3) * Delta
            tmin = np.min(tx3) + np.min(th3)
            tmax = np.max(tx3) + np.max(th3)

            t = np.arange(tmin, tmax + Delta, Delta)

            tx1 = np.arange(-4, 0+Delta, Delta)
            tx2 = np.arange(0, 4+Delta, Delta)
            tx = np.concatenate((tx1,tx2))
            x_tx1 = np.exp(tx1+1)-np.exp(tx1-3)
            x_tx2 = np.exp(1)-np.exp(tx2-3)
            
            x_t = np.concatenate((x_tx1,x_tx2))

            generate_double_continuous_graphique(t[:len(y)], y, tx, x_t, DARK_PURPLE_COLOR, LIGHT_BLUE_COLOR, "Python", "Analitico")


elif selected_option == "Créditos":
    st.markdown(CSS_CREDITS_STYLES, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    column_1, column_2 = st.columns(2)
    with column_1:
        st.markdown("""
        <div class="custom-column">
        <h3 class="custom-header">Desarrolladores</h3>
        - Emmanuel Cabrera Janer<br>
        - Haxell Gómez Lara<br>
        - Nikolas Pedraza Wilson
        </div>
        """, unsafe_allow_html=True)

    with column_2:
        st.markdown("""
        <div class="custom-column custom-offset"> <!-- Aplicar el margen superior aquí -->
        <h3 class="custom-header">Profesor Supervisor</h3>
        - PhD Juan Tello Portillo
        </div>
        """, unsafe_allow_html=True)

    column_3, column_4 = st.columns(2)
    with column_3:
        st.markdown("""
        <div class="custom-column custom-offset">
        <h3 class="custom-header">Universidad del Norte</h3>
        - Departamento de Ingeniería Eléctrica y Electrónica
        </div>
        """, unsafe_allow_html=True)

    with column_4:
        st.markdown("""
        <div class="custom-column"> <!-- Aplicar el margen superior aquí -->
        <h3 class="custom-header">Tecnologías Utilizadas</h3>
        - Python: Lenguaje de programación<br>
        - Streamlit: Framework para la creación de interfaces gráficas web<br>
        - HTML: Lenguaje para crear el esquema básico de la página<br>
        - CSS: Lenguaje para personalizar los estilos de la interfaz
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="custom-footer">
        Esta interfaz fue presentada como parte del segundo laboratorio del curso de Señales y Sistemas para el año académico 2024-03
        </div>
    """, unsafe_allow_html=True)
