
'''
## ask the user below

(1) ask the user for the number of seat he would want to reserve, (2) print out the chairs,
(3) check if all the seats are occupied and (4) ask the user now if he/she wants to reserve again.

'''

from string import ascii_letters

class Concert:

    matrix = []
    print("Please define seat capacity\n")
    n1, n2 = int(input()), int(input())
    sc=n1*n2
    seat_occupied = 0
    # mat_state=[]


    def __init__(self):

        for i in range(self.n1):
            l = ascii_letters[i]
            row = []
            for j in range(self.n2):
                row.append(l + str(j))

            self.matrix.append(row)

        # self.seat_display(self.matrix)
        self.matrix1=[]


    def seatreserve(self):
        print("Welcome to concert, Please choose below options\n")

        # self.seats = ['-' for self.i in range(self.n1 * self.n2)]
        while True:

            print("1. which seat you want to book ? \n",
                  "2. Display the seats \n",
                  "3. current status of bookings \n"
                  "4. Book again")

            self.uchoice = input()

            if self.uchoice == '1':
                if self.seat_occupied!=self.sc:
                    self.seats_manage()
                else:
                    print("seats full! cant book")

            elif self.uchoice == '2':
                self.seat_display()
            elif self.uchoice == '3':
                if self.check_booking():
                    break
                else:
                    continue

            elif self.uchoice == '4':
                if self.seat_occupied!=self.sc:
                    self.seats_manage()
                else:
                    print("seats full! cant book")

            else:
                print("wrong selection")
                break
            continue

    def seat_display(self):

        if self.seat_occupied==0:
            mat11 = self.matrix
            rev = reversed(mat11)
        else:
            mat1=self.matrix1
            rev = reversed(mat1)

        # print(matrix)

        # mat1=mat
        # rev=reversed(mat)
        for i in rev:
            print('\n')
            print('-----------------')
            for j in i:
                print(j, end=' | ')
            #
        print("\n")
        print("#######################\n"
              "#                     #\n"
              "#                     #\n"
              "#------STAGE----------#\n"
              "#                     #\n"
              "########################")




    def seats_manage(self):

        print("which seat you want to book")
        # self.seat_display(self.matrix)
        if self.seat_occupied==0:
            mat1=self.matrix
        else:
            mat1=self.matrix1
        seat_codes=input().split(',')
        self.seat_occupied+=len(seat_codes)
        for i in seat_codes:
            for j in mat1:
                if i in j:
                    k=mat1.index(j)
                    index1=mat1[k].index(i)
                    mat1[k][index1]='X'

        print("seats are booked")
        self.matrix1=mat1
        return self.matrix1
        

    def check_booking(self):
        # seat_occupied=0
        if self.seat_occupied == self.sc:
            print("seats are full")
            return True
        else:
            print("Lucky! Seats are not full yet")
            return False

ob=Concert()
ob.seatreserve()




