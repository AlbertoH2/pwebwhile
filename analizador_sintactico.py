import ply.yacc as yacc
from analizador_lexico import tokens

# Resultado del análisis
resultado_gramatica = []

# Definición de precedencia y asociatividad
precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)

# Definición de variables
nombres = {}

# Regla para la declaración de asignación
def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMA'
    nombres[t[1]] = t[3]

# Regla para la expresión
def p_declaracion_expr(t):
    'declaracion : expresion'
    t[0] = t[1]

# Regla para operaciones aritméticas
def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMA expresion
                |   expresion RESTA expresion
                |   expresion MULT expresion
                |   expresion DIV expresion
    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]

# Regla para expresiones unarias
def p_expresion_uminus(t):
    'expresion : RESTA expresion %prec UMINUS'
    t[0] = -t[2]

# Regla para expresiones agrupadas
def p_expresion_grupo(t):
    '''
    expresion  : PARIZQ expresion PARDER
               | LLAIZQ expresion LLADER
               | CORIZQ expresion CORDER
    '''
    t[0] = t[2]

# Regla para comparaciones
def p_expresion_comparacion(t):
    '''
    expresion   : expresion MENORQUE expresion 
                | expresion MAYORQUE expresion 
                | expresion MENORIGUAL expresion 
                | expresion MAYORIGUAL expresion 
                | expresion DISTINTO expresion
    '''
    if t[2] == "<": t[0] = t[1] < t[3]
    elif t[2] == ">": t[0] = t[1] > t[3]
    elif t[2] == "<=": t[0] = t[1] <= t[3]
    elif t[2] == ">=": t[0] = t[1] >= t[3]
    elif t[2] == "!=": t[0] = t[1] != t[3]

# Regla para operaciones lógicas
def p_expresion_logica(t):
    '''
    expresion   : expresion AND expresion 
                | expresion OR expresion 
    '''
    if t[2] == "AND":
        t[0] = t[1] and t[3]
    elif t[2] == "OR":
        t[0] = t[1] or t[3]

# Regla para la expresión negada
def p_expresion_negada(t):
    'expresion : NOT expresion'
    t[0] = not t[2]

# Regla para números enteros
def p_expresion_numero(t):
    'expresion : ENTERO'
    t[0] = t[1]

# Regla para cadenas
def p_expresion_string(t):
    'expresion : STRING'
    t[0] = t[1]

# Regla para identificadores
def p_expresion_identificador(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("Nombre desconocido ", t[1])
        t[0] = 0

# Regla para el bucle while
def p_while_loop(t):
    'declaracion : WHILE PARIZQ expresion MAYORQUE ENTERO PARDER LLAIZQ imprimir LLADER'
    print("Bucle while encontrado")
    t[0] = ("Bucle while encontrado",)

# Regla para imprimir
def p_imprimir(t):
    '''
    imprimir : PRINT PARIZQ STRING PARDER PUNTOCOMA
             | PRINT PARIZQ STRING SUMA ENTERO PARDER PUNTOCOMA
    '''
    pass  # Aquí podrías realizar acciones específicas si necesitas algún tipo de procesamiento especial

# Regla para manejar errores
def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintáctico de tipo {} en el valor {}".format(str(t.type), str(t.value))
    else:
        resultado = "Error sintáctico: Token inválido"
    print(resultado)
    resultado_gramatica.append(resultado)

# Instanciamos el analizador sintáctico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()
    
    # Realizar el análisis sintáctico en el código completo
    parser.parse(data)

    return resultado_gramatica

if __name__ == '__main__':
    while True:
        try:
            s = input('Ingresa el dato >>> ')
        except EOFError:
            continue
        if not s:  
            continue
        
        gram = parser.parse(s)
        print("Resultado ", gram)
        prueba_sintactica(s)
