entrada = input().split()
qtde_frutas = int(entrada[0])
qtde_codificadas = int(entrada[1])
v_f = [""]*qtde_frutas
v_c = [""]*qtde_codificadas
for i in range(qtde_frutas):
   v_f[i] = input().lower()    
for i in range(qtde_codificadas):
   v_c[i] = input().lower()  
for i in v_f:
   Come = False
   i_inv = i[::-1]
   for j in v_c:
       if (i in j) or (i_inv in j):
           Come = True
           break
   if Come:
       print("Sheldon come a fruta", i)
   else:
       print("Sheldon detesta a fruta", i)