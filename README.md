# Sudoku solving algorythm

A sudoku solver I wrote some time ago

## How it works

The algorythm will loop to fill all the squeres that can hold only 1 possible number. When only those squeres that can hold more than 1 number remain, the algorythm break the loop, save the current state and will begin to experiment. It will put 1 random number in random place, fill those squeres that have only 1 possible option, and will repeat this new loop until:

- The sudoku is solved
    -in this case, the algorytm returns the solved sudoku
- The algorythm will detect that the sudoku is impossible to solve in the current state
    -in this case, it will return to the saved state, and try again
