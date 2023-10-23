# Import the 'subprocess' module to run external executables and the 'csv' module to work with CSV files.
import subprocess
import csv

# Function to run the 'CrackMe.exe' executable and return the output
def runExe(username, pin):
    # Use 'subprocess.check_output' to run 'CrackMe.exe' with the specified username and PIN as arguments.
    out = subprocess.check_output(["CrackMe.exe", username, str(pin)], shell=True)
    # Convert the output to a string and remove leading/trailing whitespace.
    out = str(out, 'utf-8')
    out = out.strip()
    return out

# Load the list of usernames from 'usernames.csv'
usernames = []
with open('usernames.csv', 'r') as file:
    reader = csv.reader(file)
    # Loop through each row in the CSV file and extend the 'usernames' list with the rows.
    for row in reader:
        usernames.extend(row)

# Function to find valid combinations of usernames and 3-digit PINs
def find_valid_combinations():
    valid_combinations = []

    for username in usernames:
        for pin in range(100, 1000):  # Iterate through 3-digit PINs from 100 to 999
            output = runExe(username, pin)
            if output == "User not found":
                # If the output is "User not found," the username is invalid, so break the loop.
                break
            elif output == "Incorrect Pin":
                # If the output is "Incorrect Pin," the PIN is incorrect, so continue to the next PIN.
                continue
            else:
                # If none of the above conditions are met, a valid combination is found and added to the list.
                valid_combinations.append((username, pin))
                # Break the loop as we found a valid combination for this username.
                break

    return valid_combinations

# Find and print valid combinations of usernames and 3-digit PINs
valid_combinations = find_valid_combinations()

# Loop through the list of valid combinations and print them
for username, pin in valid_combinations:
    print(f"Valid combination found: Username='{username}', PIN={pin}")
