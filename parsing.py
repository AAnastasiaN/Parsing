# f = open('somefile.txt', encoding='utf-8')<-- для примера

# сначала просматриваем код сайта, ознакамливаемся с его структурой
from bs4 import BeautifulSoup
with open('for_example.html', encoding='utf-8') as file:
   scr = file.read()
# print(scr)
# выстраиваем дерево объектов при помощи этой бт
soup = BeautifulSoup(scr, "lxml")
#выводим нужную нам информацию
# title=soup.title
# print(title.text)

# методы .find() .find_all() <-- работают сверху вниз

# выводит первый попавшийся искомый элемент
# page_h3 = soup.find("h3")
# print(page_h3)


# ищет все элементы и сохраняет их в список
# page_all_h3 = soup.find_all("h3")
# print(page_all_h3)

# с помощью цикла делаем запись более удобной для нас

# for item in page_all_h3:
#     print(item.text)

# найдём имя пользователя

# user_name = soup.find("div", class_ = "user__name")
# print(user_name.text)

# соберём все span теги из класса user info

# find_all_span_user_info = soup.find(class_ = "user__info").find_all("span")
# print(find_all_span_user_info)
# for item in find_all_span_user_info:
#     print(item.text)
    
# парсим ссылки

# social_links = soup.find(class_= "social__networks").find("ul").find_all("a")
# print(social_links)

# all_a = soup.find_all("a")
# print(all_a)

# приведём ссылки в порядок

# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f"{item_text}: {item_url}")


# методы .find_parent() .find_parents() <-- работают снизу вверх

# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)


# методы .next_element .previous_element

# next_el = soup.find(class_="post__title").next_element.next_element
# print(next_el)

# метод .previous_element работает наоборот


# методы .find_next_sibling() .find_previous_sibling()

# next_sub = soup.find(class_="post__title").find_next_sibling()
# print(next_sub)


# метод re.compile("...") = поиск по слову



    