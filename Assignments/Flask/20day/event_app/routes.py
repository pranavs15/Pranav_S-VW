from flask import Flask, request, jsonify
from models import db, Event, Registration

def setup_routes(app):

    # Create event
    @app.route("/events", methods=["POST"])
    def create_event():
        data = request.get_json()
        name = data.get("name")
        total_seats = data.get("total_seats")
        if not name or total_seats is None:
            return jsonify({"error": "Name and total_seats are required"}), 400
        event = Event(name=name, total_seats=total_seats, available_seats=total_seats)
        db.session.add(event)
        db.session.commit()
        return jsonify({"message": "Event created", "event": {"id": event.id, "name": event.name}}), 201

    # List all events
    @app.route("/events", methods=["GET"])
    def list_events():
        events = Event.query.all()
        result = [
            {"id": e.id, "name": e.name, "total_seats": e.total_seats, "available_seats": e.available_seats} 
            for e in events
        ]
        return jsonify(result)

    @app.route("/register/<int:event_id>", methods=["POST"])
    def register(event_id):
        event = Event.query.get(event_id)
        if not event:
            return jsonify({"error": "Event not found"}), 404
        if event.available_seats == 0:
            return jsonify({"error": "No seats available"}), 400

        data = request.get_json()
        user_name = data.get("user_name")
        if not user_name:
            return jsonify({"error": "user_name is required"}), 400

        registration = Registration(user_name=user_name, event_id=event_id)
        db.session.add(registration)
        event.available_seats -= 1
        db.session.commit()
        return jsonify({"message": f"{user_name} registered for {event.name}"}), 201

    @app.route("/events/full", methods=["GET"])
    def full_events():
        events = Event.query.filter_by(available_seats=0).all()
        result = [{"id": e.id, "name": e.name, "total_seats": e.total_seats} for e in events]
        return jsonify(result)