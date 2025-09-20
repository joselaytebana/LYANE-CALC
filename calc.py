from tkinter import *
from tkinter import filedialog
import os



root=Tk()
root.title("LYANE CALC")
root.resizable(False, False)

frame=Frame(root)
frame.pack()

#pantalla
numero_pantalla=IntVar()
mi_pantalla=StringVar()

pantalla=Label(frame, textvariable=numero_pantalla, font=("cambria", 29, "bold"), justify="right", background="light blue")
pantalla.grid(row=0, column=0, sticky="we", columnspan=5)

#botones

confi={
    "font":("cambria", 18)
}


#funciones
contador=""
num=StringVar()
def pantallita(num):
    global contador

    if num=="0":

        if contador =="":
            return
        num= num
    elif num in [",", "."]:
        cc="\r"
        num= f" {'0' + num if contador=='' else(cc if '.' in contador else(cc if ',' in contador else('.' if num=='.' else ',')))}"

    contador+=num.strip()
    print(f"{len(contador)} numero de digitos en pantalla.....", end="\r")
    if len(contador)>19:
        numero_pantalla.set(">>Max 19 digi<<")
        contador=""
        return
    numero_pantalla.set(contador.strip())
    #return num


def signo():
    global contador
    global result
    
    if contador != "":
        contador= float(contador) * -1
        numero_pantalla.set(str(contador))
    elif contador =="" and result !=0:
        result= float(result) * -1
        numero_pantalla.set(str(result))
vez=0
def borrado():
    global contador
    global vez
    global result
    numero_pantalla.set(0)
    contador=""
    if vez >=1:
        result=0
    vez+=1


