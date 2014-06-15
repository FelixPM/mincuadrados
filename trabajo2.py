from numpy import *
import matplotlib.pyplot as plt
set_printoptions(precision=4)

def mult(matriz1,matriz2):
    if matriz1.shape[1] != matriz2.shape[0]:
        return ("Dimensiones incorrectas")
    else:
        nmatriz = zeros((matriz1.shape[0],matriz2.shape[1]))
        for i in range(matriz1.shape[0]):
            for j in range(matriz2.shape[1]):
                for k in range(matriz2.shape[0]):
                    nmatriz[i][j]+= matriz1[i][k]*matriz2[k][j]
        return nmatriz

		
def transp(matriz):
	tmatriz=zeros((matriz.shape[1],matriz.shape[0]))
	for i in range(matriz.shape[0]):
		for j in range(matriz.shape[1]):
			tmatriz[j][i] = matriz[i][j]
	return tmatriz


def det(matriz):
    fil=matriz.shape[0]
    col=matriz.shape[1]
    d=0
    if fil==2 and col==2:
        return (matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0])
    else:
        for j in range(fil):
            d+=matriz[0][j]*(((-1)**(j+2))*(det(subm(matriz,0,j))))
    return d


def cofactores(matriz):
    cmatriz=zeros_like(matriz)
    fil,col =matriz.shape
    for i in range(fil):
        for j in range(col):
            cmatriz[i][j]+=((-1)**(i+j+2))*(det(subm(matriz,i,j)))
    return cmatriz


def inversa(matriz):
    fil,col=matriz.shape
    if (fil,col)==(2,2):
        if det(matriz)==0:
            return (0)
        else:
            return (1/det(matriz))*array([[matriz[1][1],-matriz[1][0]],[-matriz[0][1],matriz[0][0]]])
    else:
        if det(matriz)==0:
            return(0)
        else:
            return (1/det(matriz))*(transp(cofactores(matriz)))

        
def subm(matriz,i,j):
    smatriz = zeros((matriz.shape[0]-1,matriz.shape[1]-1))
    ccol = cfil = 0
    for fil in range(matriz.shape[0]):
	    if not fil == i:
		    for col in range(matriz.shape[1]):
			    if not col == j:					
				    smatriz[cfil][ccol]=matriz[fil][col]
				    ccol+=1
		    ccol=0
		    cfil+=1
    return smatriz


def mincuad(a,b):
    ata=mult((transp(a)),a)
    atb=mult((transp(a)),b)
    ata2=inversa(ata)
    return(mult(ata2,atb))

#1recta
#2cuadratica
#3recta y cuadratica
#4calcular recta y cuadra
#5cubica
#6calcular todas
#7 graficar todas

