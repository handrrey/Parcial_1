import API.consumeAPI
import UI.mostrarDatos

departamento_usuario = input("Bienvenido al programa de consulta de casos de covid\nIngrese el departamento del que desea consultar los registros: ")
limite = int(input("Ingrese la cantidad de registros que desea consultar: "))

if(limite < 204):
    datosPD = API.consumeAPI.consume("departamento_nom='"+departamento_usuario+"'", limite)

    UI.mostrarDatos.printf(datosPD)

#despues del 203 se cuelga y solo me muestra alrededor de 140 asi que 203 es el limite sin importar la ciudad
else: print("El numero ingresado es muy grande para el procesamiento, ingrese un numero menor o igual a 203")