from django.urls import path
from direct_msg.views import inbox, Directs, SendMessage, UserSearch, NewConversation

urlpatterns = [
    path('', inbox, name='inbox'),
    path('direct_msgs/<username>', Directs, name='directs'),
    path('send/', SendMessage, name='send_direct_msg'),
    path('new/',UserSearch, name='usersearch'),
    path('new/<username>',NewConversation, name='newconversation'),
    
]