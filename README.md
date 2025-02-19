# Дополнительные задания по курсу ООП

Этот репозиторий содержит дополнительные задания по курсу ООП на Python. 
Задания помогут закрепить ваши знания объектно-ориентированного программирования и применить их на практике.

___
### Домашние задания:

- [14_1_homework](#14_1_homework) ✅ 
- [14_2_homework](#14_2_homework)    
    - [Задание 1](#задание-1)
    - [Задание 2](#задание-2)
    - [Задание 3](#задание-3)
    - [Задание 4](#задание-4)
    - [Задание 5](#задание-5) 
- [14_3 Homework](#14_3_homework)
- [14_4_homework](#14_4_homework)

___

## 14_1_homework 
В данном домашнем задании созданы классы `Product` и `Category`, которые в дальнейшем будут развиваться. 
Количество категорий и количество товаров подсчитывается автоматически при инициализации нового объекта.
___

Для класса Product определены свойства:

- название (`name`),
- описание (`description`),
- цена (`price`),
- количество в наличии (`quantity`).

[в начало ⮭](#домашние-задания)
___


Для класса Category определены свойства:

- название (`name`),
- описание (`description`),
- список товаров категории (`products`).

[в начало ⮭](#домашние-задания)

___

Написаны тесты для классов, которые проверяют:

- корректность инициализации объектов класса `Category`, 
- корректность инициализации объектов класса `Product`, 
- подсчет количества продуктов, 
- подсчет количества категорий.

Благодаря этим тестам можно убедиться, что всё сделано верно, и протестировать реализованную 
в прошлых пунктах функциональность. 

[в начало ⮭](#домашние-задания)
___
Реализована подгрузка данных по категориям и товарам из файла `products.json`. 

Ссылка на файл: [products.json](https://drive.google.com/file/d/1fTgJX1_-rI2JbuM2He6OPyU_N5PyePsd/view).

[в начало ⮭](#домашние-задания)
___

# 14_2_homework

В этом домашнем задании работа продолжается в рамках того же проекта, который был начат ранее в 14_1_homework. 

> По большей части задание состоит в том, чтобы изменить режимы доступа для уже имеющихся атрибутов.

**Продолжается работа над магазином:**

Теперь нужно защитить данные, которые не должны быть изменены через публичный доступ, 
чтобы не нарушилась целостность данных.

[в начало ⮭](#домашние-задания)
___


## Задание 1

Для класса `Category` сделайте список товаров `приватным атрибутом`, чтобы к нему нельзя было получить доступ извне. 
Для добавления товаров в категорию реализуйте специальный метод `add_product()` в классе `Category`, 
в который нужно передавать объект класса `Product` и уже его записывать в приватный атрибут списка товаров.

>> #приватные_атрибуты #методы_класса #self

> Задание посвящено работе с приватными атрибутами, к которым нельзя обращаться от объекта, но 
> можно обращаться внутри класса. Чтобы не нарушить функционирование нашей программы, мы создаем специальный метод, 
> который позволит добавлять продукты в категории.

[в начало ⮭](#домашние-задания)


## Задание 2

Так как вы сделали атрибут со списком товаров приватным, то атрибут «список товаров категории» у вас освободился, 
но вы лишили программу возможности выводить список товаров. Чтобы вернуть возможность просмотра товаров, 
нужно реализовать геттер, который будет выводить список товаров в виде строк в формате:

```bash
Название продукта, 80 руб. Остаток: 15 шт.
```

>> #@property #методы_класса #публичные_методы

>Используйте декоратор `property` для создания геттера с выводом списка товаров. 
>Геттер должен возвращать строку, чтобы пользователь класса мог их распечатать или записать в какой-то другой интерфейс.


## Задание 3

Для класса `Product` необходимо создать класс-метод `new_product`, который будет принимать 
на вход параметры товара в словаре и возвращать созданный объект класса `Product`.

>> #класс-методы  #__init__  #list

> В класс-методе класса `Product` необходимо вызывать метод-конструктор `__init__` от класса продуктов,
> а созданный объект возвращать как результат работы метода. 
> При этом в класс-метод должны передаваться отдельные параметры товара, такие как:
> `название, цена, описание и количество на складе`.

[в начало ⮭](#домашние-задания)


### Дополнительное задание (к заданию 3) *

Для данного метода реализуйте проверку наличия такого же товара схожего по имени. 
В случае если товар уже существует, необходимо сложить количество в наличии старого товара и нового. 
При конфликте цен выбрать ту, которая является более высокой. 
Для этого можно в метод передать список товаров, в котором нужно искать дубликаты.

>> #класс-методы  #if  #for

> Речь идет о работе со списком товаров, которые уже были добавлены. 
> Не бойтесь передавать новые атрибуты в класс-методы, которые создаете. 
> Проверка товара заключается в переборе имеющегося списка товаров и сравнения названий.


[в начало ⮭](#домашние-задания)

## Задание 4

Для класса `Product` сделайте атрибут цены приватным и опишите `геттеры` и `сеттеры`. 

В `сеттере` реализуйте проверку: 
в случае если цена равна или ниже нуля, выводите сообщение в консоль 
`“Цена не должна быть нулевая или отрицательная”`, при этом новую цену устанавливать не нужно.

>> #@property  #setter  #if

> `Задание посвящено работе с геттерами и сеттерами`. 
> Мы `защищаем пользователя` от случайного введения некорректной цены. 
> То есть необходимо выводить сообщение, только если цена ниже или равна нулю, чтобы не продать товар бесплатно.

[в начало ⮭](#домашние-задания)

### Дополнительное задание (к заданию 4) *

В случае если цена товара понижается, добавить логику подтверждения пользователем вручную через ввод `y` (значит `yes`)
или `n` (значит `no`) для согласия понизить цену или для отмены действия соответственно.

> Проще всего в сеттере вывести сообщение через `input` и обработать ответ, где `y` считается за согласие, 
> а любой другой ответ отменяет действие.

>> #input  #if

> Расширяем прошлую задачу и предоставляем пользователю большую защиту от введения некорректной цены. 
> `Обратите внимание, что логика защиты срабатывает, когда цена просто ниже прошлой`.

[в начало ⮭](#домашние-задания)

## Задание 5

**`Напишите тесты` для новой функциональности.**

При этом убедитесь, что тесты, которые были написаны ранее, выполняются `без ошибок`.

>> #pytest  #assert
___

`*` *P.S. Дополнительные задания, помеченные звездочкой, `желательно`, но `не обязательно` выполнять.*

[в начало ⮭](#домашние-задания)
___

## 14_3_homework

[в начало ⮭](#домашние-задания)

___

## 14_4_homework

[в начало ⮭](#домашние-задания)

___
>