# linguist.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///linguist.db')
Session = sessionmaker(bind=engine)
session = Session()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


class Deck(Base):
    __tablename__ = 'decks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))


class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)


def user_create(name, email, password):
    user = User(name=name, email=email, password=password)
    session.add(user)
    session.commit()
    return user


def user_get_by_id(user_id):
    return session.query(User).get(user_id)


def user_update_name(user_id, name):
    user = session.query(User).get(user_id)
    user.name = name
    session.commit()
    return user


def user_change_password(user_id, old_password, new_password):
    user = session.query(User).get(user_id)
    if user.password == old_password:
        user.password = new_password
        session.commit()
        return True
    else:
        return False


def user_delete_by_id(user_id):
    user = session.query(User).get(user_id)
    session.delete(user)
    session.commit()
    return True


def deck_create(name, user_id):
    deck = Deck(name=name, user_id=user_id)
    session.add(deck)
    session.commit()
    return deck


def deck_get_by_id(deck_id):
    return session.query(Deck).get(deck_id)


def deck_update(deck_id, name):
    deck = session.query(Deck).get(deck_id)
    deck.name = name
    session.commit()
    return deck


def deck_delete_by_id(deck_id):
    deck = session.query(Deck).get(deck_id)
    session.delete(deck)
    session.commit()
    return True


def card_create(user_id, word, translation, tip):
    card = Card(user_id=user_id, word=word, translation=translation, tip=tip)
    session.add(card)
    session.commit()
    return card


def card_get_by_id(card_id):
    return session.query(Card).get(card_id)


def card_filter(sub_word):
    return session.query(Card).filter(
        (Card.word.like(f"%{sub_word}%")) |
        (Card.translation.like(f"%{sub_word}%")) |
        (Card.tip.like(f"%{sub_word}%"))
    ).all()


def card_update(card_id, word=None, translation=None, tip=None):
    card = session.query(Card).get(card_id)
    if word:
        card.word = word
    if translation:
        card.translation = translation
    if tip:
        card.tip = tip
    session.commit()
    return card


def card_delete_by_id(card_id):
    card = session.query(Card).get(card_id)
    session.delete(card)
    session.commit()
    return True
