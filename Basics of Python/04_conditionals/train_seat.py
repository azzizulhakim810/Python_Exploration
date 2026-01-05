seat_type = input("Enter seat type (AC/Sleeper/Luxury/General): ").lower()

match seat_type:
  case "ac":
    print(f"AC - Air Conditioned")
  case "sleeper":
    print(f"Sleeper - Ac with Bed")
  case "luxury":
    print(f"Luxury - Premium Seats with meals")
  case "general":
    print(f"General - Cheapest Option")
  case _:
    print(f"Invalid Seat Types")