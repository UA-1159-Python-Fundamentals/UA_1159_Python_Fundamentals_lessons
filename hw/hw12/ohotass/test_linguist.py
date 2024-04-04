# test_linguist.py

from linguist import *

# Create a user
user = user_create("John Doe", "john@example.com", "password")

# Retrieve a user by ID
retrieved_user = user_get_by_id(user.id)
assert retrieved_user.name == "John Doe"

# Update user's name
updated_user = user_update_name(user.id, "John Smith")
assert updated_user.name == "John Smith"

# Change user's password
password_changed = user_change_password(user.id, "password", "new_password")
assert password_changed is True

# Create a deck
deck = deck_create("Vocabulary", user.id)

# Retrieve a deck by ID
retrieved_deck = deck_get_by_id(deck.id)
assert retrieved_deck.name == "Vocabulary"

# Update deck's name
updated_deck = deck_update(deck.id, "New Vocabulary")
assert updated_deck.name == "New Vocabulary"

# Create a flashcard
card = card_create(user.id, "Hello", "Привіт", "A common greeting")

# Retrieve a flashcard by ID# test_linguist.py (continued)

retrieved_card = card_get_by_id(card.id)
assert retrieved_card.word == "Hello"

# Filter flashcards by substring
filtered_cards = card_filter("common")
assert len(filtered_cards) == 1
assert filtered_cards[0].tip == "A common greeting"

# Update flashcard
updated_card = card_update(card.id, word="Hi", translation="Привіт", tip="A casual greeting")
assert updated_card.word == "Hi"

# Delete flashcard
card_deleted = card_delete_by_id(card.id)
assert card_deleted is True

# Delete user
user_deleted = user_delete_by_id(user.id)
assert user_deleted is True
