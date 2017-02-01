#УПРАЖНЕНИЯ 
'''
3-10 . Все функции: придумайте информацию, которую можно было бы хранить в списке . 
Например, создайте список гор, рек, стран, городов, языков… словом, чего угодно . 
Напишите программу, которая создает список элементов, а затем вызывает каждую функцию, упоминавшуюся в этой главе, хотя бы один раз .
'''
languages = ["украинский", "русский", "английский", "японский", "китайский"]
print(languages[1].title())
languages.append("немецкий")
print(languages)
languages.insert(2, 'мандаринский(диалект)') 
print(languages)
del languages[0]
print(languages) 
languages.pop(1)
print(languages)
languages.remove('китайский') 
print(languages)
languages.sort()
print(languages)
print(sorted(languages))
print(languages)
languages.reverse()
print(languages)
print(len(languages))


