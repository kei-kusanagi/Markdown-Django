Bueno empecemos este nuevo proyecto, creando nuestro entorno virtual como es habitual e inicializando nuestro git y activamos nuestro entorno virtual

![image](README%20IMG/Pasted%20image%2020220707124831.png)

ahora instalamos Django ``pip install django`` y después creamos nuestro proyecto ``django-admin startproject markdownblog`` 

![image](README%20IMG/Pasted%20image%2020220707125650.png)

antes de continuar hacemos las migraciones app que no nos salga el molesto letrerito rojo ese al correr el servidor

![image](README%20IMG/Pasted%20image%2020220707130954.png)

ahora si ``python manage.py runserver``
![image](README%20IMG/Pasted%20image%2020220707131046.png)
![image](README%20IMG/Pasted%20image%2020220707131116.png)

ahora crearemos una app ``python manage.py startapp blog`` y la registramos en settings.py pero la instalaremos de manera diferente para que vea que es un blog

![image](README%20IMG/Pasted%20image%2020220707131439.png)

ahora crearemos nuestro modelos para la base de datos en blog/models.py

```
from django.db import models

  

class Post(models.Model):

    title = models.CharField(max_length=255)

    intro = models.TextField()

    body = models.TextField()

    cheated_at = models.DateTimeField(auto_now_add=True)
```

y volvemos a hacer la migration
![image](README%20IMG/Pasted%20image%2020220707133702.png)

ya con nuestro modelo crearemos un super usuario para poder ingresar notas a nuestro blog ``python manage.py createsuperuser``

![image](README%20IMG/Pasted%20image%2020220707134217.png)

ahora vamos a la area de administration a registrar esto en /blog/admin.py
```
from django.contrib import admin

  

from .models import Post

  

admin.site.register(Post)
```

si vamos a la area de administration podremos ver "Posts"
![image](README%20IMG/Pasted%20image%2020220707134437.png)

creemos varios de prueba
![image](README%20IMG/Pasted%20image%2020220707134629.png)

ahora nos toca poder mostrar estos Post creados en nuestra pantalla principal de la aplicación, para esto en nuestra app de blog crearemos las carpetas y archivo html /templates/blog/base.html

```
<!DOCTYPE html>

<html>

	<head>
	
		<meta charset="utf-8">
		
		<meta name="viewport" content="width=device-width, initial-scale=1">
		
		<title>Hello Bulma!</title>
		
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css">
	
	</head>

	<body>

		<nav class="navbar is-dark">
		
			<div class="navbar-brand">
			
				<a href="/" class="navbar-item">Markdown blog</a>
			
			</div>
			
		</nav>
			
		<section class="section">
			
			<div class="container">
			
				{% block content %}
				
				{% endblock %}
			
			</div>
		
		</section>
	
	</body>

</html>
```

y creamos otro archivo allí mismo llamado /templates/blog/index.html

```
{% extends 'blog/base.html' %}

  

{% block content %}

    {% for post in posts %}

        <div class="box">

            <section class="hero is-primary">

                <div class="hero-body">

                    <p class="title">{{ post.title }}</p>

                    <p class="subtitle">{{ post.created_ad|date:"Y-m-d H:i" }}</p>

                </div>

            </section>

  

            <div class="content">

                <p>{{ post.intro }}</p>

  

                <a href="#">Read more</a>

            </div>

        </div>

    {% endfor %}

{% endblock %}
```

ya tenemos nuestras plantillas ahora vamos a /blog/views.py y declaremos nuestra function que nos llevara a esa pagina

```
from django.shortcuts import render

  

from .models import Post

  

def index(request):

    posts = Post.objects.all()

  

    return render(request, 'blog/index.html', {'posts': posts})
```

ahora vamos a /markdownblog/urls.py y declaramos ese path

```
from django.contrib import admin

from django.urls import path

  

from blog import views

  

urlpatterns = [

    path('admin/', admin.site.urls),

    path('',  views.index, name='index'),

]
```

salvamos y vamos a nuestra pagina y refrescamos

![image](README%20IMG/Pasted%20image%2020220707140919.png)