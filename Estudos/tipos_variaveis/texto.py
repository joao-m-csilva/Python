nome_completo = "João Marcos"
print("Nome completo =", nome_completo)

nome_completo_aspas = """João
Marcos"""
print("Nome completo com aspas =", nome_completo_aspas)

nome_completo_quebra = "João \ Marcos"
print("Nome completo com quebra de linha =", nome_completo_quebra)

nome = "João"
sobrenome = "Marcos" 
print("Nome e sobrenome =", nome, sobrenome)    


# Formatação

print("Nome completo (1ª forma):", nome_completo)
print("Nome completo (2ª forma):" + nome_completo)
print("Nome completo (3ª forma):" + " João" + " Marcos")
print("Nome completo (4ª forma):" + "João", "Marcos")
print("Nome completo (5ª forma):", nome_completo_aspas)
print("Nome completo (6ª forma):", nome_completo_quebra)
print("Nome completo (7ª forma): %s" %nome_completo)
print("Nome completo (8ª forma): %s %s" %(nome, sobrenome))
print(f"Nome completo (9ª forma): {nome} {sobrenome}")
print("Nome completo (10ª forma): {} {}".format(sobrenome,  nome))
