"""
Entrada
salario bruto-->float-->salab
salidas
categorias-->int-->cate
Sueldo-->float-->Sueldo
"""
#Entrada
salab=float(input("Digite el salario bruto: "))
#Caja negra
if(salab>=5000000):
    cate="es 1"
    sueldo=salab*0.10+salab#float
elif(salab>=4300000 and salab<5000000):
    cate="es 2"
    sueldo=salab*0.15+salab#float
elif(salab>=3600000 and salab<4300000):
    cate="es 3"
    sueldo=salab*0.20+salab#float
elif(salab>=2000000 and salab<3600000):
    cate="es 4"
    sueldo=salab*0.40+salab#float
elif(salab>=900000 and salab<2000000):
    cate="es 5"
    sueldo=salab*0.60+salab#float
else:
    cate=("no existe")
    sueldo=(salab)
    #Salida
    print("No se encontro categoria ni aumento para tu sueldo")  
print("Tu categoría",cate,"y tu sueldo es de $",sueldo,)