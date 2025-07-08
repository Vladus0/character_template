from jinja2 import Environment, FileSystemLoader, select_autoescape
import random

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('template.html')


def main():
    cards_count = int(input("Сколько карточек вы хотите созадть: "))

    for card_number in range(cards_count):
        personages_name = input("Введите имя персонажа ")

        races = ["Человек", "Орк"]

        while True:
            personages_race = input(f"{races} \nВведите название рассы из предлженных: ")
            if personages_race in races:
                break
            else:
                print("Расса введена неправильно")


        classes = ["Охотник", "Маг", "Воин", "Ассасин", "Бард"]

        while True:
            personages_class = input(f"{classes} \nВведите название класса из предлженных: ")
            if personages_class in classes:
                break
            else:
                print("Класс введен неправильно")

        personages_strength = random.randint(1, 3)
        personages_agility = random.randint(1, 3)
        personages_intelligence = random.randint(1, 3)
        personages_luck = random.randint(1, 3)
        personages_temper = random.randint(1, 3)

        clases_base = {
            "Охотник": {
                "skills": ['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
                "characteristics": {
                        "strength": personages_strength,
                        "agility": 15,
                        "intelligence": personages_intelligence,
                        "luck": personages_luck,
                        "temper": personages_temper
                },
                "img_path": 'images/archer.png'
            },
            "Маг": {
                "skills": ['Стрела ледяного огня', 'Снятие проклятия', 'Огненный взрыв', 'Обледенение', 'Ледяное копье', 'Конус холода', 'Прилив сил', 'Морозный доспех'],
                "characteristics": {
                        "strength": personages_strength,
                        "agility": personages_agility,
                        "intelligence": 15,
                        "luck": personages_luck,
                        "temper": personages_temper
                },
                "img_path": 'images/wizard.png'
            },
            "Воин": {
                "skills": ['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
                "characteristics": {
                        "strength": 15,
                        "agility": personages_agility,
                        "intelligence": personages_intelligence,
                        "luck": personages_luck,
                        "temper": personages_temper
                },
                "img_path": 'images/warrior.png'
            },
            "Ассасин": {
                "skills": ['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'],
                "characteristics": {
                        "strength": personages_strength,
                        "agility": personages_agility,
                        "intelligence": personages_intelligence,
                        "luck": 15,
                        "temper": personages_temper
                },
                "img_path": 'images/assasin.png'
            },
            "Бард": {
                "skills": ['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием'],
                "characteristics": {
                        "strength": personages_strength,
                        "agility": personages_agility,
                        "intelligence": personages_intelligence,
                        "luck": personages_luck,
                        "temper": 15
                },
                "img_path": 'images/bard.png'
            },
        }
        skills = clases_base[personages_class]["skills"]
        personages_skills = random.sample(skills, 3)


        rendered_page = template.render(
            name = personages_name,
            race = personages_race,
            character_class = personages_class,
            strength = clases_base[personages_class]["characteristics"]["strength"],
            agility = clases_base[personages_class]["characteristics"]["agility"],
            intelligence = clases_base[personages_class]["characteristics"]["intelligence"],
            luck = clases_base[personages_class]["characteristics"]["luck"],
            temper = clases_base[personages_class]["characteristics"]["temper"],
            image = clases_base[personages_class]["img_path"],
            first_skill = personages_skills[0],
            second_skill = personages_skills[1],
            third_skill = personages_skills[2]
        )

        with open(f'characters/index{card_number}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)

if __name__=="__main__":
    main()