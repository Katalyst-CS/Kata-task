from peewee import PostgresqlDatabase


DB_CONNECTION = {
    'user': 'app',
    'name': 'kata_tasks',
    'host': 'localhost',
    'port': 6000,
    'pass': 'Estafeta,13'
}

database = PostgresqlDatabase(DB_CONNECTION['name'],
                              password=DB_CONNECTION['pass'],
                              host=DB_CONNECTION['host'],
                              port=DB_CONNECTION['port'],
                              user= DB_CONNECTION['user'])