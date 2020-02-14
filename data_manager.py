import bcrypt
import connection_to_database


def hash_password(input_password):
    hashed_bytes = bcrypt.hashpw(input_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


@connection_to_database.connection_handler
def add_user_into_db(cursor, input_username, hashed_password):
    cursor.execute(f"""
        INSERT INTO users (username, password) VALUES ('{input_username}', '{hashed_password}');
""")
