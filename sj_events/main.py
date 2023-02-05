import constants
from clients.seat_junky import SeatJunky

if __name__ == '__main__':
    seat_junky = SeatJunky(username="", password="", region=constants.Regions.PHOENIX.value)
    seat_junky.do_user_login()


