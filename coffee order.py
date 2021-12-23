# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 07:33:03 2021
This script take coffee order and display price
@author: cresc
"""

def cupPrize(size):
    cupChoice = {
        'small': 2,
        'medium': 3,
        'large': 4,
    }
    return cupChoice.get(size, "Please, choose between small, medium,large.")

def brewPrize(types):
    brewChoice = {
        'brewed': 0,
        'espresso': 0.5,
        'cold brew': 1,
    }
    return brewChoice.get(types, "Please, choose between brewed, espresso, or cold press.")

def flavorPrize(flavor):
    flavorChoice = {
        'no': 0,
        'yes': 0.5, 
    }
    return flavorChoice.get(flavor, "Please,choose between yes or no.")

def flavors(flavors1):
    flavoring = {
        'hazelnut': 'hazelnut',
        'vanilla': 'vanilla', 
        'caramel': 'caramel', 
    }
    return flavoring.get(flavors1)

def test():
    flavorPick = 'no flavor'
    cupSize = input('Do you want a small, medium or large coffee? ').lower()
    try:
        sum = (cupPrize(cupSize))
        # Brew type
        typePrize = input('Do you want brewed, espresso, or cold brew? ').lower()
        sum += float(brewPrize(typePrize))
        
        # Flavor
        flavoring = input('Do you want a flavored syrup? (yes or no) ').lower()
        sum += float(flavorPrize(flavoring))
        if(flavoring.lower() == 'yes'):
            flavorPick = input('Do you want hazelnut, vanilla, or caramel? ').lower()
            flavorPick = flavors(flavorPick)
            if (flavorPick == None):
                raise ValueError("Please,choose between hazelnut, vanilla, or caramel") 
                
        #Summary
        print('You asked for a',cupSize,'of',typePrize,'coffee with',flavorPick ,'syrup')
        print('Your  cup of coffee costs','%.2f'%sum,'$')
        print('price with a tip is','%.2f'%(sum*0.15+sum),'$')
        
    except (KeyError,ValueError, TypeError, NameError,None) as error:
        print(f"Unexpected {error = }")

if __name__ == "__main__":
    
   test()
