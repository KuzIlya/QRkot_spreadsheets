<details>
    <summary>Содержание</summary>
    <ul> 
        <li>
            <a href="#что-за-котики">Что за котики?</a>
            <ul>
                <li><a href="#ну-что-умеем">Что умеем?</a></li>
                <li><a href="#на-каких-технологиях">На каких технологиях?</a></li> 
            </ul>
        </li>
        <li>
            <a href="#как-начать-с-котиками-работать">Как начать с котиками работать?</a>
            <ul>
                <li><a href="#какие-штуки-нам-нужны">Какие штуки нам нужны?</a></li>
                <li><a href="#ставим-систему-на-локалку">Ставим систему на локалку</a></li>
                <li><a href="#локальный-подгон">Локальный подгон</a></li>
            </ul>
        </li>
        <li><a href="#как-мы-это-используем">Как мы это используем?</a></li>
        <li><a href="#кто-тут-автор">Кто тут автор?</a></li>
    </ul>
</details>
<a name="что-за-котики"></a>

Благотворительный фонд по спасению котиков. Мы собираем бабки на всякие классные котячьи проекты: то хвостатому лечилку оплатить, то подвал для колонии котиков сделать уютным, то корм закинуть хвостатым бедняжкам. Короче, поддержка кошачьей банды во всех направлениях.

# Ну что умеем?
У нас можно запилить сколько угодно котопроектов.
Каждый, кто хочет, может подкинуть денежку и оставить комментарий с посланием хвостатым.
Денежки в котопроекты распределяются по справедливой схеме — First In, First Out (то есть кто первый дал, тот и молодец).

# Как начать с котиками работать?
Гоним по инструкции, чтобы всё заработало на локальном компе.

# Какие штуки нам нужны?
Python 3.7+
Ставим систему на локалку
Клоним репозиторий

```bash
git clone https://github.com/tvules/QRKot.git
cd QRKot
```

### Локальный подгон
### Залетай в зависимости

```bash
pip install -r requirements.txt
```

### В корне создай .env файл

```dotenv
SECRET="<твой секретный ключ>"
```

### *Секретный ключ? Держи его тут

### Подними локальный сервер

```bash
uvicorn app.main:app
```

### Идём на http://localhost:8000/ и котики ждут тебя!

# Как мы это используем?

Залетай на Swagger UI по адресу http://localhost:8000/docs и смотри, какие есть API, плюс можешь прямо тут же запросы катать.

<h4 align="center"> Проект замутил: <a href="https://github.com/KuzIlya">Kuznetsov Ilya</a> </h4>