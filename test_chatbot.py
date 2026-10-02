import unittest

from chatbot import FALLBACK, reply, tokenize


class ChatbotTests(unittest.TestCase):
    def test_tokenize_normalizes_case_and_yo(self):
        self.assertEqual(tokenize("ДОБРЫЙ, всё хорошо!"), {"добрый", "все", "хорошо"})

    def test_greeting(self):
        self.assertEqual(reply("Здравствуйте"), "Здравствуйте! Чем могу помочь?")

    def test_operator(self):
        self.assertIn("специалист", reply("Хочу связаться с человеком"))

    def test_unknown_request(self):
        self.assertEqual(reply("непонятный вопрос"), FALLBACK)

    def test_empty_request(self):
        self.assertEqual(reply("   "), FALLBACK)


if __name__ == "__main__":
    unittest.main()
