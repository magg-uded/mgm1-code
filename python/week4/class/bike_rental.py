#customers can:
'''
- see available bike in the shop
- rent bikes on hourly basis $5 per hour
- rent bikes on daily basis $20 per day
- rent bikes on weekly basis $60 per week
- family rental, a promotion that includes 3 to 5 rentals of any type with a discount of 30% of the total price
'''
#the bike rental shop can:
'''
- issue a bill when customer decides to return the bike
- display available inventory
- take requests on hourly, daily and weekly basis by cross verifying stock
'''
#for simplicity we assume that:
'''
- any customer requests rentals for only type ie hourly, daily etc
- any customer is free to choose the number of bikes they want
- requested bikes should be less than available stock
'''

import datetime #to check number of days and weeks

class BikeRental:
    def __init__(self, stock = 0):

        self.stock = stock

    def displaystock(self):
        print('we currently have {} to rent'.format(self.stock))

        return self.stock

    def hourly_rent(self, n):
        if n <= 0:
            print('number of bikes should be positive!')
            return None
        elif n > self.stock:
            print('sorry, we currently have {} bikes available to rent'.format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print('you have rented {} bike(s) today for {} hours'.format(n, now.hour))
            print('you will be charged $5 for each hour per bike')
            print('we hope that you enjoy our service')

            self.stock -= n
            return now

    def daily_rent(self, n):
        if n <= 0:
            print('number of bikes should be positive!')
            return None
        elif n > self.stock:
            print('sorry, we currently have {} bikes available to rent'.format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print('you have rented {} bike(s) today for {} days'.format(n, now.hour))
            print('you will be charged $20 for each day per bike')
            print('we hope that you enjoy our service')

            self.stock -= n
            return now

    def weekly_rent(self, n):
        if n <= 0:
            print('number of bikes should be positive!')
            return None
        elif n > self.stock:
            print('sorry, we currently have {} bikes available to rent'.format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print('you have rented {} bike(s) today for {} weeks'.format(n, now.hour))
            print('you will be charged $60 for each week per bike')
            print('we hope that you enjoy our service')

            self.stock -= n
            return now

    def returnBike(self, request):
        rentalTime, rentalBasis, numOfBikes = request #variables that factor into billing
        bill = 0 #we don't know the actual charge until you return the bike

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime #getting time difference from renting to returning bike

            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days) / 7 * 60 * numOfBikes

        if(3 <= numOfBikes <= 5):
            print('you are eligible for a family package of 30% off')
            bill = bill * 0.7

            print('thank you for returning our bike. We hope to serve you soon again')
            print('that would be ${} in total.'.format(bill))

        else:
            print('are you sure you rented a bike with us?')
            return None

