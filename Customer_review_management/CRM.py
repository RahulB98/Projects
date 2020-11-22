from tkinter import *
import os
import mysql.connector
import csv
from tkinter import ttk


root = Tk()
root.title('CRM app')
root.iconbitmap('C:/Users/messi/Downloads/favicon.ico')
root.geometry("400x600")

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=str(os.environ.get('MY_PASSWORD')),
    auth_plugin='mysql_native_password'
)

# Check to see if connection to MySQL was created
# print(mydb)

# Create a cursor and initialize it
my_cursor = mydb.cursor()

# Create database
my_cursor.execute("CREATE DATABASE IF NOT EXISTS CRM1")

# Test to see if database was created
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#	print(db)

# Drop table
# my_cursor.execute("DROP TABLE customers")

# Create a table
my_cursor.execute("USE CRM1")
my_cursor.execute("""CREATE TABLE IF NOT EXISTS customer (
    first_name VARCHAR(255),
	last_name VARCHAR(255),
	zipcode INT(10),
	price_paid DECIMAL(10, 2),
	user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255),
	address_1 VARCHAR(255),
	address_2 VARCHAR(255),
	city VARCHAR(50),
	state VARCHAR(50),
	country VARCHAR(255),
	phone VARCHAR(255),
	payment_method VARCHAR(50),
	discount_code VARCHAR(255)
	)""")

# show table
# my_cursor.execute("SELECT * FROM customers")
# print(my_cursor.description)

# for thing in my_cursor.description:
#	print(thing)

# Clear Text Fields
def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)


# Submit Customer To Database
def add_customer():
    sql_command = "INSERT INTO customer (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(), email_box.get(),
              address1_box.get(), address2_box.get(), city_box.get(), state_box.get(), country_box.get(),
              phone_box.get(), payment_method_box.get(), discount_code_box.get())
    my_cursor.execute(sql_command, values)

    # Commit the changes to the database
    mydb.commit()
    # Clear the fields
    clear_fields()

#WRITE to EXCEL function
def save_excel(result):
    with open("Customer_data.csv", 'a', newline='') as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)


#customer list display function
def customer_list():
    customer_list_query = Tk()
    customer_list_query.title("List of All Customers")
    customer_list_query.iconbitmap('C:/Users/messi/Downloads/favicon.ico')
    customer_list_query.geometry("800x600")

    my_cursor.execute("SELECT * FROM customer")
    result = my_cursor.fetchall()
    #print data
    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(customer_list_query, text=y)
            lookup_label.grid(row=index, column=num)
            num += 1
    #save to excel file button
    save_as_excel = Button(customer_list_query, text="Save in Excel", command=lambda:save_excel(result))
    save_as_excel.grid(row=index+1, column=0, pady=10)

