"""
Entradas
Presupuesto anual-->float-->presupuesto
Salidas
Presupuesto anual de ginecología-->float-->ginecologia
Presupuesto anual de traumatología-->float-->traumatologia
Presupuesto anual de pediatría-->float-->pediatria
"""
#Entradas
presupuesto=float(input("Digite el presupuesto anual del hospital: "))
#Caja negra
ginecologia=presupuesto*0.40#float
traumatologia=presupuesto*0.30#float
pediatria=presupuesto*0.30#float
#Salidas
print("Ginecología le corresponde del presupuesto anual: $",ginecologia)
print("Traumatología le corresponde del presupuesto anual: $",traumatologia)
print("Pediatría le corresponde del presupuesto anual: $",pediatria)