#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-info">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Привет Сергей! Меня зовут Марат, и я буду твоим ревьюером. По поводу обращения - в IT сфере принято общаться на «ты» :) Но, если привычней на «вы», дай знать. Как ревьюера моя задача помочь тебе в развитии, дав хорошие советы. Я внимательно посмотрю твой код, ознакомлюсь с твоими выводами и оставлю комментарии. Где то могу предложить небольшие исправление в коде, но ненавязчиво. Где потребуются уточнения, я оставлю много наводящих вопросов. Они помогут тебя с поиском верного решения.
# 
# Все мои комментарии размечены по цветам, для лучшего восприятия. 
#     
# <div class="alert alert-success">Зеленым цветом и словом «Успех» отмечены особо удачные и элегантные решения, которыми ты можешь гордиться. </div>
#         
# <div class="alert alert-warning">Желтым и значком словом «Совет», помечены решения у которых есть альтернативные решения, более оптимальные. Ты можешь найти их сразу и доработать проект, или отложить это на потом, для будущих проектах. Проект будет принят и без их доработки. </div>
#         
# <div class="alert alert-danger"> Красным цветом и значком словом «Ошибка» помечу твои решения, на которые стоит обратить внимание прежде всего. После их доработки проект будет принят. </div>
#         
# Залог успеха - работа сообща, взаимное уважение и работа в диалоге. Поэтому, помечай свои ответные комментарии на мои реплики заметным цветом или курсивом, так мне будет легче их отслеживать. Пожалуйста, не изменяй и не удаляй мои комментарии. Все это поможет выполнить повторную проверку быстрей.
# 
# </div>

# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Ошибка:
# 
# 
# Вступление в работу очень важно, так человек, который смотрит твой проект (и на работе в том числе) будет сразу введен в курс дела.
# 
# 
# Можно пойти дальше, внедрив интерактивное оглавление. Это сделает проект более удобным для использования. Ты можешь добавить гиперссылки или использовать плагин toc (Table of Contents), чтобы создать автоматическое оглавление в своем Jupyter Notebook. В разделе "Полезные инструкции для учёбы" курса ты найдешь подробное руководство о том, как это сделать.

# Перед нами стоит задача промаркировать уровень финансовой активности постоянных покупателей. В компании принято выделять два уровня активности: «снизилась», если клиент стал покупать меньше товаров, и «прежний уровень».
# Нужно собрать данные по клиентам по следующим группам:
# Признаки, которые описывают коммуникацию сотрудников компании с клиентом.
# Признаки, которые описывают продуктовое поведение покупателя. Например, какие товары покупает и как часто.
# Признаки, которые описывают покупательское поведение клиента. Например, сколько тратил в магазине.
# Признаки, которые описывают поведение покупателя на сайте. Например, как много страниц просматривает и сколько времени проводит на сайте.

# # Проект: Обучение с учителем: качество модели

# Описание проекта \
# Интернет-магазин «В один клик» продаёт разные товары: для детей, для дома, мелкую бытовую технику, косметику и даже продукты. Отчёт магазина за прошлый период показал, что активность покупателей начала снижаться. Привлекать новых клиентов уже не так эффективно: о магазине и так знает большая часть целевой аудитории. Возможный выход — удерживать активность постоянных клиентов. Сделать это можно с помощью персонализированных предложений.
# «В один клик» — современная компания, поэтому её руководство не хочет принимать решения просто так — только на основе анализа данных и бизнес-моделирования. У компании есть небольшой отдел цифровых технологий, и вам предстоит побыть в роли стажёра в этом отделе. 
# Итак, вашему отделу поручили разработать решение, которое позволит персонализировать предложения постоянным клиентам, чтобы увеличить их покупательскую активность.

# <a href='#sec1'>Шаг 1. Загрузка данных</a>\
# <a href='#sec1.1'> Шаг 1.1. Загрузка датасетов</a>\
# <a href='#sec1.2'> Шаг 1.2. Анализ данных</a>\
# <a href='#sec2'>Шаг 2. Предобработка данных</a>\
# <a href='#sec3'>Шаг 3. Исследовательский анализ данных</a>\
# <a href='#sec4'>Шаг 4. Объединение таблиц</a>\
# <a href='#sec5'>Шаг 5. Корреляционный анализ</a>\
# <a href='#sec6'>Шаг 6. Использование пайплайнов</a>\
# <a href='#sec7'>Шаг 7. Анализ важности признаков</a>\
# <a href='#sec8'>Шаг 8. Сегментация покупателей</a>\
# <a href='#sec9'>Шаг 9. Общий вывод</a>
# 

# In[1]:


#Код ревьюера
get_ipython().system(' pip install phik')
get_ipython().system(' pip install shap')
get_ipython().system('pip install -U scikit-learn')


# Импортируем библиотеки

# In[2]:


import pandas as pd
import copy
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats as st
from scipy.stats import shapiro
import numpy as np
import plotly.express as px
import matplotlib.colors as mcolors
import sklearn
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import (
    OneHotEncoder,
    OrdinalEncoder,
    StandardScaler,
    MinMaxScaler,
    RobustScaler,
    PolynomialFeatures
)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    mean_absolute_error, 
    r2_score, 
    mean_squared_error, 
    mean_absolute_error, 
    recall_score, 
    precision_score, 
    roc_auc_score,
    confusion_matrix,
    f1_score
)
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
import phik
from phik.report import plot_correlation_matrix
from phik import report
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import shap
from sklearn.inspection import permutation_importance
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import SelectKBest, f_classif
from scipy.cluster.hierarchy import dendrogram, linkage


# 
# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Успех:
# 
# Собираем все импорты в верхней части, чтобы легче было ориентироваться и добавлять новые по необходимости. 
# 
#     
# <div class="alert alert-warning">
#  
# 
# Совет 🤔:
# 
# Смотри что  можно сделать согласно PEP-8.  Вместо
#     
# 
#     from sklearn.model_selection import cross_val_score
#     from sklearn.model_selection import train_test_split
#     from sklearn.model_selection import StratifiedKFold
#     from sklearn.model_selection import GridSearchCV
#     
# 
# Пишем в одну строку через запятую    
# 
#     
#     from sklearn.model_selection import cross_val_score,  train_test_split, ...
#     
#     
# 
# Если запись получается слишком длинной, это тоже противоречит PEP8, тогда скобочки:
# 
# 	from sklearn.metrics import (
# 	   accuracy_score, 
#  	   confusion_matrix, 
# 	   r2_score,
#  	   precision_score,
#  	   recall_score
# 	)
# 
# 
# 
# Во-вторых видишь у тебя есть pip install. Допустим:
#     
#     
#     # pip install nltk # доустанавливаем необходимые библиотеки
#     # pip install pywsd
#     # pip install transformers  
#     
#     
#     
# Это значит что у нас сторонние библиотеки и значит    
# 
#     
#     
#     import transformers
#     
# итд
#     
# ставим в самый конец    
#     
# По аналогии можешь исправить  
# 
# 

# <a id='sec1'></a>
# ## Загрузка данных

# <a id='sec1.1'></a>
# ### Загрузка датасетов

# In[3]:


market_file = pd.read_csv('/datasets/market_file.csv', sep=',')
market_money = pd.read_csv('/datasets/market_money.csv', sep=',')
market_time = pd.read_csv('/datasets/market_time.csv', sep=',')
money = pd.read_csv('/datasets/money.csv', sep=';', decimal=',')


# <a id='sec1.2'></a>
# ### Анализ данных

# In[4]:


market_file.info()


# In[5]:


market_file.head(20)


# In[6]:


