days=int(input("Enter total days of the months="))
hall_rent=int(input("Enter your hall/hostel rent="))
food=int(input("Enter the approximate daily cost of food="))
electricity_spend=int(input("Enter the total unit of electricity spend="))
charge_per_unit=int(input("Enter the charge of unit="))
gas_bill=int(input("Enter the gas bill="))
water_bill=int(input("Enter the water bill="))
transportation_cost=int(input("Enter the daily approximate charge of transportations="))
persons=int(input("Enter the number of persons living in hall/hostel="))
total_bill=electricity_spend*charge_per_unit
transport_cost=transportation_cost*days
food_rent=food*days
rent=(food_rent + total_bill + gas_bill + water_bill + transport_cost)//persons 
print("You have to contribute=",rent)
