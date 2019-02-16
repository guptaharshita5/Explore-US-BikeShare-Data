import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday','sunday']

def filterdata():
    print("Hello let see some Bikeshare data\n")
    city=input('Enter the city whose data you wish to see:(Chicago,New York City or Washington)\n ').lower()
    print('How would you like to filter the data ?\nEnter the number for your choice\n')
    filter1=input('1.month\n2.day of the week\n3.Both\n4.No filter\n')
    filter2=int(filter1)
    if filter2 == 1:
        month = input('\nSelect the month you would like to filter by:\n(January, February, March, April, May, June)\n').lower()
        day='all'
    elif filter2 == 2:
        day = input('\nSelect the day you would like to filter by:\n(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday)\n').lower()
        month='all'
    elif filter2 == 3:
        month = input('\nSelect the month you would like to filter by:\n(January, February, March, April, May, June)\n').lower()
        day = input('\nSelect the day you would like to filter by:\n(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday)\n').lower()
    
    else:
        month='all'
        day='all'
    return(city,month,day)
        
def station_status(df):
    print("\nCalculating station info.........\n") 
    print('Most start station of the month:',df['Start Station'].mode().max())
    print('Most End station of the month:',df['End Station'].mode().max())
    df['Start End Station'] = df['Start Station'] + ", " + df['End Station']
    common_start_end_station= (df['Start End Station'].value_counts().idxmax())
    print('Most loved route:',common_start_end_station)
    
    
def user_stats(df):
    print("\nFetching User info.........\n")
    print("\nCalculating User info.........\n")
    user_counts = df['User Type'].value_counts() 
    print("\nDifferenet types of users are:\n")
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))
    print("\nHow would you like to see Gender and Birth info. Enter your choice.........\n")
    a=input('Select A for information based on user type and B for no filter:').lower()
    if a== 'a':
        b=input('Enter 1 for subscriber type and 2 for customer type:\n')
        s=int(b)
        if s == 1:
            df=df[df['User Type'].str.contains("Subscriber")]
            print("\nGender and Birth info. for Subscriber User Type.........\n")
            if 'Birth Year' in df.columns:
                user_stats_birth(df)                
            else:
                print("No data available")
                
            if 'Gender' in df.columns:
                user_stats_gender(df)
            else:
                print("No data available")
             
                
        else:
                df=df[df['User Type'].str.contains("Customer")]
                print("\nGender and Birth info. for Customer User Type.........\n")
                if 'Birth Year' in df.columns:
                    user_stats_birth(df)         
                else:
                    print("No data available")    
                if 'Gender' in df.columns:
                    user_stats_gender(df)
                else:
                    print("No data available")
                    
                    
    else:
             print("\nGender and Birth info..........\n")
             if 'Gender' in df.columns:
                user_stats_gender(df)
             else:
                print("No data available")  
             if 'Birth Year' in df.columns:
                user_stats_birth(df)
             else:
                print("No data available")            
            
def user_stats_gender(df):
    print("Counts of gender:\n",df['Gender'].value_counts())
      
           
def user_stats_birth(df):
    """Displays statistics of analysis based on the birth years of bikeshare users."""
    # Display earliest, most recent, and most common year of birth
    print("The most common birth year:", df['Birth Year'].value_counts().idxmax())
    # the most recent birth year
    print("The most recent birth year:", df['Birth Year'].max())
    # the most earliest birth year
    print("The most earliest birth year:", df['Birth Year'].min())
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    
    # TO DO: display total travel time
    print('Total Travel Time:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Average Travel Time:', df['Trip Duration'].mean())
    
    
def load_data(city, month, day):
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    df['day']= df['Start Time'].dt.weekday
    df['month']= df['Start Time'].dt.month
    df['hour']= df['Start Time'].dt.hour
    if month != 'all':
        mo= MONTHS.index(month)+1
        df=df[(df.month == mo)]
              
    if day != 'all':
        da=DAYS.index(day)+1
        df=df[(df.day== da)]
            
    return df
def time_stat(df,month,day):
    if ((day=='all') & (month!='all')):
        print('Most popular hour:',df['hour'].mode().max())
        p_d=df['day'].mode().max()
        print('Most popular day of the month:',DAYS[p_d])
    elif((day!='all') & (month=='all')):
        print('Most popular hour:',df['hour'].mode().max())
        p_d=df['month'].mode().max()
        d=p_d-1
        print('Most popular month for the day:',MONTHS[d])
    elif((day=='all') & (month=='all')):
        p_d=df['month'].mode().max()
        d=p_d-1
        p=df['day'].mode().max()
        print('Most popular month :',MONTHS[d])
        print('Most popular day :',DAYS[p])
        print('Most popular hour:',df['hour'].mode().max())
    else:
        print('Most popular hour:',df['hour'].mode().max())
        
        

        
def main():
    while True:
        city, month, day = filterdata()
        df = load_data(city, month, day)
        time_stat(df,month,day)
        station_status(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break
        if __name__ == "__main__":
            main()
    
main()
        
        
        
            
            
        
        
        
    
    
    

    
