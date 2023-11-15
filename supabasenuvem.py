import supabase

# Substitua 'your_supabase_url' e 'your_supabase_key' pelos valores reais do seu projeto Supabase
supabase_url = 'https://ciankaqiamkpovyqvmqz.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNpYW5rYXFpYW1rcG92eXF2bXF6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDAwNjUzMDcsImV4cCI6MjAxNTY0MTMwN30.0N4Lhfxa6tHvpOth8K5-FfOkm9JKoxxtcNezkAzg_Xo'

conexao = supabase.create_client(supabase_url, supabase_key)

nome_curso = input("Insira o nome do curso: ")

response_curso = conexao.table('curso').upsert([
    {'nome': nome_curso}
])

cursos = conexao.table('curso').select().execute()

if isinstance(cursos, dict) and 'data' in cursos:
    print("\nCursos:")
    for curso in cursos['data']:
        print(f"ID: {curso['id']}, Nome: {curso['nome']}")

nome_estudante = input("Insira o nome do estudante: ")

curso_id = cursos.get('data')[0].get('id') if isinstance(cursos, dict) and 'data' in cursos and cursos.get('data') else None

response_estudante = conexao.table('estudante').upsert([
    {'nome': nome_estudante, 'curso_id': curso_id}
])

estudantes = conexao.table('estudante').select().execute()

if isinstance(estudantes, dict) and 'data' in estudantes:
    print("\nEstudantes:")
    for estudante in estudantes['data']:
        print(f"ID: {estudante['id']}, Nome: {estudante['nome']}, Curso ID: {estudante['curso_id']}")