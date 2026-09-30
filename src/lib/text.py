def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализует текст: приведение к регистру, замена ё/Ё и очистка пробелов.
    """
    if casefold: text = text.casefold()
    
    if yo2e: text = text.replace('ё', 'е').replace('Ё', 'Е')
        
    return " ".join(text.split())


def tokenize(text: str) -> list[str]:
    """
    Разбивает текст на слова, учитывая дефисы внутри слов.
    """
    tokens = []
    current_word = []
    
    for i, char in enumerate(text):
        is_word_char = char.isalnum() or char == '_'
        
        if is_word_char: current_word.append(char)
        elif char == '-':
            prev_is_word = i > 0 and (text[i - 1].isalnum() or text[i - 1] == '_')
            next_is_word = i + 1 < len(text) and (text[i + 1].isalnum() or text[i + 1] == '_')
            
            if current_word and prev_is_word and next_is_word: current_word.append(char)
            elif current_word:
                tokens.append("".join(current_word))
                current_word = []
        elif current_word:
            tokens.append("".join(current_word))
            current_word = []
                
    if current_word: tokens.append("".join(current_word))
        
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Подсчитывает частоту слов.
    """
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Сортирует слова по убыванию частоты и по алфавиту при равной частоте.
    """
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]


if __name__ == "__main__":
    print(fr'''
    normalize

    "ПрИвЕт\nМИр\t" -> {normalize("ПрИвЕт\nМИр\t")}
    "ёжик, Ёлка" -> {normalize("ёжик, Ёлка")}
    "Hello\r\nWorld" -> {normalize("Hello\r\nWorld")}
    "  двойные   пробелы  " -> {normalize("  двойные   пробелы  ")}
    ''')

    print(fr'''
    tokenize

    "привет мир" -> {tokenize("привет мир")}
    "hello,world!!!" -> {tokenize("hello,world!!!")}
    "по-настоящему круто" -> {tokenize("по-настоящему круто")}
    "2025 год" -> {tokenize("2025 год")}
    "emoji 😀 не слово" -> {tokenize("emoji 😀 не слово")}
    ''')

    print(fr'''
    count_freq + top_n

    Токены ["a","b","a","c","b","a"] -> частоты {count_freq(["a", "b", "a", "c", "b", "a"])};
    top_n(..., n=2) -> {top_n(count_freq(["a", "b", "a", "c", "b", "a"]), 2)}

    При равенстве частот: токены ["bb","aa","bb","aa","cc"] -> {count_freq(["bb", "aa", "bb", "aa", "cc"])};
    top_n(..., n=2) → {top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), 2)}
    ''')