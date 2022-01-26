"""file = open("flight.txt","w")
file.write("Hello")
file.close()"""
"""try:
    file = open("flight.txt","r")
    text = file.read()
    print(text)
    file.write(", Good Morning")
    file.close()
except Exception as e:
    print("Error Message : ",e)
    if file.closed == True:
        print('File is closed')
    else:
        print('File is Open')"""

"""try:
    flight_file=open("flight.txt","r")
    text=flight_file.read()
    print(text)
    flight_file.write(",Good Morning")
except Exception as e:
    print("Error Message : ",e)
finally:
    print("File is being closed")
    flight_file.close()
    if flight_file.closed:
        print("File is closed")
    else:
        print("File is open")
"""

"""
try:
    hello_file=open("flight.txt","w")
    text="Hello everyone! Welcome"
    hello_file.write(text)
except:
    print("Error occurred, not able to write to file")
finally:
    hello_file.close()
try:
    hello_file=open("flights.txt","r")
    text_from_file=hello_file.read()
    print(text_from_file)
except:
    print("Error Occurred, not able to read from file")
finally:
    hello_file.close()"""


try:
    hello_file=open("flight.txt","w")
    text="Hello everyone! Welcome"
    hello_file.write(text)
except:
    print("Error occurred, not able to write to file")
finally:
    hello_file.close()
try:
    hello_file=open("flight.txt","r")
    text_from_file=hello_file.read()
    print(text_from_file)
except:
    print("Error Occurred, not able to read from file")
finally:
    hello_file.close()

