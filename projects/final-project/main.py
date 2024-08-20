from datetime import timedelta, date, time, datetime
from random import choice, sample

#--GENERAL SETTINGS--# 
Theater='Mignon'
ScreensNr=2
SeatsRows=10
SeatsCols=10

#GENERATING THE SEATS LIST OF THE SCREENS
SeatsList=[]
for Row in range(1,SeatsRows+1):
    for Col in range(1,SeatsCols+1):
        SeatsList.append('F{}-P{}'.format(Row,Col))
#

Opening=time(8,0)
PauseStart=time(13,0)
PauseEnd=time(15,0)
Closing=time(23,0)
PrjGap=timedelta(minutes=15)
PrjProgramDuration=7 #days
FilmOccurenceLimit=4
FilmDic = {# Title: duration in minutes
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

#--SUBROUTINES--#
def SetPrjProgramStart():
    """
    Function to set date and time for the first projection
    """
    CurrentTime=time(datetime.now().hour,datetime.now().minute)
    CurrentDate=date.today()
    if CurrentTime<Closing:
        if CurrentTime<Opening:
            PrjDay=CurrentDate
            NextPrjtime0=Opening
            PrjLimit0=PauseStart
        elif CurrentTime<PauseStart:
            PrjDay=CurrentDate
            NextPrjtime0=CurrentTime
            PrjLimit0=PauseStart
        else:
            PrjDay=CurrentDate
            NextPrjtime0=PauseEnd
            PrjLimit0=Closing     
    else:
        PrjDay=CurrentDate+timedelta(1)
        NextPrjtime0=Opening
        PrjLimit0=PauseStart
    return PrjDay, NextPrjtime0, PrjLimit0

def FindSuitableFilms(FilmDic,FilmOccurence,TimeLeft):
    """
    Function to find a list of films that can be projected during the remaining projection time and that occur less than FilmOccurrenceLimit in the projection program
    """
    SuitableFilm=[]
    for Film in FilmDic:
        FilmDuration=timedelta(minutes=FilmDic[Film])
        if FilmDuration+PrjGap<=TimeLeft:
            if not Film in FilmOccurence or Film in FilmOccurence and FilmOccurence[Film]['Occurence']<FilmOccurenceLimit:
                SuitableFilm.append(Film)
    return SuitableFilm

def Booking(PrjProgramDic,PrjId,SeatsNr,UserReservationDic):
    BookedSeats=sample(PrjProgramDic[PrjId]['FreeSeats'],SeatsNr)
    for Seat in BookedSeats:
        PrjProgramDic[PrjId]['FreeSeats'].remove(Seat)
    if len(UserReservationDic)>0:
        ReservationId=list(UserReservationDic.keys())[-1]+1
        UserReservationDic[ReservationId]={'PrjId':PrjId,'Seats':BookedSeats}
    else:
        UserReservationDic[1]={'PrjId':PrjId,'Seats':BookedSeats}

def CheckForOtherDate(Title,FilmOccurence,SeatsNr,PrjProgramDic):
    if FilmOccurence[Title]['Occurence']>1:
        OtherId=FilmOccurence[Title]['Id']
        OtherPrjDic={}
        for Id in OtherId:
            if SeatsNr<=len(PrjProgramDic[Id]['FreeSeats']):
                OtherPrjDic[Id]=PrjProgramDic[Id]
    
    if len(OtherPrjDic)>0:
        return OtherPrjDic

#--MAIN ROUTINES--#
def PrjProgramGen(FilmDic):
    #SET THE PROJECTION PROGRAM START
    PrjDay, NextPrjtime0, PrjLimit0=SetPrjProgramStart()
    NextPrjtime=NextPrjtime0
    PrjLimit=PrjLimit0

    #PROJECTON PROGRAM GENERATION
    FilmOccurence={} #Dictionary for accounting films occurence into the projection program
    PrjProgramDic={}
    for i in range(PrjProgramDuration):
        Screen=1
        while Screen<=ScreensNr:
            if NextPrjtime<PrjLimit:
                TimeLeft=datetime.combine(PrjDay,PrjLimit)-datetime.combine(PrjDay,NextPrjtime) #Calculating the time left for the projections (Datetime module doesn't allow to perform operation between time objects)
                SuitableFilm=FindSuitableFilms(FilmDic,FilmOccurence,TimeLeft) #Finding films that can be porjected during the TimeLeft
                
                if len(SuitableFilm)>0: #If there are suitable films, then pick up a random one, else pass to the next projection limit (PauseStart or Closing)
                    Film=choice(SuitableFilm)
                    FilmDuration=timedelta(minutes=FilmDic[Film])
                    if Film in FilmOccurence: #Updating the occurence of a certain film into the projection program
                        FilmOccurence[Film]['Occurence']+=1
                    else:
                        FilmOccurence[Film]={'Occurence':1,'Id':[]}
                    
                    #GENERATING A RANDOM NUMBER OF SEATS FOR THE PROJECTION (just to make possible simulating sold out)
                    FreeSeatsNr=choice(range(1,SeatsRows*SeatsCols+1))
                    FreeSeatsList=sample(SeatsList,FreeSeatsNr)

                    #SAVING PROJECTION INFO TO THE PROJECTION PROGRAM DICTIONRAY
                    if len(PrjProgramDic.keys())>0:
                        LastPrjId=list(PrjProgramDic.keys())[-1]
                        FilmOccurence[Film]['Id'].append(LastPrjId+1)
                        PrjProgramDic[LastPrjId+1]={'Screen':Screen,'DateTime':datetime.combine(PrjDay,NextPrjtime),'Title':Film,'FreeSeats':FreeSeatsList}
                    else:
                        FilmOccurence[Film]['Id'].append(1)
                        PrjProgramDic[1]={'Screen':Screen,'DateTime':datetime.combine(PrjDay,NextPrjtime),'Title':Film,'FreeSeats':FreeSeatsList}

                    #SETTING THE TIME OF NEXT PROJECTION
                    NextPrjtime=datetime.combine(PrjDay,NextPrjtime)+FilmDuration+PrjGap #Datetime module doesn't allow to sum timedelta to time objects
                    NextPrjtime=time(NextPrjtime.hour,NextPrjtime.minute)
                else:
                    #SETTING A NEW PROJECTION LIMIT OR PASSING TO THE NEXT SCREEN/DAY (there is not enough time to project another film)
                    if PrjLimit<Closing: #New projection limit (Closing)
                        PrjLimit=Closing
                        NextPrjtime=PauseEnd
                    else: 
                        Screen+=1
                        if i<2: #If writing the projection program for the first day, then set the first projection time for the new screen to the same of the previous screen
                            NextPrjtime=NextPrjtime0
                            PrjLimit=PrjLimit0
                        else:
                            NextPrjtime=Opening
                            PrjLimit=PauseStart
            else:
                #SETTING A NEW PROJECTION LIMIT OR PASSING TO THE NEXT SCREEN/DAY (next projection time overcome the actual projection limit)
                if PrjLimit<Closing: #New projection limit (Closing)
                    PrjLimit=Closing
                    NextPrjtime=PauseEnd
                else:
                    Screen+=1
                    if i<2: #If writing the projection program for the first day, then set the first projection time for the new screen to the same of the previous screen
                        NextPrjtime=NextPrjtime0
                        PrjLimit=PrjLimit0
                    else:
                        NextPrjtime=Opening
                        PrjLimit=PauseStart
        
        #NEW PROJECTION DAY
        PrjDay=PrjDay+timedelta(1)
        NextPrjtime=Opening
        PrjLimit=PauseStart
    return PrjProgramDic, FilmOccurence

def PrintPrjProgram(PrjProgramDic):
    #SETTING PADDING VALUE FOR THE PROJECTION PROGRAM INFO
    TitleMaxLen=0
    for Id in PrjProgramDic:
        Title=PrjProgramDic[Id]['Title']
        if len(Title)>TitleMaxLen:
            TitleMaxLen=len(Title)
    TitlePadding='{:<'+str(TitleMaxLen)+'}'

    DurationMaxLen=0
    IdMaxLen=0
    for Id in PrjProgramDic:
        Title=PrjProgramDic[Id]['Title']
        Duration=str(FilmDic[Title])
        if len(Duration)>DurationMaxLen:
            DurationMaxLen=len(Duration)
        Id=str(Id)
        if len(Id)>IdMaxLen:
            IdMaxLen=len(Id)
    DurationPadding='{:<'+str(DurationMaxLen)+'}'
    IdPadding='{:<'+str(IdMaxLen)+'}'

    #WRITING PROJECTION PROGRAM STRING
    PrjProgramStart=PrjProgramDic[1]['DateTime'].date()
    PrjProgramStr=''
    for i in range(PrjProgramDuration):
        PrjDate=PrjProgramStart+timedelta(i)
        PrjProgramStr=PrjProgramStr+PrjDate.strftime("%a %d/%m/%y").upper()+'\n'
        for Screen in range(1,ScreensNr+1):
            PrjProgramStr=PrjProgramStr+'SCREEN {}'.format(Screen)+'\n'
            for Id in PrjProgramDic:
                if PrjProgramDic[Id]['DateTime'].date()==PrjDate and PrjProgramDic[Id]['Screen']==Screen:
                    Time=PrjProgramDic[Id]['DateTime'].time().strftime("%H:%M")
                    Title=PrjProgramDic[Id]['Title']
                    Duration=FilmDic[Title]
                    FreeSeats=len(PrjProgramDic[Id]['FreeSeats'])
                    InfoStr='Prj ID: '+IdPadding+' - Time: {} - Title: '+TitlePadding+' - Duration: '+DurationPadding+' min - Free seats: {}\n'
                    PrjProgramStr=PrjProgramStr+InfoStr.format(Id,Time,Title,Duration,FreeSeats)
            PrjProgramStr=PrjProgramStr+'-'*20+'\n'
        PrjProgramStr=PrjProgramStr+'-'*20+'\n\n'
    print(PrjProgramStr)

def PrintPrjAlternative(PrjProgramDic):
    #SETTING PADDING VALUE FOR THE PROJECTION PROGRAM INFO
    TitleMaxLen=0
    for Id in PrjProgramDic:
        Title=PrjProgramDic[Id]['Title']
        if len(Title)>TitleMaxLen:
            TitleMaxLen=len(Title)
    TitlePadding='{:<'+str(TitleMaxLen)+'}'

    DurationMaxLen=0
    IdMaxLen=0
    for Id in PrjProgramDic:
        Title=PrjProgramDic[Id]['Title']
        Duration=str(FilmDic[Title])
        if len(Duration)>DurationMaxLen:
            DurationMaxLen=len(Duration)
        Id=str(Id)
        if len(Id)>IdMaxLen:
            IdMaxLen=len(Id)
    DurationPadding='{:<'+str(DurationMaxLen)+'}'
    IdPadding='{:<'+str(IdMaxLen)+'}'

    #WRITING PROJECTION PROGRAM STRING
    PrjProgramStr=''
    for Id in PrjProgramDic:
        PrjDate=PrjProgramDic[Id]['DateTime'].date()
        PrjProgramStr=PrjProgramStr+PrjDate.strftime("%a %d/%m/%y").upper()+'\n'
        Screen=PrjProgramDic[Id]['Screen']
        PrjProgramStr=PrjProgramStr+'SCREEN {}'.format(Screen)+'\n'
        Time=PrjProgramDic[Id]['DateTime'].time().strftime("%H:%M")
        Title=PrjProgramDic[Id]['Title']
        Duration=FilmDic[Title]
        FreeSeats=len(PrjProgramDic[Id]['FreeSeats'])
        InfoStr='Prj ID: '+IdPadding+' - Time: {} - Title: '+TitlePadding+' - Duration: '+DurationPadding+' min - Free seats: {}\n'
        PrjProgramStr=PrjProgramStr+InfoStr.format(Id,Time,Title,Duration,FreeSeats)
        PrjProgramStr=PrjProgramStr+'-'*20+'\n'
    print(PrjProgramStr)

def PrintUserReservation(PrjProgramDic,UserReservationDic,ReservationId=None):
    if ReservationId==None:
        UserReservationStr=''
        for Id in UserReservationDic:
            PrjId=UserReservationDic[Id]['PrjId']

            SeatsStr=''
            for Seat in UserReservationDic[Id]['Seats']:
                SeatsStr=SeatsStr+Seat+' - '
            SeatsStr=SeatsStr.rstrip(' - ')

            Title=PrjProgramDic[PrjId]['Title']
            Duration=FilmDic[Title]
            DateStr=PrjProgramDic[PrjId]['DateTime'].date().strftime("%a %d/%m/%y")
            TimeStr=PrjProgramDic[PrjId]['DateTime'].time().strftime("%H:%M")
            Screen=PrjProgramDic[PrjId]['Screen']
            
            UserReservationStr=UserReservationStr+'RESERVATION ID: {}\n{} - {}\'\n{} - {} - Screen {}\nBooked seats: {}\n'.format(Id,Title,Duration,DateStr,TimeStr,Screen,SeatsStr)
            UserReservationStr=UserReservationStr+'-'*20+'\n\n'    
    else:
        UserReservationStr=''
        PrjId=UserReservationDic[ReservationId]['PrjId']

        SeatsStr=''
        for Seat in UserReservationDic[ReservationId]['Seats']:
            SeatsStr=SeatsStr+Seat+' - '
        SeatsStr=SeatsStr.rstrip(' - ')

        Title=PrjProgramDic[PrjId]['Title']
        Duration=FilmDic[Title]
        DateStr=PrjProgramDic[PrjId]['DateTime'].date().strftime("%a %d/%m/%y")
        TimeStr=PrjProgramDic[PrjId]['DateTime'].time().strftime("%H:%M")
        Screen=PrjProgramDic[PrjId]['Screen']
        
        UserReservationStr=UserReservationStr+'RESERVATION ID: {}\n{} - {}\'\n{} - {} - Screen {}\nBooked seats: {}\n'.format(ReservationId,Title,Duration,DateStr,TimeStr,Screen,SeatsStr)
        UserReservationStr=UserReservationStr+'-'*20+'\n\n' 
    print(UserReservationStr)

def DeleteReservation(UserReservationDic,PrjProgramDic,ReservationId):
    PrjId=UserReservationDic[ReservationId]['PrjId']
    BookedSeats=UserReservationDic[ReservationId]['Seats']
    del(UserReservationDic[ReservationId])
    PrjProgramDic[PrjId]['FreeSeats'].append(BookedSeats)
    print('Reservation deleted!')


def main():
    #GENERAZIONE DICTIONARY DELLE PRENOTAZIONI EFFETTUATE DALL'UTENTE
    UserReservationDic={}

    #GENERAZIONE PROGRAMMA PROIEZIONI
    PrjProgramDic,FilmOccurence=PrjProgramGen(FilmDic)
    PrjProgramStart=PrjProgramDic[1]['DateTime'].date()
    PrjProgramStartStr=PrjProgramDic[1]['DateTime'].date().strftime("%a %d/%d/%y")
    PrjProgramEnd=(PrjProgramStart+timedelta(PrjProgramDuration)).strftime("%a %d/%d/%y")

    #CONSOLE DI CONTROLLO
    operation=''
    while operation!=0:
        #ASKING FOR THE OPERATION TO PERFORM
        if len(UserReservationDic)==0:
            print('You can perform these operations:\n- book a some seats for a projection [1]\n- exit [0]')
            operation=input('Please, enter the number of the operation you want to perform:')
            while not operation in ['0','1']:
                operation=input('Wrong input, please retry:')
        else:
            print('You can perform these operations:\n- book a some seats for a projection [1]\n- modify an existing reservation [2]\n- delete an existing reservation [3]\n- exit [0]')
            operation=input('Please, enter the number of the operation you want to perform:')
            while not operation in ['0','1','2','3']:
                operation=input('Wrong input, please retry:')
        operation=int(operation)
        #PERFORMING OPERATION
        if operation==1:
            print('{} THEATER\nPROJECTION PROGRAM FROM {} TO {}\n\n'.format(Theater.upper(),PrjProgramStartStr,PrjProgramEnd))
            PrintPrjProgram(PrjProgramDic)
            #ASKING PROJECTION ID AND SEATS NUMBER TO BOOK
            PrjId=input('Please, enter the projection id you are interested in:')
            while not PrjId.isdigit():
                PrjId=input('Only numeric values, retry:')
            PrjId=int(PrjId)
            while not PrjId in list(PrjProgramDic.keys()):
                PrjId=input('The id you entered is wrong. Please, retry:')
            
            SeatsNr=input('Please, enter the number of seats to book:')
            while not SeatsNr.isdigit():
                SeatsNr=input('Only numeric values. Please, retry:')
            SeatsNr=int(SeatsNr)

            #BOOKING
            if SeatsNr<=len(PrjProgramDic[PrjId]['FreeSeats']):
                Booking(PrjProgramDic,PrjId,SeatsNr,UserReservationDic)
                ReservationId=list(UserReservationDic.keys())[-1]
                PrintUserReservation(PrjProgramDic,UserReservationDic,ReservationId)
            else:
                print('There are not enough free seats for the projection id selected, you can:\n- Main menu [1]\n- Search for the same film in other dates [2]\n- Exit [0]')
                Operation=input('What you want to do:\n')
                while not Operation in ['0','1','2']:
                    Operation=input('Wrong input, retry:')

                if Operation=='2':
                    Title=PrjProgramDic[PrjId]['Title']
                    OtherPrjDic=CheckForOtherDate(Title,FilmOccurence,SeatsNr,PrjProgramDic)
                    if OtherPrjDic!=None:
                        print('Here\'s some other dates for the film you choose!')
                        PrintPrjAlternative(OtherPrjDic)
                        PrjId=input('If you want to book for one of these dates, input the relevant ID or, if you want to exit, enter 0:')
                        while not PrjId.isdigit():
                            PrjId=input('Only numeric values, retry:')
                            PrjId=int(PrjId)
                        if PrjId!=0:
                            while not PrjId in list(PrjProgramDic.keys()):
                                PrjId=input('The id you entered is wrong. Please, retry:')
                                PrjId=int(PrjId)
                            Booking(PrjProgramDic,PrjId,SeatsNr,UserReservationDic)
                            ReservationId=list(UserReservationDic.keys()[-1])
                            PrintUserReservation(PrjProgramDic,UserReservationDic,ReservationId)
                    else:
                        print('Sorry, no alternatives dates for the film you choose.')
        elif operation==2:
            #MODIFICA PRENOTAZIONE
            PrintUserReservation(PrjProgramDic,UserReservationDic)
        elif operation==3:
            PrintUserReservation(PrjProgramDic,UserReservationDic)
            ReservationId=input('Please, enter the reservation id you want to delete:')
            while not ReservationId.isdigit():
                ReservationId=input('Only numeric values, retry:')
            ReservationId=int(ReservationId)
            while not ReservationId in list(PrjProgramDic.keys()):
                ReservationId=input('The id you entered is wrong. Please, retry:')
            DeleteReservation(UserReservationDic,PrjProgramDic,ReservationId)

if __name__=='__main__':
    main()