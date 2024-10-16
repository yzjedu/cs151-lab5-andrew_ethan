[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SuR8ZRK0)
# Lab5 ATM: Menu Driven Program
### 🔴🔴 *DO NOT* Start to code before the instructor Approve your algorithm, and test cases 🔴🔴
- ### Grade: EMRN
- ### Due: Before Next Lab
- ### [Markdown Tutorial-1](https://www.youtube.com/shorts/-aSSrmAXHDg)
- ### [Markdown Tutorial-2](https://www.youtube.com/shorts/0YLTInrkaHg)
- ### Use [markdown_basics file](markdown_cheatsheet.md) to write readable algorithm

## `Problem: `
Build a simulation of an ATM (Automatic Teller Machine), where users can 
- View their balance, 
- Deposit (e.g. add money to the account), or 
- Withdraw (e.g. take money from the account).

## `Purpose: `
This lab gives you practice with:
* Designing and programming loops
* Re-using many of the other aspects of Python we've learned so far
* Testing code
* Error checking

## `Details:`
The initial balance is fixed at $1000.<br>
The user can choose any of the following options as they interact with your program:
* D - Deposit
* W - Withdraw
* V - View Balance
* E - Exit   `(loop until choice is E - sentinel value)`

After the user inputs an option, you do the correct task related to that action. <br>
Then they get to choose an action again. <br>
Only when they choose to exit does it stop looping.

### `Error Checking`
Unfortunately, users often don't pay attention to what they are typing. <br>
Give an error and ask them to try again when

1. Choice is not D,W,V or E. 
   1. Case should not matter for `D/W/V/E or d/w/v/e` choice.
2. A negative number is given for amount to deposit or withdraw

Also give an error message when:

1. The balance becomes negative. 
   1. Warn them that they will be charged 5% interest <br>
      `(do not actually bother calculating this, it's just an output).`

### `Design Hints`
Start by thinking of the tasks for this problem. <br>
Then think how you'd solve a task, which may end up as your algorithm for that section. <br>
Focus on what it needs to do without the loops or error checking, <br>
then once that makes sense add in the looping and then the error checking.

If you find yourself doing the same set of steps many times, <br>
perhaps even just with different numbers, <br>
then those set of steps should probably be in a loop.

## `Steps:`
1. Understand the problem
2. Write an algorithm in `algorithm.md` showing the steps the program will go through to solve this problem.
3. Test that your algorithm works by walking through it with example input, and re-reading the requirements above.
4. When you think your algorithm is correct, ask the lab instructor to approve it. 
   1. **The lab instructor must approve your algorithm before you code**
5. Write your code following your algorithm and using good usability principles. 
6. Properly comment your code with intro comments and line comments
---------
7. Create **_a set of test cases on your own_** to test that your program works correctly. 
   1. Make sure you fully test the error checking aspects of your program, and <br> 
   that you have at least one test that goes into each if statement option. <br>
   You are welcome to draw a flowchart to help you ensure you have tested all paths, <br>
   but you don't need to turn it in. Save test cases into testcases.xlsx.
-------
8. **_NOT REQUIRED BUT HELPFUL TO PRACTICE FLOWCHART_**
   - But First add `diagrams.net` plugin 
     - File -> Settings -> Plugins -> Marketplace: Then such and install `diagrams.net`
   - Update the flowchart of your project using `flowchart.svg`
-------

## `What to Submit in GitHub:`

1. Completed `main.py` file  
2. `algorithm.md`
   1. Must contain image of your flow chart
3. An Excel file with your test cases.  
    - Edit the `test_cases.xlsx` file with Excel software 
    - If it can open then ok. Otherwise
      - Right click on `test_cases.xlsx` -> Open In -> Associated Application
4. Encrypt your files using the `keys` and `process_reflection.py`
   1. `RD1.md` -> Reflection for Drive 1
   2. `RD2.md` -> Reflection for Drive 2
   3. If you use a different key, it is considered unsubmited

**As a reminder, reflections count toward your participation grade.**

Type the Reflection INSIDE the respective Word file and addressing the following questions:

 - Objective:
   - What were you supposed to learn/accomplish?

 - Procedure:
   - What steps were followed and what techniques did you use to solve the problem?
   - What were the Key concepts explored?

 - Results:
   - Did your results match what you expected to get? 
   - Did you try using various test cases, or extreme test cases?
  
 - Reflection:
   - What challenges did you encounter? 
   - How did you follow the first 3 rules of programming?
   - Did you overcome them, and how? 
   - Any key takeaways? 
   - Do you think you learned what you were supposed to learn for this lab? 
   - What was it like working with your partner?