# CRIANDO O AMBIENTE VIRTUAL ==>
                              # python -m venv pystore ==> ambiente virtual
# ==============================================================================#

#Activando o ambiente virtual ==>
                                #pyStore/Scripts/Activate.ps1"

#INICIANDO U  PROJECTO ==>
                        # django-admin startproject lojaPy ==> Nome do projecto
# ==============================================================================#


#LIGANDO O SERVIDOR ==>
# (pystore) PS C:\Users\Oscar AlbertoGuiamba\Documents\GitHub\site\ ==>
                                                                 # cd lojapy> 
                                                                # python manage.py runserver

# ==============================================================================#

#Actualizando o pip ==>
                      #python -m pip install --upgrade pip

#==============================================================================#


#=============================================================================#

#CRIANDO IUM APP ==>
                  #python .\manage.py startapp usuarios

#=============================================================================#
#ANALIZANDO A COBERTURA DOS TESTES ==>
                                   #pytest --cov --cov-report=html
#=============================================================================#
#Installation Directory: ==> C:\Program Files\PostgreSQL\13
#Server Installation Directory: ==> C:\Program Files\PostgreSQL\13
#Data Directory: ==> C:\Program Files\PostgreSQL\13\data
#Database Port: ==> 5432
#Database Superuser: ==>postgres
#Operating System Account:==> NT AUTHORITY\NetworkService
#Database Service: ==> postgresql-x64-13
#Command Line Tools Installation Directory: ==> C:\Program Files\PostgreSQL\13
#pgAdmin4 Installation Directory: ==> C:\Program Files\PostgreSQL\13\pgAdmin 4


#===============================================================================#

  #<form class="form-group" action="{% url 'cart:add' product.id %}" method="post">
                #<p class="form-inline">
                   # {{ form.quantity.label_tag }}
                    #{% render_field form.quantity class+="form-control ml-sm-3" %}
                    #{{ form.override }}
               # </p>
               # {% csrf_token %}
               # <input class="btn btn-success" type="submit" value="Adicionar ao Carrinho">
            #</form> -->
#=================================================================================#



# Media
#MEDIA_URL = "/media/"
#MEDIA_ROOT = BASE_DIR / "media"