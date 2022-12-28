class Star_cinema:
    hall_list=[]
    def __init__(self):
        pass
    
    def entry_hall(self,hall):
        self.hall_list.append(hall)

def decoration():
    print('---------------------------------')
    print('\n')        

        
       
class Hall(Star_cinema):
    def __init__(self,hall_name, rows, cols):
        self._seats = {}
        self._show_list = []
        self.hall_no = hall_name
        self.rows = rows
        self.cols = cols
        self.customer = {}
        super().__init__()
        self.entry_hall(self)
    
    def entry_show(self, movie_id, movie_name, show_time):
        _show_info = (movie_id, movie_name, show_time)
        self._show_list.append(_show_info)
        self._seats[movie_id] = [[i for i in range(0,self.cols)] for j in range(0,self.rows)]
        
    def view_show_list(self):
        decoration()
        
        for shows in self.show_list:
            print(f"MOVIE NAME : {shows[1]} \t\t SHOW ID : {shows[0]} \t\t SHOW TIME : {shows[2]}")
        decoration()
    
    
    def show_avalible_seats(self,movie_id):
        try:
            seat_list = self.seats[movie_id]
            for shows in self.show_list:
                if move_id == shows[0]:  
                    print(f"\n MOVIE NAME : {shows[1]} \t SHOW TIME : {shows[2]} \n X for already booked seat")
            decoration() 
            for i,lst in enumerate(seat_list):
                for j,ch in enumerate(lst):
                    if ch =='X':
                        sc='X '
                    else:
                        sc=chr(ord('A')+i) + str(lst[j])
                    print(sc, end="     ")
                print("\n")
            decoration() 
        except:
            print("wrong movie id") 
     
    def book_tickets(self):
        movie_id= input("Enter move id: ")
        flag=0
        for shows in self.show_list:
            if movie_id == shows[0]:
                flag=1
                customar_name = input("Enter your name: ")
                customar_phone = input("Enter your phone number: ")
                ticket_amount = int(input("Enter ticket amount: "))
                seat_numbers = []
                while(ticket_amount):
                    seat = input("Enter seats number: ").capitalize()
                    try:
                        i= ord(seat[0])-ord('A')
                        j = int(seat[1])
                        if self.seats[movie_id][i][j] != 'X':
                            self.seats[movie_id][i][j] = 'X'
                            seat_numbers.append(seat)
                        else:
                            print("this seat is already booked")
                            continue
                        ticket_amount-=1
                    except:
                        print("Invalid ticket number")
                        continue
                print("##### Ticket booked successfully #####")
                decoration()
                print(f"Name: {customar_name}\nPhone: {customar_phone}\n")
                print(f"MOVIE NAME : {shows[1]} \t TIME : {shows[2]}\n")
                print(f"Seat Numbers: {' '.join(map(str, seat_numbers))}\n")
                print(f"Hall Name: {self.hall_no}\n")
                decoration()
        if flag == 0 :
            print("invalid movie id")                         
                 
                    
                         
        
                
                
        
        
        
cinema_company = Star_cinema()
hall_01 = Hall('Simanto Somvar', 3,5)
hall_02 = Hall('Bosundhara Shoping Complex', 10, 15)
hall_01.entry_show('ave1', 'Avengers End Game', '29th December 2022 06:30pm')
hall_01.entry_show('bla2', 'Black Adams', '29th December 2022 08:30pm')

while True:
    print("Choose an option: \n 1. Show avalible shows \n 2. Show avalible seats \n 3. Book ticket")
    sel_opt = int(input("Enter option : "))
    
    match sel_opt:
        case 1:
            hall_01.view_show_list()
        case 2:
            move_id= input("Enter move id: ")
            hall_01.show_avalible_seats(move_id)
        case 3:
            hall_01.book_tickets()
            
    
            
        
        
        
        
        
         
       
        

