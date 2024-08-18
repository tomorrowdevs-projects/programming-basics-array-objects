from datetime import timedelta, date, time, datetime
from random import choice, random, sample
from copy import deepcopy
from math import floor

#General data
theater_name='Mignon'
theater_screens=2
seats_rows=10
seats_cols=10
screen_daily_projections=4
projections_gap=15 #minutes
opening_hour=8
projection_program_duration=7 #days
days_of_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
films_dic = {# Title: duration in minutes
    "The Birth of a Nation": 195,
    "Metropolis": 153,
    "Gone with the Wind": 238,
    "Casablanca": 102,
    "Citizen Kane": 119,
    "The Wizard of Oz": 102,
    "Sunset Boulevard": 110,
    "Singin' in the Rain": 103,
    "12 Angry Men": 96,
    "Ben-Hur": 212,
    "Lawrence of Arabia": 227,
    "The Godfather": 175,
    "The Godfather Part II": 202,
    "Jaws": 124,
    "Star Wars: Episode IV - A New Hope": 121,
    "Star Wars: Episode V - The Empire Strikes Back": 124,
    "Star Wars: Episode VI - Return of the Jedi": 131,
    "E.T. the Extra-Terrestrial": 115,
    "Blade Runner": 117,
    "Back to the Future": 116,
    "The Terminator": 107,
    "Jurassic Park": 127,
    "Pulp Fiction": 154,
    "The Shawshank Redemption": 142,
    "Titanic": 195,
    "The Matrix": 136,
    "Gladiator": 155,
    "The Lord of the Rings: The Fellowship of the Ring": 178,
    "The Lord of the Rings: The Two Towers": 179,
    "The Lord of the Rings: The Return of the King": 201,
    "The Dark Knight": 152,
    "Avatar": 162,
    "Pirates of the Caribbean: The Curse of the Black Pearl": 143,
    "The Matrix Reloaded": 138,
    "The Matrix Revolutions": 129,
    "Inception": 148,
    "The Dark Knight Rises": 164,
    "Interstellar": 169,
    "The Avengers": 143,
    "Avengers: Age of Ultron": 141,
    "Avengers: Infinity War": 149,
    "Avengers: Endgame": 181,
    "Frozen": 102,
    "Frozen II": 103,
    "Black Panther": 134,
    "Guardians of the Galaxy": 121,
    "Guardians of the Galaxy Vol. 2": 136,
    "Star Wars: The Force Awakens": 138,
    "Star Wars: The Last Jedi": 152,
    "Star Wars: The Rise of Skywalker": 142,
    "Tenet": 150,
    "Dune": 155,
    "No Time to Die": 163,
    "The Batman": 176,
    "Spider-Man: No Way Home": 148,
    "Black Widow": 134,
    "Wonder Woman 1984": 151,
    "Soul": 100,
    "Encanto": 102,
    "Avatar: The Way of Water": 192,
    "Top Gun: Maverick": 131,
    "The Suicide Squad": 132,
    "Eternals": 156,
    "Shang-Chi and the Legend of the Ten Rings": 132,
    "Doctor Strange in the Multiverse of Madness": 126,
    "Thor: Love and Thunder": 119,
    "Black Panther: Wakanda Forever": 161,
    "Guardians of the Galaxy Vol. 3": 149,
    "Mission: Impossible - Dead Reckoning Part One": 163,
    "Jurassic World: Dominion": 146
}

def FirstWeekDay():
    #Computes the first day of the current week
    today=date.today()
    weekday=today.isocalendar().weekday
    first_date_week=today-timedelta(days=weekday-1)
    return first_date_week

