from src.models.store import Store
from src.models.user import User


class ServiceUser:

    def __init__(self):
        self.store = Store()
        self.users = []

    def add_user(self, name, job):
        # if type(name) == str and type(job) == str  (if do professor)
        if name != None and job != None:
            if isinstance(name, str) and isinstance(job, str):
                    user_bd = self.valid_user(name=name)
                    if user_bd == None:
                        user = User(name=name, job=job)
                        self.store.bd.append(user)
                        return "Usuário do tipo string foi adicionado com sucesso"
                    else:
                        return "Usuário já existe"
            else:
                return "Usuário não é do tipo string"
        else:
            return "Usuario não adicionado pois é nulo"

    def valid_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None

    def remove_user(self, name):
        user_bd = self.valid_user(name)
        if user_bd != None:
            self.store.bd.remove(user_bd)
            return "Usuário removido com sucesso"
        else:
            return "Usuário não encontrado"

    def update_user(self, name, new_job):
        user_bd = self.valid_user(name)
        if user_bd != None:
            user_bd.job = new_job
            return "Job atualizado com sucesso"
        else:
            return "Usuário não encontrado"

    def select_user(self, name):
        user_bd = self.valid_user(name)
        if user_bd != None:
            return "Job: " + user_bd.job
        else:
            return "Usuario não encontrado"



