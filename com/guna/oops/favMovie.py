# user has to select 1 option among 5

class Movies:

    def __init__(self):
        movie_names = """
        1 darling
        2 mirchi
        3 sita ramam
        4 rrr
        5 bhahubali
        """
        print(movie_names)

    def main_execution(self, user_input):
        if user_input == 1:
            print("darling")
        elif user_input == 2:
            print("mirchi")
        elif user_input == 3:
            print("sita ramam")
        elif user_input == 4:
            print("rrr")
        elif user_input == 5:
            print("bhahubali")


names = Movies()
names.main_execution(2)

