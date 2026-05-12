import socket
import sys
import random
import pandas as pd

def handle_request(client_connection):
    """
    This method Handles the client's weather prediction.
    Loads the Excel file, selects a random city, and manages the guessing process.
    """
    try:
        weather_data = pd.read_excel("weathers.xlsx")
    except Exception as e:
        msg_error_server = f"Failed to load Excel file given in the homework1 pdf: {e}"
        print(msg_error_server)
        client_connection.sendall(msg_error_server.encode())
        return

    # Select a random row from the dataframe
    row = weather_data.sample(1).iloc[0]
    # The code reads "City" value from the excel file.
    try:
        city = row["City"]
    except KeyError:
        msg_error_server = "Excel error: 'City' not found."
        print(msg_error_server)
        client_connection.sendall(msg_error_server.encode())
        return

    try:
        # Uses "Temp" column for temperature from the excel file.
        actual_temp = row["Temp"]
    except KeyError:
        msg_error_server = "Excel error: 'Temp' not found."
        print(msg_error_server)
        client_connection.sendall(msg_error_server.encode())
        return

    tolerance = abs(actual_temp) * 0.1  # 10% tolerance for the prediciton of the weather is defined here.

    # Send the first prompt to the client 
    prompt = f"You should guess the temperature for {city}:"
    client_connection.sendall(prompt.encode())

    attempts = 0
    while attempts < 3:
        data = client_connection.recv(1024)
        if not data:
            break

        guess_str = data.decode().strip()
        #if the client ended the communication show this message
        if guess_str.upper() == "END":
            end_msg = "Connection terminated by client."
            client_connection.sendall(end_msg.encode())
            break

        try:
            guess = float(guess_str)
        except ValueError:
            msg_error_server = "Please enter a valid number or 'END' to quit."
            client_connection.sendall(msg_error_server.encode())
            continue

        if abs(guess - actual_temp) <= tolerance:
            msg_IfSuccess = f"Congrats, Your guess is satisfying 10% tolerance. And the actual temperature is {actual_temp}."
            client_connection.sendall(msg_IfSuccess.encode())
            break
        else:
            attempts = attempts + 1
            hint = {True: "Higher",False: "Lower"}[guess < actual_temp]

            if attempts < 3:
                client_connection.sendall(hint.encode())
            else:
                msg_IfFail = f"You failed to guess correctly in three attempts. The correct temperature is: {actual_temp}."
                client_connection.sendall(msg_IfFail.encode())

def serve_forever():
    """
    this method Initializes the server after that listens on port 8888, and finally handles incoming connections.
    """
    sock_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_listener.bind(("localhost", 8888))
    
    sock_listener.listen(5)
    print("Listening on port 8888")

    while True:
        client_connection, client_address = sock_listener.accept()
        print("Connection created with:", client_address)
        handle_request(client_connection)
        client_connection.close()
        print("Connection closed. New connection is being waited.\n")

if __name__ == "__main__":
    serve_forever()
