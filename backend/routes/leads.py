from flask import Blueprint, request, jsonify
from backend.services.lead_service import process_lead

leads_bp = Blueprint("leads", __name__, url_prefix="/api/leads")


@leads_bp.route("", methods=["POST"])
def create_lead():
    """
    Create a new lead
    """
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Invalid JSON payload"
        }), 400

    success, message = process_lead(data)

    if not success:
        return jsonify({
            "success": False,
            "message": message
        }), 400

    return jsonify({
        "success": True,
        "message": message
    }), 201
