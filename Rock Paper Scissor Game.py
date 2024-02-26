import random
while(True):
    a=input('Choose One - Rock, Paper, Scissor ')
    print(a)
    List=['Rock','Paper','Scissor']
    b=random.choice(List)
    print(b)
    if a=='Rock' and b=='Paper':
        print('You Lost','Paper Wins')
    elif a=='Rock' and b=='Scissor':
        print('You Won','Rock Wins')
        break
    elif a==b:
        print('Match Tied')
    elif a=='Paper' and b=='Rock':
        print('You Won','Paper wins')
        break
    elif a=='Paper' and b=='Scissor':
        print('You lost','Scissor Wins')
    elif a==b:
        print('Match Tied')
    if a=='Scissor' and b=='Rock':
        print('You Lost','Rock Wins')
    elif a=='Scissor' and b=='Paper':
        print('You Won')
        print('Scissor Wins')
        break
while True:
    print('Want To Play Again')
    c=input('yes or no - ')
    if c=='yes':
        while True:
            a=input('Choose One - Rock, Paper, Scissor ')
            print(a)
            List=['Rock','Paper','Scissor']
            b=random.choice(List)
            print(b)
            if a=='Rock' and b=='Paper':
                print('You Lost','Paper Wins')
            elif a=='Rock' and b=='Scissor':
                print('You Won','Rock Wins')
                break
            elif a==b:
                print('Match Tied')
            elif a=='Paper' and b=='Rock':
                print('You Won','Paper wins')
                break
            elif a=='Paper' and b=='Scissor':
                print('You lost','Scissor Wins')
            elif a==b:
                print('Match Tied')
            if a=='Scissor' and b=='Rock':
                print('You Lost','Rock Wins')
            elif a=='Scissor' and b=='Paper':
                print('You Won')
                print('Scissor Wins')
                break
    else:
        print('Thanks For Playing')
        break


