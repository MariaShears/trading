from . import Broker


def get_brokers(session):
    return session.query(Broker).all()


def presentable_broker(broker):
    return (broker.name, broker)
