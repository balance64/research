A couple of algorithms I found in a book I got from the library 
"Essential Computer Science: A Programmer's Guide to Foundational Concepts"
by 
Paul D. Crutcher
Neeraj Kumar Singh
Peter Tiegs

I wrote them out manually and tried to understand the thinking behind them. 
I found it interesting and even tried to get my own version of bubble sort 
working for a few hours but it was too hard to improve upon. The idea I had 
was to compare the start of the list (index 0) to the next item and if it's 
higher then shuffle it to the right, then go back to the start and check the 
next one and do the same (hoping to shuffle all higher values to the right and 
lower values to the left). This however didn't work and after a frustrating couple
of hours I can now understand why. Iterating through the list going right doesn't 
make sense, if we move the value right then we run into it again! And if a 
higher value(s) is on the right then where exactly do you place the next one? 
It means you need a check within a check! So in hindsight the book was right 
and very efficient and I was wrong lol. 
