from . import Exemption


def get_exemptions(session):
    return session.query(Exemption).all()
 