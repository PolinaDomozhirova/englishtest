import random


class QuestionsAnswers:
    def __init__(self, question, correct_answer, other_answers):
        self.question = question
        self.correct_answer = correct_answer
        self.other_answers = other_answers

def open_file():
    q = open("english.txt", encoding='utf-8')
    info_from_file = q.readlines()
    qa_list = []
    number_tasks = 0
    for st in info_from_file:
        st = [x.rstrip() for x in st.split(', ')]
        qa_list.append(QuestionsAnswers(st[0], st[1], st[2:]))
        number_tasks += 1
    test(number_tasks, qa_list)

def test(number_tasks, qa_list):
    counter = 0
    random.shuffle(qa_list)
    for qa_item in qa_list:
        print(qa_item.question)
        print("Выберите правильный вариант ответа:")
        possible = qa_item.other_answers + [qa_item.correct_answer]
        random.shuffle(possible)
        count = 0
        while count < len(possible):
            print(str(count + 1) + ": " + possible[count])
            count += 1
        print("Ответ: ")
        user_answer = input().strip()
        while not user_answer.isdigit():
            print("Но ведь это не цифра! Пожалуйста, введите номер ответа:")
            user_answer = input().strip()
        if user_answer.isdigit():
            user_answer = int(user_answer)
            while not (user_answer > 0 and user_answer <= len(possible)):
                print("Такого номера нет. Пожалуйста, введите номер:")
                user_answer = input().strip()
                user_answer = int(user_answer)
            if possible[user_answer - 1] == qa_item.correct_answer:
                print("Верно!")
                counter += 1
                number_tasks -= 1
            else:
                print("Неверно!")
                number_tasks -= 1
                print("Правильный ответ: " + qa_item.correct_answer)
                print("")
        if number_tasks != 0:
            continue
        print("Вы ответили правильно на " + str(counter) + " из " + str(len(qa_list)) + " заданий.")


print("Данный тест, напрвленный на изучение английского языка, включает в себя предложения"
            " с пропуском слова или словосочетания, который необходимо заполнить, выбрав правильный вариант ответа. "
            "Всего в тесте 12 заданий.\nЖелаем удачи!")
select = input("Введите ДА, если хотите начать тест, введите НЕТ, если хотите выйти из программы для прохождения теста: ").lower().strip()
if select == "да":
    open_file()
elif select == "нет":
    print("Вы вышли из программы!")
else:
    print("Вы ввели что-то отличное от ДА или НЕТ!")

