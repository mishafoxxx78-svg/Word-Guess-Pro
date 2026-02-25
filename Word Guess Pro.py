import random
import os

# ==============================
# WORD GUESS PRO
# ==============================

WORDS = [
    "python", "developer", "telegram", "algorithm",
    "database", "function", "variable", "internet",
    "keyboard", "monitor"
]

MAX_ATTEMPTS = 6
SAVE_FILE = "rating.txt"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def load_rating():
    try:
        with open(SAVE_FILE, "r") as f:
            return int(f.read())
    except:
        return 0


def save_rating(score):
    with open(SAVE_FILE, "w") as f:
        f.write(str(score))


def display_word(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])


def game():
    word = random.choice(WORDS)
    guessed_letters = []
    attempts = MAX_ATTEMPTS

    while attempts > 0:
        clear()
        print("🎮 WORD GUESS PRO")
        print("-" * 30)
        print("Слово:", display_word(word, guessed_letters))
        print("Попытки:", attempts)
        print("Использованные буквы:", ", ".join(guessed_letters))

        guess = input("Введите букву: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Введите одну букву!")
            input("Enter для продолжения...")
            continue

        if guess in guessed_letters:
            print("⚠ Вы уже вводили эту букву!")
            input("Enter для продолжения...")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Верно!")
        else:
            print("❌ Неверно!")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            clear()
            print("🎉 ПОБЕДА!")
            print("Слово было:", word)
            return True

        input("Enter для продолжения...")

    clear()
    print("💀 ВЫ ПРОИГРАЛИ")
    print("Слово было:", word)
    return False


def menu():
    rating = load_rating()

    while True:
        clear()
        print("======== WORD GUESS PRO ========")
        print("🏆 Ваш рейтинг:", rating)
        print("1. Новая игра")
        print("2. Выход")
        choice = input("Выберите пункт: ")

        if choice == "1":
            if game():
                rating += 1
                save_rating(rating)
        elif choice == "2":
            break
        else:
            print("Неверный ввод!")
            input("Enter для продолжения...")


if __name__ == "__main__":
    menu()