# Encuesta 
def obtener_respuesta(pregunta):
    while True:
        respuesta = input(pregunta + " ").strip().lower()
        if respuesta in ["a", "b", "c"]:
            return respuesta.upper()
        else:
            print("Respuesta incorrecta. Por favor, elige A, B o C.")

def hacer_encuesta():

    contador=0

    print("Pregunta #1")
    print("¿Qué tan satisfecho te sientes con el entrenamiento en RIWI?")
    print("A. Muy satisfecho")
    print("B. Poco satisfecho")
    print("C. Insatisfecho")
    respuesta1 = obtener_respuesta("Tu respuesta:")
    contador += 1

    print("\nPregunta #2")
    print("¿Qué tanto has aprendido con RIWI?")
    print("A. Mucho")
    print("B. Poco")
    print("C. Nada")
    respuesta2 = obtener_respuesta("Tu respuesta:")
    contador += 1

    print("\nPregunta #3")
    print("¿Recomendarías RIWI?")
    print("A. Sí, lo recomendaría")
    print("B. Poco lo recomendaría")
    print("C. No, no lo recomendaría")
    respuesta3 = obtener_respuesta("Tu respuesta:")
    contador += 1

    print("\nGracias por responder la encuesta. Aquí están tus respuestas:")
    print(f"Pregunta 1: {respuesta1}")
    print(f"Pregunta 2: {respuesta2}")
    print(f"Pregunta 3: {respuesta3}")
    print(f"Total de respuestas realizadas {contador}")

# Ejecutar la encuesta
hacer_encuesta()