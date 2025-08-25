"""
Module: bob_responses
Purpose: Determine Bob's reply based on the input message.
Bob responds differently to questions, yelling, silence, and other statements.
"""

def bob_reply(message):
    """
    Determine Bob's response based on the input message.

    Rules:
    1. "Calm down, I know what I'm doing!" -> if the message is a YELLING QUESTION (all caps + ends with '?')
    2. "Whoa, chill out!" -> if the message is yelling (all caps, not empty)
    3. "Sure." -> if the message is a question (ends with '?')
    4. "Fine. Be that way!" -> if the message is empty or only whitespace
    5. "Whatever." -> for any other message

    Args:
        message (str): The input string from the user.

    Returns:
        str: Bob's response.
    """

    # Remove leading/trailing whitespace for accurate checks
    stripped_message = message.strip()

    if not stripped_message:
        return "Fine. Be that way!"

    is_question = stripped_message.endswith('?')
    is_yelling = stripped_message.isupper()

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_yelling:
        return "Whoa, chill out!"
    else:
        return "Whatever."


# Example Usage
if __name__ == "__main__":
    test_messages = [
        "HOW ARE YOU?",
        "HOW ARE YOU",
        "How are you?",
        "   ",
        "Hello there."
    ]
    for test in test_messages:
        print(f"message is '{test}' and response is '{bob_reply(test)}'")