import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    db='Construct'
)

cursor = conexao.cursor()


def listar(query):
    lista = []
    c = "\'[](),"
    cursor.execute(query)

    for b in cursor:
        b = str(b)
        for i in range(0, len(c)):
            b = b.replace(c[i], '')
        lista.append(b)

    return lista
