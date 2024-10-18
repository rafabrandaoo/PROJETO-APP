import sqlite3
import csv

def connect_db():
    return sqlite3.connect("users.db")  

def exportar_tabela_para_csv():
    # Conectar ao banco de dados
    conn = connect_db()
    cursor = conn.cursor()
    

    cursor.execute('SELECT * FROM Users')
    dados = cursor.fetchall()  


    colunas = [descricao[0] for descricao in cursor.description]


    with open('sistemas.csv', mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)


        escritor_csv.writerow(colunas)

        escritor_csv.writerows(dados)

   
    conn.close()
    print("Exportação concluída com sucesso para sistemas.csv")


exportar_tabela_para_csv()
