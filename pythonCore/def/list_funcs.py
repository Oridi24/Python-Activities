

def convert(elements:list, change_element) ->list :
    """
    Recibe una lista y una operación que convierte un elemento en otro.
    Devuelve una nueva lista, de la misma logitud y con cada elemento
    convertido en otro mediante la operación que recibe.
    """
    new_list = []
    for element in elements:
        new_list.append(change_element(element))
    return new_list


def select(elements: list, predicate)-> list:
    """
    Recibe una lista y un predicado. Devuelve una nueva lista con aquellos elementos
    que superan el test del predicado.
    """
    selected = []
    for element in elements:
        if predicate(element):
            selected.append(element)
    return selected


def compress(elements, initial_value, operation):
    """
    Recibe una secuencia de elementos, un valor inicial y 
    una función que representa una operación de combinación
    de dos elementos.
    Devuelve un solo valor comprimido
    """
    accum = initial_value
    for element in elements:
        accum = operation(accum, element)
    return accum 
 
def join(first:list, second:list, fill = None, composer = None)->list:
    """
    Recibe dos listas de igual tamaño y las unifica en una sóla lista de parejas.
    Si cualquier de las dos es la vacía, devuelve la vacía.
    Si una de las dos es menor que la otra, se rellena con `None`
    """

    def make_list(a,b):
        return [a,b]
    
    joined = []
    
    if len(first) >= len(second):
        second = second + [fill] * (len(first) - len(second))
    else:
        first = first + [fill] * (len(second) - len(first))

    if composer == None:
        composer = make_list
    
    for index, element in enumerate(first):
        joined.append(composer(element, second[index]))
    return joined
