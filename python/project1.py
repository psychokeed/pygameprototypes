print('welcome to the "POP QUIZ"')

playing = input('Will you play this game? ')

if playing.lower() != 'yes':
    quit()

print('okay then, lets play :) !')
score = 0

question = input('What does CPU stand for? ')

if question.lower() == 'central processing unit':
    print('Correct!' )
    score += 1
else:
    print('Incorrect!')
    
question = input('What does GPU stand for? ')

if question.lower() == 'graphics processing unit':
    print('Correct! ')
    score += 1
else:
    print('Incorrect! ')
    
question = input('What does RAM stand for? ')

if question.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
question = input('What does PSU stand for?  ')

if question.lower() == 'power supply':
    print('Correct! ')
    score += 1
else:
    print('Incorrect! ')

print('you got ' + str(score) + 'questions correct!')
print('you got ' + str((score / 4) * 100) + '%.')
