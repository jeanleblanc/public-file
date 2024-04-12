
"""
 # Python syntaxe : 
     ## Python indentation
         Very important -> indique un block de code (utilisation general x4)
     ## Variables
         crée quand on leur assigne une valeur (... = "")
    ## Comments
        "#" / voir comment c'est fait
# Variables
    Crée en attribuant une valeur (=)
    elles ont des "types" qui peuvent être spécifié  => pour connaitre le type on peut utiliser la fonction "type()
    elles sont sensible aux Maj/min (A diff a)
    
    # Noms de variables
    doit commencer avec une lettre ou un underscore
    que des caractères alphanumérique + underscore
    ne peut pas être un mot clefs python
    
    # Multiple values
    on peut assigner plusieur valeurs a plusieur variables en une ligne
    ex : x, y, z = 'ok', 'non', 'yes'
    on peut egalement assigner plusieur variables a la même valeurs (en une ligne) => x = y = z
    Il existe un moyen d'unpack les list (voir plus tard)
    
    # Output variables
    permette de sortir l'info d'une variables (print())
    on peut sortir plusieur variable en un print séparé d'une virgule (ou une + mais va 
    etre utiliser comme un opérateur mathématique peut pas être utiliser sur  des variables de diff types)
    
    # Global variables
    variables crée exterieur a une fonction
    -> Variables local est crée dans une fonction est valables que dans ccelle-ci
    On peut utiliser le mot clefs "global" pour crée une variables global a l'interieur d'une fonction
    
# DATA TYPE

    Variable stock des donnée de différents type associé a differentes action
    Ceux préconsu par défauts : 
    
    - Text Type:	str
    - Numeric Types:	int, float, complex
    - Sequence Types:	list, tuple, range
    - Mapping Type:	dict
    - Set Types:	set, frozenset
    - Boolean Type:	bool
    - Binary Types:	bytes, bytearray, memoryview
    - None Type:	NoneType
    
    automatiquement spéciffié mais peut l'etre fait mannuellement (str("helloworld"))
    
# Numbers
    int, float, complex
    # int = entier +/- taille illimité
    # Float = avec une ou plus décimal, on peut aussi utiliser "e" ou "E" pour indiquer une puissance de 10
    # complex : j is the imaginary part
    on peut convertir une setup une autre variable et en spécifiant le type.
    
    # Random
    pas de tel fonction, mais un module appelé "random" voir plus tard

# strings
    stock des caractère alphabetique, est immubable
    qualifié par '' ou ""
    pour en plusieur ligne on peut utiliser ''' /// ''' ou """  """
    
    Les strings sont des tableaux de bytes qui represente des caractères unicode, dans python un caractères seul est simplement un string de longueur 1
    Les caractères sont indexer et peuvent être retrouver a l'aide de [] ; a noter que le premier caractère est en position 0
    on peut loop dans une string (voir "for loop")    
    
    la longueur d'une string peut être retrouver avec len()
    
    on peut verifier si un caractère est presant dans une string avec "in". et en utilisant "if/else"
    regarder si quelque chose n'est pas presant : "no in"
    
    # Slicing strings
        on peut retrouver un range de caractère avec la slice synthax : 
        print(b[x:y]) x inclu, y non, si x est le premier caractère de la string il n'a pas besoin d'être spécifié
        pareil si y est le dernier.
        indice négatif : World : o position x = -4, W en position y = 0 ...
        
    #  Modifier une strings : 
        upper case : .upper()
        lower case : .lower()
        enlever l'espace au début ou à la fin: .strip()
        remplacer un caractère : .replace("x", "y") tous les x par y
        séparé, fait devenir une liste avec le séparateur spécifié : .split(",")
        
    # combiner les strings avec +
    a = jkjkjl    b = fkdsjklf     c = a + b
    
    # String format
    on peut pas combiner string et num avec le +
    maisn on peut le faire avec "format()"
    arguments : {} dans le string, remplacer par ce qu'il y a dans le format()
        possibilité d'ajouter une indexation dans l'arguments ex : {1}
    
    # \\
        pour utiliser quellque chose d'illegal dans une string on le met après un \\
    
    # Mehtods
        https://www.w3schools.com/python/python_strings_methods.asp
        you can use to modify your strings, create a new value, do not modify directly de strings
    
# Booleans
    represente une valeur sur deux (true or false)
    en python on peut comparer plusieur valeurs pour que le script renvoie une reponsonse boleene
    On peut evaluer une valeur avec bool(), tout est vrai sauf les strings vide ou le num 0, les liste vide
    aussi faux les __len__ qui retourne à 0
    
    Built-in fonction qui renvoie des boolene valeurs (ex : isinstance(x, int) => test si x est un entier)
    
# Operators  
    pour faire des opération sur les variables et les valeurs
    Divisé en 8 groupes : 
    - Arithmetic operators : valeurs numérique, mathematique basiques
    - Assignment operators : pour associé valeurs aux variables
    - Comparison operators : pour comparer deux valeurs
    - Logical operators : combiner phrases logiques
    - Identity operators : comparer des objets en fonction de leurs type et de leurs location
    - Membership operators : tester si une séquence est présente dans un objet
    - Bitwise operators : comparer binary num
    - Operator precedence : decrive l'ordre d'application des operateur
    https://www.w3schools.com/python/python_operators.asp 
    
# Lists
    manière de stocker plusieur items dans une variable
    une des quatres manière de stocker des collection d'info (avec tuple, set, dictionnaires)
    crée avec des [] : var = ['this', 'is', 'list'], info de n'importe quel types.

    les list sont ordonée (on un ordre qui ne changera pas, si on ajoute un truc, il est placé à la fin)
    on peut retrouver chaque objet avec print(obj[x]),
    modifiable(on peut changer ajouter ou enlever un item) et accepte les doublons (parce que ordonée)

    La longueur d'une list (nb d'objets dedans) peut être retrouver grace à len()
    Le type (type()) de la variable est "list", possibilité de le spécifié : 
        TL = list(('objet', 'other'))
    
    Pour changer la valeur d'un item specifique on le précise en créean une nouvelle variable
        var = ['list', 'de', 'trucs']
        var[2] = 'choses'
    De la même manière on peut changer un rang avec[3:4]
    
    pour inserer un nouvelles objet on utilise la méthode .inster(x, items) (x la pos)
    pour juste en ajouter un nv (à la fin)  : 
    pour combiné 2 list : .extend(listenplus) mais marche aussi si c'est pas une liste (array)
    
    pour enlever un objets spécifique .remove("objet") (si plus d'un "objet" retire le premier)
    enelevr a un indexe spécifique : .pop(x) si x pas spécifié retire le dernier
    meme fonction le mot clefs del
        del varlist[0] si indexe pas spécifié del la list complete
    Pour vider la list on peut utiliser la methode .clear
    
    On peut loop en utilisant une for loop
    
    Pour crée une nouvelle list a partir d'une ancienne : on utilise comprhension
        newlist = ["expression" for "item" in "iterable" if "condition" == True]
        
    methode : .sort() va renvoyer la list dans l'odre alphabetique (ou numérique)
    si on veut dans l'autre sens on peut utiliser l'arguments "reverse = True"
"""
var = "salut comment ca va ?"
print(var)