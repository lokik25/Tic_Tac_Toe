matrix=[['1,1','1,2','1,3'],['2,1','2,2','2,3'],['3,1','3,2','3,3']]
# print('C1 C2 C3')
# print('\nR1\n''\nR2\n''\nR3\n')
for i in matrix:
    for j in i:
        print(j,end='  ')
    print('\n')
win=0
moves=9
while i==0 or win==0:
    moves-=1
    row=int(input('Enter desired Row:'))
    col=int(input('Enter desired Column:'))
    ip=input("Enter X or O:")
    matrix[row-1][col-1]=ip.upper()
    for i in matrix:
        for j in i:
            print(j.center(3),end='  ')
        print('\n')
  # row win check
    for cr in range(3):
        if (matrix[cr][0]==matrix[cr][1]==matrix[cr][2]=='X'):
            print('player X wins!!!')
            win=1
        elif (matrix[cr][0]==matrix[cr][1]==matrix[cr][2]=='O'):
            print('player O wins!!!')
            win=1
  # col win check
    for cc in range(3):
        if (matrix[0][cc]==matrix[1][cc]==matrix[2][cc]=='X'):
            print('player X wins!!!')
            win=1
        elif (matrix[0][cc]==matrix[1][cc]==matrix[2][cc]=='O'):
            print('player O wins!!!')
            win=1
    # right diagonal
    if (matrix[0][0]==matrix[1][1]==matrix[2][2]=='X'):
        print('player X wins!!!')
        win=1
    elif (matrix[0][0]==matrix[1][1]==matrix[2][2]=='O'):
        print('player O wins!!!')
        win=1
    # left diagonal
    if (matrix[0][2]==matrix[1][1]==matrix[2][0]=='X'):
        print('player X wins!!!')
        win=1
    elif (matrix[0][2]==matrix[1][1]==matrix[2][0]=='O'):
        print('player O wins!!!')
        win=1
    # tie condition
    if moves==0:
        print('its a tie')
        win=1


