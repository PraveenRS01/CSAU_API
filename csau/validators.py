from csau.models import User
import re

regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

departments = [
    "aeronautical engineering",
    "architecture",
    "agriculture and irrigation engineering",
    "apparel technology",
    "automobile engineering",
    "bio-medical engineering",
    "ceramic technology",
    "chemical engineering",
    "civil engineering",
    "computer science and engineering",
    "electrical and electronics engineering",
    "electronics and communication engineering",
    "electronics and instrumentation engineering",
    "food technology",
    "geo-infomatics",
    "industrial bio-technology",
    "industrial engineering",
    "information technology",
    "leather technology",
    "manufacturing engineering",
    "material science and engineering",
    "mechanical engineering",
    "mining engineering",
    "pharmaceutical technology",
    "printing technology",
    "production engineering",
    "petroleum engineering and technology",
    "rubber and plastics technology",
    "textile technology",
]

tags = ["brown", "red", "grey", "purple", "orange", "green"]

domains = ["web and app development", "marketing", "event management", "designing"]


def validate_email(email):
    if re.match(regex, email):
        return True

    return False


def validate_user(req):

    if "username" not in req or req["username"] == "":
        return False, {"message": "Name is required"}

    if "reg_no" not in req:
        return False, {"message": "Register number is required"}

    if "department" not in req:
        return False, {"message": "Department is required"}

    if "tag" not in req:
        return False, {"message": "Tag is required"}

    if "domain" not in req:
        return False, {"message": "Domain number is required"}

    if "mobile_no" not in req:
        return False, {"message": "Mobile number is required"}

    if "email" not in req:
        return False, {"message": "Email is required"}

    u1 = User.query.filter_by(reg_no=req["reg_no"]).first()

    if u1:
        return False, {"message": "You are already registered with CSAU"}

    if len(str(req["reg_no"])) < 10:
        return False, {
            "message": "Invalid register number. Number should be atleast 10 digits"
        }

    if str(req["department"]).lower() not in departments:
        return False, {"message": "Enter a valid department name"}

    if str(req["tag"]).lower() not in tags:
        return False, {"message": "Enter a valid tag colour"}

    if str(req["domain"]).lower() not in domains:
        return False, {"message": "Enter a valid domain name"}

    if len(str(req["mobile_no"])) != 10:
        return False, {"message": "Enter a valid mobile number"}

    if len(req["email"]) == 0 or not validate_email(str(req["email"])):
        return False, {"message": "Invalid Email ID"}

    u1 = User.query.filter_by(mobile_no=req["mobile_no"]).first()

    if u1:
        return False, {"message": "This Mobile no. is already registered with CSAU"}

    u1 = User.query.filter_by(email=str(req["email"])).first()

    if u1:
        return False, {"message": "This Email id is already registered with CSAU"}

    return True, {}