def importar():
    sumando=None
    divisor=None
    producto=None
    minuendo=None
            

    pp=os.path.join(__file__).split("\\")
    user= pp[2]

    archivo= filedialog.askopenfile(title="Elije un archivo que contenga ejercicios", initialdir=os.path.join(f"c:\\users\\{user}\\desktop\\"), filetypes=(("archivos de texto", ".txt"), ("archivos de word microsof", ".docx"), ("archivos pdfs", ".pdf")))

    if archivo:
        import re
        el_archi=str(archivo).split("'")[1]

        def nuevo_archivo(sumando, producto, divisor, minuendo):
            operaciones=[sumando, producto, divisor, minuendo]
            operaciones=[cada for cada in operaciones if cada]
            nombre=el_archi.split('/')[-1].split('.')[0] + " resuelto"
            with open(f"{nombre}.txt", "w", encoding="utf-8")as txt:
                for operacion in operaciones:
                    txt.write(f"""
                        operacion {operacion[0]}
                        {f'{" * " if operacion[0]=="multiplicacion" else(" + " if operacion[0]=="suma" else(" - " if operacion[0]=="resta" else " ÷ "))}'.join(operacion[1])} = {operacion[-1]}
                    """)
                export.config(state="disable")
                os.startfile(f"{nombre}.txt")

        if "." in el_archi:
            if el_archi.split(".")[-1]=="txt":
                with open(el_archi, "r", encoding="utf-8")as txt:
                    for linea in txt:
                        if "+" in linea.lower() or "suma" in linea.lower():
                            datos= re.findall(r"-?\d+", linea)
                            resultado= sum([float(numeros) for numeros in datos])
                            sumando= ("suma", [cada for cada in datos], resultado)

                        elif "-" in linea.lower() or "resta" in linea.lower() or "restar" in linea.lower():
                            datos= re.findall(r"-?\d+", linea)
                            if len(datos)>1:
                                resultado=0
                                for i in range(0, len(datos)):
                                    rre= resultado if resultado !=0 else float(datos[i]) - float(datos[i+1 if i+1 <len(datos) else 0])
                                    resultado=rre
                            minuendo= ("resta", datos, resultado)

                        elif "*" in linea or "multiplica" in linea.lower() or "multiplicacion" in linea.lower() or "producto" in linea.lower():
                            datos= re.findall(r"-?\d+", linea)
                            if len(datos)>1:
                                num=[float(cada) for cada in datos]
                                resultado=[]
                                for numero in num:
                                    resultado.append((numero * resultado[-1] if resultado else numero * 1))
                                resultado=resultado[-1]
                                producto= ("multiplicaion", datos, resultado)

                        elif "/" in linea or "divide" in linea.lower() or "division" in linea.lower() or "cociente" in linea.lower() or "÷" in linea or "entre" in linea.lower():
                            datos= re.findall(r"-?\d+", linea)
                            if len(datos)>1:
                                resultado=None
                                num=[float(numero) for numero in datos]
                                if len(num)==2:
                                    resultado= num[0] / num[1]
                                elif len(num)==3:
                                    resultado= num[0] / num[1]
                                    resultado = resultado / num[2]
                                    divisor= ("division", datos, resultado)

            elif el_archi.split(".")[-1]=="docx":
                from docx import Document
                contenido=""
                archiv= Document(el_archi)
                for paragraph in archiv.paragraphs:
                    contenido += paragraph.text + "\n"
                for cada in contenido.split("\n"):
                    if "+" in cada.lower() or "suma" in cada.lower():
                        datos= re.findall(r"-?\d+", cada)
                        resultado=sum([float(numeros) for numeros in datos])
                        sumando= ("suma", [cada for cada in datos], resultado)


                    elif "-" in cada.lower() or "resta" in cada.lower() or "restar" in linea.lower():
                        datos= re.findall(r"-?\d+", cada)
                        if len(datos)>1:
                            resultado=0
                            for i in range(0, len(datos)):
                                rre= resultado if resultado !=0 else float(datos[i]) - float(datos[i+1 if i+1 <len(datos) else 0])
                                resultado=rre
                            minuendo= ("resta", datos, resultado)

                    elif "*" in cada or "multiplica" in cada.lower() or "multiplicacion" in cada.lower() or "producto" in cada.lower():
                        datos= re.findall(r"-?\d+", cada)
                        if len(datos)>1:
                            num=[float(cada) for cada in datos]
                            resultado=[]
                            for numero in num:
                                resultado.append((numero * resultado[-1] if resultado else numero * 1))
                            resultado=resultado[-1]
                            producto= ("multiplicaion", datos, resultado)


                    elif "/" in linea or "divide" in linea.lower() or "division" in linea.lower() or "cociente" in linea.lower() or "÷" in linea or "entre" in linea.lower():
                        datos= re.findall(r"-?\d+", linea)
                        if len(datos)>1:
                            resultado=None
                            num=[float(numero) for numero in datos]
                            if len(num)==2:
                                resultado= num[0] / num[1]
                            elif len(num)==3:
                                resultado= num[0] / num[1]
                                resultado = resultado / num[2]
                            divisor= ("division", datos, resultado)


            elif el_archi.split(".")[-1]=="pdf":
                import pdfplumber
                contenido=""
                with pdfplumber.open(el_archi)as pdf:
                    for page in pdf.pages:
                        contenido += page.extract_text() + "\n"

                for cada in contenido.split("\n"):
                    if "+" in cada.lower() or "suma" in cada.lower():
                        datos= re.findall(r"-?\d+", cada)
                        resultado=sum([float(numeros) for numeros in datos])
                        sumando= ("suma", [cada for cada in datos], resultado)


                    elif "-" in cada.lower() or "resta" in cada.lower() or "restar" in cada.lower():
                        datos= re.findall(r"-?\d+", cada)
                        if len(datos)>1:
                            resultado=0
                            for i in range(0, len(datos)):
                                rre= resultado if resultado !=0 else float(datos[i]) - float(datos[i+1 if i+1 <len(datos) else 0])
                                resultado=rre
                            minuendo= ("resta", datos, resultado)

                    elif "*" in cada or "multiplica" in cada.lower() or "multiplicacion" in cada.lower() or "producto" in cada.lower():
                        datos= re.findall(r"-?\d+", cada)
                        if len(datos)>1:
                            num=[float(cada) for cada in datos]
                            resultado=[]
                            for numero in num:
                                resultado.append((numero * resultado[-1] if resultado else numero * 1))
                            resultado=resultado[-1]
                            producto= ("multiplicacion", datos, resultado)


                    elif "/" in linea or "divide" in linea.lower() or "division" in linea.lower() or "cociente" in linea.lower() or "÷" in linea or "entre" in linea.lower():
                        datos= re.findall(r"-?\d+", linea)
                        if len(datos)>1:
                            resultado=None
                            num=[float(numero) for numero in datos]
                            if len(num)==2:
                                resultado= num[0] / num[1]
                            elif len(num)==3:
                                resultado= num[0] / num[1]
                                resultado = resultado / num[2]
                                divisor= ("division", datos, resultado)



        if sumando or minuendo or producto or divisor:
            def escritura(texto, indice=0):
                if indice<len(texto):
                    export.config(text=export.cget("text") + texto[indice])
                    root.after(100, escritura, texto, indice+1)

            def llamda(sumando, producto, divisor, minuendo):
                root.after(3000, lambda:nuevo_archivo(sumando, producto, divisor, minuendo))
                export.config(text="")
                escritura("Cargando...")

            export=Button(frame, text=f"Descargar '{el_archi.split('/')[-1].split('.')[0]}' resuelto", font=("cambria", 15), relief="groove", bg="light blue", command=lambda:llamda(sumando, producto, divisor, minuendo), state="normal")
            export.grid(row=6, column=0, columnspan=4, sticky="we")
        else:
            from tkinter import messagebox
            messagebox.showerror(title="Error", message=f"El archivo '{el_archi.split('/')[-1].split('.')[0]}' no contiene operaciones compatibles con LYANE CALC. Busque otro")

