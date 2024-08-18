from datetime import timedelta, date, time, datetime
from random import choice, random, sample
from copy import deepcopy
from math import floor

#General data
Theater='Mignon'
ScreensNr=2
SeatsRows=10
SeatsCols=10

SeatsList=[]
for Row in range(1,SeatsRows+1):
    for Col in range(1,SeatsCols+1):
        SeatsList.append('F{}-P{}'.format(Row,Col))

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

def PrjProgramGen(FilmDic):
    #--SET THE PROJECTION PROGRAM START--#
    CurrentTime=time(datetime.now().hour,datetime.now().minute)
    CurrentDate=date.today()
    if CurrentTime<Closing:
        if CurrentTime<Opening:
            PrjDay=CurrentDate
            NextPrjtime=Opening
            PrjLimit=PauseStart
        elif CurrentTime<PauseStart:
            PrjDay=CurrentDate
            NextPrjtime=CurrentTime
            PrjLimit=PauseStart
        else:
            PrjDay=CurrentDate
            NextPrjtime=PauseEnd
            PrjLimit=Closing     
    else:
        PrjDay=CurrentDate+timedelta(1)
        NextPrjtime=Opening
        PrjLimit=PauseStart
    
    #--PROJECTON PROGRAM GENERATION--#
    FilmOccurence={} #Dictionary for accounting films occurance into the projection program
    PrjProgramDic={}
    for i in range(PrjProgramDuration):
        Screen=1
        while Screen<=ScreensNr:
            if NextPrjtime<PrjLimit:
                TimeLeft=datetime.combine(PrjDay,PrjLimit)-datetime.combine(PrjDay,NextPrjtime) #Datetime module doesn't allow to perform operation between time objects
                
                #Choosing a random film among film with duration minor than the time left and already insert less then FilmOccurenceLimit times
                SuitableFilm=[]
                for Film in FilmDic:
                    FilmDuration=timedelta(minutes=FilmDic[Film])
                    if FilmDuration+PrjGap<=TimeLeft:
                        if not Film in FilmOccurence or Film in FilmOccurence and FilmOccurence[Film]<FilmOccurenceLimit:
                            SuitableFilm.append(Film)
                
                if len(SuitableFilm)>0:
                    Film=choice(SuitableFilm)
                    FilmDuration=timedelta(minutes=FilmDic[Film])
                    if Film in FilmOccurence:
                        FilmOccurence[Film]+=1
                    else:
                        FilmOccurence[Film]=1
                    
                    #Generating a random number of free seats#
                    FreeSeatsNr=choice(range(1,SeatsRows*SeatsCols+1))
                    FreeSeatsList=sample(SeatsList,FreeSeatsNr)

                    #Saving the projection info to the projection program dictionary
                    if len(PrjProgramDic.keys())>0:
                        LastPrjId=list(PrjProgramDic.keys())[-1]
                        PrjProgramDic[LastPrjId+1]={'Screen':Screen,'DateTime':datetime.combine(PrjDay,NextPrjtime),'Title':Film,'FreeSeats':FreeSeatsList}
                    else:
                        PrjProgramDic[1]={'Screen':Screen,'DateTime':datetime.combine(PrjDay,NextPrjtime),'Title':Film,'FreeSeats':FreeSeatsList}

                    NextPrjtime=datetime.combine(PrjDay,NextPrjtime)+FilmDuration+PrjGap
                    NextPrjtime=time(NextPrjtime.hour,NextPrjtime.minute)
                else:
                    if PrjLimit<Closing:
                        PrjLimit=Closing
                        NextPrjtime=PauseEnd
                    else:
                        Screen+=1
            else:
                if PrjLimit<Closing:
                    PrjLimit=Closing
                    NextPrjtime=PauseEnd
                else:
                    Screen+=1
        PrjDay=PrjDay+timedelta(1)
        NextPrjtime=Opening
        PrjLimit=PauseStart
    return PrjProgramDic

def main():
    PrjProgramDic=PrjProgramGen(FilmDic)
    print(PrjProgramDic)
    #STAMPA A VIDEO PROGRAMMA PROIEZIONI

    print('You can perform these operations:\n- book a some seats for a projection [1]\n- exit [0]')
    operation=input('Please, enter the number of the operation you want to perform:')
    while not operation in ['0','1']:
        operation=input('Wrong input, please retry:')

    while operation!='0':
        if operation==1:
            #PRENOTAZIONE
            print('You can perform these operations:\n- book a some seats for a new projection [1]\n- modify an existing projection [2]\n- exit [0]')
            operation=input('Please, enter the number of the operation you want to perform:')
        elif operation==2:
            #MODIFICA PRENOTAZIONE
            print('You can perform these operations:\n- book a some seats for a new projection [1]\n- modify an existing projection [2]\n- exit [0]')
            operation=input('Please, enter the number of the operation you want to perform:')

if __name__=='__main__':
    main()