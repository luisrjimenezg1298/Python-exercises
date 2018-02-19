

#Solo funciona con mayusculas#
#Creditos Totales Por Cuatrimestre
pctcred=21
sctcred=20
tctcred=19
cctcred=19
qctcred=18
sexctcred=14
sepctcred=15
#Creditos Totales Por Cuatrimestre

#Valores Literales
A=4
a=4
B=3
b=3
C=2
c=2
F=0
f=0
#Valores Literales

tcred=0
tptos=0
indcuatr=0
indicacum=0
valmatr=0
#Primer Cuatrimestre (Materias)------------------------------
FC=3
SO=3
HU=2
RC=2
PC=5
OA=1
EC=2
IN=3
#segundo Cuatrimestre (Materias)------------------------------
HD=2
EF=2
CB=4
FR=3
SO2=3
SI=3
#tercer Cuatrimestre (Materias)------------------------------
SO3=3
FE=4
FP=4
PyE=2
Adm1=3
#cuarto Cuatrimestre (Materias)------------------------------
CyE=4
SSO=4
HE1=4
Mtdi=2
EC2=2
#quinto Cuatrimestre (Materias)------------------------------
FS=3
CF=4
SA=3
IGP=3
EC3=2
qcIN5=3
#sexto Cuatrimestre (Materias)------------------------------
HE2=3
SR=4
GPT=3
EMP=2
TOEIC=2
#septimo Cuatrimestre (Materias)------------------------------
SAR=5
ALSI=3
ES=3
PFT=4

cont=0
lista=[]
#Variables
#Pidiendo Datos
nombre=input("Ingresa tu Nombre: ")
matricula=str(input("Ingresa tu Matricula: "))
valmatr=str(input("Valida tu matricula una vez mas: "))
#Pidiendo Datos
while (valmatr!=matricula):
    

        valmatr=str(input("*Matricula Incorrecta*..Valida tu matricula: "))
        (valmatr==matricula)
#Validacion De Matricula