def search_customer():
    search_customers = Tk()
    search_customers.title("Search Customer(s)")
    search_customers.iconbitmap('C:/Users/messi/Downloads/favicon.ico')
    search_customers.geometry("1200x800")
    #update record function
    def update():
        sql_command = """ UPDATE customer SET first_name = %s, last_name = %s,
	    zipcode = %s, price_paid = %s, email = %s, address_1 = %s, address_2 = %s,
	    city = %s, state = %s, country = %s, phone = %s, payment_method = %s, discount_code = %s WHERE user_id = %s"""
        #fetching the modified values
        first_name = first_name_box_edit.get()
        last_name = last_name_box_edit.get()
        zipcode = zipcode_box_edit.get()
        price_paid = price_paid_box_edit.get()
        email = email_box_edit.get()
        address_1 = address1_box_edit.get()
        address_2 = address2_box_edit.get()
        city = city_box_edit.get()
        state = state_box_edit.get()
        country = country_box_edit.get()
        phone = phone_box_edit.get()
        payment_method = payment_method_box_edit.get()
        discount_code = discount_code_box_edit.get()
        ID = user_id_box_edit.get()

        inputs = (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code, ID)
        #making vhanges to record in database
        my_cursor.execute(sql_command, inputs)
        mydb.commit()

        search_customers.destroy()



    #edit data function
    def edit_now(id, row):
        sql2 = "SELECT * FROM customer WHERE user_id = %s"
        name2 = (id,)
        result2 = my_cursor.execute(sql2, name2)
        result2 = my_cursor.fetchall()
        #print(result2)

        row += 1
        # create MAIN FORM to enter customer data
        first_name_edit = Label(search_customers, text="First Name").grid(row=row+1, column=0, padx=10, sticky=W)
        last_name_edit = Label(search_customers, text="Last Name").grid(row=row+2, column=0, padx=10, sticky=W)
        address1_edit = Label(search_customers, text="Address 1").grid(row=row+3, column=0, padx=10, sticky=W)
        address2_edit = Label(search_customers, text="Address 2").grid(row=row+4, column=0, padx=10, sticky=W)
        city_edit = Label(search_customers, text="City").grid(row=row+5, column=0, padx=10, sticky=W)
        state_edit = Label(search_customers, text="State").grid(row=row+6, column=0, padx=10, sticky=W)
        zipcode_edit = Label(search_customers, text="Zipcode").grid(row=row+7, column=0, padx=10, sticky=W)
        country_edit = Label(search_customers, text="Country").grid(row=row+8, column=0, padx=10, sticky=W)
        phone_edit = Label(search_customers, text="Phone Number").grid(row=row+9, column=0, padx=10, sticky=W)
        email_edit = Label(search_customers, text="Email address").grid(row=row+10, column=0, padx=10, sticky=W)
        payment_method_edit = Label(search_customers, text="Payment Method").grid(row=row+11, column=0, padx=10, sticky=W)
        discount_code_edit = Label(search_customers, text="Discount Code").grid(row=row+12, column=0, padx=10, sticky=W)
        price_paid_edit = Label(search_customers, text="Price Paid").grid(row=row+13, column=0, padx=10, sticky=W)
        user_id_edit = Label(search_customers, text="User ID").grid(row=row + 14, column=0, padx=10, sticky=W)

        # Entry Boxes
        global first_name_box_edit
        first_name_box_edit = Entry(search_customers)
        first_name_box_edit.grid(row=row+1, column=1, pady=5)
        first_name_box_edit.insert(0, result2[0][0])
        global last_name_box_edit
        last_name_box_edit = Entry(search_customers)
        last_name_box_edit.grid(row=row+2, column=1, pady=5)
        last_name_box_edit.insert(0, result2[0][1])
        global address1_box_edit
        address1_box_edit = Entry(search_customers)
        address1_box_edit.grid(row=row+3, column=1, pady=5)
        address1_box_edit.insert(0, result2[0][6])
        global address2_box_edit
        address2_box_edit = Entry(search_customers)
        address2_box_edit.grid(row=row+4, column=1, pady=5)
        address2_box_edit.insert(0, result2[0][7])
        global city_box_edit
        city_box_edit = Entry(search_customers)
        city_box_edit.grid(row=row+5, column=1, pady=5)
        city_box_edit.insert(0, result2[0][8])
        global state_box_edit
        state_box_edit = Entry(search_customers)
        state_box_edit.grid(row=row+6, column=1, pady=5)
        state_box_edit.insert(0, result2[0][9])
        global zipcode_box_edit
        zipcode_box_edit = Entry(search_customers)
        zipcode_box_edit.grid(row=row+7, column=1, pady=5)
        zipcode_box_edit.insert(0, result2[0][2])
        global country_box_edit
        country_box_edit = Entry(search_customers)
        country_box_edit.grid(row=row+8, column=1, pady=5)
        country_box_edit.insert(0, result2[0][10])
        global phone_box_edit
        phone_box_edit = Entry(search_customers)
        phone_box_edit.grid(row=row+9, column=1, pady=5)
        phone_box_edit.insert(0, result2[0][11])
        global email_box_edit
        email_box_edit = Entry(search_customers)
        email_box_edit.grid(row=row+10, column=1, pady=5)
        email_box_edit.insert(0, result2[0][5])
        global payment_method_box_edit
        payment_method_box_edit = Entry(search_customers)
        payment_method_box_edit.grid(row=row+11, column=1, pady=5)
        payment_method_box_edit.insert(0, result2[0][12])
        global discount_code_box_edit
        discount_code_box_edit = Entry(search_customers)
        discount_code_box_edit.grid(row=row+12, column=1, pady=5)
        discount_code_box_edit.insert(0, result2[0][13])
        global price_paid_box_edit
        price_paid_box_edit = Entry(search_customers)
        price_paid_box_edit.grid(row=row+13, column=1, pady=5)
        price_paid_box_edit.insert(0, result2[0][3])
        global user_id_box_edit
        user_id_box_edit = Entry(search_customers)
        user_id_box_edit.grid(row=row+14, column=1, pady=5)
        user_id_box_edit.insert(0, result2[0][4])

        save_record = Button(search_customers, text="Update Record", command=update)
        save_record.grid(row=row+15, column=0, pady=2)

    def search_now():
        selectd = drop.get()
        sql = ""
        if selectd == "Search by...":
            test = Label(search_customers, text="Please select one of the listed parameters for the search!")
            test.grid(row=3, column=0)
        elif selectd == "Last Name":
            sql = "SELECT * FROM customer WHERE last_name = %s"
        elif selectd == "Email":
            sql = "SELECT * FROM customer WHERE email = %s"
        elif selectd == "Customer ID":
            sql = "SELECT * FROM customer WHERE user_id = %s"

        searched = search_box.get()
        name = (searched, )
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()
        if not result:
            result = "Record Not Found...."
            searched_label = Label(search_customers, text=result)
            searched_label.grid(row=3, column=0, padx=2, pady=2, columnspan=2)
        else:
            for index, record in enumerate(result):
                num = 0
                index += 2
                id_reference = str(record[4])
                edit_button = Button(search_customers, text="Edit", command=lambda id_reference=id_reference: edit_now(id_reference, index))
                edit_button.grid(row=index, column=num)
                for data in record:
                    searched_label = Label(search_customers, text=data)
                    searched_label.grid(row=index, column=num+1, padx=5, pady=5)
                    num += 1
            save_as_excel = Button(search_customers, text="Save in Excel", command=lambda: save_excel(result))
            save_as_excel.grid(row=index + 1, column=0, pady=10)

    #Entry box to search for customer
    search_box = Entry(search_customers)
    search_box.grid(row=0, column=1, padx=10, pady=10)
    #LAbel for Search box
    search_box_label = Label(search_customers, text="Search cutomer: ")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)
    #Search button
    search_button = Button(search_customers, text="Search", command=search_now)
    search_button.grid(row=1, column=0, padx=10, pady=5)
    #drop down box
    drop = ttk.Combobox(search_customers, value=["Search by...", "Last Name", "Email", "Customer ID"])
    drop.current(0)
    drop.grid(row=0, column=2, padx=2)

