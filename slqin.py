import sqlite3

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Vulnerabilidad de inyección de SQL
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
    
    user = cursor.fetchone()
    conn.close()
    
    return user

if __name__ == "__main__":
    username = input("Alberto: ")
    user = get_user(username)
    
    if user:
        print("¡Bienvenido, {}!".format(user[1]))
    else:
        print("Usuario no encontrado.")
