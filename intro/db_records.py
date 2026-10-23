approved = [
    {
        "customer_id" : "C001",
        "customer_name" : "Anna Lopez",
        "email_address" : "anna.lopez@example.com",
        "city" : "Manila"
    },
    {
        "customer_id" : "C002",
        "customer_name" : "Peter Ramos",
        "email_address" : "peter.ramos@example.com",
        "city" : "Quezon"
    },
    {
        "customer_id" : "C003",
        "customer_name" : "Carla Mendoza",
        "email_address" : "carla.mendoza@example.com",
        "city" : "Malolos"
    },
    {
        "customer_id" : "C004",
        "customer_name" : "David Flores",
        "email_address" : "david.flores@example.com",
        "city" : "Angeles"
    },
    {
        "customer_id" : "C005",
        "customer_name" : "Sofia Reyes",
        "email_address" : "sofia.reyes@example.com",
        "city" : "San Fernando"
    },
    {
        "customer_id" : "C006",
        "customer_name" : "John Almario",
        "email_address" : "john.michael@example.com",
        "city" : "San Fernando"
    }

]

to_verify = [
    {
        "customer_id" : "C001",
        "customer_name" : "Anna Lopez",
        "email_address" : "anna.lopez@example.com",
        "city" : "Guiguinto"
    },
    {
        "customer_id" : "C002",
        "customer_name" : "Peter Ramos",
        "email_address" : "petro.ramos@example.com",
        "city" : "Pampanga"
    },
    {
        "customer_id" : "C003",
        "customer_name" : "Carla Mendoza",
        "email_address" : "carla.mendoza@example.com",
        "city" : "Baliwag"
    },
    {
        "customer_id" : "C004",
        "customer_name" : "David Flores",
        "email_address" : "david.flores@example.com",
        "city" : "Angeles"
    },
    {
        "customer_id" : "C005",
        "customer_name" : "Sofia Reyes",
        "email_address" : "sofia.reyes@example.com",
        "city" : "San Fernando"
    },
    {
        "customer_id" : "C006",
        "customer_name" : "John Almario",
        "email_address" : "john.john@example.com",
        "city" : "San Fernando"
    }
]

def check_customer_records(db_approved, id, name, email, city):
    for rcrd in db_approved:
        if rcrd["customer_id"] == id:
            if email == rcrd["email_address"]:
                return True
            else:
                return False

def verify_customer_records(approved, to_verify):
    for rcrd in to_verify:
        id = rcrd["customer_id"]
        name = rcrd["customer_name"]
        email = rcrd["email_address"]
        city = rcrd["city"]

        if check_customer_records(approved, id, name, email, city) == False:
            print(f"{name}: invalid")

def main():
    # verify_customer_records()
    verify_customer_records(approved, to_verify)

if __name__ == '__main__':
    main()