market_money.info()


# In[7]:


market_money.head(20)


# In[8]:


market_time.info()


# In[9]:


market_time.head(20)


# In[10]:


money.info()


# In[11]:


money.head(20)


# Данные соответствуют описанию, все в порядке

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Успех:
# 
# Предварительный обзор данных проведён
#     
#     
# 

# <a id='sec2'></a>
# ## Предобработка данных

# In[12]:


market_file.isna().sum()


# In[13]:


market_file.duplicated().sum()


# In[14]:


market_file['Покупательская активность'].unique()


# In[15]:


market_file['Тип сервиса'].unique()


# In[16]:


market_file['Тип сервиса'] = market_file['Тип сервиса'].str.replace('стандартт', 'стандарт')


# In[17]:


market_file['Тип сервиса'].unique()


# Убрал неявные дубликаты

# In[18]:


market_money.isna().sum()


# In[19]:


market_money.duplicated().sum()


# In[20]:


market_time.isna().sum()


# In[21]:


market_time.duplicated().sum()


# In[22]:


market_time['Период'].unique()


# In[23]:


market_time['Период'] = market_time['Период'].str.replace('предыдцщий_месяц', 'предыдущий_месяц')


# In[24]:


market_time['Период'].unique()


# Исправил грамматические ошибки, ибо сильно бросались в глаза

#     
# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# 
# 
# Успех:
# 
# 
#     
# - Здорово что обращено внимание  скрытые дубликаты, и грамматические ошибки найдены    
#     
# 
# 
# 
# 

# In[25]:


money.isna().sum()


# In[26]:


money.duplicated().sum()


# 
#  <div class="alert alert-warning">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Совет: 
# 
# 
# Неплохо бы привезти название столбцов к змеиному виду. Можно  автоматизировать процесс воспользовавшись  .lower, а с помощью регуляризации    (или .rename) избавиться от точек, % итп, а если надо организовать нижние подчёркивание (привезти название столбцов к змеиному коду). Пример регулярного выражения:  
#      
# 

# <a id='sec3'></a>
# ## Исследовательский анализ данных

# In[27]:


market_file['Покупательская активность'].value_counts().plot(title='Данные о покупательской активности', kind='pie', autopct = '%1.0f%%', figsize=(7,7))
display(market_file['Покупательская активность'].value_counts())


# In[28]:


market_file['Тип сервиса'].value_counts().plot(title='Данные о типе сервиса', kind='pie', autopct = '%1.0f%%', figsize=(7,7))
display(market_file['Тип сервиса'].value_counts())


# In[29]:


market_file['Разрешить сообщать'].value_counts().plot(title='Данные о возможности присылать покупателю дополнительные предложения о товаре', kind='pie', autopct = '%1.0f%%', figsize=(7,7))
display(market_file['Разрешить сообщать'].value_counts())


# In[30]:


market_file.hist('Маркет_актив_6_мес', bins=10, figsize=(10,7))
plt.xlabel('Среднемесячное значение маркетинговых коммуникаций компании')
plt.show()

display('Диаграмма размаха')
market_file.boxplot(column=['Маркет_актив_6_мес'], figsize=(10,7), grid=True)
plt.xlabel('Среднемесячное значение маркетинговых коммуникаций компании')
plt.show()

print(market_file['Маркет_актив_6_мес'].describe())

