# Password Generator 💡🔐

Generate secure and random passwords with ease! This Python module allows you to import and use the Password Generator functionality in your own projects, enabling you to create strong passwords for your online accounts. 🦾

## Features

✨ **Length Customization:** Specify the desired length of your password.
✨ **Complexity Options:** Choose which character types to include in your password.
✨ **Pronounceable Passwords:** Generate passwords that are easy to remember.

## Usage

1. Make sure you have Python 3 installed.

2. Install the required modules:

    ```bash
    pip install random string
    ```

3. Import the password_generator module in your Python code:

    ```python
    import password_generator
    ```

4. Generate a password using the generate_password() function:

    ```python
    password = password_generator.generate_password(length=12, complexity="all", pronounceable=False)
    print("Generated Password:", password)
    ```
    Customize the arguments (length, complexity, pronounceable) to fit your requirements.  

## License

This project is licensed under the MIT License  

Feel free to contribute, provide feedback, or share your ideas for additional features. Happy password generating! 😄🔒