def ProjectionProgram(film_dic,projection_program_duration,projections_gap):
    #Generates a projection program for the current week
    film_list=list(film_dic.keys())
    projection_program_dic={}
    projection_day=FirstWeekDay()
    projection_time=time(hour=opening_hour)
    for n in range(projection_program_duration):
        projection_program_dic[projection_day]={}
        for i in range(theater_screens):
            screen_name='Screen {}'.format(i+1)
            projection_program_dic[projection_day][screen_name]={}
            screen_daily_dic=projection_program_dic[projection_day][screen_name]
            for j in range(screen_daily_projections):
                rand_film=choice(film_list)
                film_list.remove(rand_film)
                screen_daily_dic[projection_time]=rand_film
                if j<screen_daily_projections-1:
                    next_projection_hour=projection_time.hour+film_dic[rand_film]//60+(film_dic[rand_film]%60+projections_gap)//60
                    next_projection_minute=(film_dic[rand_film]%60+projections_gap)%60
                    projection_time=time(next_projection_hour,next_projection_minute)
            projection_time=time(hour=opening_hour)
        projection_day=projection_day+timedelta(days=1)
        projection_time=time(hour=opening_hour)
    return projection_program_dic #={date:{screen:{time:{title}}}}

def PrintProgram(projection_program_dic):
    daily_program_str=''
    for prj_date in projection_program_dic:
        daily_program_str=daily_program_str+prj_date.strftime('%A %d %B %Y')
        for screen in projection_program_dic[prj_date]:
            daily_program_str=daily_program_str+'\n{}\n'.format(screen.upper())
            for prj_time in projection_program_dic[prj_date][screen]:
                projection_time_str=prj_time.strftime('%H:%M')
                film_title=projection_program_dic[prj_date][screen][prj_time]
                film_duration=films_dic[film_title]
                daily_program_str=daily_program_str+'{} - {} - {}\'/ '.format(projection_time_str,film_title,film_duration)
            daily_program_str=daily_program_str.rstrip(' / ')
        daily_program_str=daily_program_str+'\n\n'
    print(daily_program_str)

def FreeSeatsSimulator(seats_rows,seats_cols,projection_program_dic):
    screen_seats=[]
    for row in range(1,seats_rows+1):
        for col in range(1,seats_cols+1):
            screen_seats.append('F{}-P{}'.format(row,col))

    screen_seats_nr=seats_cols*seats_rows
    free_seats_dic=deepcopy(projection_program_dic)
    for prj_date in free_seats_dic:
        for screen in free_seats_dic[prj_date]:
            for prj_time in free_seats_dic[prj_date][screen]:
                reservations_nr=floor(random()*screen_seats_nr)
                free_seats_dic[prj_date][screen][prj_time]=sample(screen_seats,screen_seats_nr-reservations_nr)
    return free_seats_dic

def SeatsAvailability(free_seats_dic,datetime_str,screen_nr,booking_nr):
    prj_datetime=datetime.fromisoformat(datetime_str)
    prj_date=date(prj_datetime.year,prj_datetime.month,prj_datetime.day)
    prj_time=time(prj_datetime.hour,prj_datetime.minute)
    available_seats=free_seats_dic[prj_date]['Screen {}'.format(screen_nr)][prj_time]
    if len(available_seats)>=booking_nr:
        return True
    else:
        return False

def MakeReservation(projection_program_dic,free_seats_dic,datetime_str,screen_nr,booking_nr,reservations_dic):
    if len(list(reservations_dic.keys()))>0:
        reservation_id=list(reservations_dic.keys())[-1]+1
    else:
        reservation_id=1
    prj_datetime=datetime.fromisoformat(datetime_str)
    prj_date=date(prj_datetime.year,prj_datetime.month,prj_datetime.day)
    prj_time=time(prj_datetime.hour,prj_datetime.minute)
    available_seats=free_seats_dic[prj_date]['Screen {}'.format(screen_nr)][prj_time]
    booked_seats=sample(available_seats,booking_nr)
    booked_seats_str=''
    for seat in booked_seats:
        free_seats_dic[prj_date]['Screen {}'.format(screen_nr)][prj_time].remove(seat)
        booked_seats_str=booked_seats_str+seat+', '
    booked_seats_str=booked_seats_str.rstrip(', ')
    film_title=projection_program_dic[prj_date]['Screen {}'.format(screen_nr)][prj_time]
    reservation_details_str='Reservation ID: {}\nFilm: {}\nDate: {}\nTime: {}\nScreen: {}\nSeats: {}'.format(reservation_id,film_title,prj_date,prj_time,screen_nr,booked_seats_str)
    reservations_dic[reservation_id]={'Film':projection_program_dic[prj_date]['Screen {}'.format(screen_nr)][prj_time],'Datetime':prj_datetime,'Screen':screen_nr,'Seats:':booked_seats}
    return reservation_details_str

