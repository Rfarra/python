def main():
    top_artists = [
        "The Beatles",
        "Madonna",
        "Elton John",
        "Elvis Presley",
        "Mariah Carey",
        "Stevie Wonder",
        "Janet Jackson",
        "Michael Jackson",
        "Whitney Houston",
        "Rihanna",
    ]
    def replace_artist(top_artists):
     try:
        index = int(input("Enter the index of the artist to replace: "))
        new_artist_name = input("Enter the new artist name: ")
        top_artists = new_artist_name
        print("Updated list:", top_artists)
    
    print("An input error occurred.")


main()
