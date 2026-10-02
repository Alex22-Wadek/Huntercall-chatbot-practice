"""Учебный прототип чат-бота для отчета по производственной практике."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Intent:
    keywords: frozenset[str]
    answer: str


INTENTS: dict[str, Intent] = {
    "greeting": Intent(
        frozenset({"привет", "здравствуйте", "добрый"}),
        "Здравствуйте! Чем могу помочь?",
    ),
    "services": Intent(
        frozenset({"услуги", "сервис", "поддержка", "обработка"}),
        "Мы помогаем обрабатывать обращения и поддерживать цифровые коммуникации.",
    ),
    "schedule": Intent(
        frozenset({"режим", "график", "время", "работаете"}),
        "Уточните нужный проект — я передам запрос ответственному специалисту.",
    ),
    "request": Intent(
        frozenset({"заявка", "обращение", "оставить", "создать"}),
        "Опишите вопрос без лишних персональных данных. Обращение будет передано специалисту.",
    ),
    "operator": Intent(
        frozenset({"оператор", "специалист", "человек", "связаться"}),
        "Передаю запрос специалисту. Пожалуйста, ожидайте ответа.",
    ),
    "goodbye": Intent(
        frozenset({"пока", "спасибо", "до", "свидания"}),
        "Спасибо за обращение! Хорошего дня.",
    ),
}

FALLBACK = (
    "Не удалось точно определить вопрос. Уточните формулировку "
    "или напишите: «связаться со специалистом»."
)


def tokenize(text: str) -> set[str]:
    """Нормализует строку и возвращает множество слов."""
    normalized = text.lower().replace("ё", "е")
    return set(re.findall(r"[а-яa-z0-9]+", normalized))


def reply(text: str) -> str:
    """Возвращает ответ намерения с максимальным числом совпадений."""
    words = tokenize(text)
    if not words:
        return FALLBACK

    scored = [
        (len(words & intent.keywords), name, intent.answer)
        for name, intent in INTENTS.items()
    ]
    score, _, answer = max(scored)
    return answer if score > 0 else FALLBACK


def main() -> None:
    print("Чат-бот запущен. Для выхода напишите: выход")
    while True:
        message = input("Вы: ").strip()
        if message.lower() in {"выход", "exit", "quit"}:
            print("Бот: Спасибо за обращение! Хорошего дня.")
            break
        print(f"Бот: {reply(message)}")


if __name__ == "__main__":
    main()
