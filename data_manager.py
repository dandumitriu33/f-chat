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


@connection_to_database.connection_handler
def get_password_by_username(cursor, username):
    cursor.execute(f"""
        SELECT password FROM users WHERE username = '{username}';
""")
    result = cursor.fetchone()
    password = result['password']
    return password


def verify_password(input_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_bytes_password)


@connection_to_database.connection_handler
def get_user_id_by_username(cursor, username):
    cursor.execute(f"""
            SELECT id FROM users WHERE username = '{username}';
    """)
    result = cursor.fetchone()
    user_id = result['id']
    return user_id


@connection_to_database.connection_handler
def add_new_message(cursor, user_id, message):
    cursor.execute(f"""
        INSERT INTO messages (user_id, message) VALUES ({user_id}, '{message}');
""")


@connection_to_database.connection_handler
def get_newest_messages(cursor):
    cursor.execute(f"""
        SELECT message, users.username FROM messages
        LEFT JOIN users ON messages.user_id = users.id
        ORDER BY posted ASC 
        LIMIT {30}
        ;
    """)
    messages = cursor.fetchall()
    return messages
