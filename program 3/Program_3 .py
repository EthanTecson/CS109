"""
Created on Wed Oct 12 16:52:34 2022

@author: ethantecson
"""
"""
     Author/copyright: Ethan Tecson.  All rights reserved.
     Used with permission and modified by: WhoeverModifiesIt
     Date: 12 October 2022
"""
#123456789 123456789 123456789 123456789 123456789 123456789 123456789
#######################################################################
def investment_computation(investment, rate_of_return, time):
    """
     This function will compute accured wealth monthly based off of a steady
          investment plan.
          Parameters:
              investment   -- monthly investment amount
              rate_of_return -- the yearly rate of return as a percentage
              months_of_investment_plan -- how many months the investor plans to invest
          Returns:
              Accured wealth after investments
    """
    #turn yearly rate of return into monthly percentage
    rate_of_return = rate_of_return/100
    rate_of_return = rate_of_return/12

    #Create three variabels that are initialized as monthly investment.
    #'initial' will stay consistently stay as the monthly investment without manipulation.
    #'total' will be the money accured at the beginning of each month
    #'investment' will manipulated by the 'rate_of_return'
    initial = investment
    total = investment
    
    for number in range(1, time + 1):
        print('                 Month:', number) 
        print('              --------------')
        sss = f'{total:9.2f}'
        print('(accrual + monthly investment)', sss)
        investment = investment * rate_of_return
        sss = f'{investment:22.2f}'
        print('(amount returned)', sss)
        total = total + investment
        sss = f'{total:24.2f}'
        print('(total accrued)', sss)
        total = total + initial
        investment = total
        print(' ')
        
######################################################################
def main():
     """  This main function prompts the user for the investment amount,
         yearly rate of return as a percentage, months of investment plan,
         and then uses the investment_computation() function to compute
         the accured wealth.
     """
     investment = float(input('Monthly Investment: '))
     rate_of_return = float(input('Yearly Rate of Return in Percentage (ex. %6.00): %'))
     time = int(input('Number of Months of investing: '))
     investment_computation(investment, rate_of_return, time)

######################################################################
main()
