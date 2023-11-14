def resta(poly1, poly2):
    result = []
    poly2_dict = {term[1]: term[0] for term in poly2}
    
    for term1 in poly1:
        exponent = term1[1]
        coefficient1 = term1[0]
        
        if exponent in poly2_dict:
            coefficient2 = poly2_dict[exponent]
            new_coefficient = coefficient1 - coefficient2
            if new_coefficient != 0:
                result.append((new_coefficient, exponent))
        else:
            result.append(term1)
    
    for term2 in poly2:
        if term2[1] not in [term[1] for term in poly1]:
            result.append((-term2[0], term2[1]))
    
    return result

def dividir(dividend, divisor):
    if len(divisor) == 0:
        raise ValueError("El divisor no puede ser un polinomio nulo.")
    
    quotient = []
    remainder = list(dividend)

    while len(remainder) >= len(divisor):
        leading_term_dividend = remainder[0]
        leading_term_divisor = divisor[0]
        coefficient = leading_term_dividend[0] / leading_term_divisor[0]
        exponent = leading_term_dividend[1] - leading_term_divisor[1]
        quotient.append((coefficient, exponent))
        
        temp = [(coefficient * term[0], term[1] - exponent) for term in divisor]
        remainder = resta(remainder, temp)

    return "Resultado Division: Cociente: " + str(quotient) + " Resto: " + str(remainder) + "/" + str(divisor)

def remove_term(polynomial, term_to_remove):
    result = []
    for term in polynomial:
        if term != term_to_remove:
            result.append(term)
    return result

def term_exists(polynomial, term_to_find):
    for term in polynomial:
        if term == term_to_find:
            return print("termino existe")
    return print("termino no existe")


poligono1 = [(4, 2), (4, 1), (6, 0)]
poligono2 = [(2, 2), (2, 1), (2, 0)]


print("Resultado resta: " + str(resta(poligono1, poligono2)))


print(dividir(poligono1, poligono2))

coefficient_delete = float(input("Escribe el coeficiente del numero a remover: "))
exponent_delete = int(input("Escribe su exponente: "))
elejir_delete = int(input("Quieres remover un elemento del polinomio 1 o 2: "))
term_to_remove = (coefficient_delete, exponent_delete)
if elejir_delete == 1:
    result = remove_term(poligono1, term_to_remove)
    print("Poligono 1: " + str(result))

if elejir_delete == 2:
    result = remove_term(poligono2, term_to_remove)
    print("Poligono 2: " + str(result))



coefficient_check = float(input("Escribe un coeficiente del numero a buscar: "))
exponent_check = int(input("Escribe su exponente: "))
elejir_check = int(input("Quieres buscar un elemento del polinomio 1 o 2: "))
term_to_find = (coefficient_check, exponent_check)
if elejir_check == 1:
    exists = term_exists(poligono1, term_to_find)
if elejir_check == 2:
    exists = term_exists(poligono2, term_to_find)

