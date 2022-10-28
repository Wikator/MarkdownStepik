from copy import deepcopy
from random import randint

def SolveSudoku(sudoku):

    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

    groups = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    numbersLeft = 81
    firstTime = True
            
    for i in range (9):
        for j in range (9):
            if sudoku[i][j] != ' ':
                numbersLeft -= 1
     
    while True:
        
        numberWasAdded = False
        possibleNumbers = {}
        numberToPlace = {}
        canGo = {}
        
        for i in range (9):
            for j in range(9):
                possibleNumbers[str(i)+str(j)] = 0
                for number in numbers:
                    canGo[number+str(i)+str(j)] = False
                    
        #Sprawdzanie, czy się wszystko zgadza oraz uzupełnianie wierszy i kolumn, jeżeli brakuje tylko 1 liczby
        
        try:
            
            for z in range(0, 9, 3):
                for k in range (0, 9, 3):
                    numberToAdd = list(numbers)
                    for i in range (0+z, 3+z):
                        for j in range (0+k, 3+k):
                            if sudoku[i][j] != ' ':
                                numberToAdd.remove(sudoku[i][j])
                    if len(numberToAdd) == 1:
                        for i in range (0+z, 3+z):
                            for j in range (0+k, 3+k):
                                if sudoku[i][j] == ' ':
                                    numbersLeft -= 1
                                    sudoku[i][j] = numberToAdd[0]
                                    numberWasAdded = True
                                
            for z in range(3):
                for k in range (3):
                    numberToAdd = list(numbers)
                    for i in range (0+z, 9, 3):
                        for j in range (0+k, 9, 3):
                            if sudoku[i][j] != ' ':
                                numberToAdd.remove(sudoku[i][j])
                    if len(numberToAdd) == 1:
                        for i in range (0+z, 9, 3):
                            for j in range (0+k, 9, 3):
                                if sudoku[i][j] == ' ':
                                    numbersLeft -= 1
                                    sudoku[i][j] = numberToAdd[0]
                                    numberWasAdded = True

        except ValueError:
            
            #Próba nie powiodła się, powrót do zapisanej listy

            try:
                
                numbersLeft = savedNumbersLeft
                sudoku = deepcopy(testSudoku)

                while True:
                    
                    i = randint(0, 8)
                    j = randint(0, 8)
                    number = str(randint(1, 9))
                    if savedCanGo[number+str(i)+str(j)] is True:
                        break
                    
                sudoku[i][j] = number
                numbersLeft -= 1
                continue
        
            except UnboundLocalError:
                
                return 'Cannot solve'
     
        #Sprawdzanie, gdzie każda liczba może być wypisana
        
        for number in numbers:
            for i in range (9):
                if sudoku[i].count(number) == 0:
                    places = 0
                    placei = 0
                    placej = 0
                    for j in range (9):
                        if sudoku[i][j] == ' ':
                            works = True
                            
                            for z in range (groups[i//3][0], groups[i//3][2]+1):
                                for k in range(groups[j//3][0], groups[j//3][2]+1):
                                    if sudoku[z][k] == number:
                                        works = False
                                        break
                                if works is False:
                                    break
                            if works:
                                for z in range (i%3, 9, 3):
                                    for k in range(j%3, 9, 3):
                                        if sudoku[z][k] == number:
                                            works = False
                                            break
                                    if works is False:
                                        break
                                    
                            if works:
                                possibleNumbers[str(i)+str(j)] += 1
                                numberToPlace[str(i)+str(j)] = number
                                canGo[number+str(i)+str(j)] = True
                                places += 1
                                placei = i
                                placej = j

                    #Dodanie liczby, jeśli w danej komórce ma tylko jedne możliwe miejsce
                                
                    if places == 1:
                        numberWasAdded = True
                        sudoku[placei][placej] = number
                        numbersLeft -= 1

        #Wpisanie liczby do komórki, jeżeli w tej komórce pasuje tylko 1 liczba                
                        
        for i in range(9):
            for j in range(9):
                if possibleNumbers[str(i)+str(j)] == 1 and sudoku[i][j] == ' ':
                    sudoku[i][j] = numberToPlace[str(i)+str(j)]
                    numbersLeft -= 1
                    numberWasAdded = True

        if numbersLeft == 0:
            return sudoku

        #Nie ma żadnej liczby z tylko jedną możliwością bądź komórki z tylko jedną możliwością, rozpoczęcie kombinowania
            
        if numberWasAdded is False:
                
            #Zapisanie list w momencie, kiedy trzeba zacząć kombinować
                
            if firstTime:
                savedNumbersLeft = numbersLeft
                firstTime = False
                testSudoku = []
                testSudoku = deepcopy(sudoku)
                savedCanGo = deepcopy(canGo)
            
            while True:
                
                i = randint(0, 8)
                j = randint(0, 8)
                number = str(randint(1, 9))
                if canGo[number+str(i)+str(j)] is True:
                    break
                
            sudoku[i][j] = number
            numbersLeft -= 1
                
    return 'Cannot solve'
