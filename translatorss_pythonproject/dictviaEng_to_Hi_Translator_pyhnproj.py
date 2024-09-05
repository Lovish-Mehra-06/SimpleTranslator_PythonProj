def script():
    # Write the code here....
    # ....
    # ....
    print("English To Hindi Translator")

    dictionaryinfodecrypt = {"eyes": "आंखें",
                             "nose": "नाक",
                             "ear": "कान",
                             "mouth": "मुंह",
                             "tongue": "जीभ",
                             "face": "चेहरा",
                             "teeth": "दांत",
                             "head": "सिर",
                             "forehead": "माथा",
                             "hairs": "बाल",
                             # "": "",  #####   Here Add More Keys and Values .....
                             # "": "",
                             # "": "",
                             # "": "",
                             # "": "",
                             # "": "",
                             # "": "",
                             "smile": "मुस्कुराओ"}

    infoput = input("Enter The Word (use small letters only)\n")

    # Now
    if infoput == "2060":
        print("___Welcome___")
        infoput2 = input("Kesa hai re tu...?\n")
        # 2nd factor Authentication
        if infoput2 == "badiya":
            print("____ok Welcome___")
            ### Write code and notes here ###you can create your dictionary here for secretcodes....
            print("0000 0 0-00 0--0 vagara vagare ......  Hello Bro's")  # -->Help


        else:
            print("--> \n", infoput)
            print("-->\n ")
            print(dictionaryinfodecrypt.get(infoput))
    else:
        print("--> \n", infoput)
        print("-->\n ")
        print(dictionaryinfodecrypt.get(infoput))









    restart = input("\nWould you like to restart this program?  ")
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        print("ok bye... Goodbye")


script()