def PrintReservation(reservations_dic):
    reservation_details_str=''
    for reservation in reservations_dic:
        film=reservations_dic[reservation]['Film']
        prj_datetime=reservations_dic[reservation]['Datetime']
        date_str=date(prj_datetime.year,prj_datetime.month,prj_datetime.day).strftime('%A %d %B %Y')
        time_str=time(prj_datetime.hour,prj_datetime.minute).strftime('%H:%M')
        screen=reservations_dic[reservation]['Screen']
        seats=reservations_dic[reservation]['Seats']
        reservation_details_str=reservation_details_str+'Reservation ID: {}\nFilm: {}\nDate: {}\nTime: {}\nScreen: {}\nSeats: {}\n'.format(reservation,film,date_str,time_str,screen,seats)
    print(reservation_details_str)

def DeleteReservation(reservations_dic,reservation_id,free_seats_dic):
    prj_datetime=reservations_dic[reservation_id]['Datetime']
    prj_date=date(prj_datetime.year,prj_datetime.month,prj_datetime.day)
    prj_time=time(prj_datetime.hour,prj_datetime.minute)
    screen=reservations_dic[reservation_id]['Screen']
    seats=reservations_dic[reservation_id]['Seats']
    del reservations_dic[reservation_id]
    for i in seats:
        free_seats_dic[prj_date]['Screen {}'.format(screen)][prj_time].append(i)

def ChangeFilm(projection_program_dic,reservations_dic,reservation_id,free_seats_dic,datetime_str,new_screen):
    prj_datetime=reservations_dic[reservation_id]['Datetime']
    prj_date=date(prj_datetime.year,prj_datetime.month,prj_datetime.day)
    prj_time=time(prj_datetime.hour,prj_datetime.minute)
    new_prj_datetime=datetime.fromisoformat(datetime_str)
    new_prj_date=date(prj_datetime.year,prj_datetime.month,prj_datetime.day)
    new_prj_time=time(prj_datetime.hour,prj_datetime.minute)
    screen=reservations_dic[reservation_id]['Screen']
    seats=reservations_dic[reservation_id]['Seats']
    film=projection_program_dic[new_prj_date]['Screen {}'.forma(screen)][new_prj_time]
    reservations_dic[reservation_id]['Film']=film
    reservations_dic[reservation_id]['Datetime']=new_prj_datetime
    reservations_dic[reservation_id]['Screen']=new_screen
    available_seats=free_seats_dic[new_prj_date]['Screen {}'.forma(new_screen)][new_prj_time]
    booked_seats=sample(available_seats,len(seats))
    for i,j in zip(seats,booked_seats):
        free_seats_dic[prj_date]['Screen {}'.format(screen)][prj_time].append(i)
        free_seats_dic[new_prj_date]['Screen {}'.format(new_screen)][new_prj_time].remove(j)
    booked_seats_str=''
    for seat in booked_seats:
        booked_seats_str=booked_seats_str+seat+', '
    booked_seats_str=booked_seats_str.rstrip(', ')
    reservation_details_str='Reservation ID: {}\nFilm: {}\nDate: {}\nTime: {}\nScreen: {}\nSeats: {}'.format(reservation_id,film,new_prj_date,new_prj_time,new_screen,booked_seats_str)
    print(reservation_details_str)