def aprox(pts,grf):
    
    x1=pts[:,0]
    y1=pts[:,1]
    y=hsplit(pts, 2)[1]
    n=len(x1)
    plt.plot(x1,y,"ko",label="$Puntos$")
    plt.xlabel("X")
    plt.ylabel("Y")    
    plt.title("Aproximación polinomial de puntos metodo mínimos cuadrados")
    print(grf)
    A1=array([[x1[j], 1] for j in range(n)])
    X1=mincuad(A1,y)
    xr=linspace(amin(x1)-2,amax(x1)+2,3)
    recta=X1[0]*x1+X1[1]
    recta2=X1[0]*xr+X1[1]
    d1=sum((recta-y1)**2)
    if grf>=2:
        x2=x1**2
        A2=array([[x2[j], x1[j], 1] for j in range(n)])
        X2=mincuad(A2,y)
        xcd=linspace(amin(x1)-2,amax(x1)+2,40)
        cuad=X2[0]*x1**2+X2[1]*x1+X2[2]
        cuad2=X2[0]*xcd**2+X2[1]*xcd+X2[2]
        d2=sum((cuad-y1)**2)    
    if grf>=5:
        x3=x1**3
        A3=array([[x3[j], x2[j], x1[j], 1] for j in range(n)])
        X3=mincuad(A3,y)
        xcb=linspace(amin(x1)-3,amax(x1)+3,60)
        cub=X3[0]*x1**3+X3[1]*x1**2+X3[2]*x1+X3[3]
        cub2=X3[0]*xcb**3+X3[1]*xcb**2+X3[2]*xcb+X3[3]
        d3=sum((cub-y1)**2)
    if grf==6 or grf==4:
        if grf==6 and d3<d2 and d3<d1:
            plt.plot(xcb,cub2,"g",label=r'$%.3f*x^3%+.3f*x^2%+.3f*x%+.3f" $'% (X3[0],X3[1],X3[2],X3[3]))
            print("La curva que mejor se aproxima es la ecuacion cúbica: \n %.3f*x^3%+.3f*x^2%+.3f*x%+.3f" % (X3[0],X3[1],X3[2],X3[3]))
        elif d1<=d2:
            plt.plot(xr,recta2,"b-",label=r'$y=%10.3f*x%+.3f" $'% (X1[0],X1[1]))
            print("La mejor aproximación es la recta: \n %10.3f*x%+.3f" % (X1[0],X1[1]))
        elif d2<d1:            
            plt.plot(xcd,cuad2,"r",label=r'$%.3f*x^2%+.3f*x%+.3f" $'% (X2[0],X2[1],X2[2]))
            print("La curva que mejor se aproxima es la ecuacion cuadrática\n %.3f*x^2%+.3f*x%+.3f" % (X2[0],X2[1],X2[2]))
    elif grf==7 or grf==3:
        if grf==7:
            print(int(X3[0]))
            plt.plot(xcb,cub2,"g",label=r'$%.3f*x^3%+.3f*x^2%+.3f*x%+.3f" $'% (X3[0],X3[1],X3[2],X3[3]))
            print("La ecuacion cúbica es: \n %.3f*x^3%+.3f*x^2%+.3f*x%+.3f" % (X3[0],X3[1],X3[2],X3[3]))
        plt.plot(xcd,cuad2,"r",label=r'$%.3f*x^2%+.3f*x%+.3f" $'% (X2[0],X2[1],X2[2]))
        print("La ecuacion cuadrática es: \n %.3f*x^2%+.3f*x%+.3f" % (X2[0],X2[1],X2[2]))
        plt.plot(xr,recta2,"b-",label=r'$%10.3f*x%+.3f" $'% (X1[0],X1[1]))
        print("La recta es: \n %.3f*x%+.3f" % (X1[0],X1[1]))
    elif grf==1:
        plt.plot(xr,recta2,"b-",label=r'$%10.3f*x%+.3f" $'% (X1[0],X1[1]))
        print("La recta es: \n %.3f*x%+.3f" % (X1[0],X1[1]))
    elif grf==2:
        plt.plot(xcd,cuad2,"r",label=r'$%.3f*x^2%+.3f*x%+.3f" $'% (X2[0],X2[1],X2[2]))
        print("La ecuacion cuadrática es: \n %.3f*x^2%+.3f*x%+.3f" % (X2[0],X2[1],X2[2]))
    else:
        plt.plot(xcb,cub2,"g",label=r'$%.3f*x^3%+.3f*x^2%+.3f*x%+.3f" $'% (X3[0],X3[1],X3[2],X3[3]))
        print("La ecuacion cúbica es: \n %.3f*x^3%+.3f*x^2%+.3f*x%+.3f" % (X3[0],X3[1],X3[2],X3[3]))
    
          
    plt.legend(loc = 4)            
    plt.show()
##    if grf==4:
##        if d1<=d2 and d1<=d3:
##            return(plt.show(pl1))
##        elif d2<d1 and d2<=d3:
##            return(plt.show(pl2))
##        else:
##            return(plt.show(pl3))
    
