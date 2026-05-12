import socket

def main():
    """
    this method connects to the server on localhost:8888 and handles the guessing interaction.
    """
    sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock_client.connect(("localhost", 8888))
    except Exception as exc:
        print("Connection error:", exc)
        return

    init_message = sock_client.recv(1024).decode()
    if not init_message:
        print("No message received from the server.")
        sock_client.close()
        return

    print(init_message)
    #with this for loop the code will iterate until the user will find the answer or it will iterate for 3 times and gives a message.
    for _ in iter(lambda: True, False):
        user_input = input("Enter your guess or 'END' to quit the loop: ")
        sock_client.sendall(user_input.encode())
        #code sends the user input to the server
        server_reply = sock_client.recv(1024).decode()
        print("Server:", server_reply)
        #with the server reply wheter the answer is true or not it will give a message using the if below.
        if user_input.upper() == "END" or any(keyword in server_reply for keyword in ["Congrats", "The correct temperature"]):
         break


    sock_client.close()

if __name__ == "__main__":
    main()
