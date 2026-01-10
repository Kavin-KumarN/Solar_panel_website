from flask import Blueprint, jsonify
from backend.models.testimonial_model import get_active_testimonials

testimonials_bp = Blueprint(
    "testimonials",
    __name__,
    url_prefix="/api/testimonials"
)


@testimonials_bp.route("", methods=["GET"])
def fetch_testimonials():
    """
    Get all active testimonials
    """
    testimonials = get_active_testimonials()

    return jsonify({
        "success": True,
        "data": testimonials
    }), 200
