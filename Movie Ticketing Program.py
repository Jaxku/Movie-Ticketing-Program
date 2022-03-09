# This routine helps to script to start running and directs the code
def main_routine():
    adult_tickets = 0
    pupil_tickets = 0
    children_tickets = 0
    gift_tickets = 0
    total_sales = 0
    tickets_sold = 0
    ticket_wanted = input("Do you want to sell a ticket? (Yes/No): ").upper()
    while ticket_wanted != "NO":
        ticket = sell_ticket()

        # get the number of tickets wanted in the category chosen
        num_tickets = int(input("How many of these tickets do you want: "))
        confirm = input(f"Confirm purchase of {num_tickets} type {ticket} ticket(s)? (Y/N): ").upper()

        if confirm == "Y":  # Giving user the option to cancel the sale
            price = num_tickets * float(get_price(ticket))
            total_sales += price
            tickets_sold += num_tickets
            if ticket == "A":
                adult_tickets += num_tickets
            elif ticket == "C":
                pupil_tickets += num_tickets
            elif ticket == "S":
                children_tickets += num_tickets
            else:
                gift_tickets += num_tickets

            ticket_wanted = input("\nDo you want to sell another ticket? (Y/N): ").upper()
    print("-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-")
    print(f"The total tickets sold today was {tickets_sold}\n"
          f"This was made up of: \n"
          f"\t{adult_tickets} for adults; and \n"
          f"\t{pupil_tickets} for students; and \n"
          f"\t{children_tickets} for children; and \n"
          f"\t{gift_tickets} gift vouchers \n")
    print(f"Sales for the day came to ${total_sales:.2f}")
    print("Thank you for supporting local art")


def sell_ticket():
    ticket_type_ = input("What kind of ticket do you want: \n"
                         "\ta for Adult, or\n"
                         "\ts for Student, or\n"
                         "\tc for Child, or \n"
                         "\t G for Gift voucher \n"
                         ">> ").upper()  # uppercase to minimise input errors
    return ticket_type_


# Get the price for each ticket in the category of ticket chosen
def get_price(type_):
    prices = [["A", 12.5], ["S", 9], ["C", 7], ["G", 0]]
    for price in prices:
        if price[0] == type_:
            return price[1]


# Main routine
print("Welcome to Indie Art Theatres")
main_routine()
