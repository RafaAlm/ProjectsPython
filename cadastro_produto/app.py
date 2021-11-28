from PyQt5 import  uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="AlocacaoDeCarro"
)

def tela_login():
    # usuario = login.lineEdit.text()
    # senha = login.lineEdit_2.text()

    # cursor = banco.cursor()

    # usuario = cursor.execute("select login from cliente")
    # dadoslogin = cursor.fetchall()
    # usuario = dadoslogin[0]

    # senha = cursor.execute("select senha from cliente")
    # dadosSenha = cursor.fetchall()
    # senha = dadosSenha[0]

    # tamanho = (usuario)
    # print(tamanho)

    # for i in tamanho:
    #         print(usuario[i], senha[i])
    

    cadastro.show()
    
def tela_cadastro():

    
    

def logout():
  segunda_tela_login.close()
  primeira_tela_login.show()

app=QtWidgets.QApplication([])
login = uic.loadUi("primeira_tela_login.ui")
cadastro = uic.loadUi("segunda_tela_login.ui")

login.pushButton.clicked.connect(tela_login) 
# login.pushButton_2.clicked.connect() # vai criar ainda

login.show()
app.exec()