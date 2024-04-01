import ply.lex as lex

resultado_lexema = []

# Palabras reservadas
reserved = {
    'FOR': 'FOR', 
    'DO': 'DO', 
    'WHILE': 'WHILE', 
    'IF': 'IF', 
    'ELSE': 'ELSE',
    'STATIC': 'STATIC',
    'VOID': 'VOID',
    'PUBLIC': 'PUBLIC',
    'LENGTH': 'LENGTH', 
    'PRINT': 'PRINT', 
    'MAIN': 'MAIN',
    'SYSTEM': 'SYSTEM',
    'OUT': 'OUT',
}

# Tokenss
tokens = [
    'IDENTIFICADOR',
    'ENTERO',
    'STRING',
    'ASIGNAR',
    
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',
    
    'PLUSPLUS',
    'MINUSMINUS',
    
    #Logica
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MAYORQUE',
    'MENORIGUAL',
    'MAYORIGUAL',
    'DISTINTO',
    
    # Simbolos
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',
    
    # Otros
    'PUNTO',
    'PUNTOCOMA',
    'COMA',
    'COMDOB',
    'MAYORDER', #>>
    'MAYORIZQ', #<<
]+ list(reserved.values())


# Expresiones regulares para tokens simples
t_STRING = r'(\'[^\']*\'|\"[^\"]*\")'
t_ASIGNAR = r'='

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_POTENCIA = r'(\*\*|\^)'
t_MODULO = r'\%'

t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'\-\-'

t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_DISTINTO = r'!='

t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'

t_PUNTO = r'\.'
t_PUNTOCOMA = r';'
t_COMA = r','
t_COMDOB = r'\"'
t_MAYORDER = r'>>'
t_MAYORIZQ = r'<<'


# Regla para identificadores
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z]*'
    if t.value.upper() in reserved:  # Verificar si es una palabra reservada
        t.type = reserved[t.value.upper()]  # Asignar el tipo de token correspondiente a la palabra reservada
    else:
        t.type = 'IDENTIFICADOR'  # Asignar el tipo de token como IDENTIFICADOR si no es una palabra reservada
    return t

# Regla para números
def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar caracteres como espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print("Carácter inválido '%s' en la posición %d" % (t.value[0], t.lexpos))
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
        resultado_lexema.append(estado)
    return resultado_lexema

# Construir el analizador léxico
lexer = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("Ingrese: ")
        prueba(data)
        print(resultado_lexema)
