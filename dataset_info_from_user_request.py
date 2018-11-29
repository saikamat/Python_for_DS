# this string is to be removed.
filename = ''


def inputSettings():
    infoString = ''
    infoDS = ["none"]*5
    infoDS[0] = input("Enter direction.\nACW => Anticlockwise, \
     CW => Clockwise, N=>NIL.\n>> ")
    infoDS[1] = input("Enter loop count.\n>> ")
    infoDS[2] = input("Enter external lighting conditions\
     \nOB => Outside Bright, \
     OBN => Outside Dark\
     \n>> ")
    infoDS[3] = input("Enter internal lighting conditions\
     \nIB => Well lit in room\
     \nIBP => Partially well lit room (only one set of lights are on)\
     \nIBN => All lights in the room are out.\
     \n>> ")
    infoDS[4] = input("Enter remarks if any.\n>> ")
    for i in infoDS:
        infoString += "_"+str(i)
    return(infoString)


if (input("Do you wish to add info about the DS? Press <y> if yes. Any other "\
          "key if no.\n>> ") == 'y'):
    filename = inputSettings()
