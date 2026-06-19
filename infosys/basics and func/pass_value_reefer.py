# def change_number(num):
#     num+=10
# def change_list(num_list):
#     num_list.append(20)
# num_val=10
# print("*********effect of pass by value*********")
# print("num_val before function call:", num_val)
# change_number(num_val)
# print("num_val after function call:", num_val)
# print("-----------------------------------------------")
# val_list=[5,10,15]
# print("*********effect of pass by reference*********")
# print("val_list before function call:", val_list)
# change_list(val_list)
# print("val_list after function call:", val_list)
def display1(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)
print("code-1: positional arguments")
display1("FN789",200)
#Uncomment and execute the below function call statement and observe the output
#display1(300,"FN123")
def display2(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)
print("-------------------------------------------------")
print("code-2: keyword arguments")
display2(seating_capacity=250, flight_number="FN789")
def display3(flight_number, flight_make="Boeing", seating_capacity=150):
    print("Flight Number:", flight_number)
    print("Flight Make:", flight_make)
    print("Seating Capacity:", seating_capacity)
print("-------------------------------------------------")
print("code-3: default arguments")
display3("FN789","Eagle")
#Uncomment and execute the below function call statements one by one and observe the output
#display3("FN234")
#display3("FN678","Qantas",200)
def display4(passenger_name, *baggage_tuple):
    print("Passenger name:",passenger_name)
    total_wt=0
    for baggage_wt in baggage_tuple:
        total_wt+=baggage_wt
    print("Total baggage weight in kg:", total_wt)
print("-------------------------------------------------")
print("code-4: variable argument count")
display4("Jack",12,8,5)
#Uncomment and execute the below function call statements one by one and observe the output
#display4("Chan",20,12)
#display4("Henry",23)
