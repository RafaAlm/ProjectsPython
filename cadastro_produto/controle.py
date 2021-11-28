from PyQt5 import  uic,QtWidgets
import mysql.connector

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="alocacaoDeCarro"
)

def salvar_dados():
    global numero_id

    codigo = tela_editar.lineEdit_2.text()
    descricao = tela_editar.lineEdit_3.text()
    preco = tela_editar.lineEdit_4.text()
    categoria = tela_editar.lineEdit_5.text()

    cursor = banco.cursor()
    cursor.execute("update produtos set codigo ='{}' ,descricao ='{}',preco ='{}',categoria ='{}' where id = {} ".format(codigo,descricao,preco,categoria, numero_id))
    banco.commit()
    tela_editar.close()
    segunda_tela.close()
    chama_segunda_tela()
   



def editar_dados():
    global numero_id
    linha = segunda_tela.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT codigo FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("select * from produtos where codigo =" + str(valor_id))
    produto = cursor.fetchall()
    tela_editar.show()

    numero_id = valor_id

    tela_editar.lineEdit.setText(str(produto[0][0]))
    tela_editar.lineEdit_2.setText(str(produto[0][1]))
    tela_editar.lineEdit_3.setText(str(produto[0][2]))
    tela_editar.lineEdit_4.setText(str(produto[0][3]))
    tela_editar.lineEdit_5.setText(str(produto[0][4]))


def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("delete from produtos where id =" + str(valor_id))
    banco.commit()


def funcao_principal():
    descricao = formulario.lineEdit_2.text()
    preco = formulario.lineEdit_3.text()
    categoria = ""

    if formulario.radioButton.isChecked():
        print("Categoria Informatica foi selecionado")
        categoria = "Informatica"
    elif formulario.radioButton_2.isChecked():
        print("Categoria Alimentos foi selecionado ")
        categoria = "Alimentos"

    else:
        print("Categoria Eletronicos foi selecionado  ")
        categoria = "Eletronicos"

    print("descricao: ", descricao)
    print("preço: ", preco)
    print("categoria: ", categoria)

    cursor = banco.cursor()
    comando_sql = "INSERT INTO produtos (descricao,preco,categoria) VALUES (%s,%s,%s)"
    dados = ( str(descricao), str(preco),categoria)                           
    cursor.execute(comando_sql, dados)
    banco.commit()
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")


def cadastro_cliente():
    form_cliente.show()

    nome = form_clientee


def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    linha = segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0, linha):
        for j in range(0, 5):
           segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j]))) 

app=QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
segunda_tela = uic.loadUi("listar_dados.ui")
tela_editar = uic.loadUi("editar_dados.ui")
form_cliente = uic.loadUi("form_cliente.ui")

formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
formulario.pushButton_3.clicked.connect(cadastro_cliente)
segunda_tela.pushButton_3.clicked.connect(excluir_dados)
segunda_tela.pushButton_2.clicked.connect(editar_dados)
tela_editar.pushButton.clicked.connect(salvar_dados)

formulario.show()
app.exec()
