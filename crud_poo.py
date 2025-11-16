class Curso:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome


class Campus:
    def __init__(self, nome):
        self.__nome = nome
        self.cursos = []

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def procurar_curso(self, nome):
        for curso in self.cursos:
            if curso.get_nome().lower() == nome.lower():
                return curso
        return None

    def remover_curso(self, nome):
        curso = self.procurar_curso(nome)
        if curso:
            self.cursos.remove(curso)
            return True
        return False


class UFC:
    def __init__(self):
        self.campi = []

    def adicionar_campus(self, campus):
        self.campi.append(campus)

    def procurar_campus(self, nome):
        for campus in self.campi:
            if campus.get_nome().lower() == nome.lower():
                return campus
        return None

    def remover_campus(self, nome):
        campus = self.procurar_campus(nome)
        if campus:
            self.campi.remove(campus)
            return True
        return False


def linha():
    print("============================================")


def menu():
    ufc = UFC()

    while True:
        linha()
        print("                 MENU UFC")
        linha()
        print("1 - Cadastrar Campus")
        print("2 - Listar Campi")
        print("3 - Editar Campus")
        print("4 - Remover Campus")
        print("5 - Gerenciar Cursos")
        print("0 - Sair")
        linha()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            linha()
            nome = input("Nome do novo campus: ")
            ufc.adicionar_campus(Campus(nome))
            print("Campus cadastrado com sucesso!")

        elif opc == "2":
            linha()
            print("Campi cadastrados:")
            if not ufc.campi:
                print("Nenhum campus cadastrado.")
            else:
                for c in ufc.campi:
                    print(f"• {c.get_nome()}")

        elif opc == "3":
            linha()
            nome = input("Nome do campus que deseja editar: ")
            campus = ufc.procurar_campus(nome)
            if campus:
                novo = input("Novo nome: ")
                campus.set_nome(novo)
                print("Campus atualizado com sucesso!")
            else:
                print("Campus não encontrado.")

        elif opc == "4":
            linha()
            nome = input("Nome do campus que deseja remover: ")
            if ufc.remover_campus(nome):
                print("Campus removido com sucesso!")
            else:
                print("Campus não encontrado.")

        elif opc == "5":
            linha()
            nome = input("Nome do campus para gerenciar: ")
            campus = ufc.procurar_campus(nome)

            if not campus:
                print("Campus não encontrado.")
                continue

            while True:
                linha()
                print(f"      Cursos do Campus {campus.get_nome()}")
                linha()
                print("1 - Adicionar Curso")
                print("2 - Listar Cursos")
                print("3 - Editar Curso")
                print("4 - Remover Curso")
                print("0 - Voltar")
                linha()
                opc2 = input("Escolha uma opção: ")

                if opc2 == "1":
                    nome_curso = input("Nome do novo curso: ")
                    campus.adicionar_curso(Curso(nome_curso))
                    print("Curso cadastrado com sucesso!")

                elif opc2 == "2":
                    linha()
                    print("Cursos cadastrados:")
                    if not campus.cursos:
                        print("Nenhum curso cadastrado.")
                    else:
                        for curso in campus.cursos:
                            print(f"• {curso.get_nome()}")

                elif opc2 == "3":
                    nome_antigo = input("Nome do curso que deseja editar: ")
                    curso = campus.procurar_curso(nome_antigo)
                    if curso:
                        novo_nome = input("Novo nome: ")
                        curso.set_nome(novo_nome)
                        print("Curso atualizado com sucesso!")
                    else:
                        print("Curso não encontrado.")

                elif opc2 == "4":
                    nome_del = input("Nome do curso que deseja remover: ")
                    if campus.remover_curso(nome_del):
                        print("Curso removido com sucesso!")
                    else:
                        print("Curso não encontrado.")

                elif opc2 == "0":
                    break

                else:
                    print("Opção inválida.")

        elif opc == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
