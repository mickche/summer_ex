def analize_text(text:str):
    total_characters = len(text)
    
    chars_without_spaces = 0
    for char in text:
        if char != " ":
            chars_without_spaces = chars_without_spaces + 1
            
    words_list = text.split()
    total_words = len(words_list)
    
    longest_word = ""
    for word in words_list:
        clean_word = word.strip(".,!?:;\"'()")
        if len(clean_word) > len(longest_word):
            longest_word = clean_word
            
    sentence_count = 0
    punctuation_marks = ".!?"
    for char in text:
        if char in punctuation_marks:
            sentence_count = sentence_count + 1
            
    if sentence_count == 0 and total_words > 0:
        sentence_count = 1

    print("\n--- РЕЗУЛЬТАТИ АНАЛІЗУ ---")
    print("Загальна кількість символів (з пробілами):", total_characters)
    print("Кількість символів (без пробілів):", chars_without_spaces)
    print("Загальна кількість слів:", total_words)
    print("Приблизна кількість речень:", sentence_count)
    print("Найдовше слово у тексті:", longest_word)


text = """Технології вже давно перестали бути просто інструментом — вони стали тканиною нашого повсякденного життя. Щодня ми взаємодіємо з алгоритмами штучного інтелекту, користуємося хмарними сховищами та зв'язуємося з людьми на іншому кінці планети за лічені секунди.
Сучасні інновації трансформують ключові сфери:
Медицина: Штучний інтелект допомагає діагностувати захворювання на ранніх стадіях, а 3D-друк дає змогу створювати протези та навіть тканини.
Освіта: Інтерактивні платформи та віртуальна реальність роблять навчання доступним із будь-якої точки світу.
Екологія: «Зелені» технології, такі як відновлювана енергетика та електромобілі, допомагають зменшити людський слід на планеті.
Головна цінність технологій полягає не в самих залізяках чи коді, а в можливостях, які вони відкривають для людини. Вони беруть на себе рутину, звільняючи час для творчості, пізнання та спілкування."""


analize_text(text)

