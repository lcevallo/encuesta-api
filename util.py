def SplitNombres(nombre):
    u"""
    Autor original en código PHP: eduardoromero.
    https://gist.github.com/eduardoromero/8495437

    Separa los nombres y los apellidos y retorna una tupla de tres
    elementos (string) formateados para nombres con el primer caracter
    en mayuscula. Esto es suponiendo que en la cadena los nombres y
    apellidos esten ordenados de la forma ideal:

    1- nombre o nombres.
    2- primer apellido.
    3- segundo apellido.

    SplitNombres( '' )
    >>> ('Nombres', 'Primer Apellido', 'Segundo Apellido')
    """

    # Separar el nombre completo en espacios.
    tokens = nombre.split(" ")

    # Lista donde se guarda las palabras del nombre.
    names = []

    # Palabras de apellidos y nombres compuestos.
    especial_tokens = ['da', 'de', 'di', 'do', 'del', 'la', 'las',
                       'le', 'los', 'mac', 'mc', 'van', 'von', 'y', 'i', 'san', 'santa']

    prev = ""
    for token in tokens:
        _token = token.lower()

        if _token in especial_tokens:
            prev += token + " "

        else:
            names.append(prev + token)
            prev = ""

    num_nombres = len(names)
    print(f"este el total de nombres ingresados: {num_nombres}")
    nombres, apellido1, apellido2 = "", "", ""

    # Cuando no existe nombre.
    if num_nombres == 0:
        nombres = ""

    # Cuando el nombre consta de un solo elemento.
    elif num_nombres == 1:
        nombres = names[0]

    # Cuando el nombre consta de dos elementos.
    elif num_nombres == 2:
        nombres = names[0]
        apellido1 = names[1]

    # Cuando el nombre consta de tres elementos.
    elif num_nombres == 3:
        nombres = names[0]
        apellido1 = names[1]
        apellido2 = names[2]

    # Cuando el nombre consta de más de tres elementos.
    else:
        print(nombres)
        nombres = nombres.title()
        apellido1 = apellido1.title()
        apellido2 = apellido2.title()


    # Establecemos las cadenas con el primer caracter en mayúscula.
    nombres = nombres.title()
    apellido1 = apellido1.title()
    apellido2 = apellido2.title()

    return (nombres, apellido1, apellido2)