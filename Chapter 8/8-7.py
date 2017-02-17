# 8-8 . Пользовательские альбомы: начните с программы из упражнения 8-7 . 
# Напишите цикл while, в котором пользователь вводит исполнителя и название 
# альбома . Затем в цикле вызывается функция make_album() для введенных 
# пользователей и выводится созданный словарь . Не забудьте предусмотреть 
# признак завершения в цикле while .
def make_album(musician, album_title, count = ""):
    album = {"name": musician.title(), "title" : album_title.title()}
    if count:
        album["count"] = count
    return album

while True:
    print("Для выхода нажмите 'q' в любое время")
    name = input("введите имя артиста: ")
    if name == "q":
        break
    album = input("введите наименование альбома: ")
    if album == "q":
        break
    count = input("введите количество дорожек: ")
    if count == "q":
        break
    album = make_album(name, album, count)
    print(album)