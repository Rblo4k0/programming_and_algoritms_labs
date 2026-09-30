from src.lib.text import normalize, tokenize, count_freq, top_n

input_text = input()

if not input_text.strip():
    print("Ввод пуст.")
else:
    normalized = normalize(input_text)
    tokens = tokenize(normalized)
    freq_dict = count_freq(tokens)
    top_5 = top_n(freq_dict)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq_dict)}")
    print("Топ-5:")
    for word, count in top_5:
        print(f"{word}:{count}")