def ingreso (matrizA,matrizB):
    print("Ingrese dimensiones de la matriz(Filas x Columnas) entre 1 y 5")
    while True:
        try:
            filas = int(input('Filas:'))
            columnas = int(input('Columnas:'))
        except ValueError:
            print("Intentelo nuevamente")
        else:
            if filas < 1 or filas > 5 or columnas < 1 or columnas > 5:
                print("Intentelo nuevamente")
            else:
                break
        
    matrizA = empty((filas,columnas))
    matrizB = empty((filas))
    
    print ("Ingrese valores de la matriz A: ")
    for i in range(filas):
        for j in range(columnas):
            while True:
                try:
                    valor=float(input("Elemento %d,%d : " % (i+1,j+1) ))
                except ValueError:
                    print("Intentelo nuevamente")
                else:
                    matrizA[i][j]=valor
                    break

    print("Ingrese valores matriz de soluciones: ")
    for i in range(filas):
        while True:
            try:
                valor=float(input("Elemento %d : " % (i+1) ))
            except ValueError:
                print("Intentelo nuevamente")
            else:
                matrizB[i]=valor
                break
    matrizB=matrizB.reshape(filas,1)
    print (matrizA,matrizB)
    return matrizA,matrizB

def ingpto(puntos):
    print("Cuantos puntos desea ingresar: "),
    while True:
        try:
            npts=int(input())
        except ValueError:
            print("Intentelo nuevamente")
        else:
            if npts>20:
                print("Son demasiados puntos por favor sea más considerado")
            elif npts<2:
                print("Se necesitan al menos 2 puntos!")
            else:
                break
    puntos=empty((npts,2))
    while True:
        for i in range(npts):
                while True:
                    try:
                        valorx=float(input("Coordenada X N° %d : " % (i+1)))
                        valory=float(input("Coordenada Y N° %d : " % (i+1)))
                    except ValueError:
                        print("Intentelo nuevamente")
                    else:
                        puntos[i][0]=valorx
                        puntos[i][1]=valory
                        break
        if len(unique(puntos[:,0]))<2:
            print("Se necesitan al menos 2 coordenadas X distintas!")
        else:
            break
    print(puntos)
    return(puntos,len(unique(puntos[:,0])))

    
print("Aproximacion de Minimos cuadrados \n 1)Aproximacion para sistemas de ecuaciones \n 2)Aproximacion a partir de puntos")
elije=input()
if elije=="1":
    matrizA=matrizB=array
    matrizA,matrizB=ingreso(matrizA,matrizB)
    if matrizA.shape[1]==linalg.matrix_rank(matrizA):
        print ("Soluciones por minimos cuadrados: ")
        print (mincuad(matrizA,matrizB))
    else:
        print("No tiene solucion por minimos cuadrados")

#1recta
#2cuadratica
#3recta y cuadratica
#4calcular recta y cuadra
#5cubica
#6calcular todas
#7 graficar todas

else:
    puntos=array
    puntos,cx=ingpto(puntos)
    grf=0
    if cx==2:
        grf=1
        aprox(puntos,grf)
    elif cx==3:
        print("Aproximar los puntos a: \n 1)Recta \n 2)Función Cuadrática \n 3)Ambas \n 4)Calcular la que mejor aproxime")
        while True:
            try:
                grf=int(input())
            except ValueError:
                        print("Intentelo nuevamente")
            else:
                if grf==1 or grf==2 or grf==3 or grf==4:
                    break
                else:
                    print("Ingrese una opción válida")
        aprox(puntos,grf)
    else:
        print("Aproximar los puntos a: \n 1)Recta \n 2)Función Cuadrática \n 3)Función Cubica \n 4)Calcular la que mejor aproxime \n 5)Todas")
        while True:
            try:
                grf=int(input())
            except ValueError:
                        print("Intentelo nuevamente")
            else:
                if grf==1 or grf==2:
                    break
                elif grf==3:
                    grf=5
                    break
                elif grf==4:
                    grf=6
                    break
                elif grf==5:
                    grf=7
                    break
                else:
                    print("Ingrese una opción válida")
        aprox(puntos,grf)
        