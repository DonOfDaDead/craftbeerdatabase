#!/bin/env python
'''
All Files Located On GitHub: https://github.com/DonOfDaDead/craftbeerdatabase.git

Welcome to the Craft Beer Database.  This database relies on craft beer taken from https://www.kaggle.com/nickhould/craft-cans.

To properly launch the database, please do the following:
1. Download the breweries.csv and beers.csv files.
2. Download finalproject.py
3. In your terminal, run the command 'python3 finalproject.py breweries.csv beers.csv'.

It is important that you run the command for breweries and beers in this order because we are taking sys.argv[1] and sys.argv[2] for analysis.
If you run it backwards, your breweries will be beers and your beers will be breweries.

Have fun...thank you!
'''
import sys
import csv

#Taking two arguments from users: breweries.csv as the first arg and beers.csv as the second arg
breweries = sys.argv[1]
beers = sys.argv[2]

#function that opens the csv file and uses the csv import to read the file into a list
def read_csv(my_file):
    try:
        f = open(my_file, "r", encoding="ISO-8859-1")    
    except IOError:
        print("File was not found.  Please make sure you typed the following: 'python3 finalproject.py breweries.csv beers.csv'")
        print("Please make sure breweries.csv and beers.csv are in the same location as finalproject.py")
        sys.exit()
    my_file = csv.reader(f)
    next(my_file, None)
    return my_file

#function for landing page menu of options
def print_menu():
    try:
        print ('\nWELCOME TO THE CRAFT BEER DATABASE\nThis database includes...')
        #calls function to sum the number of breweries and beers in the two csv files
        print('{} Breweries and {} Different Beers'.format(len(brew_total(breweries)), len(brew_total(beers))))
        print('\n1. States')
        print('2. Popular Styles')
        print('3. ABV & IBU')
        print('4. Beer Selector')
        print('5. Quit')
        print()
    except SyntaxError:
        print("There is something wrong with the menu syntax.")
        sys.exit()

#function that counts the total number of breweries and beers in the two csv files.
#It iterates over the file and pulls the breweries and beers into a list
def brew_total(my_file):
    try:
        brew_list = []
        for row in read_csv(my_file):
            brew_list.append(row[1])
    except:
        print("When script was run, please make sure breweries.csv was sys.argv[1] and beers.csv was sys.argv[2] not the other way around.")
        sys.exit()
    return brew_list

#function that creates a dictionary of breweries and beers with keys being the names and values being the count
#It iterates over the csv files and counts unique keys
def count_things(my_file, col_number):
    try:
        my_dict = {}
        brewerylist = read_csv(my_file)
        for row in brewerylist:
            key_name = row[col_number]
            if key_name in my_dict:
                my_dict[key_name] = my_dict[key_name] + 1
            else:
                my_dict[key_name] = 1
    except:
        print("When script was run, please make sure breweries.csv was sys.argv[1] and beers.csv was sys.argv[2] not the other way around.")
        print("Otherwise, we'll be counting breweries for beers and beers for breweries.")
        sys.exit()
    return my_dict

#function that determines which style is most popular in the dictionary
#It iterates over the dictionary created by the count_things function and determines which beers match the maximum of abv or ibu
def maxstyle(stylecount):
    try:
        maxstyle = []
        for style, count in stylecount.items():
            if count == max(stylecount.values()):
                maxstyle.append(style)
    except:
        print("Please make sure you aren't counting breweries as styles.  Breweries should be sys.argv[1].")
        sys.exit()
    return maxstyle

#function that determines which style is most popular in the dictionary
#It iterates over the dictionary created by the count_things function and determines which beers match the minimum of abv or ibu
def minstyle(stylecount):
    try:
        minstyle = []
        for style, count in stylecount.items():
            if count == min(stylecount.values()):
                minstyle.append(style)
    except:
        print("Please make sure you aren't counting breweries as styles.  Breweries should be sys.argv[1].")
        sys.exit()
    return minstyle

#function that determines the average abv and ibu
#It iterates over the CSV and counts and sums the values for use in calculating the average
def average(my_file, col_number):
    my_file = read_csv(my_file)
    vals_to_avg = []
    counter = 0
    for row in my_file:
        vals_to_avg.append(float(row[col_number]))
        if row[col_number] == '0':
            counter += 1
    #sum of values
    total = sum(vals_to_avg)
    #number of values with '0' removed because they were blank cells in the datasheet.  Remove here to prevent skewing of average.
    #counter is the number of cells which did not have data.
    count = len(vals_to_avg) - counter
    try:
        avg = total/count
    except ZeroDivisionError:
        print("The count is zero, and you can't divide by zero.  Please make sure the number of beers with ABV and IBU is being counted.")
        sys.exit()
    return avg

#function for maximum abv or ibu in the beer list
def max_abv_ibu(my_file, col_number):
    try:
        my_file = read_csv(my_file)
        vals_to_avg = []
        for row in my_file:
            vals_to_avg.append(str(row[col_number]))
        maxprofile = max(vals_to_avg)
    except:
        print("When script was run, please make sure breweries.csv was sys.argv[1] and beers.csv was sys.argv[2] not the other way around.")
        sys.exit()
    return maxprofile

