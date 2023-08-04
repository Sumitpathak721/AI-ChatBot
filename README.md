# Query-Solving Chatbot using Python

A simple yet effective query-solving chatbot implemented in Python. This chatbot aims to provide answers to user queries by leveraging past data stored in text files. It uses a comparison mechanism to match user questions with a database of previously answered questions and responds accordingly.

## Features

- Utilizes user input and past data to provide accurate answers to queries.
- Handles variations of the same question using word comparison techniques.
- Allows users to confirm or provide answers for unmatched or partially matched questions.
- Offers a user-friendly interface for interacting with the chatbot.

## How it Works

1. The chatbot reads user input and attempts to match it with questions stored in the `questions.txt` database.
2. It uses word comparison techniques to identify potential matches.
3. If a matching question is found, the chatbot displays the corresponding answer.
4. If multiple potential matches are found, the chatbot presents options for the user to select the correct question.
5. If no match is found, the chatbot prompts the user to provide an answer and stores it for future use.

## Getting Started

1. Clone this repository to your local machine.
2. Ensure you have Python installed (version X.Y or higher).
3. Place your initial questions and answers in the `questions.txt` and `answers.txt` files, respectively.
4. Run the provided Python script to launch the chatbot interface.

## Usage

- Run the Python script.
- Enter your question or query.
- The chatbot will attempt to provide a relevant answer based on the stored data.
- Follow the prompts to confirm or update answers as necessary.

## Contributions

Contributions to this project are welcome! Feel free to submit pull requests to enhance the functionality, user experience, or code quality.

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy Code :)
