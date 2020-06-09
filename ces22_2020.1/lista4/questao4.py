import tkinter as tk

# classe invoker
class Invoker:

    def __init__(self, window):
        self.commandHistory = []
        self.window = window
    def executeCommand(self, command):
        command.execute(self.window)
        self.commandHistory.append(command.__class__.__name__)
        
# classe botão com acesso ao invoker
class InvokerButton(tk.Button):
    def __init__(self, comm, invoker = None, **buttonArgs):
        self.invoker = invoker
        self.command = comm()
        tk.Button.__init__(self, **buttonArgs, command = lambda: self.invoker.executeCommand(self.command))

# classe abstrata de comando
class Command:
    def execute(self):
        raise NotImplementedError

# comando de saldo
class BalanceCommand(Command):
    def execute(self, window):
        window.configure(background='pink')
        print('Balance')

# comando de extrato
class StatementCommand(Command):
    def execute(self, window):
        window.configure(background='blue')
        print('Statement')

# comando de transferência
class TransferCommand(Command):
    def execute(self, window):
        window.configure(background='red')
        print('Transfer')


# criação dos elementos de tela
class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.invoker = Invoker(self.window)
        print('----------------------------------------------')
        self.lbl = tk.Label(self.window, text = 'Aperte os botões para fazer as operações.\n Histórico exibido no terminal ao fechar a janela', font=("Helvetica", 32))
        self.lbl.pack(side=tk.TOP)
        self.buttonBalance = InvokerButton(BalanceCommand, self.invoker, master = self.window, text = 'Saldo', font=("Helvetica", 32))
        self.buttonBalance.pack(padx=30, pady=10, side=tk.LEFT)

        self.buttonStatement = InvokerButton(StatementCommand,self.invoker, master = self.window, text = 'Extrato', font=("Helvetica", 32))
        self.buttonStatement.pack(padx=30, pady=10, side=tk.LEFT)

        self.buttonTransfer = InvokerButton(TransferCommand,self.invoker, master = self.window, text = 'Transferência', font=("Helvetica", 32))
        self.buttonTransfer.pack(padx = 30, pady = 10, side = tk.LEFT)

    


if __name__ == "__main__":

    gui = GUI()

    gui.window.mainloop()
    print('\nhistory:')
    print(gui.invoker.commandHistory)