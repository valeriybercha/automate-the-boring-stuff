# Magic 8 Ball
# Course: Automate the Boring Stuff with Python
# Developer: Valeriy B.

import random

def magic_ball():
    
    # List with answers
    answer_list = [
        'It is certain',
        'It is decidedly so',
        'Yes',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful'
    ]
    
    print(random.choice(answer_list))

magic_ball()