#operaciones
operacion=None
valores=None
result=0

def sumar():
    global contador
    global valores
    global operacion
    global result


    if contador!= "":
        if valores:
            valores = float(valores) + float(contador.strip())
            valores=f"{valores:.2f}"
            valores= float(valores)
            numero_pantalla.set(valores)
            contador=""
            operacion="suma"
        elif not valores and result==0:
            valores= float(contador)
            valores=f"{valores:2f}"
            valores= float(valores)
            numero_pantalla.set(valores)
            contador=""
            operacion="suma"
        elif not valores and result !=0:
            valores= float(contador)
            valores=f"{valores:.2f}"
            valores= float(valores) + result
            result= valores
            numero_pantalla.set(result)
            contador=""
            operacion="suma"
    elif contador=="":
        result=result
        operacion="suma"


def restar():
    global contador
    global result
    global valores
    global operacion

    if contador !="":
        if valores:
            valores= float(valores) - float(contador.strip())
            valores= f"{valores:.2f}"
            result=float(valores)
            numero_pantalla.set(result)
            contador=""
            operacion="resta"
        elif not valores and result ==0:
            valores= float(contador.strip())
            valores= f"{valores:.2f}"
            result=float(valores)
            numero_pantalla.set(result)
            contador=""
            operacion="resta"
        elif not valores and result !=0:
            cc= float(contador.strip())
            cc= result - cc
            cc= f"{cc:.2f}"
            result= float(cc)
            numero_pantalla.set(result)
            contador=""
            operacion="resta"
    elif contador=="":
        operacion="resta"

def multip():

    global contador
    global result
    global valores
    global operacion

    if contador !="":
        if valores:
            cc= float(contador.strip())
            cc= float(valores) * cc
            valores= f"{cc:.2f}"
            result= float(valores)
            numero_pantalla.set(result)
            valores= None
            contador=""
            operacion="multi"

        elif not valores and result==0:
            valores= float(contador.strip())
            valores= f"{valores:.2f}"
            result= float(valores)
            numero_pantalla.set(result)
            contador=""
            operacion="multi"
        
        elif not valores and result !=0:
            valores= float(contador.strip())
            cc= result * valores
            valores=f"{cc:.2f}"
            result=float(valores)
            numero_pantalla.set(result)
            contador=""
            operacion="multi"
    elif contador=="":
        operacion="multi"

