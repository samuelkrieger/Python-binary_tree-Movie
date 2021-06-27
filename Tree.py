from Filme import Filme


class No:



    def __init__(self, filme):
        self.filme=filme

        self.setaFilhos(None, None)



    def insere(self, filme):
        if filme.nota <= self.filme.nota:
            if not self.esq:
                self.esq= No(filme)

            else:
                self.esq.insere(filme)

        else:
            if not self.dir:
                self.dir = No(filme)

            else:
                self.dir.insere(filme)

        self.executaBalanco()
    def setaFilhos(self, esq, dir):
        self.esq = esq
        self.dir = dir

    def balanco(self):
        prof_esq = 0
        if self.esq:
            prof_esq = self.esq.profundidade()
        prof_dir = 0
        if self.dir:
            prof_dir = self.dir.profundidade()
        return prof_esq - prof_dir

    def profundidade(self):
        prof_esq = 0
        if self.esq:
            prof_esq = self.esq.profundidade()
        prof_dir = 0
        if self.dir:
            prof_dir = self.dir.profundidade()
        return 1 + max(prof_esq, prof_dir)

    def rotacaoEsquerda(self):
        self.filme, self.filme = self.dir.filme, self.filme
        old_esquerda = self.esq
        self.setaFilhos(self.dir, self.dir.dir)
        self.esq.setaFilhos(old_esquerda, self.esq.esq)

    def rotacaoDireita(self):
        self.filme, self.esq.filme = self.esq.filme, self.filme
        old_direita = self.dir
        self.setaFilhos(self.esq.esq, self.esq)
        self.dir.setaFilhos(self.dir.dir, old_direita)

    def rotacaoEsquerdaDireita(self):
        self.esq.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
        self.dir.rotacaoDireita()
        self.rotacaoEsquerda()

    def executaBalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.esq.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsquerdaDireita()
        elif bal < -1:
            if self.dir.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()

    def imprimeArvore(self, indent=0):
        print(" " * indent + str(self.filme.nome))
        if self.esq:
            self.esq.imprimeArvore(indent + 2)
        if self.dir:
            self.dir.imprimeArvore(indent + 2)
print("Programa Arvore Binaria")
i=0
opcao = 0
while opcao != 3:
     print("***********************************")
     print("Entre com a opcao:")
     print(" --- 1: Inserir Realizando Balancemaneto Avl")
     print(" --- 2: Exibir Arvore Balanceada")
     print(" --- 3: Sair do programa")
     print("***********************************")
     opcao = int(input("-> "))
     if opcao == 1:
          y = str(input(" Informe o nome do filme-> "))
          x = int(input(" Informe a nota do filme-> "))
          a=Filme(y,x)
          if(i==0):
              ae=No(a)
              i=i+1
          else:
            ae.insere(a)

     elif opcao == 2:
         ae.imprimeArvore()
     elif opcao == 3:
          break


