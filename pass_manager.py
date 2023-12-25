import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
    host="localhost",
    user=input("Enter the user: "),
    password=input("Enter the password: "),
)

mycursor = mydb.cursor()



mycursor.execute("CREATE DATABASE IF NOT EXISTS pass;")
mycursor.execute("USE pass;")
mycursor.execute("CREATE TABLE IF NOT EXISTS password (application VARCHAR(30) PRIMARY KEY, password VARCHAR(30), date_modified DATE);")
print("Database and table created")
while True:
    print("1.Add a password\n2.Update password\n3.Delete data\n4.Show passwords\n5.delete database\n6.exit")
    choice = input("Enter your choice (1/2/3/4):")

    if choice == "1":
        sql = "INSERT INTO password (application, password,date_modified) VALUES (%s, %s,current_date)"
        a = input("Enter application:")
        p = input("Enter password:")
        val = (a, p)
        mycursor.execute(sql, val)
        mydb.commit()

    elif choice == "2":
        sql = "UPDATE password SET password = %s,date_modified=current_date WHERE application = %s"
        a=input("Enter the name of the application the password needs to be updated:")
        p=input("Enter new password:")
        val=(p,a)
        mycursor.execute(sql,val)
        mydb.commit()

    elif choice == "3":
        print("1.Delete using application name\n2.Delete using password")
        way=input("enter your choice:")

        if(way=="1"):
            sql="DELETE from password WHERE application=%s"
            a=input("application name:")
            val=(a,)
            mycursor.execute(sql,val)
            mydb.commit()

        if(way=="2"):
            sql="DELETE from password WHERE password=%s"
            a=input("password to be deleted:")
            val=(a,)
            mycursor.execute(sql,val)
            mydb.commit()
                      
    elif choice == "4":
        mycursor.execute("SELECT * FROM password;")
        result = mycursor.fetchall()
        for row in result:
            print("Application:", row[0], "Password:", row[1],"Date Modified:", row[2])

    elif choice == "5":
        mycursor.execute("DROP database pass")

    elif choice == "6":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice")

    continue_choice = input("Do you want to continue? (yes/no): ")
    if continue_choice.lower() != "yes":
        print("Exiting the program.")
        break
        
            


mycursor.close()
mydb.close()
