users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
a = len(users)
b = len(set(users))
describe = {
"Общее количество" :a,
"Уникальные посещения" : b
}
print(describe)