def conversor (tipo_de_pesos, valor_dolar):
    pesos = input ("¿cuantos pesos"  +  tipo_de_pesos + "tienes?:   " )
    pesos = float(pesos)
    dolar = pesos / valor_dolar
    dolar = round (dolar, 2)
    dolar = str(dolar)
    print ("tienes $ "+ dolar +  " dolares")
    

menu = """
bienvenido al conversor de monedas

1 - pesos colombianos
2 - pesos argentinos
3 - peos mexicanos

    elige una opcion """
tipo_moneda = int(input(menu))
if tipo_moneda ==1:
   conversor(" colombianos", 3575)
elif tipo_moneda ==2:
    conversor(" argentino", 65)
    
elif tipo_moneda ==3:
    conversor(" mexicanos", 24)
     
else:
    print ("ingrese una opcion correcta por favor ")
    
     
     

