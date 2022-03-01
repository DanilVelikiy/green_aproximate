# вывожу старт в начале, что бы видеть что начался процесс, а не зависание какое то
print('Поехали !')

# устанавливаю необхимые зависимости
import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt

# -- ПОДГОТОВКА ХОЛСТА MATPLOTLIB ---

# задаю сетку из двух частей расположенных  горизонталь
gridsize = (1, 2)

# создаю объект холста для графиков размером 16 на 8 (это в полный экран на маке
fig = plt.figure(figsize=(16,8))

# создаю объекты - сетки осей для рисования грфиков с ссоттвествующим расположением на сетке холста
ax = plt.subplot2grid(gridsize, (0,0))
ax1 = plt.subplot2grid(gridsize, (0,1))

# --- ПОДГОТОВКА ДАННЫХ  ---
# создам датафрэйм пандас из эксель файла с данными с нужной вкладки
excel_file = pd.read_excel('ANALYS.xlsx', 'КП')

# создам нужные серии пандас данных из столбоц
year = excel_file[excel_file.columns[1]]
inflation_popravka = excel_file[excel_file.columns[2]]
type_object = excel_file[excel_file.columns[3]]
square = excel_file[excel_file.columns[4]]
price = excel_file[excel_file.columns[7]]

# создам массивы чисел снужными данными
# [3:] - отсекая первые три строки, там заголовки
# array - конвертация серии пандас в массим numpy
# astype - приведение типа данных массива к числовому с плавающей точкой двойной точности
x = square[3:].array.astype('double')
y = (price[3:] * inflation_popravka[3:] / square[3:]).array.astype('double')

# подбор апрокимирующего полинома высокого порядка
t = np.polyfit(x, y, 8)
f = np.poly1d(t)
print(f)

# подбор апрокимирующего полинома низкого порядка
t1 = np.polyfit(x, y, 4)
f1 = np.poly1d(t1)
print(f1)

# укажу величину площади, для которой хочу спрогнозировать стоимость
x_input = 1500

# о полученном результате прогноза выведу строку
print(f'По полиному высокого порядка стоимость квадратного метра для {x_input} кв.м. будет {f(x_input)},'
      f'полная стоимость {f(x_input) * x_input} ({f1(x_input) * x_input} по полиному низкого порядка) ')

# на заданных полотнах нарисую матплотлибом графики
# на первом графике размещу исходные точки и оба графика
# по ключю '1' matplotlib точки отрисовывает трехлучевыми звездочками
ax.plot(x, y, '1', x, f(x), x, f1(x))
#  второй график - это полном низкой степени
ax1.plot(x, f1(x))

# показываю окно с холстом matplotlib с нарисованными графиками
plt.show()