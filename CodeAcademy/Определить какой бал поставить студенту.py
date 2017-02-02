# Массив данных о студенте. Имя, баллы за домашнее задание, опросы, тесты
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
"""функция считает среднее арифметическое"""
def average(numbers):
    lenght = float(len(numbers))
    total = sum(numbers)
    total /= lenght
    return total
"""считаем среднее арифметическое для всех категорий, и возвращаем общий бал исходя из коэффициентов полезности категорий"""
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests
"""считаем общий бал в буквенном эквиваленте"""
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
"""Буква соответствующая оценке ученика"""
print get_letter_grade(get_average(lloyd))
"""Средний бал в классе"""
def get_class_average(students):
    results = []
    for x in students:
        calculate = get_average(x)
        results.append(calculate)
    return average(results)
"""Тестируем. Взяли студентов, получили средний бал в числовом формате"""
students = [lloyd, alice, tyler]
print get_class_average(students)
"""Тестируем. Получили средний бал по студентам как букву"""
print get_letter_grade(get_class_average(students))
