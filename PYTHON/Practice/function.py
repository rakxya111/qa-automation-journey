""" Q NO 1 : 
A website stores usernames entered by different users.

usernames = ["  Admin ", "guest01", " QA_User ", "manager  ", " test_user "]

Write a function that returns a new list where every username has:

Leading and trailing spaces removed.
All usernames converted to lowercase. """

# Answer :

# def clean_usernames(usernames):
#     return [username.strip().lower() for username in usernames]

# usernames = ["  Admin ", "guest01", " QA_User ", "manager  ", " test_user "]
# print("Before :", usernames)
# result = clean_usernames(usernames)
# print("After :",result)






""" Q NO 2

A login system stores the following credentials:

credentials = {
    "admin": "admin123",
    "qa": "qa2025",
    "guest": "guest123"
}

Write a function that accepts a username and password and returns:

"Login Successful" if both match.
"Invalid Username" if the username does not exist.
"Invalid Password" if the username exists but the password is incorrect."""

# Answer :

# credentials = {
#     "admin": "admin123",
#     "qa": "qa2025",
#     "guest": "guest123"
# }

# def sign_in(username , password):
#     if username in credentials:
#         if password == credentials[username]:
#             return 'Login Sucessful'
#         else:
#             return 'Password Incorrect'
#     else:
#         return 'Invalid username'


# username = input("Enter the username: ")
# password = input("Enter the password: ")
# result = sign_in(username, password)
# print(result)






""" Q NO 3

A QA engineer collected test results.

results = ["PASS", "FAIL", "PASS", "PASS", "FAIL", "SKIPPED", "PASS"]

Write a function that returns a dictionary containing the total number of:

"PASS"
"FAIL"
"SKIPPED"

Ignore any other values if they appear. """


# SOLUTION :

# results = ["PASS", "FAIL", "PASS", "PASS", "FAIL", "SKIPPED", "PASS"]

# def count_results(results):
#     pass_no = 0
#     fail_no = 0
#     skipped_no = 0
#     for n in results:
#         if n == 'PASS':
#             pass_no += 1
#         elif n == 'FAIL':
#             fail_no += 1
#         elif n == 'SKIPPED':
#             skipped_no += 1
    
#     return {
#         'PASS' : pass_no,
#         'FAIL' : fail_no,
#         'SKIPPED' : skipped_no
#     }


# def better_count_results(results):
#     counts = {
#         'PASS' : 0,
#         'FAIL' : 0,
#         'SKIPPED' : 0
#     }

#     for result in results:
#         if result in counts:
#             counts[result] += 1

#     return counts


# result = count_results(results)
# print(result)






""" Q NO 4

A web application returns the following page titles.

titles = [
    "Home",
    "Login",
    "",
    "Dashboard",
    "Profile",
    "",
    "Settings"
]

Write a function that returns a new list containing only the valid (non-empty) page titles. """

# SOLUTION :

# titles = [
#     "Home",
#     "Login",
#     "",
#     "Dashboard",
#     "Profile",
#     "",
#     "Settings"
# ]

# def new_titles(titles):
#     new_list = []

#     for title in titles:
#         if title:
#             new_list.append(title)
    
#     return new_list

# # Using list Comprehesion
# def new_titles01(titles):
#     new_list = [title for title in titles if title]
#     return new_list

# result = new_titles(titles)
# result_01 = new_titles01(titles)
# print(result)
# print(result_01)






""" Q NO 5

A tester recorded browser names used during testing.

browsers = [
    "Chrome",
    "Firefox",
    "chrome",
    "Edge",
    "FIREFOX",
    "Safari",
    "edge"
]

Write a function that returns a list of unique browser names, treating names with different letter cases as the same browser while preserving the order of their first appearance.
"""
# SOLUTION :
 
# browsers = [
#     "Chrome",
#     "Firefox",
#     "chrome",
#     "Edge",
#     "FIREFOX",
#     "Safari",
#     "edge"
# ]

# def unique_browser_list(browers):
#     new_list = []
#     seen = set()

#     for browser in browers:
#         lower = browser.lower()
        
#         if lower not in seen:
#             seen.add(lower)
#             new_list.append(browser)

#     return new_list

       
# result = unique_browser_list(browsers)
# print(result)




""" Q NO 6

A test execution report is represented as a dictionary.

test_report = {
    "TC001": "PASS",
    "TC002": "FAIL",
    "TC003": "PASS",
    "TC004": "FAIL",
    "TC005": "PASS"
}

Write a function that:

Counts how many test cases passed.
Counts how many test cases failed.
Determines whether the overall execution result should be "SUCCESS" (all test cases passed) or "FAILED" (at least one test case failed).
Returns all of this information in a single dictionary.

"""

test_report = {
    "TC001": "PASS",
    "TC002": "FAIL",
    "TC003": "PASS",
    "TC004": "FAIL",
    "TC005": "PASS"
}

def execution_result(tests):
    counts = {
        "PASS": 0,
        "FAIL": 0,
        "RESULT": ''
    }
    
    for test in tests:
        if tests[test] == 'PASS':
            counts["PASS"] += 1
        elif tests[test] == 'FAIL':
            counts["FAIL"] += 1
    
    if counts['FAIL'] >= 1:
        counts['RESULT'] = 'FAILED'
    else:
        counts['RESULT'] = 'SUCCESS'

    return counts

# ANOTHER WAY

def execution_02(tests):
    counts = {
        "PASS": 0,
        "FAIL": 0,
        "RESULT": ''
    }

    for test in tests.values():
        if test == 'PASS':
            counts["PASS"] += 1
        elif test == 'FAIL':
            counts['FAIL'] += 1
    
    if counts['FAIL'] == 0:
        counts['RESULT'] = 'SUCCESS'
    else:
        counts['RESULT'] = 'FAILED'
    
    return counts



result = execution_result(test_report)
print(result) 
    

    



            
