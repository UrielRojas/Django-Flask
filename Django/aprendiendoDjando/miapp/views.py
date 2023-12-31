from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from miapp.forms import ForArticle
from django.contrib import messages

# Create your views here.

#MVC  = MODELO VISTA CONTROLADOR
#MVT = MODELO VISTA TEMPLATE

layout = """
<h1>Sitio Web con Django</h1>
<hr/>
<ul>
    <li>
        <a href= "/inicio">Inicio</a>
    </li>
    <li>
        <a href= "/hola-mundo">Hola mundo</a>
    </li>

    <li>
        <a href= "/pagina-pruebas">Página pruebas</a>
    </li>

    <li>
        <a href= "/contacto">Contactos</a>
    </li>
</ul>
<hr/>
   
"""

def hola_mundo(request):
    return render(request, 'hola_mundo.html')


def index(request):
    year = 2021

    hasta = range(year, 2051)


    nombre = 'Uriel Rojas'

    lenguajes = ['js', 'python', 'PHP', 'C']
    return render(request,'index.html', {
        'title': 'Inicio 2',
        'mi_variable': 'soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta},  ) 

def pagina(request, redirigir=0):
    
    if redirigir == 1:
        return redirect('contacto', nombre ="Uriel", apellidos="Rojas")
        #return redirect('/contacto/Uirle/Rojas')
    

    return render(request, 'pagina.html',
                  {
                      'texto': 'asfasd',
                      'lista': [1,2,3,4,5]
                  } )


def contacto(request, nombre="",apellidos=""):
    html = ""

    if nombre and apellidos:
        html += "<p> El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellidos} </h3"
    
    return HttpResponse(layout+ f"""
        <h2> Contacto</h2>
    """ + html)


def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()

    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")

def articulo(request):

    try:
        articulo = Article.objects.get(title="Superman", public = True)

    except:
        return HttpResponse("Articulo no encontrado")
    return HttpResponse(f"Articulo: {articulo.id} {articulo.title}")

def editarArticulo(request, id):

    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo editado: {articulo.title} - {articulo.content}")


def articulos(request):
    articulos =  Article.objects.filter(public = True)

    
    #articulos = Article.objects.filter(id__lte = 13, title__contains = "2")

    #articulos = Article.objects.filter(title__contains = "articulo").exclude(public = False)


    #articulos = Article.objects.raw("SELECT * FROM miapp_article")


    return render(request, 'articulos.html', 
                        {'articulos': articulos
                         })


def borrarArticulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')


def saveArticle(request):

    if request.method == "POST":
        title  = request.POST['title']
        content  = request.POST['content']
        public  = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        articulo.save()
        return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")

    else:
        return HttpResponse("<h2>No se ha podido crear al articulo</h2>")



def createArticle(request, ):

    return render(request, 'create_article.html')


def create_full_article(request):

    if request.method == "POST":
        formulario = ForArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title = data_form.get('title')
            content = data_form.get('content')
            public = data_form.get('public')

            articulo = Article(
            title = title,
            content = content,
            public = public)

            articulo.save()

            #Crear mensaje flask
            messages.success(request, "Has creado correctamente el artículo")
            

            return redirect('articulos')
        else:
            print(" ")

    else:
        formulario = ForArticle()

    return render(request,'create_full_article.html', {'form': formulario}
                  )