def ChangeSeats(reservations_dic,reservation_id,free_seats_dic,booking_nr):
    prj_datetime=reservations_dic[reservation_id]['Datetime']
    prj_date=date(prj_datetime.year,prj_datetime.month,prj_datetime.day)
    prj_time=time(prj_datetime.hour,prj_datetime.minute)
    screen=reservations_dic[reservation_id]['Screen']
    seats=reservations_dic[reservation_id]['Seats']
    film=projection_program_dic[new_prj_date]['Screen {}'.forma(screen)][new_prj_time]
    reservations_dic[reservation_id]['Film']=film
    reservations_dic[reservation_id]['Datetime']=new_prj_datetime
    reservations_dic[reservation_id]['Screen']=new_screen
    available_seats=free_seats_dic[new_prj_date]['Screen {}'.forma(new_screen)][new_prj_time]
    booked_seats=sample(available_seats,len(seats))
    for i,j in zip(seats,booked_seats):
        free_seats_dic[prj_date]['Screen {}'.format(screen)][prj_time].append(i)
        free_seats_dic[new_prj_date]['Screen {}'.format(new_screen)][new_prj_time].remove(j)
    booked_seats_str=''
    for seat in booked_seats:
        booked_seats_str=booked_seats_str+seat+', '
    booked_seats_str=booked_seats_str.rstrip(', ')
    reservation_details_str='Reservation ID: {}\nFilm: {}\nDate: {}\nTime: {}\nScreen: {}\nSeats: {}'.format(reservation_id,film,new_prj_date,new_prj_time,new_screen,booked_seats_str)
    print(reservation_details_str)

def main():
    projection_program_dic=ProjectionProgram(films_dic,projection_program_duration,projections_gap)
    free_seats_dic=FreeSeatsSimulator(seats_rows,seats_cols,projection_program_dic)
    reservations_dic={} #dic={datetime:{film: {screen: seats}}}
    operation=''
    while operation!='0':
        print('Wellcome to {} booking app!'.format(theater_name))
        operation=input('If you want to book some seats for a projection press 1, if you want to modify a reservation press 2, if you want to exit press 0: ')
        if operation=='1':
            print('Here\'s the projection program for this week:')
            PrintProgram(projection_program_dic)
            datetime_str=input('Enter the date and time of the projection (yyyy-mm-dd hh:mm):')
            screen_nr=int(input('Enter the screen number:'))
            booking_nr=int(input('Enter the number of seats that you want to book:'))
            if SeatsAvailability(free_seats_dic,datetime_str,screen_nr,booking_nr):
                reservation_details_str=MakeReservation(projection_program_dic,free_seats_dic,datetime_str,screen_nr,booking_nr,reservations_dic)
                print('Here\'s your reservation details: {}'.format(reservation_details_str))
            else:
                print('The projection you selected is sold out. Please, select another projection or quit')
        elif operation=='2':
            print('Here\'s the list of your reservations:')
            PrintReservation(reservations_dic)
            operation=input('If you want to delete a reservation press 1, if you want to modify film press 2, if you want to change the number of seats, press 3: ')
            if operation=='1':
                reservation_id=input('Please, input the id of the reservation that you want to delete: ')
                DeleteReservation(reservations_dic,reservation_id,free_seats_dic)
            elif operation=='2':
                while operation!='0':
                    reservation_id=input('Please, input the id of the reservation that you want to modify: ')
                    datetime_str=input('Enter the date and time of the projection (yyyy-mm-dd hh:mm):')
                    if SeatsAvailability(free_seats_dic,datetime_str,screen_nr,booking_nr):
                        ChangeFilm(projection_program_dic,reservations_dic,reservation_id,free_seats_dic)
                    else:
                        print('The projection you selected is sold out. Please, select another projection or quit by pressing 0')
                        operation=input('Please, input 2 if you want to retry, or 0 to exit: ')
                operation=''
            elif operation=='3':
                while operation!='0':
                    reservation_id=input('Please, input the id of the reservation that you want to modify: ')
                    datetime_str=input('Enter the date and time of the projection (yyyy-mm-dd hh:mm):')
                    booking_nr=int(input('Enter the number of seats that you want to add (positive) or delete (negative):'))
                    if SeatsAvailability(free_seats_dic,datetime_str,screen_nr,booking_nr):
                        ChangeFilm(projection_program_dic,reservations_dic,reservation_id,free_seats_dic)
                    else:
                        print('The projection you selected is sold out. Please, select another projection or quit by pressing 0')
                        operation=input('Please, input 3 if you want to retry, or 0 to exit: ')
                operation=''

                

if __name__=='__main__':
    main()