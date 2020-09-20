users = []
while True:   
    name = input('Введите ваше имя: ')
    age = int(input('Введите ваш возраст: '))
    gender_id = int(input('Выберете ваш гендер:\n1. Мужской\n2. Женский\n'))
    if gender_id == 1:
        gender = 'Мужской'
    elif gender_id == 2:
        gender = 'Женский'
    else:
        raise Exception('Такой пол ещё не известен человечеству') 
    weight = int(input('Введите ваш вес: '))
    height = int(input('Введите ваш рост: '))
    users.append({'name': name, 'age': age, 'gender': gender, 'weight': weight, 'height': height})
    ans = input('Continue [y/n]: ')
    if ans.lower() != 'y':
        break

for user in users: 
    print("Ваше имя: {name}\nВаш возраст: {age}\nВаш гендер: {gender}\nМасса: {weight}\nРост: {height}".format(**user))
    bmi = int(weight//((height/100)*(height/100)))
    assert 15 <= bmi <= 50, "Проверьте введённые данные"
    print('Ваш индекс массы тела ' + str(bmi))
    scale = '15' + "=" * (bmi - 15) + '|' + "="*(35 - (20 - bmi)) + "50"
    print(scale)
    if bmi <= 18:
        print('Покушайте, пожалуйста, вас скоро будет сдувать ветер')
    elif 19 <= bmi <= 25:
        print('Вы идеальны! Любите себя и не стремитесь похудеть :)')
    elif 26 <= bmi <= 50:
        print('Возможно, вы сейчас не в самой лучшней форме. Советую вам купить безглютеновый хлеб, низкопроцентный йогурт и бегать по утрам :)')
