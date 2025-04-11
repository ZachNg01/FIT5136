import pandas as pd
import asyncio

# Define login data (normally this would be stored securely in a database)
login_data = {
    'email': ['patient1@student.monash.edu', 'patient2@student.monash.edu', 'admin@monash.edu'],
    'password': ['Monash1234!', 'Monash1234!', 'Admin1234!'],
    'role': ['patient', 'patient', 'admin']
}

# Create DataFrame from login data
df_login = pd.DataFrame(login_data)

# Synchronous login check function
def sync_login(email, password):
    print(f"Synchronously checking login for {email}")
    # Check if the email and password match any row in the DataFrame
    user = df_login[(df_login['email'] == email) & (df_login['password'] == password)]
    if user.empty:
        return "Invalid credentials"
    else:
        role = user.iloc[0]['role']
        return f"Login successful. Welcome {role}!"

# Asynchronous login check function (simulating async operation)
async def async_login(email, password):
    print(f"Asynchronously checking login for {email}")
    await asyncio.sleep(1)  # Simulating async operation (e.g., querying a database)
    user = df_login[(df_login['email'] == email) & (df_login['password'] == password)]
    if user.empty:
        return "Invalid credentials"
    else:
        role = user.iloc[0]['role']
        return f"Login successful. Welcome {role}!"

# Function to display login options
def login_system(is_async=False):
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if is_async:
        result = asyncio.run(async_login(email, password))
    else:
        result = sync_login(email, password)

    print(result)

# Run the system synchronously
login_system(is_async=False)

# Run the system asynchronously
login_system(is_async=True)
