# TicTacToe---Computer-O
Python TicTacToe game - computer is challenging, but can be beat

Hosted on Replit at [https://replit.com/@JohnDugger1/TicTacToe-Computer-O#main.py](https://replit.com/@JohnDugger1/TicTacToe-Computer-O#main.py)

I've made it so that the computer is challenging with a simple algorithm for O's move:
1. Take the center
2. If two Os in a row, take the third spot
3. If two Xs in a row, take the third spot
4. If it's the fourth turn, O has the center and X has at least one corner, take an edge
5. Take a corner if available
6. Take any available spot

If there are more than one valid move within a given step, it selects one at random.  
It does not yet try to create forks for itself.

The algorithm is derived from the strategy described in the [wikepedia article](https://replit.com/@JohnDugger1/TicTacToe-Computer-O#main.py)

Please let me know if you're able to beat it!
