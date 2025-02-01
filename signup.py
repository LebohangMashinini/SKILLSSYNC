import click
import pwinput
from firebase_config import auth, db

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


def is_valid_password(password):
    """Validate password strength."""
    if len(password) < 8:
        return False
    
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        return False
    
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        return False
    
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        return False
    
    has_special = False
    special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/|`~"
    for char in password:
        if char in special_characters:
            has_special = True
            break
    if not has_special:
        return False
    
    return True

def signup():
    click.echo("Signup...")
    email = input("Enter email: ").strip()
    if not is_valid_email(email):
        click.echo("Invalid email format. Please enter a valid email.")
        return
    
    password = pwinput.pwinput("Enter your password: ")
    if not is_valid_password(password):
        click.echo("Password must be at least 8 characters long, contain an uppercase letter, "
                   "a lowercase letter, a number, and a special character.")
        return
    name = input("Enter your name: ").strip()
    role = input("What is your role (mentor/peer): ").strip().lower()
    expertise = input("Are you a Frontend or Backend developer? Please type 'Frontend' or 'Backend': ").strip()
    while expertise not in ["Frontend", "Backend"]:
        expertise = input("Invalid input. Please type 'Frontend' or 'Backend': ").strip()

    if role not in ["mentor", "peer"]:
        click.echo("Invalid input. Please enter 'mentor' or 'peer'.")
        return

    try:
        user = auth.create_user_with_email_and_password(email, password)
        user_id = user["localId"]
        auth_token = user["idToken"]

        db.child("users").child(user_id).set({
            "name": name,
            "email": email,
            "role": role,
            "expertise": expertise
        }, auth_token)
        print("User added to database successfully!")
    except Exception as e:
        click.echo(f"Error: {e}")
        if "EMAIL_EXISTS" in str(e):
            click.echo("An account with this email already exists.")