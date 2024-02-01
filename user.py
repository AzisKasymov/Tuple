user_info = {}
user_info["name"] = input("What is the user name? ")
user_info["age"] = input("What is the user age? ")
user_info["country_of_birth"] = input("What is the user country of birth? ")
user_info["known_for"] = input("What is the user known for? ")


print("User Information:")
for key, value in user_info.items():
    print(f"{key.capitalize()}: {value}")