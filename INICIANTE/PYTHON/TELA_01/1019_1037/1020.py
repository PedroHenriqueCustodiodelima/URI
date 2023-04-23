idade = int(input())
anos = int(idade/365)
conta = idade - anos * 365
meses = int(conta/30)
dias = conta - meses * 30
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")