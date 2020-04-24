def main():
    while True:
        try:
            school_number = int(input("\nEnter the number of what school you are at: "))
            break
        except ValueError:
            print("That was not a valid number.  Please try again...\n")

    if school_number < 5:
        current_day = input("Please enter what day it is (mon/tue etc): ".lower())
    else:
        current_day = None

    possible_days = ("mon", "tue", "wed", "thur", "fri", "sat")
    office_day = False
    cost, leave_time_multiplier, start_time, finish_time, school_name, day = 0, 0, 0, 0, 0, 0,

    if school_number == 1:
        school_name = "Chiryu Nishi"
        cost = (750 * 2)
        leave_time_multiplier = 1.15
        if current_day == "mon":
            start_time = 15.45
            finish_time = 20.30
        elif current_day == "tue":
            office_day = True
        elif current_day == "wed":
            start_time = 17.00
            finish_time = 20.30
        elif current_day == "thur":
            start_time = 15.45
            finish_time = 20.30
        elif current_day == "fri":
            start_time = 17.00
            finish_time = 20.30

    if school_number == 2:
        school_name = "Nishio Nishi"
        cost = (950 * 2)
        leave_time_multiplier = 1.25
        if current_day == "mon":
            start_time = 17.00
            finish_time = 20.30
        elif current_day == "tue":
            start_time = 17.00
            finish_time = 20.30
        elif current_day == "wed":
            start_time = 15.45
            finish_time = 21.45
        elif current_day == "thur":
            start_time = 17.00
            finish_time = 20.30
        elif current_day == "fri":
            start_time = 17.00
            finish_time = 21.45
        elif current_day == "sat":
            start_time = 11.15
            finish_time = 15.30

    if school_number == 3:
        school_name = "Tahara"
        cost = (700 * 2)
        leave_time_multiplier = 1.15
        if current_day == "mon":
            start_time = 17.00
            finish_time = 21.45
        elif current_day == "tue":
            start_time = 15.45
            finish_time = 20.30
        elif current_day == "wed":
            start_time = 15.45
            finish_time = 20.30
        elif current_day == "thur":
            start_time = 15.45
            finish_time = 20.30
        elif current_day == "fri":
            start_time = 15.45
            finish_time = 20.30
        elif current_day == "sat":
            start_time = 17.00
            finish_time = 20.30

    # TODO fix monday to friday times when i have the schedule
    if school_number == 4:
        school_name = "Nakagawa Takabata"
        cost = (1380 * 2)
        leave_time_multiplier = 1.75
        if current_day == "mon":
            start_time = 17.00
            finish_time = 20.30
        elif current_day == "tue":
            start_time = 17.00
            finish_time = 20.30
        elif current_day == "wed":
            start_time = 15.45
            finish_time = 21.45
        elif current_day == "thur":
            start_time = 17.00
            finish_time = 20.30
        elif current_day == "fri":
            start_time = 17.00
            finish_time = 21.45
        elif current_day == "sat":
            start_time = 17.00
            finish_time = 21.45

    if school_number == 5:
        school_name = "Okazaki Chou"
        cost = (1380 * 2)
        leave_time_multiplier = 0.75
        start_time = 09.50
        finish_time = 12.00

    # renames the days
    if current_day == "mon":
        day = "Monday"
    elif current_day == "tue":
        day = "Tuesday"
    elif current_day == "wed":
        day = "Wednesday"
    elif current_day == "thur":
        day = "Thursday"
    elif current_day == "fri":
        day = "Friday"
    elif current_day == "sat":
        day = "Saturday"

    if current_day in possible_days and school_number <= 5 and not office_day:
        leave_time = start_time - leave_time_multiplier - 1  # todo sort time from decimal
        print("\nOn {} at {}: It will cost {} return. You start at {:.02f} and finish at {:.02f} You should leave"
              " around {:.02f}".format(day, school_name, cost, start_time, finish_time, leave_time))
    elif current_day in possible_days and school_number <= 4 and office_day:
        print("\nYou have an office day. Check your emails and complete TTOSM before 11.20")
    elif current_day not in possible_days and school_number <= 4:
        print("\nThat is not a valid work day.")
    elif current_day in possible_days and school_number > 4:
        print("\nThat is not a valid school number.")
    elif school_number == 5:
        print("\nThe staff meeting at {} will cost {}, return. It starts at {:.02f} and finishes at {:.02f}."
              " You should leave around {:.02f}".format(school_name, cost, start_time, finish_time,
                                                        (start_time - leave_time_multiplier)))


print("\nWelcome to my commuting cost calculator\n\n\t 1. Chiryu Nishi\n\t 2. Nishio Nishi\n\t 3. Tahara\n\t 4. "
      "Nakagawa Takabata \n\t 5. Staff Meeting")

while True:
    main()
    retry = input("\nPress q to quit or any other key to check another day:  ".lower())
    if retry == "q":
        break