while True:
  a=str(input("Desea calcular nuevo cuatrismestre?(s=Si,n=No): "))
  if a == "s":
      cont+=1
      cuatrimestre=int(input("Ingresa el CUATRIMESTRE a calcular: "))
      print("")
      print("")
      print("")
      print("")
      print("***************************CALCULA TU INDICE***************************")
      print("")
      print("Nombre: ",nombre)
      print("Matricula: ",matricula)
      print("Cuatrimestre: ",cuatrimestre)
      print("")
      print("")
      #Calculo de Cuatrimestres
      if int(cuatrimestre==1):
        print("***************************PRIMER CUATRIMESTRE****************************")
        print("")
        print("                     Ingrese su Calificacion: A,B,C,F")
        print("")
          
        pcFC=(input("Fundamentos Del Computador: "))
        if (pcFC=="A")   or (pcFC=="a"):
             PCfc=A
             pcFC=FC*A
        elif (pcFC=="B") or (pcFC=="b"):
             pcFC=B
             pcFC=FC*B
        elif (pcFC=="C") or (pcFC=="c"):
             pcFC=C
             pcFC=FC*C
        elif (pcFC=="F") or (pcFC=="f"):
             pcFC=F
             pcFC=FC*F
               
        pcSO=(input("Sistemas Operativos 1:      "))
        if (pcSO=="A")   or (pcSO=="a"):
             pcSO=A
             pcSO=SO*A
        elif (pcSO=="B") or (pcSO=="b"):
             pcSO=B
             pcSO=SO*B
        elif (pcSO=="C") or (pcSO=="c"):
             pcSO=C
             pcSO=SO*C
        elif (pcSO=="F") or (pcSO=="f"):
             pcSO=F
             pcSO=SO*F
        
               
        pcHU=(input("Historia Universal:         "))
        if (pcHU=="A")   or (pcHU=="a"):
             pcHU=A
             pcHU=HU*A
        elif (pcHU=="B") or (pcHU=="b"):
             pcHU=HU*B
        elif (pcHU=="C") or (pcHU=="c"):
             pcHU=HU*C
        elif (pcHU=="F") or (pcHU=="f"):
             pcHU=HU*F
          
               
        pcRC=(input("Redaccion Castellana:       "))
        if (pcRC=="A")   or (pcHU=="a"):
             pcRC=A
             pcRC=RC*A
        elif (pcRC=="B") or (pcRC=="b"):
             pcRC=B
             pcRC=RC*B
        elif (pcRC=="C") or (pcRC=="c"):
             pcRC=C
             pcRC=RC*C
        elif (pcRC=="F") or (pcRC=="f"):
             pcRC=F
             pcRC=RC*F
         
          
        pcPC=(input("Pre-Calculo:                "))
        if (pcPC=="A")   or (pcPC=="a"):
             pcPC=A
             pcPC=PC*A
        elif (pcPC=="B") or (pcPC=="b"):
             pcPC=B
             pcPC=PC*B
        elif (pcPC=="C") or (pcPC=="c"):
             pcPC=C
             pcPC=PC*C
        elif (pcPC=="F") or (pcPC=="f"):
             pcPC=F
             pcPC=PC*F
         
               
        pcOA=(input("Orientacion Academica:      "))
        if (pcOA=="A")   or (pcOA=="a"):
             pcOA=A
             pcOA=OA*A
        elif (pcOA=="B") or (pcOA=="b"):
             pcOA=B
             pcOA=OA*B
        elif (pcOA=="C") or (pcOA=="c"):
             pcOA=C
             pcOA=OA*C
        elif (pcOA=="F") or (pcOA=="f"):
             pcOA=F
             pcOA=OA*F
        
        pcEC=(input("Etica:                      "))
        if (pcEC=="A")   or (pcEC=="a"):
             pcEC=A
             pcEC=EC*A
        elif (pcEC=="B") or (pcEC=="b"):
             pcEC=B
             pcEC=EC*B
        elif (pcEC=="C") or (pcEC=="c"):
             pcEC=C
             pcEC=EC*C
        elif (pcEC=="F") or (pcEC=="f"):
             pcEC=F
             pcEC=EC*F
          
               
        pcIN=(input("Ingles Nivel 1-3:           "))
        if (pcIN=="A")   or (pcIN=="a"):
             pcIN=A
             pcIN=IN*A
        elif (pcIN=="B") or (pcIN=="b"):
             pcIN=B
             pcIN=IN*B
        elif (pcIN=="C") or (pcIN=="c"):
             pcIN=C
             pcIN=IN*C
        elif (pcIN=="F") or (pcIN=="f"):
             pcIN=F
             pcIN=IN*F
        
          
        print("")
        print("")
        indcuatr=round((pcFC+pcSO+pcHU+pcRC+pcPC+pcOA+pcEC+pcIN)/pctcred,1)
        #indacumpc=indcuatr
        lista.append(indcuatr)
        
        #indicacum=float(indacumpc)
        
        print("INDICE CUATRIMESTRAL = ",indcuatr,"          ","INDICE ACUMULADO = ",indicacum)
          
      
      elif int(cuatrimestre==2):
        print("***************************SEGUNDO CUATRIMESTRE**************************")
        print("")
        print("                     Ingrese su Calificacion: A,B,C,F")
        print("")
        
        scHD=(input("Historia Dominicana:     "))
        if (scHD=="A")   or (scHD=="a"):
             scHD=A
             scHD=HD*A
        elif (scHD=="B") or (scHD=="b"):
             scHD=B
             scHD=HD*B
        elif (scHD=="C") or (scHD=="c"):
             scHD=C
             scHD=HD*C
        elif (scHD=="F") or (scHD=="f"):
             scHD=F
             scHD=HD*F
             
        scEF=(input("Educacion Fisica:        "))
        if (scEF=="A")   or (scEF=="a"):
             scEF=A
             scEF=EF*A
        elif (scEF=="B") or (scEF=="b"):
             scEF=B
             scEF=EF*B
        elif (scEF=="C") or (scEF=="c"):
             scEF=C
             scEF=EF*C
        elif (scEF=="F") or (scEF=="f"):
             scEF=F
             scEF=EF*F
        
               
        scCB=(input("Contabilidad:            "))
        if (scCB=="A")   or (scCB=="a"):
             scCB=A
             scCB=CB*A
        elif (scCB=="B") or (scCB=="b"):
             scCB=B
             scCB=CB*B
        elif (scCB=="C") or (scCB=="c"):
             scCB=C
             scCB=CB*C
        elif (scCB=="F") or (scCB=="f"):
             scCB=F
             scCB=CB*F
          
               
        scIN2=(input("Ingles Nivel 4-6:        "))
        if (scIN2=="A")   or (scIN2=="a"):
             scIN2=A
             scIN2=IN*A
        elif (scIN2=="B") or (scIN2=="b"):
             scIN2=B
             scIN2=IN*B
        elif (scIN2=="C") or (scIN2=="c"):
             scIN2=C
             scIN2=IN*C
        elif (scIN2=="F") or (scIN2=="f"):
               scIN2=F
               scIN2=IN*F
         
          
        scFR=(input("Fundamentos De Redes:    "))
        if (scFR=="A")   or (scFR=="a"):
             scFR=A
             scFR=FR*A
        elif (scFR=="B") or (scFR=="b"):
             scFR=B
             scFR=FR*B
        elif (scFR=="C") or (scFR=="c"):
             scFR=C
             scFR=FR*C
        elif (scFR=="F") or (scFR=="f"):
             scFR=F
             scFR=FR*F
         
               
        scSO2=(input("Sistemas Operativos 2:   "))
        if (scSO2=="A")   or (scSO2=="a"):
             scSO2=A
             scSO2=SO2*A
        elif (scSO2=="B") or (scSO2=="b"):
             scSO2=B
             scSO2=SO2*B
        elif (scSO2=="C") or (scSO2=="c"):
             scSO2=C
             scSO2=SO2*C
        elif (scSO2=="F") or (scSO2=="f"):
             scSO2=F
             scSO2=SO2*F
        
        scSI=(input("Seguridad Informatica:   "))
        if (scSI=="A")   or (scSI=="a"):
             scSI=A
             scSI=SI*A
        elif (scSI=="B") or (scSI=="b"):
             scSI=B
             scSI=SI*B
        elif (scSI=="C") or (scSI=="c"):
             scSI=C
             scSI=SI*C
        elif (scSI=="F") or (scSI=="f"):
             scSI=F
             scSI=SI*F
        
        print("")
        print("")
        indcuatr=round((scHD+scEF+scCB+scIN2+scFR+scSO2+scSI)/sctcred,1)
        #indacumsc=indcuatr
        #indicacum=indacumsc
        lista.append(indcuatr)
          
        print("INDICE CUATRIMESTRAL = ",indcuatr,"          ","INDICE ACUMULADO = ",indicacum)
          
      elif int(cuatrimestre==3):
        print("***************************TERCER CUATRIMESTRE**************************")
        print("")
        print("                     Ingrese su Calificacion: A,B,C,F")
        print("")
        
        tcSO3=(input("Sistemas Operativos 3:        "))
        if (tcSO3=="A")   or (tcSO3=="a"):
             tcSO3=A
             tcSO3=SO3*A
        elif (tcSO3=="B") or (tcSO3=="b"):
             tcSO3=B
             tcSO3=SO3*B
        elif (tcSO3=="C") or (tcSO3=="c"):
             tcSO3=C
             tcSO3=SO3*C
        elif (tcSO3=="F") or (tcSO3=="f"):
             tcSO3=F
             tcSO3=SO3*F
             
        tcFE=(input("Fundamentos De Enrutamiento:  "))
        if (tcFE=="A")   or (tcFE=="a"):
             tcFE=A
             tcFE=FE*A
        elif (tcFE=="B") or (tcFE=="b"):
             tcFE=B
             tcFE=FE*B
        elif (tcFE=="C") or (tcFE=="c"):
             tcFE=C
             tcFE=FE*C
        elif (tcFE=="F") or (tcFE=="f"):
             tcFE=F
             tcFE=FE*F
      
               
        tcFP=(input("Fundamentos De Programacion:  "))
        if (tcFP=="A")   or (tcFP=="a"):
             tcFP=A
             tcFP=FP*A
        elif (tcFP=="B") or (tcFP=="b"):
             tcFP=FP*B
        elif (tcFP=="C") or (tcFP=="c"):
             tcFP=FP*C
        elif (tcFP=="F") or (tcFP=="f"):
             tcFP=FP*F
        
               
        tcPyE=(input("Probabilidad Y Estadistica:   "))
        if (tcPyE=="A")   or (tcPyE=="a"):
             tcPyE=A
             tcPyE=PyE*A
        elif (tcPyE=="B") or (tcPyE=="b"):
             tcPyE=B
             tcPyE=PyE*B
        elif (tcPyE=="C") or (tcPyE=="c"):
             tcPyE=C
             tcPyE=PyE*C
        elif (tcPyE=="F") or (tcPyE=="f"):
             tcPyE=F
             tcPyE=PyE*F
       
        
        tcadm1=(input("Administracion 1:             "))
        if (tcadm1=="A")   or (tcadm1=="a"):
             tcadm1=A
             tcadm1=Adm1*A
        elif (tcadm1=="B") or (tcadm1=="b"):
             tcadm1=B
             tcadm1=Adm1*B
        elif (tcadm1=="C") or (tcadm1=="c"):
             tcadm1=C
             tcadm1=Adm1*C
        elif (tcadm1=="F") or (tcadm1=="f"):
             tcadm1=F
             tcadm1=Adm1*F
       
               
        tcIN3=(input("Ingles Nivel 7-9:             "))
        if (tcIN3=="A")   or (tcIN3=="a"):
             tcIN3=A
             tcIN3=IN*A
        elif (tcIN3=="B") or (tcIN3=="b"):
             tcIN3=B
             tcIN3=IN*B
        elif (tcIN3=="C") or (tcIN3=="c"):
             tcIN3=C
             tcIN3=IN*C
        elif (tcIN3=="F") or (tcIN3=="f"):
             tcIN3=F
             tcIN3=IN*F
       
          
        print("")
        print("")
        indcuatr=round((tcSO3+tcFE+tcFP+tcPyE+tcadm1+tcIN3)/tctcred,1)
        #indacumtc=indcuatr
        #indicacum=indacumtc
        lista.append(indcuatr)
        print("INDICE CUATRIMESTRAL = ",indcuatr,"          ","INDICE ACUMULADO = ",indicacum)
          
          
      elif int(cuatrimestre==4):
        print("***************************CUARTO CUATRIMESTRE***************************")
        print("")
        print("                     Ingrese su Calificacion: A,B,C,F")
        print("")
        ccCyE=(input("Conmutacion y Enrutamiento:              "))
        if (ccCyE=="A")   or (ccCyE=="a"):
             ccCyE=A
             ccCyE=CyE*A
        elif (ccCyE=="B") or (ccCyE=="b"):
             ccCyE=B
             ccCyE=CyE*B
        elif (ccCyE=="C") or (ccCyE=="c"):
             ccCyE=C
             ccCyE=CyE*C
        elif (ccCyE=="F") or (ccCyE=="f"):
             ccCyE=F
             ccCyE=CyE*F
             
        ccSSO=(input("Seguridad De Sistemas Operativos:        "))
        if (ccSSO=="A")   or (ccSSO=="a"):
             ccSSO=A
             ccSSO=SSO*A
        elif (ccSSO=="B") or (ccSSO=="b"):
             ccSSO=B
             ccSSO=SSO*B
        elif (ccSSO=="C") or (ccSSO=="c"):
             ccSSO=C
             ccSSO=SSO*C
        elif (ccSSO=="F") or (ccSSO=="f"):
             ccSSO=F
             ccSSO=SSO*F
      
               
        ccHE1=(input("Hacker Etico 1:                          "))
        if (ccHE1=="A")   or (ccHE1=="a"):
             ccHE1=A
             ccHE1=HE1*A
        elif (ccHE1=="B") or (ccHE1=="b"):
             ccHE1=HE1*B
        elif (ccHE1=="C") or (ccHE1=="c"):
             ccHE1=HE1*C
        elif (ccHE1=="F") or (ccHE1=="f"):
             ccHE1=HE1*F
        
             
        ccMtdi=(input("Metodologia De La Investigacion:         "))
        if (ccMtdi=="A")   or (ccMtdi=="a"):
             ccMtdi=A
             ccMtdi=Mtdi*A
        elif (ccMtdi=="B") or (ccMtdi=="b"):
             ccMtdi=B
             ccMtdi=Mtdi*B
        elif (ccMtdi=="C") or (ccMtdi=="c"):
             ccMtdi=C
             ccMtdi=Mtdi*C
        elif (ccMtdi=="F") or (ccMtdi=="f"):
             ccMtdi=F
             ccMtdi=Mtdi*F
       
          
        ccEC2=(input("Etica 2:                                 "))
        if (ccEC2=="A")   or (ccEC2=="a"):
             ccEC2=A
             ccEC2=EC2*A
        elif (ccEC2=="B") or (ccEC2=="b"):
             ccEC2=B
             ccEC2=EC2*B
        elif (ccEC2=="C") or (ccEC2=="c"):
             ccEC2=C
             ccEC2=EC2*C
        elif (ccEC2=="F") or (ccEC2=="f"):
             ccEC2=F
             ccEC2=EC2*F
       
               
        ccIN4=(input("Ingles Nivel 10-12:                      "))
        if (ccIN4=="A")   or (ccIN4=="a"):
             ccIN4=A
             ccIN4=IN*A
        elif (ccIN4=="B") or (ccIN4=="b"):
             ccIN4=B
             ccIN4=IN*B
        elif (ccIN4=="C") or (ccIN4=="c"):
             ccIN4=C
             ccIN4=IN*C
        elif (ccIN4=="F") or (ccIN4=="f"):
             ccIN4=F
             ccIN4=IN*F
       
        
        print("")
        print("")
        indcuatr=round((ccCyE+ccSSO+ccHE1+ccMtdi+ccEC2+ccIN4)/cctcred,1)
        #indacumcc=indcuatr
        #indicacum=indacumcc
        lista.append(indcuatr)
        print("INDICE CUATRIMESTRAL = ",indcuatr,"          ","INDICE ACUMULADO = ",indicacum)
          
       
      elif int(cuatrimestre==5):
        print("***************************QUINTO CUATRIMESTRE***************************")
        print("")
        print("                     Ingrese su Calificacion: A,B,C,F")
        print("")  
        qcFS=(input("Fundamento De Seguridad:        "))
        if (qcFS=="A")   or (qcFS=="a"):
             qcFS=A
             qcFS=FS*A
        elif (qcFS=="B") or (qcFS=="b"):
             qcFS=B
             qcFS=FS*B
        elif (qcFS=="C") or (qcFS=="c"):
             qcFS=C
             qcFS=FS*C
        elif (qcFS=="F") or (qcFS=="f"):
             qcFS=F
             qcFS=FS*F
             
        qcCF=(input("Computacion Forense:            "))
        if (qcCF=="A")   or (qcCF=="a"):
             qcCF=A
             qcCF=CF*A
        elif (qcCF=="B") or (qcCF=="b"):
             qcCF=B
             qcCF=CF*B
        elif (qcCF=="C") or (qcCF=="c"):
             qcCF=C
             qcCF=CF*C
        elif (qcCF=="F") or (qcCF=="f"):
             qcCF=F
             qcCF=CF*F
      
               
        qcSA=(input("Seguridad De Aplicaciones:      "))
        if (qcSA=="A")   or (qcSA=="a"):
             qcSA=A
             qcSA=SA*A
        elif (qcSA=="B") or (qcSA=="b"):
             qcSA=SA*B
        elif (qcSA=="C") or (qcSA=="c"):
             qcSA=SA*C
        elif (qcSA=="F") or (qcSA=="f"):
             qcSA=SA*F
        
               
        qcIGP=(input("Int. Gerencia de Proyectos:     "))
        if (qcIGP=="A")   or (qcIGP=="a"):
             qcIGP=A
             qcIGP=IGP*A
        elif (qcIGP=="B") or (qcIGP=="b"):
             qcIGP=B
             qcIGP=IGP*B
        elif (qcIGP=="C") or (qcIGP=="c"):
             qcIGP=C
             qcIGP=IGP*C
        elif (qcIGP=="F") or (qcIGP=="f"):
             qcIGP=F
             qcIGP=IGP*F
         
          
        qcEC3=(input("Etica 3:                        "))
        if (qcEC3=="A")   or (qcEC3=="a"):
             qcEC3=A
             qcEC3=EC3*A
        elif (qcEC3=="B") or (qcEC3=="b"):
             qcEC3=B
             qcEC3=EC3*B
        elif (qcEC3=="C") or (qcEC3=="c"):
             qcEC3=C
             qcEC3=EC3*C
        elif (qcEC3=="F") or (qcEC3=="f"):
             qcEC3=F
             qcEC3=EC3*F
       
               
        qcIN5=(input("Ingles Tecnico:                 "))
        if (qcIN5=="A")   or (qcIN5=="a"):
             qcIN5=A
             qcIN5=IN*A
        elif (qcIN5=="B") or (qcIN5=="b"):
             qcIN5=B
             qcIN5=IN*B
        elif (qcIN5=="C") or (qcIN5=="c"):
             qcIN5=C
             qcIN5=IN*C
        elif (qcIN5=="F") or (qcIN5=="f"):
             qcIN5=F
             qcIN5=IN*F
       
          
        print("")
        print("")
        indcuatr=round((qcFS+qcCF+qcSA+qcIGP+qcEC3+qcIN5)/qctcred,1)
        #indacumqc=indcuatr
        #indicacum=indacumqc
        lista.append(indcuatr)  
        print("INDICE CUATRIMESTRAL = ",indcuatr,"          ","INDICE ACUMULADO = ",indicacum)
       
      elif int(cuatrimestre==6):
        print("***************************SEXTO CUATRIMESTRE***************************")
        print("")
        print("                     Ingrese su Calificacion: A,B,C,F")
        print("") 
        scHE2=(input("Hacker Etico 2:                "))
        if (scHE2=="A")   or (scHE2=="a"):
             scHE2=A
             scHE2=HE2*A
        elif (scHE2=="B") or (scHE2=="b"):
             scHE2=B
             scHE2=HE2*B
        elif (scHE2=="C") or (scHE2=="c"):
             scHE2=C
             scHE2=HE2*C
        elif (scHE2=="F") or (scHE2=="f"):
             scHE2=F
             scHE2=HE2*F
             
        scSR=(input("Seguridad De Redes:            "))
        if (scSR=="A")   or (scSR=="a"):
             scSR=A
             scSR=SR*A
        elif (scSR=="B") or (scSR=="b"):
             scSR=B
             scSR=SR*B
        elif (scSR=="C") or (scSR=="c"):
             scSR=C
             scSR=SR*C
        elif (scSR=="F") or (scSR=="f"):
             scSR=F
             scSR=SR*F
      
               
        scGPT=(input("Gerencia De Proyectos de TI:   "))
        if (scGPT=="A")   or (scGPT=="a"):
             scGPT=A
             scGPT=GPT*A
        elif (scGPT=="B") or (scGPT=="b"):
             scGPT=GPT*B
        elif (scGPT=="C") or (scGPT=="c"):
             scGPT=GPT*C
        elif (scGPT=="F") or (scGPT=="f"):
             scGPT=GPT*F
        
             
        scEMP=(input("Emprendimiento:                "))
        if (scEMP=="A")   or (scEMP=="a"):
             scEMP=A
             scEMP=EMP*A
        elif (scEMP=="B") or (scEMP=="b"):
             scEMP=B
             scEMP=EMP*B
        elif (scEMP=="C") or (scEMP=="c"):
             scEMP=C
             scEMP=EMP*C
        elif (scEMP=="F") or (scEMP=="f"):
             scEMP=F
             scEMP=EMP*F
       
        
        scTOEIC=(input("Preparacion Para el TOEIC:     "))
        if (scTOEIC=="A")   or (scTOEIC=="a"):
             scTOEIC=A
             scTOEIC=TOEIC*A
        elif (scTOEIC=="B") or (scTOEIC=="b"):
             scTOEIC=B
             scTOEIC=TOEIC*B
        elif (scTOEIC=="C") or (scTOEIC=="c"):
             scTOEIC=C
             scTOEIC=TOEIC*C
        elif (scTOEIC=="F") or (scTOEIC=="f"):
             scTOEIC=F
             scTOEIC=TOEIC*F
       
        print("")
        print("")
        indcuatr=round((scHE2+scSR+scGPT+scEMP+scTOEIC)/sexctcred,1)
        #indacumsexc=indcuatr
        #indicacum=indacumsexc
        lista.append(indcuatr)
        
        print("INDICE CUATRIMESTRAL = ",indcuatr,"          ","INDICE ACUMULADO = ",indicacum)
       
      elif int(cuatrimestre==7):
        print("***************************SEPTIMO CUATRIMESTRE***************************")
        print("")
        print("                     Ingrese su Calificacion: A,B,C,F")
        print("") 
        sepcSAR=(input("Seguridad Avanzadas de Redes:           "))
        if (sepcSAR=="A")   or (sepcSAR=="a"):
             sepcSAR=A
             sepcSAR=SAR*A
        elif (sepcSAR=="B") or (sepcSAR=="b"):
             sepcSAR=B
             sepcSAR=SAR*B
        elif (sepcSAR=="C") or (sepcSAR=="c"):
             sepcSAR=C
             sepcSAR=SAR*C
        elif (sepcSAR=="F") or (sepcSAR=="f"):
             sepcSAR=F
             sepcSAR=SAR*F
             
        sepcALSI=(input("Aspectos Legales De La Seguridad Inf:   "))
        if (sepcALSI=="A")   or (sepcALSI=="a"):
             sepcALSI=A
             sepcALSI=ALSI*A
        elif (sepcALSI=="B") or (sepcALSI=="b"):
             sepcALSI=B
             sepcALSI=ALSI*B
        elif (sepcALSI=="C") or (sepcALSI=="c"):
             sepcALSI=C
             sepcALSI=ALSI*C
        elif (sepcALSI=="F") or (sepcALSI=="f"):
             sepcALSI=F
             sepcALSI=ALSI*F
      
             
        sepcES=(input("Estandares De Seguridad:                "))
        if (sepcES=="A")   or (sepcES=="a"):
             sepcES=A
             sepcES=ES*A
        elif (sepcES=="B") or (sepcES=="b"):
             sepcES=ES*B
        elif (sepcES=="C") or (sepcES=="c"):
             sepcES=ES*C
        elif (sepcES=="F") or (sepcES=="f"):
             sepcES=ES*F
        
             
        sepcPFT=(input("Proyecto Final TSI:                     "))
        if (sepcPFT=="A")   or (sepcPFT=="a"):
             sepcPFT=A
             sepcPFT=PFT*A
        elif (sepcPFT=="B") or (sepcPFT=="b"):
             sepcPFT=B
             sepcPFT=PFT*B
        elif (sepcPFT=="C") or (sepcPFT=="c"):
             sepcPFT=C
             sepcPFT=PFT*C
        elif (sepcPFT=="F") or (sepcPFT=="f"):
             sepcPFT=F
             sepcPFT=PFT*F
        print("")
        print("")
        indcuatr=round((sepcSAR+sepcALSI+sepcES+sepcPFT)/sepctcred,1)
        #indacumsepc=indcuatr
        #indicacum=indacumsepc
        lista.append(indcuatr)
        print("INDICE CUATRIMESTRAL = ",indcuatr,"          ","INDICE ACUMULADO = ",indicacum)
        print()
        print()
  else:
    suma=sum(lista)
    indicacum=suma/cont 
     
    
    print("Su indice acumulado es: ", indicacum)
    break
  
  

  
  
  