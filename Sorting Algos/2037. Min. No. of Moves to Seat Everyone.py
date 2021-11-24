
def minMovesToSeat(seats, student):

    seats.sort()
    student.sort()

    ans = [abs(seats[i]-students[i]) for i in range(len(seats))]

    return sum(ans)

seats = [3,1,5]
students = [2,7,4]

print(minMovesToSeat(seats,students))