#!/usr/bin/env python3
import psycopg2

#####################################################
##  Database Connection
#####################################################

def openConnection():
    # connection parameters - ENTER YOUR LOGIN AND PASSWORD HERE
    userid = "y25s2c9120_unikey"
    passwd = ""
    myHost = "awsprddbs4836.shared.sydney.edu.au"

    # Create a connection to the database
    conn = None
    try:
        # Parses the config file and connects using the connect string
        conn = psycopg2.connect(database=userid,
                                    user=userid,
                                    password=passwd,
                                    host=myHost)
        return conn

    except psycopg2.Error as sqle:
        print("psycopg2.Error : " + sqle.pgerror)
    
    # return the connection to use
    
'''
Validate user login credentials against the database
Login comparison is case insensitive, password comparison is case sensitive
Parameters:
    login: login ID
    password: User password
Returns:
    [login, firstName, lastName, role] if valid, None if invalid
'''
def checkLogin(login, password):
   
    return ['jdoe', 'John', 'Doe' , 'Customer']

"""
Retrieve all tracks from the database with associated artist information and average ratings
Returns:
    List of dictionaries containing track information:
        - trackid: Track ID
        - title: Track title
        - duration: Track duration
        - age_restriction: Boolean indicating if track has age restrictions
        - singer_name: Full name of the singer
        - composer_name: Full name of the composer
        - avg_rating: Average rating from all reviews (0 if no reviews)
"""
def list_tracks(): 
    
    return None

"""
Retrieve all users from the database
Returns:
    List of dictionaries containing user information:
        - login: User login ID
        - firstname: User's first name
        - lastname: User's last name
        - email: User's email address
        - role: User's role (Customer, Artist, Staff)
"""
def list_users(): 
   
    return None

"""
Retrieve all reviews from the database with associated track and customer information
Returns:
    List of dictionaries containing review information:
        - reviewid: Review ID
        - track_title: Title of the reviewed track
        - rating: Review rating (1-5)
        - content: Review content text
        - customer_login: Login ID of the reviewer
        - customer_name: Full name of the reviewer
        - review_date: Date when the review was written
"""
def list_reviews(): 
    
    return None

"""
Search for tracks based on a search string
Parameters:
    searchString: Search term to find matching tracks
Returns:
    List of dictionaries containing matching track information:
        - trackid: Track ID
        - title: Track title
        - duration: Track duration
        - age_restriction: Boolean indicating if track has age restrictions
        - singer_name: Full name of the singer
        - composer_name: Full name of the composer
        - avg_rating: Average rating from all reviews (0 if no reviews)
"""
def find_tracks(searchString):
    
    return None

"""
Add a new user to the database
Parameters:
    login: User's login ID
    firstname: User's first name
    lastname: User's last name
    password: User's password
    email: User's email address (can be empty)
    role: User's role (Customer, Artist, Staff)
Returns:
    True if user added successfully, False if error occurred
"""
def add_user(login, firstname, lastname, password, email, role):

    return True

"""
Add a new review to the database
Parameters:
    trackid: ID of the track being reviewed
    rating: Review rating (1-5)
    customer_login: Login ID of the customer writing the review
    content: Review content text (can be null)
    review_date: Date when the review was written
Returns:
    True if review added successfully, False if error occurred
"""
def add_review(trackid, rating, customer_login, content, review_date):
   
    return True

"""
Update an existing track in the database
Parameters:
    trackid: ID of the track to update
    title: Updated track title
    duration: Updated track duration
    age_restriction: Updated age restriction setting
    singer_login: Updated singer's login ID (must exist as Artist, case insensitive)
    composer_login: Updated composer's login ID (must exist as Artist, case insensitive)
Returns:
    True if track updated successfully, False if error occurred
"""
def update_track(trackid, title, duration, age_restriction, singer_login, composer_login):

    return True

"""
Update an existing review in the database
If update is successful, the review date will be updated to the current date
Parameters:
    reviewid: ID of the review to update
    rating: Updated review rating (1-5)
    content: Updated review content text (can be null)
Returns:
    True if review updated successfully, False if error occurred
"""
def update_review(reviewid, rating, content):

    return True

"""
Update an existing user in the database
Parameters:
    user_login: Login ID of the user to update
    firstname: Updated user's first name
    lastname: Updated user's last name
    email: Updated user's email address (can be null)
Returns:
    True if user updated successfully, False if error occurred
"""
def update_user(user_login, firstname, lastname ,email ):

    return True

