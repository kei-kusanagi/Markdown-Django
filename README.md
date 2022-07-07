Bueno empecemos este nuevo proyecto, creando nuestro entorno virtual como es habitual e inicializando nuestro git y activamos nuestro entorno virtual

![[Pasted image 20220707124831.png]]

ahora isntalamos Django ``pip install django`` y despues creamos nuestro proyecto ``django-admin startproject markdownblog`` 

![[Pasted image 20220707125650.png]]

antes de continuar hacemos las migraciones ap que no nos salga el molesto letrerito rojo ese al correr el servidor

![[Pasted image 20220707130954.png]]

ahora si ``python manage.py runserver``
![[Pasted image 20220707131046.png]]
![[Pasted image 20220707131116.png]]

ahora crearemos una app ``python manage.py startapp blog`` y la registramos en settings.py pero la isntalaremos de manera diferente para que vea que es un blog

![[Pasted image 20220707131439.png]]

