# classe do documento
class Document:
    def __init__(self, state = None, user = None):
        self.state = state
        self.state.setDoc(self)
        self.user = user
        self.approvedByAdmin = False
        self.isExpired = False

    def changeState(self, state):
        self.state = state

    def render(self):
        self.state.render()

    def publish(self):
        self.state.publish()

# classe abstrata de estado
class State:
    def render(self):
        raise NotImplementedError
    def publish(self):
        raise NotImplementedError

# implementação do estado de rascunho
class Draft(State):
    def __init__(self, doc = None):
        self.document = doc
        if doc != None:
            self.document.approvedByAdmin = False

    def publish(self):
        if self.document.user == 'admin':
            self.document.changeState(Published(self.document))
        else:
            self.document.changeState(Moderation(self.document))
    
    def render(self):
        if self.document.user != None:
            print('render document (draft)')

    def setDoc(self, doc):
        self.document = doc
        self.document.approvedByAdmin = False

# implementação do estado de moderação
class Moderation(State):
    def __init__(self, doc = None):
        self.document = doc

    def publish(self):
        if self.document.approvedByAdmin:
            self.document.changeState(Published(self.document))
        else:
            self.document.changeState(Draft(self.document))

    def render(self):
        if self.document.user != None:
            print('render document (moderation)')

    def setDoc(self, doc):
        self.document = doc

# implementação do estado de publicação
class Published(State):
    def __init__(self, doc = None):
        self.document = doc

    def publish(self):
        print('Document already published')

    def render(self):
        if (self.document.isExpired):
            self.document.changeState(Draft(self.document))
            self.document.isExpired = False
            print('Documento expirado, voltando para draft')
        elif self.document.user != None:
            print('render document (published)')

    def setDoc(self, doc):
        self.document = doc

print('----------------------------------------------------------------------------------------------------------')
print('vamos criar um doc em draft com usuário não admin e renderizar (acompanhamos o estado a cada passo)')
doc = Document(Draft(), 'non-admin')
doc.render()
print('estado: ', doc.state.__class__.__name__)

print('\nvamos agora publicar o documento (deve ir para moderation)')
doc.publish()
print('estado: ', doc.state.__class__.__name__)

print('\nvamos tentar publicar sem aprovação do admin')
doc.publish()
print('estado: ', doc.state.__class__.__name__)

print('\nvamos publicar de novo e renderizar e, em seguida, dar aprovação do admin e publicar')
doc.publish()
print('estado: ', doc.state.__class__.__name__)
doc.render()
doc.approvedByAdmin = True
doc.publish()
print('estado: ', doc.state.__class__.__name__)

print('\nvamos renderizar e publicar um documento já publicado')
doc.render()
doc.publish()

print('\nvamos expirar o documento publicado e tentar renderizá-lo')
doc.isExpired = True
doc.render()
print('estado: ', doc.state.__class__.__name__)

print('\nvamos publicar o documento partindo do draf com user admin')
doc.user='admin'
doc.publish()
print('estado: ', doc.state.__class__.__name__)

print('\nPronto, passamos por todos os estados em todos os fluxos desenhados no diagrama!')
print('----------------------------------------------------------------------------------------------------------')
