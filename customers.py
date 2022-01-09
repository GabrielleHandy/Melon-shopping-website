"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""
    def __init__(
        self,
        first_name,
        last_name,
        email,
        password
    ):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


    def __repr__(self):

        return f"""Customer: {self.first_name} {self.last_name}\n Email: {self.email}\n Password: {self.password}"""

    # TODO: need to implement this
def read_customers_from_file(filepath):
    """Creates a dictionary of customers from a given txt filename"""
    customers = {}
    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                email,
                password
            ) = line.rstrip().split("|")
            customers[email] = Customer(first_name, last_name, email, password)

    return customers

def get_by_email(email):
    """Gets a customer's info by email"""
    # needs a global dictionary to work
    return customers_list[email]

customers_list = read_customers_from_file("customers.txt")
