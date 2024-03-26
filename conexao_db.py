import psycopg2

if __name__ == '__main__':
    conexao = psycopg2.connect(host='stampy.db.elephantsql.com', database='emigcegq', user='emigcegq', password='G4b9U2d4aa31P-2YeE7RBBGiYHLMslra')
    print('Conectado ao banco de dados')
    conexao.close()