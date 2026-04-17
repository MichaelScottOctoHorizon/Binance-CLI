import sub_programs.helpers as helpers
import sub_programs.binance_test_net as api

#This function is the main point for the "Binance Spot Trading Platform (CLI Edition)"
def main_application():

    commands_list = [
        {"name":"binance_cli ping", "description": "This command prints the time and date of the server."},
    ]

    while True:

        cli_command = input("\n\tEnter a CLI command here: ")
        commands_menu(cli_command)

        if cli_command in ["exit", "Exit"]:
            break

def commands_menu(command):

    if command == "binance_cli ping":
        api.get_server_time() # Prints out the server time and date


main_application()