#create a LABEL
title_label = Label(root, text="YOUR WARDROBE Customer Database", font=('Helvetica', 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

#create MAIN FORM to enter customer data
first_name_label = Label(root, text="First Name").grid(row=1, column=0, padx=10, sticky=W)
last_name_label = Label(root, text="Last Name").grid(row=2, column=0, padx=10, sticky=W)
address1_label = Label(root, text="Address 1").grid(row=3, column=0, padx=10, sticky=W)
address2_label = Label(root, text="Address 2").grid(row=4, column=0, padx=10, sticky=W)
city_label = Label(root, text="City").grid(row=5, column=0, padx=10, sticky=W)
state_label = Label(root, text="State").grid(row=6, column=0, padx=10, sticky=W)
zipcode_label = Label(root, text="Zipcode").grid(row=7, column=0, padx=10, sticky=W)
country_label = Label(root, text="Country").grid(row=8, column=0, padx=10, sticky=W)
phone_label = Label(root, text="Phone Number").grid(row=9, column=0, padx=10, sticky=W)
email_label = Label(root, text="Email address").grid(row=10, column=0, padx=10, sticky=W)
payment_method_label = Label(root, text="Payment Method").grid(row=11, column=0, padx=10, sticky=W)
discount_code_label = Label(root, text="Discount Code").grid(row=12, column=0, padx=10, sticky=W)
price_paid_label = Label(root, text="Price Paid").grid(row=13, column=0, padx=10, sticky=W)

#Entry Boxes
first_name_box = Entry()
first_name_box.grid(row=1, column=1, pady=5)
last_name_box = Entry()
last_name_box.grid(row=2, column=1, pady=5)
address1_box = Entry()
address1_box.grid(row=3, column=1, pady=5)
address2_box = Entry()
address2_box.grid(row=4, column=1, pady=5)
city_box = Entry()
city_box.grid(row=5, column=1, pady=5)
state_box = Entry()
state_box.grid(row=6, column=1, pady=5)
zipcode_box = Entry()
zipcode_box.grid(row=7, column=1, pady=5)
country_box = Entry()
country_box.grid(row=8, column=1, pady=5)
phone_box = Entry()
phone_box.grid(row=9, column=1, pady=5)
email_box = Entry()
email_box.grid(row=10, column=1, pady=5)
payment_method_box = Entry()
payment_method_box.grid(row=11, column=1, pady=5)
discount_code_box = Entry()
discount_code_box.grid(row=12, column=1, pady=5)
price_paid_box = Entry()
price_paid_box.grid(row=13, column=1, pady=5)

#create BUTTONS
add_button = Button(root, text="Add Customer", command=add_customer)
add_button.grid(row=14, column=0, padx=10, pady=10)
clear_button = Button(root, text="CLear Fields", command=clear_fields)
clear_button.grid(row=14, column=1)
customer_list_button = Button(root, text="Customers List", command=customer_list)
customer_list_button.grid(row=15, column=0, padx=10, pady=10)
search_customer_button = Button(root, text="Search Customer(s)", command=search_customer)
search_customer_button.grid(row=15, column=1, padx=10, sticky=W)

root.mainloop()