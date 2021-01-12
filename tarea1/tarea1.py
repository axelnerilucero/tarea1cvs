import pandas as pd

def leerElArchivo():
    arch = pd.read_csv('presenciaredes.csv')
    df = pd.DataFrame(arch)
    print (arch)
    print ("\n\n")

    def diferenciaSeguidoresTwitter():
        num1 =df.iloc[7]['ENERO']
        #print (num1)

        num2 =df.iloc[7]['JUNIO']
        #print (num2)

        diferencia = (int(num2)-int(num1))
        letrasOtraVez = str(diferencia)
        print ("\n\n""La diferencia de seguidores en TWITTER de enero a Junio fue de: " + letrasOtraVez + " seguidores" "\n\n")
        #conversion = int(num1.split('.')[0])

    def diferenciaVisualizacionesYoutube():

        fecha1 = df.iloc[15]['ENERO']
        fecha2 = df.iloc[15]['FEBRERO']
        fecha3 = df.iloc[15]['MARZO']
        fecha4 = df.iloc[15]['ABRIL']
        fecha5 = df.iloc[15]['MAYO']
        fecha6 = df.iloc[15]['JUNIO']
        #print ("jeje")
        date = input("Escribe el primer mes: ")
        dateUpper =date.upper()
        date2 = input("Escribe el segundo mes: ")
        date2Upper =date2.upper()


        if (dateUpper == 'ENERO' and date2Upper == 'JUNIO'):
            diferenciaY = (int(fecha6)-int(fecha1))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'ENERO' and date2Upper == 'MAYO'):
            diferenciaY = (int(fecha5)-int(fecha1))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'ENERO' and date2Upper == 'ABRIL'):
            diferenciaY = (int(fecha4)-int(fecha1))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'ENERO' and date2Upper == 'MARZO'):
            diferenciaY = (int(fecha3)-int(fecha1))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'ENERO' and date2Upper == 'FEBRERO'):
            diferenciaY = (int(fecha2)-int(fecha1))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'FEBRERO' and date2Upper == 'JUNIO'):
            diferenciaY = (int(fecha6)-int(fecha2))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'FEBRERO' and date2Upper == 'MAYO'):
            diferenciaY = (int(fecha5)-int(fecha2))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'FEBRERO' and date2Upper == 'ABRIL'):
            diferenciaY = (int(fecha4)-int(fecha2))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'FEBRERO' and date2Upper == 'MARZO'):
            diferenciaY = (int(fecha3)-int(fecha2))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'MARZO' and date2Upper == 'JUNIO'):
            diferenciaY = (int(fecha6)-int(fecha3))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'MARZO' and date2Upper == 'MAYO'):
            diferenciaY = (int(fecha5)-int(fecha3))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'MARZO' and date2Upper == 'ABRIL'):
            diferenciaY = (int(fecha4)-int(fecha3))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'ABRIL' and date2Upper == 'JUNIO'):
            diferenciaY = (int(fecha6)-int(fecha4))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'ABRIL' and date2Upper == 'MAYO'):
            diferenciaY = (int(fecha5)-int(fecha4))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")
        if (dateUpper == 'MAYO' and date2Upper == 'JUNIO'):
            diferenciaY = (int(fecha6)-int(fecha5))
            letrasOtraVez2 = str(diferenciaY)
            print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")


        #if (dateUpper == 'ENERO' and date2Upper == 'JUNIO'):
        #    diferenciaY = (int(fecha6)-int(fecha1))
        #    letrasOtraVez2 = str(diferenciaY)
        #    print ("\n\n""La diferencia de visualizaciones entre los meses seleccionados es de: " + letrasOtraVez2 + " visualizaciones""\n\n")


    def promedioCrecimientoTwitter():
        mes1 =df.iloc[8]['ENERO']
        mes2 =df.iloc[8]['FEBRERO']
        mes3 =df.iloc[8]['ABRIL']
        mes4 =df.iloc[8]['MARZO']
        mes5 =df.iloc[8]['MAYO']
        mes6 =df.iloc[8]['JUNIO']

        promedio = ((int(mes1)+int(mes2)+int(mes3)+int(mes4)+int(mes5)+int(mes6))/6)
        letrasAgain = str(promedio)
        print ("\n\n""El promedio de crecimiento de followers en Twitter durante el primer semestre fue de: " + letrasAgain + " followers al mes""\n\n")




    def promedioCrecimientoFacebook():
        month1 =df.iloc[1]['ENERO']
        month2 =df.iloc[1]['FEBRERO']
        month3 =df.iloc[1]['ABRIL']
        month4 =df.iloc[1]['MARZO']
        month5 =df.iloc[1]['MAYO']
        month6 =df.iloc[1]['JUNIO']

        promedio2 = ((int(month1)+int(month2)+int(month3)+int(month4)+int(month5)+int(month6))/6)
        letrasAgain2 = str(promedio2)
        print ("\n\n""El promedio de crecimiento de followers en Facebook durante el primer semestre fue de: " + letrasAgain2 + " followers al mes""\n\n")




    def menu():
        opc = 0
        while (opc !=1):
            print ("1. Salir")
            print ("2. Diferencia de Seguidores em twitter")
            print ("3. diferencia visualizaciones de Youtube")
            print ("4. promedio crecimiento twitter")
            print ("5. promedio crecimiento de facebook")
            opc = int(input("Dame opcion: "))
            if (opc == 2):
                diferenciaSeguidoresTwitter()
            if (opc == 3):
                diferenciaVisualizacionesYoutube()
            if (opc == 4):
                promedioCrecimientoTwitter()
            if (opc == 5):promedioCrecimientoFacebook()

    menu()

leerElArchivo()
