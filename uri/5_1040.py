notas=input()
(N1,N2,N3,N4)=notas.split( )
N1=float(N1)
N2=float(N2)
N3=float(N3)
N4=float(N4)
promedio=(N1*2+N2*3+N3*4+N4*1)/10
print("Media:",round(promedio,1))
if promedio>=7.0:
    print("Aluno aprovado.")
elif promedio<5.0:
     print("Aluno reprovado.")
elif promedio>=5.0 and promedio<7:
    print("Aluno em exame.")
    examen=float(input())
    print("Nota do exame:",round(examen,1))
    promedio2=(promedio+examen)/2
    if promedio2>=5.0:
        print("Aluno aprovado.")
        print("Media final:",round(promedio2,1))
    else:
        print("Aluno reprovado.")
        print("Media final:",round(promedio2,1))