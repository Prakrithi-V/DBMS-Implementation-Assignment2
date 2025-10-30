#!/usr/bin/env python3
import psycopg2

#####################################################
##  Database Connection
#####################################################

def openConnection():
    # connection parameters - ENTER YOUR LOGIN AND PASSWORD HERE
    userid = "y25s2c9120_pupp0621"
    passwd = "Welcome2holla"
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
    
def checkLogin(login, password):
    '''
    Validate user login credentials against the database.
    Login comparison is case insensitive, password comparison is case sensitive.

    Parameters:
        login: login ID
        password: user password

    Returns:
        [login, firstName, lastName, role] if valid, None if invalid
    '''
    conn = None
    try:
        conn = openConnection()
        if conn is None:
            print("Could not connect to database.")
            return None

        cur = conn.cursor()

        query = """
            SELECT 
                login,
                firstname,
                lastname,
                role
            FROM Account
            WHERE LOWER(login) = LOWER(%s)
              AND PASSWORD = %s;
        """

        cur.execute(query, (login, password))
        userInfo = cur.fetchone()

        cur.close()
        conn.close()

        # Return user details if found
        if userInfo:
            return list(userInfo)
        else:
            return None

    except Exception as e:
        print("Database error:", e)
        if conn:
            conn.close()
        return None

# """
# Retrieve all tracks from the database with associated artist information and average ratings
# Returns:
#     List of dictionaries containing track information:
#         - trackid: Track ID
#         - title: Track title
#         - duration: Track duration
#         - age_restriction: Boolean indicating if track has age restrictions
#         - singer_name: Full name of the singer
#         - composer_name: Full name of the composer
#         - avg_rating: Average rating from all reviews (0 if no reviews)
# """
# def list_tracks(): 
    
#     return None

def list_tracks():
    '''
    Retrieve all tracks from the database with associated artist information and average ratings.
    Returns:
        List of dictionaries containing:
        - trackid
        - title
        - duration
        - age_restriction
        - singer_name
        - composer_name
        - avg_rating
    '''
    conn = None
    try:
        conn = openConnection()
        cur = conn.cursor()

        query = """
            SELECT 
                t.id AS trackid,
                t.title,
                t.duration,
                t.age_restriction,

                -- Singer full name
                CASE 
                    WHEN sa.firstname IS NULL AND sa.lastname IS NULL THEN 'N/A'
                    ELSE sa.firstname || ' ' || sa.lastname
                END AS singer_name,

                -- Composer full name 
                CASE 
                    WHEN ca.firstname IS NULL AND ca.lastname IS NULL THEN 'N/A'
                    ELSE ca.firstname || ' ' || ca.lastname
                END AS composer_name,

                -- Average rating (0 if NULL)
                CASE 
                    WHEN AVG(r.rating) IS NULL THEN 0
                    ELSE ROUND(AVG(r.rating), 2)
                END AS avg_rating

            FROM Track t
                LEFT JOIN Account sa ON t.singer = sa.login
                LEFT JOIN Account ca ON t.composer = ca.login
                LEFT JOIN Review r ON t.id = r.trackID
            GROUP BY 
                t.id, t.title, t.duration, t.age_restriction,
                sa.firstname, sa.lastname,
                ca.firstname, ca.lastname
            ORDER BY t.id;
        """

        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.close()

        # Transform SQL rows into dictionaries
        results = []
        for row in rows:
            results.append({
                'trackid': row[0],
                'title': row[1],
                'duration': row[2],
                'age_restriction': row[3],
                'singer_name': row[4],
                'composer_name': row[5],
                'avg_rating': float(row[6])
            })
        return results

    except Exception as e:
        print("Database error:", e)
        if conn:
            conn.close()
        return None

def list_users():
    '''
    Retrieve all users from the database.
    Returns:
        List of dictionaries containing:
            - login
            - firstname
            - lastname
            - email
            - role
    '''
    conn = None
    try:
        conn = openConnection()
        cur = conn.cursor()

        query = """
            SELECT 
                login,
                firstname,
                lastname,
                email,
                role
            FROM Account
            ORDER BY role, firstname, lastname;
        """

        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.close()

        # Transform SQL rows into dictionaries (simple output formatting)
        results = []
        for row in rows:
            results.append({
                'login': row[0],
                'firstname': row[1],
                'lastname': row[2],
                'email': row[3],
                'role': row[4]
            })
        return results

    except Exception as e:
        print("Database error:", e)
        if conn:
            conn.close()
        return None


def list_reviews():
    '''
    Retrieve all reviews from the database with associated track and customer information.
    Returns:
        List of dictionaries containing:
            - reviewid
            - track_title
            - rating
            - content
            - customer_login
            - customer_name
            - review_date
    '''
    conn = None
    try:
        conn = openConnection()
        cur = conn.cursor()

        query = """
            SELECT 
                r.reviewID AS reviewid,
                t.title AS track_title,
                r.rating,
                r.content,
                r.customerID AS customer_login,
                (a.firstname || ' ' || a.lastname) AS customer_name,
                r.reviewDate
            FROM Review r
                JOIN Track t ON r.trackID = t.id
                JOIN Account a ON r.customerID = a.login
            ORDER BY r.reviewDate DESC, r.reviewID;
        """

        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.close()

        # Convert tuples → dictionaries (allowed minimal formatting)
        results = []
        for row in rows:
            results.append({
                'reviewid': row[0],
                'track_title': row[1],
                'rating': row[2],
                'content': row[3],
                'customer_login': row[4],
                'customer_name': row[5],
                'review_date': row[6]
            })
        return results

    except Exception as e:
        print("Database error:", e)
        if conn:
            conn.close()
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
    """
    Add a new user to the database using stored procedure add_user_proc().
    """
    default_password = password if password else 'default123'
    conn = openConnection()
    if conn is None:
        return False

    cur = conn.cursor()
    try:
        # Call the stored procedure with all six parameters
        cur.execute("CALL add_user_proc(%s, %s, %s, %s, %s, %s);",
                    (login, firstname, lastname, email, default_password, role))
        conn.commit()
        return True
    except psycopg2.Error as e:
        print("Database error in add_user:", e)
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()

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
def update_user(user_login, firstname, lastname, email):
    '''
    Update user details using stored procedure update_user_proc().
    '''
    conn = openConnection()
    if conn is None:
        return False

    cur = conn.cursor()
    try:
        cur.execute("CALL update_user_proc(%s, %s, %s, %s);",
                    (user_login, firstname, lastname, email))
        conn.commit()
        return True
    except psycopg2.Error as e:
        print("Database error in update_user:", e)
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()

