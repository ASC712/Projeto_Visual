import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

app = ttk.Window('Formulário')
app.geometry('550x500')
style = Style(theme='darkly')

label = ttk.Label(app, text='Formulário de Cadastro', font=('Arial', 20))
label.pack(pady=20)

nome = ttk.Frame(app)
nome.pack(pady=18, padx=10, fill='x')
ttk.Label(nome, text='Nome:').pack(side=LEFT, padx=5)
ttk.Entry(nome).pack(side=LEFT, padx=5, fill=X, expand=YES)

email = ttk.Frame(app)
email.pack(pady=18, padx=10, fill='x')
ttk.Label(email, text='Email:').pack(side=LEFT, padx=5)
ttk.Entry(email).pack(side=LEFT, padx=5, fill=X, expand=YES)

idade = ttk.Frame(app)
idade.pack(pady=18, padx=10, fill='x')
ttk.Label(idade, text='Idade:').pack(side=LEFT, padx=5)
ttk.Entry(idade).pack(side=LEFT, padx=5, fill=X, expand=YES)

checkbox = ttk.Frame(app)
checkbox.pack(pady=15, padx=10, fill='x')
ttk.Checkbutton(checkbox, text='Aceito os termos e condições').pack(side=LEFT, padx=5)

botao = ttk.Frame(app)
botao.pack(pady=30, padx=10, fill='x')
ttk.Button(botao, text='Cadastrar').pack(side=RIGHT, padx=5)
ttk.Button(botao, text='Cancelar').pack(side=RIGHT, padx=5)

app.mainloop()