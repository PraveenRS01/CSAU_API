from csau import db, ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    reg_no = db.Column(db.BigInteger, unique=True, nullable=False)
    department = db.Column(db.String(30), nullable=False)
    tag = db.Column(db.String(10), nullable=False)
    domain = db.Column(db.String(30), nullable=False)
    mobile_no = db.Column(db.BigInteger, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(
        self, username, reg_no, department, tag, domain, mobile_no, email
    ) -> None:
        self.username = username
        self.reg_no = reg_no
        self.department = department
        self.tag = tag
        self.domain = domain
        self.mobile_no = mobile_no
        self.email = email

    def __repr__(self) -> str:
        return "Name - {} Register No. - {} Department - {} Email - {}".format(
            self.username, self.reg_no, self.department, self.email
        )


class UserSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "username",
            "reg_no",
            "department",
            "tag",
            "domain",
            "mobile_no",
            "email",
        )


user_schema = UserSchema()
users_schema = UserSchema(many=True)
