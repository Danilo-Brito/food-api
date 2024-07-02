SECRET_KEY = 'food'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='K21h3fI5X!!',
        servidor='localhost',
        database='calculator'
    )