# if/else
ranking = {
    "1": "first",
    "2": "second",
    "3": "third",
    "4": "fourth"
}

akash_ranking = "1"

# if akash_ranking == "1":
#     print("He came " + ranking[akash_ranking] + " in the class")
# elif akash_ranking == "2":
#     print("He came " + ranking[akash_ranking] + " in the class")
# elif akash_ranking == "3":
#     print("He came " + ranking[akash_ranking] + " in the class")
# else:
#     print("He failed!")

match akash_ranking: # "10"
    case "1" | "2" | "3":
        print("He came " + ranking[akash_ranking] + " in the class")
    case _: # default
        print('failed!')

number = 100
# even = number % 2

# 11 / 2 => 2 * 5 + 1

match number % 2:
    case 0:
        print("Even")
    case _:
        print("Odd")

a = [1,2,3,4]

