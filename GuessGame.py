Music = {"Name":"Uptown Funk","SongWriter1":"Bruno Mars","SongWriter2":"Bhaskar Jeffrey","Director":"Cameron Duddy","ReleaseYear":2014,"Genre":"Funk-Pop","DurationInMinutes":6.3}
print(Music)
for i in Music:
    print(i,":",Music[i])

def GuessGame(key,value):
    for z in Music:
        if z == key:
            if Music[z] == value:
                print("You are absolutely correct!")
                return True
            else:
                print("You are wrong!")
                return False
        else:
            print("Please select a valid option from the choices!")
            return False

key = input("Hey! What do you want to guess? Choose any one: Name/SongWriter1/Director/Release Year/Genre/Duration in Minutes")
value = input("Please type in your assumption! Let's see if it matches")
Status = GuessGame(key,value)
print(Status)
