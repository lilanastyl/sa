from telebot.types import User
import random

sex = ['Чоловік', 'Жінка']
kids_d_46 = ['Може мати дітей', 'Може мати дітей', 'Може мати дітей', 'Не може мати дітей']
kids_u_46_to_55 = ['Може мати дітей', 'Не може мати дітей', 'Не може мати дітей']



profession = ["автомеханик","агент ФБР","агент ЦРУ","агроном","адвокат","актёр","акушер-гинеколог","альпинист","археолог","архитектор","астролог","астронавт","астроном","банкир",
"бариста","бармен","библиотекарь","бизнесмен","биолог","блогер","боец спецназа","боксёр","бортпроводник","ботаник",
"браконьер","бурильщик","бухгалтер","ветеринар","визажист","вирусолог","военнослужащий","географ","геолог","грузчик","дайвер",
"дальнобойщик","дегустатор","депутат","детектив","диджей","дизайнер","дровосек","егерь","журналист","иммунолог","инженер","инструктор по выживанию","инфекционист","картограф",
"каскадёр","кассир","киллер","кинолог","клоун","композитор","кондитер","консультант","косметолог","криминалист","критик",
"лифтёр","маркетолог","машинист","модель","мясник","окулист","онколог","официант","охранник","парикмахер","пастух","патологоанатом","певец","переводчик",
"пилот","писатель","плотник","повар","пожарный","политолог","полицейский","портной","почтальон","президент","программист","продавец мороженого",
"прокурор","психолог","психотерапевт","пчеловод","радист","разнорабочий","редактор","режиссёр",
"рыбак","садовник","сантехник","сварщик","священник","секретарь","сексолог","скульптор","слесарь","социолог","спасатель",
"стоматолог","стример","строитель","судебно-медицинский эксперт","судья","татуировщик","телеведущий","телохранитель","тренер по физической культуре","уборщик","уролог",
"учитель младших классов","учёный","фармацевт","фельдшер","фермер","физик-ядерщик","физик","философ","фотограф","футболист","химик","хирург","художник","шахтёр","эколог"]
illness = [
"ВИЧ", "авитаминоз", 
"алкоголизм", "аллергия на животных", "анорексия", "астма", "бессонница", 
"биполярное расстройство", "болезнь Альцгеймера", "ветрянка", "гайморит",
"гастрит", "гемофилия", "гепатит B", "глаукома", "глухонемота", "дальтонизм", 
"депрессия", "диарея", "заикание", "кариес", "косоглазие", "межпозвоночная грыжа", 
"мигрень", "мочекаменная болезнь", "наркомания", "недержание мочи", "ожирение", "остеохондроз",
"отсутствие ноги", "отсутствие руки", "паранойя", "плоскостопие", "пневмония", "простуда", "псориаз",
"птичий грипп", "рак крови", "рак лёгкого", "сахарный диабет второго типа", "сахарный диабет первого типа",
 "синдром Туретта", "слепота", "туберкулёз", "умственная отсталость", "цинга", "шизофрения", "эпилепсия", "язва желудка"]
character = [
"авантюризм", "безотказность", 
"безынициативность", "благоразумность", "боязливость",
"буйность", "весёлость", "властность", "внимательность", "внушаемость", 
"ворчливость", "гостеприимность", "грубость", "деликатность", "добродушие", "доброта",
"доверчивость", "жадность", "жестокость", "жизнерадостность", "истеричность", "конфликтность",
"лицемерие", "любезность", "надёжность", "невозмутимость", "нежность", "ненадёжность", "неравнодушие", 
"неусидчивость", "обидчивость", "осторожность", "пофигизм", "предприимчивость", "равнодушие", "расчётливость", 
"самовлюбленность", "самостоятельность", "сдержанность", "скандальность", "слабохарактерность",
 "собранность", "терпеливость", "тревожность", "трусость", "усидчивость", "флегматичность", "харизматичность", "храбрость", "эгоизм"]

inventar = ["Консервы и сухие продукты","Питьевая вода","Аптечка с медикаментами","Фонари и запасные батарейки","Одежда и спальные мешки","Комплект первой помощи","Предметы для гигиены","Коммуникационное оборудование", "Книги и настольные игры", 
 "Оружие и боеприпасы", 
 "Инструменты для выживания", 
 "Солнечные панели и аккумуляторы", 
 "Семена для выращивания пищи", 
 "Радио и передатчики", 
 "Противогазы и маски", 
 "Теплоизоляционные материалы", 
 "Компас и навигационное оборудование", 
 "Радиационный дозиметр", 
 "Средства для защиты от насекомых", 
 "Резервные ключи и документы" 
]

phobia = ["Арахнофобія","Клаустрофобія","Социофобия","Гіппопотомонстросесквіпедаліофобія","Номатофобія","Технофобія"]
religion = ["Християнство","Іслам","Буддизм","Дудеїзм","Модекнгеї"]
skills = ["Выращивать еду с пробирок", "Решать задачи", "Смешить людей", "Рубка дерева"]

class Person():
    def __init__(self, user):
        self.user_info: User = user
        self.choose = False
        self.sex = random.choice(sex)
        self.age = random.randint(17, 79)
        self.profession = random.choice(profession)
        self.illness = random.choice(illness)
        self.kids = self.setKids()
        self.phobia = random.choice(phobia)
        self.character = random.choice(character)
        self.skills = random.choice(character)
        self.religion = random.choice(religion)
        self.inventar = random.choice(inventar)




    def setKids(self):
        if self.age <= 46:
            return random.choice(kids_d_46)
        elif self.age > 46 and self.age < 55:
            return random.choice(kids_u_46_to_55)
        elif self.age < 55 and self.illness == 'Абсолютно здоровий':
            return 'Може мати дітей'
        else:
            return 'Не може мати дітей'


    def getPerson(self):
        persona = """
🚻Стать: {0}
🎂Вік: {1}
🔧Професія: {2}
💟Стан здоров'я: {3}
♿Інвалідність: {4}
🚼Можливість мати дітей: {5}
☀Характер: {6}
🛐Релігія: {7}
🙈Фобія: {8}
⛳Хобі/вміння: {9}
🎒Багаж: {11} 
        """.format(self.sex, self.age, self.profession, self.illness,  self.kids, self.character,
                   self.religion, self.phobia, self.skills, self.inventar)
        return persona



