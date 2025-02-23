import click
import uuid
from firebase_config import db

def view_mentors():
    click.echo("Available Mentors: ")
    mentors = db.child("mentors").get()
    if mentors.each():
        for mentor in mentors.each():
            click.echo(f"ID: {mentor.key()}, Name: {mentor.val().get('name')}, Expertise: {mentor.val().get('expertise')}")
    else:
        click.echo("No mentors available")

def book_mentor(user_id):
    mentor_id = input("Enter Mentor ID: ").strip()
    date = input("Enter Date (YYYY-MM--DD): ").strip()
    time = input("Enter Time (HH:MM): ").strip()

    booking_id = str(uuid.uuid4()) #using uuid to generats a unique unique ID for the booking
    booking = {
        "user_id": user_id,
        "mentor_id": mentor_id,
        "date": date,
        "time": time,
        "status": "confirmed"
    }
    db.child("bookings").child(booking_id).set(booking)
    click.echo("Booking confirmed")

def view_bookings(user_id):
    click.echo("Your Bookings: ")
    bookings = db.child("bookings").order_by_child("user_id").equal_to(user_id).get()
    if bookings.each():
        for booking in bookings.each():
            click.echo(f"Booking ID: {booking.key()}, Mentor: {booking.val().get('mentor_id')}, Date: {booking.val().get('date')}, Time: {booking.val().get('time')}")
    else:
        click.echo("No bookings found")


def cancel_booking():
    booking_id = input("Enter Booking ID: ").strip()
    booking = db.child("bookings").child(booking_id).get()
    if booking.val():
        db.child("bookings").child(booking_id).remove()
        click.echo("Booking cancelled successfully")
    else:
        click.echo("Booking not found")


def booking(user):
    user_id = user["localId"]

    while True:
        click.echo("Booking Menu")
        click.echo("1. View Mentors")
        click.echo("2. Book Mentor")
        click.echo("3. View Bookings")
        click.echo("4. Cancel Booking")
        click.echo("5. Logout")

        choice = input("Select an option from 1-5: ")

        if choice == "1":
            view_mentors()
        elif choice == "2":
            book_mentor(user_id)
        elif choice == "3":
            view_bookings(user_id)
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            click.echo("Logged out successful!")
            break
        else:
            click.echo("Invalid choice. Try again.")


if __name__ == "__main__":
    booking()