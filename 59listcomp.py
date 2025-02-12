names = ["Som Prakash Chaudhary", "Nishan Poudel", "Shankarsan Khadka", "Raj Poudel", "Deepak Prasad Poudel", "Hari Bist", "Dilip Karki", "Tolak Raj Chapagain", "Padam Bahadur Rai", "Kishor Saud", "Aakriti Rai", "Diwash Sharma Acharya", "Suresh Koli", "Pujana Banstola", "Nitesh Bishwokarma", "Binay Shrestha", "Mani thapa", "Kiran paudel", "Surendra shakya"]

start_with = input("Enter  the starting letter of the name:").upper()
namesstartwith = [x for x in names if x.startswith(start_with)]


print(namesstartwith)
