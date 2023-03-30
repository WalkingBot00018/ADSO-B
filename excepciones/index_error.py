def acceso_lista(lista,indice):
    try:
        return lista[indice]
    except IndexError:
        print(f"error el indice {indice} sta fuera de rango es erroneo")
mi_lista=[1, 2, 3, 4, 5]
print(acceso_lista(mi_lista, 10))