#function for minimum abv or ibu in the beer list
def min_abv_ibu(my_file, col_number):
    try:
        my_file = read_csv(my_file)
        vals_to_avg = []
        for row in my_file:
            vals_to_avg.append(str(row[col_number]))
        minprofile = min(vals_to_avg)
    except:
        print("When script was run, please make sure breweries.csv was sys.argv[1] and beers.csv was sys.argv[2] not the other way around.")
        sys.exit()
    return minprofile

#function for list of beers that match abv and ibu inputed by the user for beer selector
def max_abv_ibu_profile(my_file, col_number):
    try:
        my_file = read_csv(my_file)
        maximum = max_abv_ibu(beers, col_number)
        max_profile = []
        for row in my_file:
            if row[col_number] == maximum:
                #pulls just the beer name and beer style from the list of beers
                max_profile.append(row[3:5])
    except:
        print("Please make sure the right references are being made to ABV versus IBU column numbers in beers.csv.")
        sys.exit()
    return max_profile

#function for beer selector menu
def selector_menu():
    try:
        print ('\nAre you looking for recommendations based on ABV or IBU?')
        print('\n1. ABV (Alcohol By Volume)')
        print('2. IBU (International Bitterness Unit)')
        print('3. Return to prior menu')
        print()
    except SyntaxError:
        print("There is something wrong with the menu syntax.")
        sys.exit()

#function to find the minimum and maximum range of ABV in beer selector
def ABVrecommendation(my_file, col_number):
    my_file = read_csv(my_file)
    try:
        target_ABV = str(input("\nWhat ABV are you looking for?\nPlease pick a value between {} and {} (enter '0.128' not '.128' or '128'): ".format(min_abv_ibu(beers,1), max_abv_ibu(beers,1))))
    except:
        print("Please make sure you entered a number between the minimum and maximum and in the form of a decimal (e.g. '0.128' instead of '128' or '.128')")
    ABVselector = []
    for row in my_file:
        if row[col_number] == target_ABV:
            ABVselector.append(row[3:5])
    return ABVselector

#function to find the minimum and maximum range of IBU in beer selector
def IBUrecommendation(my_file, col_number):
    my_file = read_csv(my_file)
    IBUselector = []
    try:
        target_IBU = str(input("\nWhat IBU are you looking for?\nPlease pick an integer between {} and {}: ".format(min_abv_ibu(beers,2),max_abv_ibu(beers,2))))
    except:
        print("Please pick a valid value between the minimum and maximum.  It must be an integer.")
    for row in my_file:
        if row[col_number] == target_IBU:
            IBUselector.append(row[3:5])
    return IBUselector

#begin menu with no selection   
selection = 0

#starts menu
print_menu()

#stay within menu until 5 is selected to exit
while selection != 5:
    selection = int(input("To learn more, please select from the options above (1-5): "))
    
    #calls function show location of breweries
    if selection == 1:
        brewery_per_state = count_things(breweries,3)
        print("The breweries are from the following states: {}".format(list(brewery_per_state.keys())))      
    
    #calls function to show most and least popular beer styles
    elif selection == 2:
        popular_styles = count_things(beers, 4)
        print("\nThe dominant beer style is {}".format(maxstyle(popular_styles)))
        print("The least common beer style is {}".format(minstyle(popular_styles)))
    
    #calls function to show ABV and IBU data, average and maximums
    elif selection == 3:
        averageABV = average(beers,1)
        averageIBU = average(beers,2)
        print("\nOverall, the beers have an average ABV of {} and average IBU of {} (ABV=alcohol by volume, IBU=international bitterness unit)".format(averageABV, averageIBU))    

        maxABV = max_abv_ibu(beers,1)        
        print("\nThe highest ABV is {}.\nThe following beer(s) have this profile: {}.".format(maxABV, max_abv_ibu_profile(beers,1)))

        maxIBU = max_abv_ibu(beers,2)
        print("\nThe highest IBU is {}.\nThe following beer(s) have this profile: {}".format(maxIBU, max_abv_ibu_profile(beers,2)))

    #starts beer selector menu
    elif selection == 4:
        ABVIBUselection = 0

        #launch selector menu
        selector_menu()
        while ABVIBUselection !=3:
            ABVIBUselection = int(input("Please select from the options above (1-3): "))

            #request user input for ABV that they are interested in
            #calls function to report back beers matching input
            if ABVIBUselection == 1:
                print("We recommend the following breweries & beers: {}".format(ABVrecommendation(beers,1)))
                input("Press any button to continue...")
                selector_menu()

            #request user input for IBU that they are interested in
            #calls function to report back beers matching input
            elif ABVIBUselection == 2:
                print("We recommend the following breweries & beers: {}".format(IBUrecommendation(beers,2)))
                input("Press any button to continue...")
                selector_menu()

            elif ABVIBUselection > 3:
                print("Please enter a valid option.")
                input("Press any button to continue...")
                selector_menu()
        #go back to original landing menu
        print_menu()

    elif selection > 5:
        print("\nPlease make a valid selection.")
        print_menu()

print("Thank you for checking out the Craft Beer Database.")