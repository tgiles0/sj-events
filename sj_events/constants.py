from enum import Enum

SJ_LOGIN_PAGE = "https://www.seatjunky.com/{}/login2.php"
SJ_USER_FIELD = "username"
SJ_PASSWORD_FIELD = "password"
SJ_LOGIN_BUTTON = "submit"
SJ_LOGIN_ERROR = "Invalid username and/or password."
SJ_LOGIN_ERROR_CLASS = "alert-danger"


class Regions(Enum):
    PHOENIX = "phx"
    LOS_ANGELES = "la"
    SAN_DIEGO = "sandiego"
    DALLAS = "dallas"
    HOUSTON = "houston"
