from source_Instagram import SourceInstagram

username = input("Enter username >>>")
password = input("Enter password >>>")

output = SourceInstagram(username, password, False, None, None)

print("Enter the numbers below for the required data ")
print(" 1 : followees details ")
print(" 2 : followers details ")
print(" 3 : post details ")

num = int(input(">>>"))

if num == 1:
    print(output.get_followees())
elif num == 2:
    print(output.get_followers())
elif num == 3:
    print(output.get_posts_details())
else:
    print("Enter valid number")


