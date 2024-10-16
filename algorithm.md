# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...
1. Output purpose of code, including that the initial balance is $1000.
2. Set not choice to "G"
3. Set Sentinel to "E"
3. Set the balance to 1000
6. While choice is not Sentinel:
   1. Prompt user to enter an action (D, V, W, E)
   2. Set input value to upper case
   3. If user action = "D"
      1. Prompt user to input how much they want to deposit 
      2. If user input is less than 0
           1. Output error message and try again
      3. Otherwise set balance to balance + deposited input
         1. Output new balance
      4. Prompt user to input another action
   7. Otherwise if user action = "W"
       1. Prompt user to input how much they want to withdraw
       2. If user input is less than 0
           1. Output error message and try again
      2. Set new balance to the balance - withdrawn input
      3. If balance is less than 0 
           1. Output a warning message telling them they will be charged a 5% interest fee
      4. Output new balance
      5. Prompt user to input another action
   8. Otherwise if user action = "V"
       1. Output balance
       2. Prompt user to input another action
   9. Otherwise 
      1. Output that the input is invalid
      2. Prompt user to input another action