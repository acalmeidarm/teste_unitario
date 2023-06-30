from src.models.store import Store
from src.models.user import User
from src.service.service_user import ServiceUser

store = Store()

name_1 = "Ana"
job_1 = "QA"

user = User(name=name_1, job=job_1)

print("#Primeiro Teste")
name_1 = "Ana"
job_1 = "QA"

service = ServiceUser()
resultado = service.add_user(name=name_1, job=job_1)
print(service.store.bd[0].name)
print(service.store.bd[0].job)
print(resultado)


print("#Segundo Teste")
name_1 = None
job_1 = "QA"

service = ServiceUser()
resultado = service.add_user(name=name_1, job=job_1)
print(service.store.bd)
print(resultado)

print("#Buscando usuário")

# Criando uma instância de ServiceUser
service = ServiceUser()

# Adicionando usuários
service.add_user("Ana", "QA")
service.add_user("João", "Desenvolvedor")

# Buscando um usuário existente
resultado = service.search_user("Ana")
if isinstance(resultado, User):
    print("Nome do usuário encontrado:", resultado.name)
    print("Job do usuário encontrado:", resultado.job)
else:
    print(resultado)

# Buscando um usuário inexistente
resultado = service.search_user("Maria")
if isinstance(resultado, User):
    print("Nome do usuário encontrado:", resultado.name)
    print("Job do usuário encontrado:", resultado.job)
else:
    print(resultado)

print("#Editar usuário")

# Criando uma instância de ServiceUser
service = ServiceUser()

# Adicionando usuários
service.add_user("Ana", "QA")
service.add_user("João", "Desenvolvedor")

# Editando o job de um usuário existente
resultado = service.edit_user("Ana", "Analista")
print(resultado)

# Editando o job de um usuário inexistente
resultado = service.edit_user("Maria", "Gerente")
print(resultado)


















