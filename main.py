import random
import time
import streamlit as st

st.title("📚 Juegos educativos")

st.write("""
    \nDescripción del juego: 
    \n - Al inicio se otorgarán 4 palabras las cuales tendrá que memorizar en 15 segundos.
    \n - Después, tiene que escribir las palabras en el orden en que aparecieron.
    \n - Si las escribió correctamente, se añadirá otra palabra a la secuencia y tendrá que volver a escribirlas en orden, este proceso se repetirá hasta que haya 10 palabras en la secuencia.
    \n - El juego termina cuando escriba las 10 palabras en el orden correcto.
    \n - En caso de que las palabras no hayan sido escritas en el orden correcto, el juego terminará independientemente de cuantas palabras haya memorizado.
    \nREGLAS
    \n 1. No se permite escribir las palabras en ningún lado, todo tiene que ser memorizado.
    \n 2. No se puede tomar foto a la secuencia de palabras.
""")

# List of words for the game
lista_palabras = [
    "servilleta", "telefono", "herradura", "queso", "corbata",
    "lluvia", "canoa", "hormiguero", "regla", "mate",
    "calabaza", "pulgar", "elefante", "parrilla", "acordeon"
]

# Initialize session state variables
if "secuencia" not in st.session_state:
    st.session_state["secuencia"] = []
if "intento_jugador" not in st.session_state:
    st.session_state["intento_jugador"] = ""
if "juego_iniciado" not in st.session_state:
    st.session_state["juego_iniciado"] = False
if "intento_numero" not in st.session_state:
    st.session_state["intento_numero"] = 0

def mostrar_palabras():
    # Create a placeholder to show the words
    placeholder = st.empty()
    placeholder.write("### Palabras para memorizar:")
    # Show words as normal text
    placeholder.markdown("**" + ", ".join(st.session_state["secuencia"]) + "**")
    st.write("El temporizador ha comenzado. Tendrá 5 segundos para memorizar...")

    # Pause for the specified time
    time.sleep(5)  # Change this to 15 seconds for the actual game
    # Clear the placeholder after 15 seconds
    placeholder.empty()

def mostrar_juego():
    intento_jugador = st.chat_input("¿Cuáles eran las palabras de la lista? Escríbalas separadas por un espacio: ", key="input")
    
    if intento_jugador:
        st.session_state["intento_jugador"] = intento_jugador
        if intento_jugador.split() == st.session_state["secuencia"]:  # Compare with the word list
            st.write("¡Correcto!")
            if len(st.session_state["secuencia"]) == 10:
                st.write("¡Felicidades! Ha memorizado todas las palabras correctamente.")
                # Reset game after completion
                st.session_state["secuencia"].clear()
                gemerar_secuencia()  # Restart with new sequence
                st.session_state["intento_numero"] = 0  # Reset attempt number
                mostrar_palabras()  # Show new words to memorize
            else:
                # Add a new word to the sequence
                while True:
                    nueva_palabra = random.choice(lista_palabras)
                    if nueva_palabra not in st.session_state["secuencia"]:
                        st.session_state["secuencia"].append(nueva_palabra)
                        break
                mostrar_palabras()  # Show the new words to memorize
                st.session_state["intento_numero"] += 1  # Increment attempt number
        else:
            st.write("¡Incorrecto! El juego ha terminado.")
            st.session_state["juego_iniciado"] = False  # End the game

def gemerar_secuencia():
    while len(st.session_state["secuencia"]) < 4:
        palabra = random.choice(lista_palabras)
        if palabra not in st.session_state["secuencia"]:
            st.session_state["secuencia"].append(palabra)

# Welcome to the game
if st.button("Comenzar"):
    gemerar_secuencia()
    mostrar_palabras()
    st.session_state["juego_iniciado"] = True
    mostrar_juego()
else:
    if st.session_state["juego_iniciado"]:
        mostrar_juego()