def div():
    global contador
    global result
    global valores
    global operacion

    if contador !="":
        if valores:
            cc= float(contador.strip())
            cc= float(valores) / cc
            valores= f"{cc:.2f}"
            result= float(valores)
            numero_pantalla.set(result)
            valores= None
            contador=""
            operacion="divi"

        elif not valores and result==0:
            valores= float(contador.strip())
            valores= f"{valores:.2f}"
            result= float(valores)
            numero_pantalla.set(result)
            contador=""
            operacion="divi"
        
        elif not valores and result !=0:
            valores= float(contador.strip())
            cc= result / valores
            valores=f"{cc:.2f}"
            result=float(valores)
            numero_pantalla.set(result)
            contador=""
            operacion="divi"
    elif contador=="":
        operacion="divi"




def iguala():
    global contador
    global valores
    global result
    global operacion
    print(f"{valores} valores")
    print(f"{contador} contador")
    print(f"{operacion} operacion")
    print(f"{result} result")

    

    if operacion=="suma":
        if valores:
                
            if result==0:
                cc= float(contador)
                cc= cc + valores
                cc=f"{cc:.2f}"
                cc=float(cc)
                result=cc 
                numero_pantalla.set(result)
                valores=None
                print(f"contador es {contador} y resultado es {result}")
                contador=""
                operacion=None

            elif result !=0:
                cc= valores + result
                cc= f"{cc:.2f}"
                result=float(cc)
                numero_pantalla.set(result)
                print(f"contador es {contador} y resultado es {result}")

                contador=""
                valores=None
                operacion=None

        elif not valores:
            if result !=0:
                valores= float(contador.strip())
                cc= valores + result
                cc= f"{cc:.2f}"
                result=float(cc)
                numero_pantalla.set(result)
                print(f"contador es {contador} y resultado es {result}")
                contador=""
                valores=None
                operacion=None
   
    elif operacion=="resta":
        if valores:
            if result==0:
                cc= valores - float(contador.strip())
                cc= f"{cc:.2f}"
                result=float(cc)
                numero_pantalla.set(result)
                contador=""
                valores=None
                operacion=None


            elif result !=0:
                cc= float(contador.strip())
                cc= result - float(cc)
                cc= f"{cc:.2f}"
                result=float(cc)
                numero_pantalla.set(result)
                contador=""
                valores=None
                operacion=None

        elif not valores:
            if result==0:
                cc= float(contador.strip() if contador else numero_pantalla.get()) 
                cc= f"{cc:.2f}"
                result=float(cc)
                numero_pantalla.set(result)
                operacion=None
                contador=""
            elif result !=0:
                cc= result - float(contador.strip() if contador else numero_pantalla.get())
                cc=f"{cc:.2f}"
                result=float(cc)
                numero_pantalla.set(result)
                operacion=None
                contador=""


    elif operacion=="multi":
        if valores:
            if result==0:
                valores= float(valores)
                valores=f"{valores:.2f}"
                result=float(valores)
                numero_pantalla.set(result)
                valores= None
                operacion=None
                contador=""

            elif result !=0:
                valores= float(valores)
                cc= valores * float(contador)
                valores= f"{cc:.2f}"
                result= float(valores)
                print(f"{result} el ultimo resultado")
                numero_pantalla.set(result)
                contador=""                
                valores=None
                operacion=None
            
        elif not valores:
            if result ==0:
                cc= float(contador.strip())
                valores= f"{cc:.2f}"
                result= float(valores)
                numero_pantalla.set(result)
                operacion=None
                contador=""
            elif result !=0:
                cc= float(contador.strip())
                cc= result * cc
                valores=f"{cc:.2f}"
                result= float(valores)
                numero_pantalla.set(result)
                operacion=None
                contador=""


    elif operacion=="divi":
        if valores:
            if result==0:
                valores= float(valores)
                valores=f"{valores:.2f}"
                result=float(valores)
                numero_pantalla.set(result)
                valores= None
                operacion=None
                contador=""

            elif result !=0:
                valores= float(valores)
                cc= valores / float(contador)
                valores= f"{cc:.2f}"
                result= float(valores)
                print(f"{result} el ultimo resultado")
                numero_pantalla.set(result)
                contador=""                
                valores=None
                operacion=None
            
        elif not valores:
            if result ==0:
                cc= float(contador.strip())
                valores= f"{cc:.2f}"
                result= float(valores)
                numero_pantalla.set(result)
                operacion=None
                contador=""
            elif result !=0:
                cc= float(contador.strip())
                cc= result / cc
                valores=f"{cc:.2f}"
                result= float(valores)
                numero_pantalla.set(result)
                operacion=None
                contador=""



