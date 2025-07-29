После секоја промена во models мора
python manage.py makemigrations
python manage.py migrate


Прво пред се
python -m pip install Pillow

За кревање на серверот 
cd djangoProject
python manage.py runserver

Веќе е креиран superuser со Username и pw 123 123,
ама ако не ти дава со тоа да се најавиш оди вака
python manage.py createsuperuser
и внеси 123 123 и скипни емаил не ти треба

За да додаваш промени во базата, тоа го правиш на 
http://127.0.0.1:8000/admin

Ти треба html да ги менуваш главно оти не се фокусирав на детали на paddings and such, не знам во моментов како ти работи утре ќе ми покажеш ќе додадеме што треба за страни, меѓутоа 
кога креираш country имам ставено една color, ако е мн малце можеме да додадеме повеќе ко "title color" "question color" затоа види што како би одговарало да додаваш за секоја држава и да ми кажеш

html ти се на локацијава во проектот
djangoProject/templates/

На
http://127.0.0.1:8000/select/
Имам мн малце ставено колку да те пренасочи кон државата
Ако во админ ставиш држава насловена Бразил и на select внесеш Бразил ќе те однесе на тоа, се води по country name

Pretty much тоа е за насочување, отвори ѕирни



