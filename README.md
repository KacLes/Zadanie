# Zadanie
Program pisany i testowany z wykorzystaniem Pythona 3.8
Wymaga zainstalowanych bibliotek requests i cherrypy. Można wykorzystać komendy:

> pip install requests
> pip install cherrypy

Program można uruchomić przechodząc do folderu Zadanie i wywołując następujące polecenie

>python Main.py

Uruchomi to serwer nasłuchujący pod adresem 127.0.0.1:8080
Listę repozytoriów użytkownika GitHub można znaleźć pod

- http://127.0.0.1:8080/?username=<nazwa użytkownika>

Sumę gwiazdek ze wszystkich repozytoriów użytkownika pod

-  http://127.0.0.1:8080/stars?username=<nazwa użytkownika>

A listę używanych języków programowania pod

-  http://127.0.0.1:8080/languages?username=<nazwa użytkownika>


Potencjalnym możliwym rozszerzeniem mogłaby być możliwość listowania osób z którymi podany użytkownik współpracował nad swoimi repozytoriami (login, liczba repozytoriów nad którymi współpracowali)