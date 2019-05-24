"""newProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import finalapp.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', finalapp.views.login, name='login'),
    path('board_2p/', finalapp.views.playerSelect_2p, name='playerSelect_2p'),
    path('board_3p/', finalapp.views.playerSelect_3p, name='playerSelect_3p'),
    path('board_4p/', finalapp.views.playerSelect_4p, name='playerSelect_4p'),
    path('diceCheck/', finalapp.views.diceCheck, name='diceCheck'),
    path('game_final01/', finalapp.views.game_final01, name='game_final01'),
    path('game_final03/', finalapp.views.game_final03, name='game_final03'),
    path('game_final04/', finalapp.views.game_final04, name='game_final04'),
    path('game_final05/', finalapp.views.game_final05, name='game_final05'),
    path('game_final06/', finalapp.views.game_final06, name='game_final06'),
    path('game_final08/', finalapp.views.game_final08, name='game_final08'),
    path('game_final09/', finalapp.views.game_final09, name='game_final09'),
    path('game_final10/', finalapp.views.game_final10, name='game_final10'),
    path('game_final11/', finalapp.views.game_final11, name='game_final11'),
    path('game_final12/', finalapp.views.game_final12, name='game_final12'),
    path('game_final13/', finalapp.views.game_final13, name='game_final13'),
    path('game_final14/', finalapp.views.game_final14, name='game_final14'),
    path('game_final15/', finalapp.views.game_final15, name='game_final15'),
    path('game_final16/', finalapp.views.game_final16, name='game_final16'),
    path('game_final18/', finalapp.views.game_final18, name='game_final18'),
    path('game_final19/', finalapp.views.game_final19, name='game_final19'),
    path('game_final20/', finalapp.views.game_final20, name='game_final20'),
    path('game_final21/', finalapp.views.game_final21, name='game_final21'),
    path('game_final23/', finalapp.views.game_final23, name='game_final23'),
    
    path('game_final24A/', finalapp.views.game_final24A, name='game_final24A'),
    path('game_final24B/', finalapp.views.game_final24B, name='game_final24B'),

    path('game_final25/', finalapp.views.game_final25, name='game_final25'),
    path('game_final26/', finalapp.views.game_final26, name='game_final26'),
    path('game_final27/', finalapp.views.game_final27, name='game_final27'),
    path('game_final28/', finalapp.views.game_final28, name='game_final28'),
    path('game_final29/', finalapp.views.game_final29, name='game_final29'),
    path('game_final31b/', finalapp.views.game_final31, name='game_final31'),
    path('game_final31c/', finalapp.views.game_final31, name='game_final31'),
    path('game_final31d/', finalapp.views.game_final31, name='game_final31'),
    path('game_final32/', finalapp.views.game_final32, name='game_final32'),
    path('game_final34/', finalapp.views.game_final34, name='game_final34'),
    path('game_final35/', finalapp.views.game_final35, name='game_final35'),
    path('game_final37/', finalapp.views.game_final37, name='game_final37'),
    path('game_final38/', finalapp.views.game_final38, name='game_final38'),
    path('game_final39/', finalapp.views.game_final39, name='game_final39'),
    path('goldkey_a/', finalapp.views.goldenKey, name='goldenKey'),
    path('goldkey_b/', finalapp.views.goldenKey, name='goldenKey'),
    path('goldkey_c/', finalapp.views.goldenKey, name='goldenKey'),
]
