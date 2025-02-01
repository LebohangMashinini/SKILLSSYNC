import click
import pwinput
from firebase_config import auth

def is_valid_email(email):
    """Validate email format using regex."""
    if "@" not in email or email.startswith("@") or email.endswith("@"):
        return False
    
    local_part, domain_part = email.split("@", 1)
    if "." not in domain_part:
        return False
    
    if " " in email:
        return False
    
    if len(local_part) < 5 or len(domain_part) < 5:
        return False
    
    return True

def login():
    click.echo("Login...")
    
    # Prompt for email and validate format
    email = input("Enter email: ")
    while not is_valid_email(email):
        click.echo("Invalid email format. Please enter a valid email address.")
        email = input("Enter email: ")
    
    # Prompt for password
    password = pwinput.pwinput("Enter your password: ")
    
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        click.echo("Login successful!")
    except Exception as e:
        error_str = str(e)
        if "INVALID_PASSWORD" in error_str:
            click.echo("Incorrect password. Please try again.")
        elif "EMAIL_NOT_FOUND" in error_str:
            click.echo("Email not found. Please check your email address.")
        else:
            click.echo(f"Error: {e}")