# Python Learning Journey

![xl5cyhhqmsab1(1)(1)](https://github.com/user-attachments/assets/46900b8c-6515-4731-b8e7-097ca424762f)

This repository documents my progression learning Python through Dr. Angela Yu's "100 Days of Code" bootcamp and other resources. Each project represents different skills I've acquired along the way.
Each project represents my own personal interpretation of the exercise instructions provided in the course.

## About This Repository

This collection documents my Python learning journey, completed independently in my free time outside of university coursework. All projects follow Dr. Angela Yu's "100 Days of Code: The Complete Python Pro Bootcamp" and represent my personal implementation of the challenges.

## My Learning Journey

As a Python programmer relearning python fundamentals, each project represents my personal interpretation of the exercise instructions provided in the course.  

## Beginner Projects
____________________________________________________________________________________________________________________________________________________________________________________________________________

- **[Treasure Island Game](./01-beginner-projects/treasure-island)**: A text-based adventure game using conditional statements
  - In this simple text-based game, players make choices that determine whether they find the treasure or meet an unfortunate end.
  - **Game Description**  
    In Treasure Island, players navigate through a series of choices:
      1. Choose whether to go left or right at a crossroads
      2. Decide whether to swim across a lake or wait for a boat
      3. Select one of three colored doors (Red, Blue, or Yellow)
   
     Only one path leads to the treasure, while wrong choices result in creative "game over" scenarios!
  - **Skills Practiced**
    1. Conditional statements (if/elif/else)
    2. User input handling
    3. String comparison
    4. ASCII art for visual feedback
    5. Logical operators (AND, OR, NOT)
  - **How to Run**  
    Simply run the Python script in your terminal:
    ```
    python treasure_island.py
    ```
    
  - **[Rock Paper Scissors](./01-beginner-projects/rock-paper-scissors)**: An interactive console game against the computer
    - A classic game implementation where players choose rock, paper, or scissors to compete against the computer's random choice.
    - **Game Description**  
      In Rock Paper Scissors, players experience:
        1. Selecting their move by typing a number (0 for Rock, 1 for Paper, 2 for Scissors)
        2. Seeing their choice displayed with ASCII art
        3. The computer randomly selects its move
        4. Game logic determines the winner based on traditional rules:
           - Rock crushes Scissors
           - Paper covers Rock
           - Scissors cut Paper
        5. Player sees the result (win, lose, or draw) with eye-catching ASCII art
   
      The game offers a visual experience with detailed ASCII art representations for each choice and outcome.
  - **Skills Practiced**
    1. Random module for computer selection
    2. Conditional logic for game rules
    3. Input validation
    4. ASCII art for visual feedback
    5. String concatenation and formatting
    6. Program flow control
  - **How to Run**  
    Simply run the Python script in your terminal:
    ```
    python rock-paper-scissors-game.py
    ```
    
- **[Password Generator](./01-beginner-projects/password-generator)**: A customizable password generator with user-defined complexity
  - A security-focused tool that creates random passwords based on user specifications for letters, symbols, and numbers.
  - **Program Description**  
    The Password Generator allows users to:
      1. Specify how many letters they want in their password (a-z, A-Z)
      2. Choose the number of symbols to include (!#$%&()*+)
      3. Select how many numbers to add (0-9)
      4. Generate a randomized, shuffled password with their specifications
      5. Receive a secure password ready for use
   
    The program creates truly random passwords by shuffling all selected characters, ensuring no predictable patterns.
  - **Skills Practiced**
    1. Random module for character selection and shuffling
    2. Lists and list manipulation
    3. For loops and range() function
    4. String methods (join())
    5. User input handling
    6. Modular code organization
    7. Random selection with random.choice()
  - **How to Run**  
    Simply run the Python script in your terminal:
    ```
    python password_generator.py
    ```

- **[Hangman](./01-beginner-projects/hangman_main)**: A classic word-guessing game with ASCII art gallows
  - A traditional hangman game where players guess letters to uncover a mystery country name before running out of lives.
  - **Game Description**  
    Players guess letters to reveal a hidden country name (6 lives total). Wrong guesses draw the hangman, correct guesses reveal letter positions. Features enhanced duplicate guess detection for both correct AND incorrect letters (using continue statements) and country-themed word list with 100+ countries.) <-  This fix wasn't coveed in the lession
  - **Skills Practiced**
    1. While loops and continue statements
    2. List manipulation and tracking
    3. Random module for word selection
    4. Input validation and duplicate checking
    5. ASCII art integration
    6. Modular programming with separate files
  - **How to Run**  
    Ensure you have `hangman_words.py` and `hangman_art.py` in the same directory, then run:
    ```
    python hangman.py
    ```
    

## Intermediate Projects
____________________________________________________________________________________________________________________________________________________________________________________________________________
- *Coming soon as I progress through the course...*

## Future Goals

- Continue adding projects as I complete them
- Revisit earlier projects to enhance them with new skills
- Explore personal project ideas using Python
- Implement more advanced features like databases, APIs, and web applications

## Acknowledgements

- Dr. Angela Yu and the App Brewery team for the excellent course content
- The Python community for their vast resources and documentation
