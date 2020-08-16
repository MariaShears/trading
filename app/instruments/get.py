from . import Stock

def get_instrments(session):
    return session.query(Stock).all()