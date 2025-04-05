"""
Email Validator Problem

Objective:
Write a function to validate email addresses based on specific rules.

Requirements:
1. Exactly one '@' symbol
2. Valid local part (before @): letters, numbers, ._%+-
3. Valid domain (after @): letters, numbers, .-
4. Domain extension must be 2-4 characters
5. Return True if valid, False otherwise

Example Valid Emails:
- user@example.com
- user.name@domain.co  
- user+tag@example.com

Example Invalid Emails:
- user@.com
- @domain.com
- user@domain..com
- user@example.c
"""

def validate_email(email):
    """
    Implement email validation according to the rules above.
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    # TODO: Implement the validation logic
    pass
