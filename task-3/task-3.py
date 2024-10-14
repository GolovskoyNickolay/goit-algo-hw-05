import timeit
from pathlib import Path

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
            else:
                if j != 0:
                    j = lps[j - 1]
                    i -= 1
                else:
                    lps[i] = 0
        return lps

    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Алгоритм Боєра-Мура
def bm_search(text, pattern):
    def build_last_occurrence(pattern):
        last = {}
        for i in range(len(pattern)):
            last[pattern[i]] = i
        return last

    last = build_last_occurrence(pattern)
    m = len(pattern)
    n = len(text)
    i = m - 1
    j = m - 1

    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            lo = last.get(text[i], -1)
            i = i + m - min(j, lo + 1)
            j = m - 1
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp_search(text, pattern, d=256, q=101):
    m = len(pattern)
    n = len(text)
    h = 1
    p = 0
    t = 0

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1


text1 = open('стаття-1.txt', 'r').read()
text2 = open('стаття-2.txt', 'r', encoding="utf8").read()



existing_substring = "таблиці"  # підрядок, що існує в текстах
non_existing_substring = "неіснуючий_підрядок"  # вигаданий підрядок

# Функція для вимірювання часу виконання алгоритму
def measure_time(func, text, pattern):
    timer = timeit.Timer(lambda: func(text, pattern))
    return timer.timeit(number=100)  # 100 запусків для точності

# Вимірюємо час для кожного алгоритму та кожного підрядка
results = {}

# Тестуємо на тексті 1
results['text1_kmp_existing'] = measure_time(kmp_search, text1, existing_substring)
results['text1_kmp_non_existing'] = measure_time(kmp_search, text1, non_existing_substring)
results['text1_bm_existing'] = measure_time(bm_search, text1, existing_substring)
results['text1_bm_non_existing'] = measure_time(bm_search, text1, non_existing_substring)
results['text1_rk_existing'] = measure_time(rabin_karp_search, text1, existing_substring)
results['text1_rk_non_existing'] = measure_time(rabin_karp_search, text1, non_existing_substring)

# Тестуємо на тексті 2
results['text2_kmp_existing'] = measure_time(kmp_search, text2, existing_substring)
results['text2_kmp_non_existing'] = measure_time(kmp_search, text2, non_existing_substring)
results['text2_bm_existing'] = measure_time(bm_search, text2, existing_substring)
results['text2_bm_non_existing'] = measure_time(bm_search, text2, non_existing_substring)
results['text2_rk_existing'] = measure_time(rabin_karp_search, text2, existing_substring)
results['text2_rk_non_existing'] = measure_time(rabin_karp_search, text2, non_existing_substring)

# Виводимо результати
for key, value in results.items():
    print(f"{key}: {value:.6f} секунд")


# Знаходимо найшвидший алгоритм для кожного тексту
def find_fastest_algorithm(text_results):
    fastest_time = float('inf')
    fastest_algorithm = ""
    for key, time in text_results.items():
        if time < fastest_time:
            fastest_time = time
            fastest_algorithm = key
    return fastest_algorithm, fastest_time

# Результати для тексту 1
text1_results = {k: v for k, v in results.items() if 'text1' in k}
fastest_text1, time_text1 = find_fastest_algorithm(text1_results)
print(f"Найшвидший алгоритм для тексту 1: {fastest_text1}, час: {time_text1:.6f} секунд")

# Результати для тексту 2
text2_results = {k: v for k, v in results.items() if 'text2' in k}
fastest_text2, time_text2 = find_fastest_algorithm(text2_results)
print(f"Найшвидший алгоритм для тексту 2: {fastest_text2}, час: {time_text2:.6f} секунд")

# Висновок для обох текстів
print("\nНа основі виконання кожного з трьох алгоритмів визначено найшвидший алгоритм для кожного з двох текстів.")