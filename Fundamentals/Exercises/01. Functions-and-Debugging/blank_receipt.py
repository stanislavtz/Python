def print_dashes():
    print(dashes)

def print_header():
    print(header)
    print_dashes()

def print_footer():
    print_dashes()
    print(footer)

def print_body():
    print(body)

def print_receipt():
    print_header()
    print_body()
    print_footer()


dashes = '------------------------------'
header = 'CASH RECEIPT'
footer = '© SoftUni'
body = 'Charged to____________________\nReceived by___________________'

print_receipt()