statistic, p_value = shapiro(market_file['Маркет_актив_6_мес'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")


# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Успех:
# 
#     
# Из плюсов:    
#     
#     
# - Правильно что продолжаешь практику с прошлого проекта и строишь 2 типа графиков для количественных признаков 
# 
#     
#     
# - Для  разных типов данных используешь  соответствующие графики
#     
# 
# - Необходимые надписи присутствует    
# 
#     
#     
# - Дополнительно тестируешь на нормальность с помощью теста Шапиро    
#     
# <div class="alert alert-warning">
# 
# 
# Совет 🤔:
# 
#    
# - можно пойти дальше  и для графиков распределений сделать разбивку по таргету. Так мы можем получить дополнительную информацию для лучшего понимания наших данные, может что-то пригодится для раздела сегментации. Если использовать seaborn, это можно сделать с помощью аргумента [hue](https://www.statology.org/seaborn-histogram-hue/). В результате мы получим наложенные (в разбивки по таргету) 2 гистограммы (boxplot тоже неплохо добавить) для каждого количественного признака. И о категориальных незабываем. Будет красиво и информативно.
# 
#     
#     
# - подумай о лучшем размещении графиков, сейчас это длинный ряд графиков, который надо прокручивать вниз, почему бы не использовать [subplots](https://nagornyy.me/it/vizualizatsiia-dannykh-v-matplotlib/) и не разместить графики еще и по вертикали в два или три столбца!? 
# 
# 
#     
# - а ещё бы  посоветовал использовать библиотеку    [seaborn](https://nagornyy.me/it/vizualizatsiia-dannykh-v-seaborn/), она строит  симпатичнее и проще matplotlib. Использовать matplotlib это как выучиться на механике, но если умеешь на механике но на автомате (seaborn) точно получится. Есть небольшие отличия в названиях графиках, и фнкциональных возможностях, но это мелочи
#     
#    
#     
# - Посоветовал бы написать функцию, чтобы можно было использовать следующих проектах. Ведь мы каждый раз строим графики    

# In[31]:


market_file.hist('Маркет_актив_тек_мес', bins=3, figsize=(10,7))
plt.xlabel('Количество маркетинговых коммуникаций в текущем месяце')
plt.show()

display('Диаграмма размаха')
market_file.boxplot(column=['Маркет_актив_тек_мес'], figsize=(10,7), grid=True)
plt.xlabel('Количество маркетинговых коммуникаций в текущем месяце')
plt.show()

print(market_file['Маркет_актив_тек_мес'].describe())

statistic, p_value = shapiro(market_file['Маркет_актив_тек_мес'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")


# In[32]:


market_file.hist('Длительность', bins=100, figsize=(10,7))
plt.xlabel('Значение, которое показывает, сколько дней прошло с момента регистрации покупателя на сайте')
plt.show()

display('Диаграмма размаха')
market_file.boxplot(column=['Длительность'], figsize=(10,7), grid=True)
plt.xlabel('Значение, которое показывает, сколько дней прошло с момента регистрации покупателя на сайте')
plt.show()

print(market_file['Длительность'].describe())

statistic, p_value = shapiro(market_file['Длительность'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")


# In[33]:


market_file.hist('Акционные_покупки', bins=15, figsize=(10,7))
plt.xlabel('Среднемесячная доля покупок по акции от общего числа покупок за последние 6 месяцев')
plt.show()

display('Диаграмма размаха')
market_file.boxplot(column=['Акционные_покупки'], figsize=(10,7), grid=True)
plt.xlabel('Среднемесячная доля покупок по акции от общего числа покупок за последние 6 месяцев')
plt.show()

print(market_file['Акционные_покупки'].describe())

statistic, p_value = shapiro(market_file['Акционные_покупки'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")


# In[34]:


market_file['Популярная_категория'].value_counts().plot(title='Данные о самой популярной категории за последние 3 месяца', kind='pie', autopct = '%1.0f%%', figsize=(7,7))
display(market_file['Популярная_категория'].value_counts())


# In[35]:


market_file.hist('Средний_просмотр_категорий_за_визит', bins=6, figsize=(10,7))
plt.xlabel('Сколько в среднем категорий покупатель просмотрел за визит в течение последнего месяца')
plt.show()

display('Диаграмма размаха')
market_file.boxplot(column=['Средний_просмотр_категорий_за_визит'], figsize=(10,7), grid=True)
plt.xlabel('Сколько в среднем категорий покупатель просмотрел за визит в течение последнего месяца')
plt.show()

print(market_file['Средний_просмотр_категорий_за_визит'].describe())

statistic, p_value = shapiro(market_file['Средний_просмотр_категорий_за_визит'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")


# In[36]:


market_file.hist('Неоплаченные_продукты_штук_квартал', bins=10, figsize=(10,7))
plt.xlabel('Общее число неоплаченных товаров в корзине за последние 3 месяца')
plt.show()

display('Диаграмма размаха')
market_file.boxplot(column=['Неоплаченные_продукты_штук_квартал'], figsize=(10,7), grid=True)
plt.xlabel('Общее число неоплаченных товаров в корзине за последние 3 месяца')
plt.show()

print(market_file['Неоплаченные_продукты_штук_квартал'].describe())

statistic, p_value = shapiro(market_file['Неоплаченные_продукты_штук_квартал'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")


# In[37]:


market_file.hist('Ошибка_сервиса', bins=10, figsize=(10,7))
plt.xlabel('Число сбоев, которые коснулись покупателя во время посещения сайта')
plt.show()

display('Диаграмма размаха')
market_file.boxplot(column=['Ошибка_сервиса'], figsize=(10,7), grid=True)
plt.xlabel('Число сбоев, которые коснулись покупателя во время посещения сайта')
plt.show()

print(market_file['Ошибка_сервиса'].describe())

statistic, p_value = shapiro(market_file['Ошибка_сервиса'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")


# In[38]:


market_file.hist('Страниц_за_визит', bins=10, figsize=(10,7))
plt.xlabel('Среднее количество страниц, которые просмотрел покупатель за один визит на сайт за последние 3 месяца')
plt.show()

display('Диаграмма размаха')
market_file.boxplot(column=['Страниц_за_визит'], figsize=(10,7), grid=True)
plt.xlabel('Среднее количество страниц, которые просмотрел покупатель за один визит на сайт за последние 3 месяца')
plt.show()

print(market_file['Страниц_за_визит'].describe())

statistic, p_value = shapiro(market_file['Страниц_за_визит'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")


# In[39]:


market_money.head(10)


# In[40]:


market_money['Период'].value_counts().plot(title='Название периода, во время которого зафиксирована выручка', kind='pie', autopct = '%1.0f%%', figsize=(7,7))
display(market_money['Период'].value_counts())


# In[41]:


market_money_new = market_money.pivot(index='id', columns='Период', values='Выручка')
market_money_new.columns = ['Текущий_месяц_выручка', 'Предыдущий_месяц_выручка', 'Второй_месяц_выручка']
market_money_new.head()


# In[42]:


market_money_new.hist('Текущий_месяц_выручка', bins=20, figsize=(10,7))
plt.xlabel('Сумма выручки за период')
plt.show()

display('Диаграмма размаха')
market_money_new.boxplot(column=['Текущий_месяц_выручка'], figsize=(10,7), grid=True)
plt.xlabel('Сумма выручки за период')
plt.show()

print(market_money_new['Текущий_месяц_выручка'].describe())

statistic, p_value = shapiro(market_money_new['Текущий_месяц_выручка'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")
    
market_money_new.hist('Предыдущий_месяц_выручка', bins=20, figsize=(10,7))
plt.xlabel('Сумма выручки за период')
plt.show()

display('Диаграмма размаха')
market_money_new.boxplot(column=['Предыдущий_месяц_выручка'], figsize=(10,7), grid=True)
plt.xlabel('Сумма выручки за период')
plt.show()

print(market_money_new['Предыдущий_месяц_выручка'].describe())

statistic, p_value = shapiro(market_money_new['Предыдущий_месяц_выручка'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")
    
market_money_new.hist('Второй_месяц_выручка', bins=5, figsize=(10,7))
plt.xlabel('Сумма выручки за период')
plt.show()

display('Диаграмма размаха')
market_money_new.boxplot(column=['Второй_месяц_выручка'], figsize=(10,7), grid=True)
plt.xlabel('Сумма выручки за период')
plt.show()

print(market_money_new['Второй_месяц_выручка'].describe())

statistic, p_value = shapiro(market_money_new['Второй_месяц_выручка'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")


# Были обнаружены аномально большие значения, избавимся от них

# In[43]:


market_money_new = market_money_new[market_money_new['Второй_месяц_выручка'] < 20000]


# In[44]:


market_money_new.hist('Второй_месяц_выручка', bins=5, figsize=(10,7))
plt.xlabel('Сумма выручки за период')
plt.show()

display('Диаграмма размаха')
market_money_new.boxplot(column=['Второй_месяц_выручка'], figsize=(10,7), grid=True)
plt.xlabel('Сумма выручки за период')
plt.show()

print(market_money_new['Второй_месяц_выручка'].describe())

statistic, p_value = shapiro(market_money_new['Второй_месяц_выручка'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")


# Без аномалий стало гораздо лучше

# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# 
# 
# Ошибка ❌:
# 
# 
# 
# 
# 
# А что мы ещё здесь видим кроме ненормального распределения?

# In[45]:


market_time['Период'].value_counts().plot(title='Название периода, во время которого зафиксировано общее время', kind='pie', autopct = '%1.0f%%', figsize=(7,7))
display(market_time['Период'].value_counts())


# In[46]:


market_time_new = market_time.pivot(index='id', columns='Период', values='минут')
market_time_new.columns = ['Текущий_месяц_минуты', 'Предыдущий_месяц_минуты']
market_time_new.head()


# In[47]:


market_time_new.hist('Текущий_месяц_минуты', bins=15, figsize=(10,7))
plt.xlabel('Значение времени, проведённого на сайте, в минутах')
plt.show()

display('Диаграмма размаха')
market_time_new.boxplot(column=['Текущий_месяц_минуты'], figsize=(10,7), grid=True)
plt.xlabel('Значение времени, проведённого на сайте, в минутах')
plt.show()

print(market_time_new['Текущий_месяц_минуты'].describe())

statistic, p_value = shapiro(market_time_new['Текущий_месяц_минуты'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")
    
market_time_new.hist('Предыдущий_месяц_минуты', bins=20, figsize=(10,7))
plt.xlabel('Значение времени, проведённого на сайте, в минутах')
plt.show()

display('Диаграмма размаха')
market_time_new.boxplot(column=['Предыдущий_месяц_минуты'], figsize=(10,7), grid=True)
plt.xlabel('Значение времени, проведённого на сайте, в минутах')
plt.show()

print(market_time_new['Предыдущий_месяц_минуты'].describe())

statistic, p_value = shapiro(market_time_new['Предыдущий_месяц_минуты'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")


# In[48]:


money.hist('Прибыль', bins=20, figsize=(10,7))
plt.xlabel('Значение прибыли')
plt.show()

display('Диаграмма размаха')
money.boxplot(column=['Прибыль'], figsize=(10,7), grid=True)
plt.xlabel('Значение прибыли')
plt.show()

print(money['Прибыль'].describe())

statistic, p_value = shapiro(money['Прибыль'])
if p_value < 0.05: 
    print("Распределение: не нормальное")
else: 
    print("Распределение: нормальное")


# 
# <div class="alert alert-warning">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# 
# 
# Совет:
# 
#     
# - для гистограмм по выручке и минутам, стоит предварительно сделать группировку по "период" (у нас будет 3 графика по выручке и 2 по минутам), это разумно, ведь именно в таком виде мы используем их      

# <a id='sec4'></a>
# ## Объединение таблиц

# In[49]:


market_all = market_file.merge(market_money_new, on=['id'])
market_all = market_all.merge(market_time_new, on=['id'])
market_all.reset_index()
market_all.head(10)


# In[50]:


market_all = market_all[market_all['Текущий_месяц_выручка'] > 0]
market_all = market_all[market_all['Предыдущий_месяц_выручка'] > 0]
market_all = market_all[market_all['Второй_месяц_выручка'] > 0]
market_all.head()


# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# 
# 
# Успех 👍:
# 
# 
# 
# - данные для моделирования подготовлены
# 
# 
# 
# - не активные клиенты убраны
# 
# 
# 
#  

# <a id='sec5'></a>
# ## Корреляционный анализ

# In[51]:


market_all.head(10)


# In[52]:


market_all_new = market_all.drop('id', axis=1)
interval_cols = ['Маркет_актив_6_мес', 'Маркет_актив_тек_мес', 'Длительность', 'Акционные_покупки', 'Средний_просмотр_категорий_за_визит', 'Неоплаченные_продукты_штук_квартал', 'Ошибка_сервиса', 'Страниц_за_визит', 'Текущий_месяц_выручка', 'Предыдущий_месяц_выручка', 'Второй_месяц_выручка', 'Текущий_месяц_минуты', 'Предыдущий_месяц_минуты']
phik_overview = market_all_new.phik_matrix(interval_cols=interval_cols)
plot_correlation_matrix(
    phik_overview.values,
    x_labels=phik_overview.columns,
    y_labels=phik_overview.index,
    title=r"correlation $\phi_K$",
    fontsize_factor=1.5,
    figsize=(25, 25)
)


# 
# 
# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# 
# 
# Успех 👍:
# 
# 
# 
# 
# 
# 
# - здорово что использован phik, и правильно стол указываешь количественные признаки через interval_cols
# 
# 
# 
# 
# 
# 
# 
# <div class="alert alert-warning">
# 
# 
# Совет: 
# 
#     
#     
#     
# 
# - можно поменять политру для удобства восприятия, через добавление cmap='coolwarm' ('bwr', 'seismic'), тогда чем ближе корреляция к 1 тем красней, чем ближе к -1 тем "синей" , ну и чем меньше связи, чем ближе к 0, тем нейтальней цвет
# 
# 
# - можно построить дополнительно  матрицы корреляций для двух датасетов разбитых по таргету. Затем проанализировать есть ли отличия в корреляции, это может быть полезно для лучшего понимания нашей данных
#  
#     
#     
# - к этому времени я бы уже убрал id, ведь это  номер строки и вряд ли он может быть связан с таргетом (если конечно там нет какой то временной составляющей). Но раз посчитал можешь педложить версию такой высокой корреляции?
# 
# 
# 
# В прошлом проекте мы активно использовали scatter_plot для уточнения характера связи между признаками и удоем, и на основе увиденного сделали некоторые преобразования, помогающие преодолеть ограничения линейной модели. В этом проекте мы используем нелинейные модели для которых это не проблема, и таргет у нас не количественный а категориальный. Тем не менее и в этом проекте можно построить scatter_plot между количественными признаками, а таргет использовать  в качестве фильтра. Напомню что проще всего это реализовать с помощью [sns.PairGrid](https://seaborn.pydata.org/generated/seaborn.PairGrid.html). Это не пригодится нам для улучшения метрики, но возможно мы увидим что то полезное для сегментации или лучшего понимания наших данных. 
# 
# - Можно c помощью scatter_plot сконцентрироваться на связи между выручка текущая - выручка за прошлый. Там явная линейная зависимость, причем как будто бы множество точек тяготеют к двум прямым. Можно поискать факторы которые описывает эти два разных множества. Можно к выручке за прошлый месяц добавить выручку за позапрошлый месяц (или отнять) и тогда в каких то группировках по категориальным признакам будет очень четкая линейная зависимость достигающая по r2 за 0.9. Из этого можно сделать вывод что  в определенных группировках, зависимость между выручками за разные периоды практически дерерминирована (очень высокий показатель r2), то есть из выручки за прошлый (и с учетом позапрошлого месяца) мы можем точно спрогнозировать расходы клиента за текущий месяц. О чем это может говорить? 
# 
# 
# 
# - Можно посмотреть scatter_plot между id и акционными покупками. Можно кое что интересное увидеть и дать этому обьяснение
# 

# Признак "Покупательская активность": 
# - Имеет высокую корреляцию с признаком: "Страниц за визит"
# - Имеет заметную корреляцию с признаками: "Маркет актив 6 мес", "Акционные покупки", "Средний просмотр категорий за визит", "Неоплаченные продукты штук квартал", "Предыдущий месяц выручка", "Текущий месяц минуты", "Предыдущий месяц минуты"
# - Остальные признаки либо имеют слабую корреляцию, либо вообще не имеют.
# Мультиколлинеарность у признаков присутвует

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюераV2</b></font>
# 
# 
# 
# Успех 👍:
# 
# 
# 
# Дополнил
# 

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюераV2</b></font>
# 
# 
# 
# Успех 👍:
# 
# 
# Принято
# 
# 
# </div>
# 

# 
# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# Ошибка:
# 
# Матрица корреляции построена, но нет полных выводов по ней, что кроме корреляции между признаками мы на ней видим? Даже если нет сильной связи между признак-таргет, об этом тоже стоит написать
# 
# 
#     
# <div class="alert alert-warning">
# 
# 
# Совет: 
# 
# 
# - шпаргалка
# 
# ![avatar](https://www.ok-t.ru/studopediaru/baza17/1942458671852.files/image012.gif)
# </div>
# 
# 
# 
# 
# </div>
# 
# 

# <a id='sec6'></a>
# ## Использование пайплайнов

# In[53]:


market_all_new = market_all_new.replace(['Снизилась', 'Прежний уровень'], [1, 0])
market_all_new.head(10)


# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# 
# 
# Ошибка ❌:
# 
# 
# 
# Судя по остановке задачи нас интересует "снизилось", а значит кодируем это единицей
#     
#     
#     
# <div class="alert alert-warning">
# 
# Совет:
# 
# 
# Тогда у нас бинарная классификация, то метрики presicion, recall, f1 считаются толко по положительному классу. Поэтому это принципиально. Кроме того predict_proba возвращает два столбцы, если мы вручную закодируем нужный класс единичкой, то его вероятность это второй столбец. В предыдущем проекте некоторые обжигались на этом, получая метрики  и матрицу ошибок по "не вкусное" молоко. Вот на такой момент хотел бы обратить внимание         

# In[54]:


RANDOM_STATE = 42
TEST_SIZE = 0.25

X_train, X_test, y_train, y_test = train_test_split(
    market_all_new.drop('Покупательская активность', axis=1),
    market_all_new['Покупательская активность'],
    test_size = TEST_SIZE,
    random_state=RANDOM_STATE,
    stratify = market_all_new['Покупательская активность']
) 
ohe_columns = [
    'Популярная_категория',    
]
ord_columns = [
    'Тип сервиса',
    'Разрешить сообщать'    
]    
num_columns = [
    'Маркет_актив_6_мес',
    'Маркет_актив_тек_мес',
    'Длительность',
    'Акционные_покупки',
    'Средний_просмотр_категорий_за_визит',
    'Неоплаченные_продукты_штук_квартал',
    'Ошибка_сервиса',
    'Страниц_за_визит',
    'Текущий_месяц_выручка',
    'Предыдущий_месяц_выручка',
    'Второй_месяц_выручка',
    'Текущий_месяц_минуты',
    'Предыдущий_месяц_минуты'   
]
ohe_pipe = Pipeline(
    [('simpleImputer_ohe', SimpleImputer(missing_values=np.nan, strategy='most_frequent')),
        ('ohe', OneHotEncoder(drop='first', handle_unknown='error'))
    ]
    )
ord_pipe = Pipeline(
    [('simpleImputer_before_ord', SimpleImputer(missing_values=np.nan, strategy='most_frequent')),
        ('ord', OrdinalEncoder(
                categories=[
                    ['премиум', 'стандарт'],
                    ['да', 'нет']
                    ],
                handle_unknown='use_encoded_value', unknown_value=np.nan
            )
        ),
    ('simpleImputer_after_ord', SimpleImputer(missing_values=np.nan, strategy='most_frequent'))
    ]
)  
data_preprocessor = ColumnTransformer(
    [
        ('ohe', ohe_pipe, ohe_columns),
        ('ord', ord_pipe, ord_columns),
        ('num', MinMaxScaler(), num_columns)
    ],
    remainder='passthrough'
)
pipe_final= Pipeline(
    [
        ('preprocessor', data_preprocessor),
        ('models', DecisionTreeClassifier(random_state=RANDOM_STATE))
    ]
)  

param_grid = [
    {
        'models': [DecisionTreeClassifier(random_state=RANDOM_STATE)],
        'models__max_depth': range(2, 10),
        'models__max_features': range(2, 10),
        'preprocessor__num': [StandardScaler(), MinMaxScaler(), 'passthrough']  
    },
    {
        'models': [KNeighborsClassifier()],
        'models__n_neighbors': range(2, 10),
        'preprocessor__num': [StandardScaler(), MinMaxScaler(), 'passthrough']   
    },
    {
        'models': [LogisticRegression(
            random_state=RANDOM_STATE, 
            solver='liblinear', 
            penalty='l1'
        )],
        'models__C': range(1, 10),
        'preprocessor__num': [StandardScaler(), MinMaxScaler(), 'passthrough']  
    }
]
randomized_search = RandomizedSearchCV(
    pipe_final, 
    param_grid, 
    cv=5,
    scoring='roc_auc',
    n_jobs=-1
)    
randomized_search.fit(X_train, y_train)

print('Лучшая модель и её параметры:\n\n', randomized_search.best_estimator_)
print ('Метрика лучшей модели на тренировочной выборке:', randomized_search.best_score_)

y_test_pred = randomized_search.predict_proba(X_test)[:, 1]
print(f'Метрика ROC-AUC на тестовой выборке: {roc_auc_score(y_test, y_test_pred)}')


# ROC-AUC позволит хорошо оценить качество бинарной классификации.

# <div class="alert alert-warning">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# 
# 
# Совет 🤔:
# 
# 
#  
# - Чем отличается ROC-AUC? Во-первых она не зависит от порога, а во-вторых в отличие от accuracy адекватно оценивает прогноз даже при сильном дисбалансе
#     
#     
#     
# - Обрати внимание randomized_search.best_score_  - это метрика на кросс валидации  

# 
# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# 
# 
# Успех 👍:
# 
# 
# 
# Тут всё логично
# 
#   
# 
# 
# 
# <div class="alert alert-warning">
# 
# 
# 
# Совет 🤔:
# 
# 
# 
# 
# В будущем при предобработке данных можешь учитывать следующие моменты:
# 
# 
# - OrdinalEncoder можно попробовать использовать, когда значения категориального признака имеют внутренний порядок (низкий/средний/высокий, майор/полковник/генерал), иначе модель будет пытаться найти какие то порядковые отношения, который нет
#     
# - если у категориального признака большое количество уникальных значений, применение One-Hot Encoding может привести к большому количеству новых признаков, это усложнит работу моделей
#     
# - у catboost и lighgbm есть собственные инструменты работы с категориальными данными, нужно только указать какие столбца содержат категориальные данные
#     
# - при работе с количественными признаками для линейных и метрических (модели в которых измеряется расстояние) моделей  обязательно делаем Scaler, в отличие от моделей на основе деревьев решений, для них Scaler не нужен
#         
# 
# Можешь подумать над вопросом почему для линейных моделей некорректное использование OrdinalEncoder может вызвать больше проблем чем для случайного леса  или других моделей в основе которых лежат деревья решений  
# 
#     

# 
# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# 
# 
# Ошибка ❌:
# 
# 
# 
# 
# 
# 
# - счтаем roc_auc_score на тестовой - это наше финальное тестирование
#     
#     
#     
# -  хорошо бы обосновать  выбор метрики    
# 
# 
# 
#     print ('Метрика лучшей модели на тренировочной выборке:', randomized_search.best_score_)
#     
# - это неверно .best_score_ это Метрика по кросс валидации, мы не выбираем лучшую модель по результату на тренировочный выборке, потому что она ничего не показывает. Например если взять дерево решение достаточно большой глубины, то метрика на тренировочной будет равна 100%, но это результат запоминание данных, а не обобщения. Раньше был проект "ведения машинное обучение", где чётко об этом рассказывалось - обучаемся на train, гиперпараметры подбираем по валидационной выборке (в случаи GS кроссвалидационной), а затем проводим финальное тестирование. В прежнем проекте студенты вручную разбивали на три выборки и в цикле подбирали гиперпараметры, а сейчас сразу GS, но он делает то же самое: ты подаёшь него X_train, и он внутри себя разбивает его на тренировочную и валидационную (причем несколько раз)... В общем такой моментик Можешь посмотреть [тут](https://towardsdatascience.com/why-do-we-need-a-validation-set-in-addition-to-training-and-test-sets-5cf4a65550e0) с помощью VPN о логике использования выборок
# 
# 
# 
# 

# <div class="alert alert-danger">
# <font size="5"><b>Комментарий ревьюераV3</b></font>
# 
# 
# 
# Ошибка ❌:
# 
# 
# ROC-AUC считаем через вероятность
# 
# 
#     
#     randomized_search.predict(X_test)  -----> randomized_search.predict_proba(X_test)[:, 1]
#     
#  

# <a id='sec7'></a>
# ## Анализ важности признаков

# In[60]:


X_train_p = pd.DataFrame(
    data_preprocessor.fit_transform(X_train),
    columns = data_preprocessor.get_feature_names_out()
)
X_test_p = pd.DataFrame(
    data_preprocessor.fit_transform(X_train),
    columns = data_preprocessor.get_feature_names_out()
)
X_train_p


# <div class="alert alert-warning">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# 
# 
# Совет 🤔:
# 
# 
# Попробуй    
#     
#     !pip install -U scikit-learn
# 
#     
# с перезапуском ядра    

# In[61]:


explainer = shap.LinearExplainer(randomized_search.best_estimator_[1], X_test_p)
shap_values = explainer(X_test_p)
shap.plots.bar(shap_values)


# In[62]:


shap.plots.beeswarm(shap_values, max_display=16) 


# In[63]:


shap.plots.waterfall(shap_values[181]) 


# Вывод о признаках:
# Признаки, которые сильнее всего влияют на целевой признак: 
# - Популярная категория 
# - Средний просмотр категорий за визит
# - Страниц за визит 
# - Акционные покупки
# - Текущий месяц минуты
# - Неоплаченные продукты штук квартал
# Признаки, которые слабо влияют на целевой признак:
# - Выручка за все месяца
# - Ошибка сервиса
# - Тип сервиса
# - Разрешить сообщать
# - Длительность
# 
# Отталкиваясь от сакмых значимых призаков, можно понять, что вляет на вероятность снижения покупательской активности клиентов, для повышения покупательской активности можно обратить внимание, что сильно влияют акционные покупки, неоплаченные покупки и популярная категория, мы берем популярную категорию клиента, и предлагаем лично для него акцию для его популярной категории, а также можем добавить напоминание о неоплаченных товарах в корзине, эти факторы должны благоприятно сказаться на покупательской активности.

#   
#     
# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# 
# 
# Успех 👍:
# 
# 
# 
# - Построен график важности факторов, график аккуратный
#     
#     
# - Присутствуют выводы о том, какие факторы сильнее/слабее влияют
#     
# 	
# - Плюс за использование .beeswarm    
#     
#     
#     
#     
# <div class="alert alert-warning">
# 
# 
# 
# Совет 🤔:
#    
# 
# 	
# - можно и по-другому оценить важность признаков, это можно сделать с помощью [.feature_importance](https://inria.github.io/scikit-learn-mooc/python_scripts/dev_features_importance.html) (но не забываем что в логистической регрессии надо учесть логарифм в функция ошибки). Или с помощью [Permutation Importance](https://scikit-learn.org/stable/modules/permutation_importance.html)	
# 	

# <a id='sec8'></a>
# ## Сегментация покупателей

# 
# <div class="alert alert-warning">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# 
# 
# Совет:
# 
# 
# 
# 
# В этом разделе студент сам выбирает как проводить сегментацию, но определённые рамки всё-таки существуют:
#     
#     
# 
# 
# 1. 
#     
# Выбираем сегмент и объясняем почему мы его выбрали. Тут делаем упор на бизнес - составляющую (мы ведь всем этим занимаемся не в сферическом вакууме, а для повышения экономической эффективности) и логику. Пример:
# 
# 
#     "нас интересуют богатенькие клиенты, поэтому...", "нас интересуют те для кого модель предсказала высокую вероятность ухода, потому что...", "нас интересуют богатенькие и уходящие, потому что..."
# 
# 
# 
# - Или ориентируемся на результаты оценки важности признаков. Пример:
# 
# 
#     "акционные покупки не показали высокую значимость на графиках shap, но если приглядеться, то yf графике beeswarm мы видим очень четкое разделение: высокие акционные покупики - высокая вероятность снижения, значит мы можем..." 
# 
# 
# 
#     
#     
# 2.    
#     
# У нас есть файл money, в нем содержится важная информация о прибыльности клиентов. Это наверно самый важный параметр с точки зрения бизнеса: клиент может много покупать, но прибыльность от него будет небольшой, или наоборот клиент может мало покупать, но он покупает товары которые продавать магазину выгодно. Чувствуешь разницу?! Стоит обогатить наши данные этой информацией
#     
#     
#     
#     
# 3.
# 
# Используем результаты моделирования, а иначе зачем мы все это делали?!  Можно использовать результат predict_proba посмотрев на уверенность модели в том что клиент снижает активность - вот и вариант сегментации.  Можно использовать модель как источник вдохновения для выбора признаков (если модель считает признак важным для прогноза активности, то логично посмотреть на него поближе). Можно приглядеться на графики shap.beeswarm, увидев там что то интересное. Или можно все это использовать вместе.  Кстати можно подглядеть внутрь моделей не только с помощью shap, но и построить [plot_tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html) и там подсмотреть  комбинацию признаков с конкретными порогами, сделав упор на признаки - причины. Например проанализировав   plot_tree мы можем увидеть что для такой то группы товаров, при таком то значении акционных покупок и при таком то сервисе, высока доля не снижающих активность клиентов (ничего такого на самом деле нет, это просто пример). И мы сможем сделать более сложные маркетинговые предложения.
# 
# Но, если ты хочешь использовать модель чтобы приглядеться к каким то признаками, то стоит различать  "признаки - индикатор", и "признаки - причины", а в разделе сегментация нам нужно дать маркетинговые предложения, то есть упор надо будет сделать на "признаки - причины", то есть на то что мы можем повлиять - акции, сервис, число ошибок при работе на сайте  итп. итд   
# 
#     
# 
# 
# 4. 
#     
# 
#     
# 
# - После выбора сегмента мы можем посмотреть усредненное лицо клиентов попавших в него, но сами по себе цифры нас не интересуют, нас интересует разница с клиентами не попавшими в сегмент. поэтому стоит проанализировать сегмент, указать на его отличия от остальных. для этого отлично подойдут графики countplot/pie (для категориальных) и гистограмму или boxplot (для количественных), а разбивке "наш сегмент" - "не наш сегмент"
#     
#     
# - А ещё можно посмотреть в динамике,  у нас есть и эта составляющая
# 
# 
# 
# 5.
#     
# И в конце составляем индивидуальные маркетинговые предложения для выбранного сегмента - иначе для чего мы всё это делали!?  При этом  выводы не должны быть слишком общими, напрмиер предложение "предложить акцию", это слишком общее предложение, лучше указать для кого, по какой группе товаров итп итд
#     
#     
#     
# 
#     
# 
# 
# Вот перечень вариантов предложенных в проекте в качестве сегментов:
# 
# - Группа клиентом с максимальными акционными покупками и высокой вероятностью снижения покупательской активности.
# - Группа клиентов, которые покупают только технику (покупают товары с длинным жизненным циклом)
# - Группа клиентов, которые покупают товары из категории "Товары для себя" (можно ввести такую новую категорию на основе текущих) или "Товары для детей".
# - Группа клиентов с высокой вероятностью снижения покупательской активности и наиболее высокой прибыльностью
# 
# Самый очевидный и наверное логичный вариант - это рассмотреть сегмент клиентов с высокой вероятностью снижения покупательской активности и наиболее высокой прибыльностью. Тут сходится всё - и бизнесовая составляющая, и результаты моделирования мы используем)
# 
# 
# 
# 
# 
#     

# Добавим столбец прибыль в наш итоговый датасет

# In[66]:


market_final = market_all.merge(money, on=['id'])
market_final['Прибыль'].describe()


# In[67]:


market_final.head()


# В своей задаче я хочу постараться сохранить богатых покупателей, поэтому обратим внимание на пользователей с значением прибыльности больше 4.67 и значением покупательской активности (Снизилась), отберем этих покупателей

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюераV2</b></font>
# 
# 
# 
# Успех 👍:
# 
# 
# 
# Логично
# 

# In[68]:


market_final_new = market_final[market_final['Прибыль'] > 4.67]
market_final_new = market_final_new[market_final_new['Покупательская активность'] == 'Снизилась']
market_final_new = market_final_new.reset_index(drop=True)
market_final_new.head(10)


# <div class="alert alert-warning">
# <font size="5"><b>Комментарий ревьюераV2</b></font>
# 
# 
# 
# Совет 🤔:
# 
# 
# 
# Вообще предполагается использовать прогноз модели 
# 

# Сделаем еще один датасет, куда покупатели с высокой прибыльностью не попадут

# <div class="alert alert-warning">
# <font size="5"><b>Комментарий ревьюераV2</b></font>
# 
# 
# 
# Совет 🤔:
# 
# 
# 
# Кстати можно выбрать таких же прибыльных клиентов, но для которых модель прогнозирует что их активность сохранится. Так мы мы получили возможность сравнивать сравнимое
# 

# In[69]:


market_final_un = market_final[market_final['Прибыль'] < 4.67]
market_final_un.head()


# In[70]:


market_final_new['Тип сервиса'].value_counts().plot(title='Данные о типе сервиса (Богатые покупатели)', kind='pie', autopct = '%1.0f%%', figsize=(7,7))
display(market_final_new['Тип сервиса'].value_counts())
plt.show()
market_final_un['Тип сервиса'].value_counts().plot(title='Данные о типе сервиса', kind='pie', autopct = '%1.0f%%', figsize=(7,7))
display(market_final_un['Тип сервиса'].value_counts())
plt.show()


# По признаку "Тип сервиса", различий не было обнаружено

# In[71]:


market_final_new['Разрешить сообщать'].value_counts().plot(title='Данные о возможности присылать покупателю дополнительные предложения о товаре (Богатые покупатели)', kind='pie', autopct = '%1.0f%%', figsize=(7,7))
display(market_final_new['Разрешить сообщать'].value_counts())
plt.show()
market_final_un['Разрешить сообщать'].value_counts().plot(title='Данные о возможности присылать покупателю дополнительные предложения о товаре', kind='pie', autopct = '%1.0f%%', figsize=(7,7))
display(market_final_un['Разрешить сообщать'].value_counts())
plt.show()


# По признаку "Разрешить сообщать", различий не было обнаружено

# In[72]:


market_final_new.hist('Маркет_актив_6_мес', bins=10, figsize=(10,7))
plt.xlabel('Среднемесячное значение маркетинговых коммуникаций компании (Богатые покупатели)')
plt.show()

print(market_final_new['Маркет_актив_6_мес'].describe())

market_final_un.hist('Маркет_актив_6_мес', bins=10, figsize=(10,7))
plt.xlabel('Среднемесячное значение маркетинговых коммуникаций компании')
plt.show()

print(market_final_un['Маркет_актив_6_мес'].describe())


# В признаке "Маркет актив 6 мес" разница в средних значениях достаточно ощутима, можно использовать данный признак для дальнейших рекомендаций

# In[73]:


market_final_new.hist('Маркет_актив_тек_мес', bins=3, figsize=(10,7))
plt.xlabel('Количество маркетинговых коммуникаций в текущем месяце (Богатые покупатели)')
plt.show()

print(market_final_new['Маркет_актив_тек_мес'].describe())

market_final_un.hist('Маркет_актив_тек_мес', bins=3, figsize=(10,7))
plt.xlabel('Количество маркетинговых коммуникаций в текущем месяце')
plt.show()

print(market_final_un['Маркет_актив_тек_мес'].describe())


# Тут отличия минимальны признак не берем

# In[74]:


market_final_new.hist('Длительность', bins=20, figsize=(10,7))
plt.xlabel('Значение, которое показывает, сколько дней прошло с момента регистрации покупателя на сайте (Богатые покупатели)')
plt.show()

print(market_final_new['Длительность'].describe())

market_final_un.hist('Длительность', bins=100, figsize=(10,7))
plt.xlabel('Значение, которое показывает, сколько дней прошло с момента регистрации покупателя на сайте')
plt.show()

print(market_final_un['Длительность'].describe())


# В признаке "Длительность" отличия минимальные 

# In[75]:


market_final_new.hist('Акционные_покупки', bins=15, figsize=(10,7))
plt.xlabel('Среднемесячная доля покупок по акции от общего числа покупок за последние 6 месяцев (Богатые покупатели)')
plt.show()

print(market_final_new['Акционные_покупки'].describe())

market_final_un.hist('Акционные_покупки', bins=15, figsize=(10,7))
plt.xlabel('Среднемесячная доля покупок по акции от общего числа покупок за последние 6 месяцев')
plt.show()

print(market_final_un['Акционные_покупки'].describe())


# Средняя доля "Акционных покупок" у покупателей с высокой прибыльностю ниже, чем у остальной выборки, этот признак стоит взять во внимание

# In[76]:


market_final_new['Популярная_категория'].value_counts().plot(title='Данные о самой популярной категории за последние 3 месяца (Богатые покупатели)', kind='pie', autopct = '%1.0f%%', figsize=(7,7))
display(market_final_new['Популярная_категория'].value_counts())
plt.show()
market_final_un['Популярная_категория'].value_counts().plot(title='Данные о самой популярной категории за последние 3 месяца', kind='pie', autopct = '%1.0f%%', figsize=(7,7))
display(market_final_un['Популярная_категория'].value_counts())
plt.show()


# В разделе "Популярная категоря", стоит обратить внимание, что у сегмента богатых покупателей вторая по популярности категория отличается от другой выборки, нужно будет учитывать

# In[77]:


market_final_new.hist('Средний_просмотр_категорий_за_визит', bins=6, figsize=(10,7))
plt.xlabel('Сколько в среднем категорий покупатель просмотрел за визит в течение последнего месяца (Богатые покупатели)')
plt.show()

print(market_final_new['Средний_просмотр_категорий_за_визит'].describe())

market_final_un.hist('Средний_просмотр_категорий_за_визит', bins=6, figsize=(10,7))
plt.xlabel('Сколько в среднем категорий покупатель просмотрел за визит в течение последнего месяца')
plt.show()

print(market_final_un['Средний_просмотр_категорий_за_визит'].describe())


# В признаке "Средний просмотр категорий за визит", можно заметить, что у нашего сегмента среднее значение ниже, чем у остальной выборки, это значит, что для нашей выборки интересуется меньшим количеством категорий, и выбирает товары более узконаправленно

# In[78]:


market_final_new.hist('Неоплаченные_продукты_штук_квартал', bins=10, figsize=(10,7))
plt.xlabel('Общее число неоплаченных товаров в корзине за последние 3 месяца (Богатые покупатели)')
plt.show()

print(market_final_new['Неоплаченные_продукты_штук_квартал'].describe())

market_final_un.hist('Неоплаченные_продукты_штук_квартал', bins=10, figsize=(10,7))
plt.xlabel('Общее число неоплаченных товаров в корзине за последние 3 месяца')
plt.show()

print(market_final_un['Неоплаченные_продукты_штук_квартал'].describe())


# По признаку "Неоплаченные продукты штук квартал" видно, что у нашего сегмента это количество больше, тоже будем учитывать 

# In[79]:


market_final_new.hist('Ошибка_сервиса', bins=8, figsize=(10,7))
plt.xlabel('Число сбоев, которые коснулись покупателя во время посещения сайта (Богатые покупатели)')
plt.show()

print(market_final_new['Ошибка_сервиса'].describe())

market_final_un.hist('Ошибка_сервиса', bins=10, figsize=(10,7))
plt.xlabel('Число сбоев, которые коснулись покупателя во время посещения сайта')
plt.show()

print(market_final_un['Ошибка_сервиса'].describe())


# По ошибкам сервиса отличия минимальны

# In[80]:


market_final_new.hist('Страниц_за_визит', bins=10, figsize=(10,7))
plt.xlabel('Среднее количество страниц, которые просмотрел покупатель за один визит на сайт за последние 3 месяца (Богатые покупатели)')
plt.show()

print(market_final_new['Страниц_за_визит'].describe())

market_final_un.hist('Страниц_за_визит', bins=10, figsize=(10,7))
plt.xlabel('Среднее количество страниц, которые просмотрел покупатель за один визит на сайт за последние 3 месяца')
plt.show()

print(market_final_un['Страниц_за_визит'].describe())


# В признаке "Страниц за визит" можно заметить, что у нашего сегмента, срднее значение гораздо меньше, чем у остальной выборки, это в будущем учтем

# In[81]:


market_final_new.hist('Текущий_месяц_выручка', bins=20, figsize=(10,7))
plt.xlabel('Сумма выручки за период (Богатые покупатели)')
plt.show()
print(market_final_new['Текущий_месяц_выручка'].describe())
market_final_un.hist('Текущий_месяц_выручка', bins=20, figsize=(10,7))
plt.xlabel('Сумма выручки за период')
plt.show()
print(market_final_un['Текущий_месяц_выручка'].describe())


# In[ ]:


market_final_new.hist('Предыдущий_месяц_выручка', bins=20, figsize=(10,7))
plt.xlabel('Сумма выручки за период (Богатые покупатели)')
plt.show()
print(market_final_new['Предыдущий_месяц_выручка'].describe())
market_final_un.hist('Предыдущий_месяц_выручка', bins=20, figsize=(10,7))
plt.xlabel('Сумма выручки за период')
plt.show()
print(market_final_un['Предыдущий_месяц_выручка'].describe())


# In[ ]:


market_final_new.hist('Второй_месяц_выручка', bins=5, figsize=(10,7))
plt.xlabel('Сумма выручки за период (Богатые покупатели)')
plt.show()
print(market_final_new['Второй_месяц_выручка'].describe())
market_final_un.hist('Второй_месяц_выручка', bins=5, figsize=(10,7))
plt.xlabel('Сумма выручки за период')
plt.show()
print(market_final_un['Второй_месяц_выручка'].describe())


# In[ ]:


По данным о выручке за последние 3 месяца видно, что среднее значение привермно одинаковое


# In[ ]:


market_final_new.head()


# In[ ]:


market_final_new.hist('Текущий_месяц_минуты', bins=10, figsize=(10,7))
plt.xlabel('Значение времени, проведённого на сайте, в минутах (Богатые покупатели)')
plt.show()
print(market_final_new['Текущий_месяц_минуты'].describe())
market_final_un.hist('Текущий_месяц_минуты', bins=15, figsize=(10,7))
plt.xlabel('Значение времени, проведённого на сайте, в минутах')
plt.show()
print(market_final_un['Текущий_месяц_минуты'].describe())


# In[ ]:


market_final_new.hist('Предыдущий_месяц_минуты', bins=10, figsize=(10,7))
plt.xlabel('Значение времени, проведённого на сайте, в минутах (Богатые покупатели)')
plt.show()
print(market_final_new['Предыдущий_месяц_минуты'].describe())
market_final_un.hist('Предыдущий_месяц_минуты', bins=20, figsize=(10,7))
plt.xlabel('Значение времени, проведённого на сайте, в минутах')
plt.show()
print(market_final_un['Предыдущий_месяц_минуты'].describe())


# По данным с общим проведенным временем в месяце видно, что наш сегмент в среднем меньше времени проводит на сайте

# Отталкиваяь от сравнений данных о двух сегментах, могу предложить добавить для нашего выбранного сегмента добавить индивидуальные акционные предложения на популярную категорию клиента, а также добавить напоминание о неоплаченных товарах в корзине, еще можно увеличить количество уведомлений для клиента, чтобы он чаще заходил на сайт и проводил больше времени, это должно повысить покупательскую активность в нашей выбранной категории.

# <div class="alert alert-success">
# <font size="5"><b>Комментарий ревьюераV2</b></font>
# 
# 
# 
# Успех 👍:
# 
# 
# 
# Сравнение проведено, маркетинговые предложения сделаны
# 

# <a id='sec9'></a>
# ## Общий вывод

# - Интернет-магазин «В один клик» продаёт разные товары: для детей, для дома, мелкую бытовую технику, косметику и даже продукты. Отчёт магазина за прошлый период показал, что активность покупателей начала снижаться. Привлекать новых клиентов уже не так эффективно: о магазине и так знает большая часть целевой аудитории. Возможный выход — удерживать активность постоянных клиентов. Сделать это можно с помощью персонализированных предложений.\
# - «В один клик» — современная компания, поэтому её руководство не хочет принимать решения просто так — только на основе анализа данных и бизнес-моделирования. У компании есть небольшой отдел цифровых технологий, и вам предстоит побыть в роли стажёра в этом отделе.\
# - Итак, вашему отделу поручили разработать решение, которое позволит персонализировать предложения постоянным клиентам, чтобы увеличить их покупательскую активность.\
# - Исходные данные:\
# market_file.csv\
# Таблица, которая содержит данные о поведении покупателя на сайте, о коммуникациях с покупателем и его продуктовом поведении.\
# market_money.csv\
# Таблица с данными о выручке, которую получает магазин с покупателя, то есть сколько покупатель всего потратил за период взаимодействия с сайтом.\
# market_time.csv\
# Таблица с данными о времени (в минутах), которое покупатель провёл на сайте в течение периода.\
# money.csv\
# Таблица с данными о среднемесячной прибыли покупателя за последние 3 месяца: какую прибыль получает магазин от продаж каждому покупателю.\
# Была произведена предобработка данных, получена информация о датасетах, поиск пропусков, явных и неявных дубликатов, исправлены грамматические ошибки, добавлены новые столбцы.\
# Для поиска лучше модели был написан пайплайн с использованием четырех моделей, двумя скейлерами и двумя энкодерами, с помощью рандомного перебора моделей и их параметров была найдена лучшая (LogisticRegression(C=3, penalty='l1', random_state=42, solver='liblinear')\
# После всей проведенной работы была предожена бизнес идея:\
# Предложить добавить для нашего выбранного сегмента добавить индивидуальные акционные предложения на популярную категорию клиента, а также добавить напоминание о неоплаченных товарах в корзине, еще можно увеличить количество уведомлений для клиента, чтобы он чаще заходил на сайт и проводил больше времени, это должно повысить покупательскую активность в нашей выбранной категории.

# 
# <div class="alert alert-info">
# <font size="5"><b>Комментарий ревьюера</b></font>
# 
# (Интересно что пропал мой последний комментарий, возможно какой-то сбой, по крайней мере восстановлю список ошибок)
# 
#     
#     
# Что стоит исправить
#     
#     
#     
# - не забываем написать введение в проект
#  
#     
#     
# - убираем аномалии    
#  
#     
# - дописываем выводы по матрице корреляции    
#     
#     
#     
#     
# - в этом проекте нас интересует "снижение",  это и есть наш положительный класс, поэтому рекомендую закодировать ее 1, чтобы не было путаницы
# 
# 
#     
# 
# 
# - объясняем почему выбрали ту или иную метрику
#     
#     
# - в тренажере была неточность, .best_score_ это метрика по кросс валидации
# 
# 
#     
# - сразу после выбора лучшей модели, проводим её финальное тестирование
# 
# 
#     
#     
# - дорабатываем проект, пишем общий вывод    

# 
# <div class="alert alert-info">
# <font size="5"><b>Комментарий ревьюераV2</b></font>
# 
# Спасибо за работу Сергей!    
# 
#     
# Красное исправлено, хотя Обрати внимание на best_score_, всё-таки стоит корректно называть что считают этод метод
# 
# 
# Отправляю на 3 итерацию чтобы убедиться что вопросов больше нет. На связи    
# 

# 
# <div class="alert alert-info">
# <font size="5"><b>Комментарий ревьюераV3</b></font>
# 
# 
# 
# Ещё раз посмотрел твою работу, пропустил ошибку - на тестовой выборке ты посчитал метрику roc-auc, но неверно. Подсказал Как правильно
#     

# 
# <div class="alert alert-info">
# <font size="5"><b>Комментарий ревьюераV4</b></font>
# 
# Спасибо за работу!    
# 
#  
# Красного нет, вопросов нет, значит все, пора принимать) Надеюсь мои советы и вопросики были полезны и в копилочку знаний упало что то новое, а проект стал лучше, и симпатичней. 
# 
#   
# Отличная работа Сергей. Желаю успехов в дальнейшей учебе!
# 
# 

# In[ ]:




