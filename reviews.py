import db

def add_review(title, body, user_id):
    sql = "INSERT INTO reviews (title, body, user_id) VALUES (?, ?, ?)"
    db.execute(sql, [title, body, user_id])

def get_reviews():
    sql = "SELECT id, title FROM reviews ORDER BY id DESC"
    return db.query(sql)

def get_review(review_id):
    sql = """
        SELECT r.id,
               r.title,
               r.body,
               r.user_id,
               u.id user_id,
               u.username
        FROM reviews r
        JOIN users u ON u.id = r.user_id
        WHERE r.id = ?
    """
    result = db.query(sql, [review_id])
    return result[0] if result else None

def update_review(review_id, title, body):
    sql = """
        UPDATE reviews
        SET title = ?,
            body = ?
        WHERE id = ?
    """
    db.execute(sql, [title, body, review_id])
