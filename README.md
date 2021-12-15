--- This simple yet powerful(potentially) program was constructed for the purpose of controlling daily expenses ---

-> On the left-handside, 'q' is our unknown variable which stands for quantatity, and the coefficients here are the unitary prices, 
   whereas the right handside of the inequality is our total limit that we do not want to exceed.

--- Features and Functions ---
* The program utilizes the power of algebra to solve the given inequality by finding the value of the 
  variable 'q' and then substitutes back to estimate as to how much it will cost at a total. 

* Since its obvious that the second argument will be our maximum cost, but sometimes the answer is in decimal, and
  since an item cannot be purchased fractionally, that's why the program rounds the number to the greatest integer value which
  is less then the decimal value.

* One of the primary features of this program is to return a number('q'), that can be used as the quantity of 
  every item, which in real life is difficult for human beings to estimate, especially when the item list is large.
  For example; you are asked to purchase three items in a given amount, let's say $500/-, and the three items are
  biscuits($10 per each), eggs($15 per each) and chips($30 per each). Hence our inequality is $10q + $15q + $30q <= $500

  Now by entering the prices of each item in our first argument and then by entering our total limit/cost in the second argument,
  like 'estimate(10+15+30, 500)', the program will return a number 9.090909090909092... and then round it to number 9.

  The number 9 tells us that if we will purchase all three items by the quantity of 9, meaning 9 biscuits, 9 eggs and 9 chips;
  Then our maximum cost will be $495, which does statisfy our inequality here ($495 <= $500).

* Then finally the quantity of each item can be adjusted by a human being according to his/her need. For example instead of 9
  biscuits I want 7 and instead of 9 eggs I want 10, then I can subtract $20 from $495, which is $475, and then add 15 again 
  to make it $490 and so on. 

--- Conclusion and Notes ---
The program might seem obvious but it provides an alternative approach in dealing with expenses, because majority of the times
we human beings think of our needs first, then our expenses, in this way we sometimes neglect the fact that we are spending more 
than we wanted. And also due to our procrastinative nature we avoid doing the math. So yeah this program solves this issue by 
taking a reverse approach. 

Finally the program has a very high potential, meaning it might not be much useful in its present state because of the absense of GUI, but it can be improved in many ways. For example; a Supervised Machine Learning model can be implemented here to track the historical data of the user and analyze it to find a suitable quantity for a specific item in a given amount.

--- End ---
