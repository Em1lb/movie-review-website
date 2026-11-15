import db

def add_review(title, body, user_id):
    sql = "INSERT INTO reviews (title, body, user_id) VALUES (?, ?, ?)"
    db.execute(sql, [title, body, user_id])

def get_reviews():
    sql = "SELECT id, title FROM reviews ORDER BY id DESC"
    return db.query(sql)

def get_review(review_id):
    sql = "SELECT id, title, body, user_id FROM reviews WHERE id = ?"
    result = db.query(sql, [review_id])
    return result[0] if result else None
