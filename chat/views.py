from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    
    chat_rooms = [
        {'id':1, 'name': 1, 'description': 'Some new message'},
        {'id':1, 'name': 2, 'description': 'Some message'},
    ]
    return render(request, 'index.html', context={'chat_rooms': chat_rooms})

def room(request, room_name):
    chat_messages = [
        {'content': 'Hello!', 'timestamp': '2023-05-22 09:00:00', 'sender': 'User1'},
        {'content': 'Hi there!', 'timestamp': '2023-05-22 09:05:00', 'sender': 'User2'},
        {'content': 'How are you?', 'timestamp': '2023-05-22 09:10:00', 'sender': 'User1'},
        {'content': 'I am doing great! I am doing great! I am doing great! I am doing great! I am doing great!I am doing great! I am doing great! I am doing great!', 'timestamp': '2023-05-22 09:15:00', 'sender': 'User2'},
        {'content': 'What about you?', 'timestamp': '2023-05-22 09:20:00', 'sender': 'User2'},
        {'content': 'I am fine too!', 'timestamp': '2023-05-22 09:25:00', 'sender': 'User1'},
    ]

    context = {
        'room_name': room_name,
        'chat_messages': chat_messages,
        # 'current_user': request.user.username, 
        'current_user': 'User1'
    }

    return render(request, 'chat_room.html', context)