Bora=Button(frame, text="C", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:borrado())
Bora.grid(row=1, column=0)
def acti(event):
    Bora.config(background="white", foreground="red")
def desac(event):
    Bora.config(background="light blue", foreground="black")
Bora.bind("<Enter>", acti)
Bora.bind("<Leave>", desac)


punto=Button(frame, text=".", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:pantallita("."))
punto.grid(row=1, column=1)

def pulsado(event):
    global contador
    nombre= event.keysym
    if nombre =="period":
        pantallita(".")
    if nombre== "comma":
        importar()
    if nombre in [str(i) for i in range(0, 10)]:
        pantallita(nombre)
    if nombre=="plus":
        sumar()
    if nombre=="Return":
        iguala()
    if nombre=="minus":
        restar()
    if nombre=="BackSpace":
        borrado()
    if nombre=="asterisk":
        multip()
    if nombre=="slash":
        div()



root.bind("<Key>", pulsado)


coma=Button(frame, text="Importar\narchivo", font=("cambria", 14), relief="flat", width=5, height=1, background="light blue", command=lambda:importar())
coma.grid(row=1, column=2, sticky="wens")

arh= Menu(root, tearoff=False)
arh.add_command(label="Puedes impotar un archivo que contenga una de las operaciones que aparecen en la calculadora y te la resolvereremos", font=("cambria", 13))
cantidad=0
def act(event):
    global cantidad
    from plyer import notification
    if cantidad <2:
        notification.notify("LyANE CALC", "Puedes impotar un archivo que contenga una de las operaciones que aparecen en la calculadora y te la resolvereremos", timeout=10)
        cantidad+=1

def des(event):
    arh.unpost

coma.bind("<Enter>", act)
coma.bind("<Leave>", des)

uno=Button(frame, text="1", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:pantallita("1"))
uno.grid(row=2, column=0)

dos=Button(frame, text="2", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:pantallita("2"))
dos.grid(row=2, column=1)


tres=Button(frame, text="3", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:pantallita("3"))
tres.grid(row=2, column=2)



division=Button(frame, text="÷", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:div())
division.grid(row=1, column=3)


cuatro=Button(frame, text="4", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:pantallita("4"))
cuatro.grid(row=3, column=0)



cinco=Button(frame, text="5", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:pantallita("5"))
cinco.grid(row=3, column=1)



seis=Button(frame, text="6", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:pantallita("6"))
seis.grid(row=3, column=2)



multi=Button(frame, text="×", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:multip())
multi.grid(row=2, column=3)


siete=Button(frame, text="7", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:pantallita("7"))
siete.grid(row=4, column=0)



ocho=Button(frame, text="8", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:pantallita("8"))
ocho.grid(row=4, column=1)




nueve=Button(frame, text="9", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:pantallita("9"))
nueve.grid(row=4, column=2)




suma=Button(frame, text="+", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:sumar())
suma.grid(row=3, column=3)



mas_menos=Button(frame, text="+/-", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:signo())
mas_menos.grid(row=5, column=0)

cero=Button(frame, text="0", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:pantallita("0"))
cero.grid(row=5, column=1)



menos=Button(frame, text="-", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:restar())
menos.grid(row=4, column=3)

igual=Button(frame, text="=", font=("cambria", 26, "bold"), relief="flat", width=5, height=1, background="light blue", command=lambda:iguala())
igual.grid(row=5, column=2, columnspan=2, sticky="we")











root.mainloop()