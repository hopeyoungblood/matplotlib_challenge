
file_name = "output.txt"

first_place = "Bob"
first_place_results = 100

second_place = "Sally"
second_place_results = 100

with open(file_name, "w") as txt_file:


    txt_file.write("Summary Results\n")
    txt_file.write("---------------\n")

    txt_file.write(f"{first_place}: {first_place_results}\n")

    txt_file.write(f"{second_place}: {second_place_results}\n")
