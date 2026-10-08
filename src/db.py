import psycopg2

DB_HOST = "~[PY_HARDCODED_HOST_0]~"
DB_PASS = "Sup3rS3cr3t!"
ADMIN_EMAIL = "~[EMAIL_1]~"
SUPPORT_EMAIL = "~[EMAIL_0]~"

conn = psycopg2.connect(host=DB_HOST, database="myapp", user="admin", password=DB_PASS)

def get_user(user_id: int):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    return cur.fetchone()
