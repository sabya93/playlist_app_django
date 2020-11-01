from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks/', views.thanks, name='thanks'),
    path('randomise/<str:game>/', views.randomise, name='randomise'),
    path('put_playlist/', views.put_playlist, name='put_playlist'),
    path('create_game/', views.create_game, name='create_game'),
    path('get_games/', views.get_games, name='get_games'),
    path('vote/', views.vote, name='vote'),
    path('find_duplicate_name/', views.find_duplicate_name, name='find_duplicate_name'),
    path('find_duplicate_game/', views.find_duplicate_game, name='find_duplicate_game'),
    path('find_duplicate_song/', views.find_duplicate_song, name='find_duplicate_song'),
    path('game_info/', views.game_info, name='game_info'),
    path('send_support_mail/', views.send_support_mail, name='send_support_mail'),
    path('tnc/', views.terms_and_conditions, name='terms_and_conditions'),
    path('about_us/', views.about_us, name='about_us'),
    path('feedback/', views.feedback, name='feedback'),
    path('gameinfo/', views.game_info_howto, name='game_info_howto'),
    path('end_game/', views.end_game, name='end_game'),
]
