with open("C:\Adi\PythonCodes\Lettter_for_all.py\data.txt","r") as names :
    names_list = names.readlines()


with open("C:\Adi\PythonCodes\Lettter_for_all.py\Starting_Letter.txt","r") as letter_file :
    letter_contents = letter_file.read()
    for name in names_list :
        stripped_name = name.strip("\n")
        new_letter = letter_contents.replace("name", stripped_name)
        with open(f"C:\Adi\PythonCodes\Lettter_for_all.py\letter_for_{stripped_name}.txt","w") as final_letter :
            final_letter.write(new_letter)
        