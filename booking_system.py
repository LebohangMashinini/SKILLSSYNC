import click
import uuid
from firebase_config import db

def view_mentors():
    mentors = db.child("mentors").get()
    if mentors.each():
        for mentor in mentors.each():
            click.echo(f"ID: {mentor.key()}, Name: {mentor.val().get("name")}, Expertise: {mentor.val().get("expertise")}")
    else:
        click.echo("No mentors available")

def book_mentor(mentor_id, date, time):
    booking_id = str(uuid.uuid4()) #using uuid to generats a unique unique ID for the booking
    booking = {
        "mentor_id": mentor_id,
        "date": date,
        "time": time,
        "status": "confirmed"
    }
    db.child("bookings").child(booking_id).set(booking)

def view_bookings(user_id):
    bookings = db.child("bookings").order_by_child("user_id").equal_to(user_id).get()
    if bookings.each():
        for booking in bookings.each():
            click.echo(f"Booking ID: {booking.key()}, Mentor: {booking.val().get('mentor_id')}, Date: {booking.val().get('date')}, Time: {booking.val().get('time')}")
    else:
        click.echo("No bookings found")


def cancel_booking(booking_id):
    booking = db.child("bookings").child(booking_id).get()
    if booking.val():
        db.child("bookings").child(booking_id).remove()
        click.echo("Booking cancelled successfully")
    else:
        click.echo("Booking not found")

    