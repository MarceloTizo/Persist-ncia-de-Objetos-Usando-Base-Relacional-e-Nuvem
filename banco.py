import mysql.connector

def exibir_cursos(cursor):
    cursor.execute("SELECT * FROM curso")
    cursos = cursor.fetchall()

    print("\nCursos:")
    for curso in cursos:
        print(f"ID: {curso[0]}, Nome: {curso[1]}")

def exibir_estudantes(cursor):
    cursor.execute("SELECT * FROM estudante")
    estudantes = cursor.fetchall()

    print("\nEstudantes:")
    for estudante in estudantes:
        print(f"ID: {estudante[0]}, Nome: {estudante[1]}, Curso ID: {estudante[2]}")

conexao = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456tizo",
    database="escola"
)

cursor = conexao.cursor()

nome_curso = input("Insira o nome do curso: ")

cursor.execute("INSERT INTO curso (nome) VALUES (%s)", (nome_curso,))
curso_id = cursor.lastrowid  

exibir_cursos(cursor)

nome_estudante = input("Insira o nome do estudante: ")

cursor.execute("INSERT INTO estudante (nome, curso_id) VALUES (%s, %s)", (nome_estudante, curso_id))

exibir_estudantes(cursor)

conexao.commit()


cursor.close()
conexao.close()
