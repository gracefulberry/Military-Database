import subprocess as sp
import pymysql
import pymysql.cursors
import getpass
import datetime
import os

try:
    from prettytable import PrettyTable
except:
    os.system("pip3 install PTable")
    from prettytable import PrettyTable

fuel_cost = 100

def get_keys(table):
    key_query = f"SHOW KEYS FROM {table} WHERE Key_name='PRIMARY'"
    cur.execute(key_query)
    rows = cur.fetchall()
    keys = []
    for row in rows:
        keys.append(row["Column_name"])
    return keys

def not_found():
    print('Not Found')

# Display data as table
def display_data(rows):
    x = PrettyTable()
    keys = list(rows[0].keys())
    x.field_names = keys
    for row in rows:
        entry = []
        for k in keys:
            entry.append(row[k])
        x.add_row(entry)
    print(x)

# Find whether a personnel is medic, soldier etc
def get_personnel_spec(id):
    query = "SELECT MEDIC.IDnumber as MEDIC, CIVIL.IDnumber as CIVIL, \
     SOLDIER.IDnumber as SOLDIER, TECH.IDnumber as TECH from MEDIC,CIVIL,SOLDIER,TECH"
    cur = con.cursor()
    cur.execute(query)
    col = cur.fetchall()

    keys = ['SOLDIER','MEDIC','TECH','CIVIL']

    for item in col:
        for k in keys:
            if item[k] == id:
                return k
    return "NULL"

# Get values of a column as a list
def get_values(table,column):
    query = "SELECT {} from {}".format(column,table)
    cur = con.cursor()
    cur.execute(query)
    col = cur.fetchall()
    values = [item[column] for item in col]
    return values

# Check validity of name
def check_name(name):
    for c in name:
        if not c.isalpha() and c != ' ' and c != '.':
            return False
    return True

# Check validity of Date
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Get the data type of a required column
def get_data_type(table,column):
    query = "SELECT COLUMN_NAME,DATA_TYPE from INFORMATION_SCHEMA.COLUMNS \
     where table_schema = 'ASH' and table_name = '{}'".format(table)
    cur = con.cursor()
    cur.execute(query)
    types = cur.fetchall()

    for type in types:
        if type['COLUMN_NAME'] == column:
            return type['DATA_TYPE']
    return "NULL"

#Dispatch (Menu A)
def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == "1"):
        b1()
    elif(ch == "2"):
        b2()
    elif(ch == "3"):
        b3()
    else:
        print("Error: Invalid Option")

#Modification (Menu B1)
def b1():
    

    
    tmp = sp.call('clear', shell=True)

    print ()
    print ("(Modification screen)  Choose your query:")
    print ()
    print ("1. Insert")
    print ("2. Delete")
    print ("3. Update")
    print ("4. Back")
    print ()

    ch = str(input("Enter choice > "))

    tmp = sp.call('clear', shell=True)

    if(ch == "1"):
        c11()
    elif(ch == "2"):
        c12()
    elif(ch == "3"):
        c13()
    elif(ch == "4"):
        return

    else:
        print("Error: Invalid Option")

#Retrieval (Menu B2)
def b2():
    

    
    tmp = sp.call('clear', shell=True)

    print ()
    print ("(Retrieval Screen) Choose your query:")
    print ()
    print ("1. Search Personnel/Vehicles/Materials")
    print ("2. Communication Analysis (Search Messages)")
    print ("3. Get min, max, average & total cost of fuel used in trips")
    print ("4. Back")
    print ()

    ch = str(input("Enter choice > "))

    tmp = sp.call('clear', shell=True)

    if(ch == "1"):
        search()
    elif(ch == "2"):
        c22()
    elif(ch == "3"):
        c23()
    elif(ch == "4"):
        return

    else:
        print("Error: Invalid Option")

#Analysis (Menu B3)
def b3():
    

    
    tmp = sp.call('clear', shell=True)

    print ()
    print ("(Analysis Screen) Choose your query:")
    print ()
    print ("1. Wing-wise Report (For wing x)")
    print ("2. Supervision Report (Specify ID to get Supervisors of ID and Supervisee of ID)")
    print ("3. Get people that can access more than X vehicles in wing Y")
    print ("4. Get list of vehicles where money spent is greater than X")
    print ("5. Back")
    print ()

    ch = str(input("Enter choice > "))

    tmp = sp.call('clear', shell=True)

    if(ch == "1"):
        c31()
    elif(ch == "2"):
        c32()
    elif(ch == "3"):
        c33()
    elif(ch == "4"):
        c34()
    elif(ch == "5"):
        return

    else:
        print("Error: Invalid Option")

#Insertion (Menu C11)
def c11():
    

    
    tmp = sp.call('clear', shell=True)

    print ()
    print ("(Insertion Screen) Choose your query:")
    print ()
    print ("1. Insert Personnel")
    print ("2. Insert Vehicle")
    print ("3. Insert Trip (for vehicle X)")
    print ("4. Insert Material")
    print ("5. Insert Intel (from Soldier with ID X)")
    print ("6. Insert Signal (from Tech with ID X)")
    print ("7. Back")
    print ()

    ch = str(input("Enter choice > "))

    tmp = sp.call('clear', shell=True)

    if(ch == "1"):
        d111()
    elif(ch == "2"):
        d112()
    elif(ch == "3"):
        d113()
    elif(ch == "4"):
        d114()
    elif(ch == "5"):
        d115()
    elif(ch == "6"):
        d116()
    elif(ch == "7"):
        b1()

    else:
        print("Error: Invalid Option")

#Deletion (Menu C12)
def c12():
    

    
    tmp = sp.call('clear', shell=True)

    print ()
    print ("(Deletion Screen) Choose your query:")
    print ()
    print ("1. Delete Personnel")
    print ("2. Delete Vehicle")
    print ("3. Delete Trip")
    print ("4. Delete Material")
    print ("5. Delete Intel")
    print ("6. Delete Signal")
    print ("7. Back")
    print ()

    ch = str(input("Enter choice > "))

    tmp = sp.call('clear', shell=True)

    if(ch == "1"):
        d121()
    elif(ch == "2"):
        d122()
    elif(ch == "3"):
        d123()
    elif(ch == "4"):
        d124()
    elif(ch == "5"):
        d125()
    elif(ch == "6"):
        d126()
    elif(ch == "7"):
        b1()

    else:
        print("Error: Invalid Option")

#Update (Menu C12)
def c13():
    

    
    tmp = sp.call('clear', shell=True)

    print ()
    print ("(Update Screen) Choose your query:")
    print ()
    print ("1. Update Personnel")
    print ("2. Update Vehicle")
    print ("3. Update Trip")
    print ("4. Update Material")
    print ("5. Update Intel")
    print ("6. Update Signal")
    print ("7. Back")
    print ()

    ch = str(input("Enter choice > "))

    tmp = sp.call('clear', shell=True)

    if(ch == "1"):
        d131()
    elif(ch == "2"):
        d132()
    elif(ch == "3"):
        d133()
    elif(ch == "4"):
        d134()
    elif(ch == "5"):
        d135()
    elif(ch == "6"):
        d136()
    elif(ch == "7"):
        b1()

    else:
        print("Error: Invalid Option")

#Search (Menu C21)
def c21():
    

    
    tmp = sp.call('clear', shell=True)

    print ()
    print ("(Search Screen) Choose your query:")
    print ()
    print ("1. Search Personnel")
    print ("2. Search Vehicle")
    print ("3. Search Trip")
    print ("4. Search Material")
    print ("5. Search Wing")
    print ("6. Back")
    print ()

    ch = str(input("Enter choice > "))

    tmp = sp.call('clear', shell=True)

    if(ch == "1"):
        d211()
    elif(ch == "2"):
        d212()
    elif(ch == "3"):
        d213()
    elif(ch == "4"):
        d214()
    elif(ch == "5"):
        d215()
    elif(ch == "6"):
        b2()

    else:
        print("Error: Invalid Option")

#Communication (Menu C22)
def c22():
    

    
    tmp = sp.call('clear', shell=True)

    print ()
    print ("(Communication screen) Choose your query:")
    print ()
    print ("1. Search by String")
    print ("2. Search by Date")
    print ("3. Search by Sender")
    print ("4. Back")
    print ()


    ch = str(input("Enter choice > "))
    tmp = sp.call('clear', shell=True)

    if(ch == "1"):
        d221()
    elif(ch == "2"):
        d222()
    elif(ch == "3"):
        d223()
    elif(ch == "4"):
        b2()

    else:
        print("Error: Invalid Option")

#Get min/max/average/total cost of fuel used in trips (Query 24)
def c23():
    
    
    try:
        print("\nTrip Cost Report")
        print("\nCost of fuel used in trip = Distance/Mileage")
        print("\nAnalysis of the cost of fuel used by Vehicles in Trips:")
        
        query = f"SELECT \
            MIN(Distance/Mileage)*{fuel_cost} as `Min Cost`, \
                MAX(Distance/Mileage)*{fuel_cost} as `Max Cost`, \
                    AVG(Distance/Mileage)*{fuel_cost} as `Average Cost`, \
                        SUM(Distance/Mileage)*{fuel_cost} as `Total Cost` FROM VEHICLE NATURAL JOIN TRIP"
        cur.execute(query)
        rows = cur.fetchall()
        display_data(rows)

    except Exception as e:
        print(e)

    tmp = input("\nEnter any key to CONTINUE>")

#Wing-wise Report (For wing x) (Query C31)
def c31():
    
    
    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Wing-wise Report (Analysis)")
    print ()
    try:
        print("Enter a wing name:")
        print("Air")
        print("Ground") 
        print("Marine") 
        wing = input("> ")

        # get budget
        get_bud = f"SELECT Budget FROM WINGS WHERE Wings='{wing}'"
        cur.execute(get_bud)
        budget = cur.fetchone()["Budget"]
        print()
        print(f"{wing} Wing")
        print(f"Remaining Budget: {budget}")

        # get all values
        get_wing = f"SELECT * FROM BELONGS_TO WHERE WingName='{wing}'"
        cur.execute(get_wing)
        rows = cur.fetchall()
        personnels = list(set([item["IDnumber"] for item in rows]))
        materials = list(set([item["MatName"] for item in rows]))
        vehicles = list(set([(item["ChassisNo"],item["Model"]) for item in rows]))

        # show personnel
        personnel = []
        for pid in personnels:
            pquery = f"SELECT * FROM PERSONNEL WHERE IDnumber={pid}"
            cur.execute(pquery)
            personnel.append(cur.fetchone())
        p_len = len(personnel)
        print(f"\nNumber of Personnel: {p_len}")
        display_data(personnel)

        # show vehicles
        vehicle = []
        for vid in vehicles:
            vquery = f"SELECT * FROM VEHICLE WHERE ChassisNo={vid[0]} AND Model='{vid[1]}'"
            cur.execute(vquery)
            vehicle.append(cur.fetchone())
        v_len = len(vehicle)
        print(f"\nNumber of Vehicles: {v_len}")
        display_data(vehicle)

        #show material
        material = []
        for mid in materials:
            mquery = f"SELECT * FROM MATERIAL WHERE Name='{mid}'"
            cur.execute(mquery)
            material.append(cur.fetchone())
        m_len = len(material)
        print(f"\nTotal types of Materials: {m_len}")
        display_data(material)

    except Exception as e:
        # print("> ",e)
        print("\nNot a valid wing name")

    print()
    tmp=input("Enter any key to CONTINUE>")

#Supervision Report (Specify ID to get Supervisors of ID and Supervisee of ID) (Query C32)
def c32():
    

    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Supervision Report")
    print ()

    try:
        while True:
            pid = input("Enter Personnel's ID: ")
            if pid != '':
                try:
                    pid = int(pid)
                    break
                except ValueError:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")

        #main person
        pquery = f"SELECT * FROM PERSONNEL WHERE IDnumber={pid}"
        print(f"\nPersonnel with ID {pid}")
        cur.execute(pquery)
        main_p = cur.fetchall()
        display_data(main_p)

        #supervisors
        try:
            get_supervisors = f"SELECT * FROM SUPERVISION WHERE IDnumber={pid}"
            cur.execute(get_supervisors)
            supervisors = cur.fetchall()
            supervisor_ids = [item["SIDnumber"] for item in supervisors]
            supervisors = []
            
            for id in supervisor_ids:
                query = f"SELECT * FROM PERSONNEL WHERE IDnumber={id}"
                cur.execute(query)
                supervisors.append(cur.fetchone())

            print(f"\nThe Personnel has {len(supervisors)} supervisor(s):")
            display_data(supervisors)
        except:
            pass

        #supervisees
        try:
            get_supervisees = f"SELECT * FROM SUPERVISION WHERE SIDnumber={pid}"
            cur.execute(get_supervisees)
            supervisees = cur.fetchall()
            supervisee_ids = [item["IDnumber"] for item in supervisees]
            supervisees = []
            
            for id in supervisee_ids:
                query = f"SELECT * FROM PERSONNEL WHERE IDnumber={id}"
                cur.execute(query)
                supervisees.append(cur.fetchone())

            print(f"\nThe Personnel supervises {len(supervisees)} supervisee(s):")
            display_data(supervisees)
        except:
            pass

    except Exception as e:
        print("Could not find that Personnel")

    tmp = input("\nEnter any key to CONTINUE>")

#Get people that can access more than X vehicles (Query C33)
def c33():
    

    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Get List of People with Access to greater than X Vehicles")
    print ()

    try:
        while True:
            x = input("Enter X (integer): ")
            if x != '':
                try:
                    x = int(x)
                    break
                except ValueError:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")
    

        get_people = f"SELECT * FROM PERSONNEL"
        cur.execute(get_people)
        rows = cur.fetchall()
        personnels = list(set([item["IDnumber"] for item in rows]))

        people = []
        for pid in personnels:
            vquery = f"SELECT COUNT(DISTINCT ChassisNo, Model) as vno FROM BELONGS_TO WHERE IDNumber = {pid}"
            cur.execute(vquery)
            vno = cur.fetchone()["vno"]
            if vno is None:
                vno = 0
            if vno > x:
                people.append(pid)

        print("\nNumber of People: ", len(people), "\n")
        dict_people = []
        if len(rows):
            for i in range(len(rows)):
                if rows[i]["IDnumber"] in people:
                    dict_people.append(rows[i])
            display_data(dict_people)

    except Exception as e:
        pass

    print()
    tmp = input("Enter any key to CONTINUE>")

#Get list of vehicles where money spent is greater than X (Query C34)
def c34():
    

    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Get List of Vehicles where Money Spent is Greater than X")
    print ()

    try:
        while True:
            x = input("Enter X: ")
            if x != '':
                try:
                    x = float(x)
                    break
                except ValueError:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")
    
        get_vehicles = f"SELECT * FROM VEHICLE"
        cur.execute(get_vehicles)
        rows = cur.fetchall()
        vehicles = list(set([(item["ChassisNo"],item["Model"]) for item in rows]))
        # print(vehicles)
        vehicle = []
        for vid in vehicles:
            vquery = f"SELECT SUM(Distance/Mileage)*{fuel_cost} as cost FROM VEHICLE NATURAL JOIN TRIP WHERE ChassisNo={vid[0]} AND Model='{vid[1]}'"
            cur.execute(vquery)
            cost = cur.fetchone()["cost"]
            if cost is None:
                cost = 0
            if cost > x:
                vehicle.append(vid)

        print("\nNumber of Vehicles: ", len(vehicle), "\n")
        dict_vehicle = []
        for i in range(len(rows)):
            if (rows[i]["ChassisNo"],rows[i]["Model"]) in vehicle:
                dict_vehicle.append(rows[i])
        display_data(dict_vehicle)
    
    except Exception as e:
        pass

    print()
    tmp=input("Enter any key to CONTINUE>")
    
#Insert Personnel (Query D111)
def d111():
    

    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Insert Personnel (Query)")
    print ()

    try:
        row = {}
        print("Enter new Personnel's details: ")

        while True:
            row["Name"] = input("Name: ")
            if row["Name"] != '' and check_name(row["Name"]):
                row["Name"] = "'" + row["Name"] + "'"
                break
            else:
                print("Enter a valid input")

        while True:
            row["Regiment"] = input("Regiment: ")
            if row["Regiment"] != '':
                row["Regiment"] = "'" + row["Regiment"] + "'"
                break
            else:
                row["Regiment"] = "NULL"
                break

        while True:
            row["Rnk"] = input("Rank (integer): ")
            if row["Rnk"] != '':
                try:
                    row["Rnk"] = int(row["Rnk"])
                    break
                except ValueError:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")

        print()
        query = "INSERT INTO PERSONNEL (Name, Regiment, Rnk) VALUES ({}, {}, {})".format(row["Name"], row["Regiment"], row["Rnk"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
        tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>", e)
        tmp = input("Enter any key to CONTINUE>")
        return

    print()
    try:
        print("This Personnel is - ")
        print("1. a Medic")
        print("2. A Soldier")
        print("3. from the Civil department")
        print("4. from the Tech department")

        while True:
            print()
            try:
                ch = int(input("Enter choice (1-4)> "))
                if ch < 1 or ch > 4:
                    print("Error: Invalid Option")
                    continue
                break
            except:
                print("Error: Invalid Option")

        pquery = "select IDnumber from PERSONNEL order by IDnumber"
        cur.execute(pquery)
        rows = cur.fetchall()
        pid = rows[-1]["IDnumber"]

        squery = ''

        # Medic
        if ch == 1:
            print("Enter Specialization: ")
            spec = input("(Leave blank if no Specialization): ")

            if spec == '':
                spec = "NULL"
            squery = "INSERT INTO MEDIC (IDnumber, Specialization) VALUES ({},'{}')".format(pid, spec)

        # SOLDIER
        elif ch == 2:
            squery = "INSERT INTO SOLDIER (IDnumber) VALUES ({})".format(pid)

        # Civil
        elif ch == 3:
            print("Enter Civil Work Area: ")
            spec = input("(Leave blank if no Specialization): ")

            if spec == '':
                spec == "NULL"
            squery = "INSERT INTO CIVIL (IDnumber, Civil) VALUES ({},'{}')".format(pid, spec)

        # TECH
        elif ch == 4:
            squery = "INSERT INTO TECH (IDnumber) VALUES ({})".format(pid)

        print(squery)
        cur.execute(squery)
        con.commit()
        print("Inserted Into Database")
        tmp = input("Enter any key to CONTINUE>")

        # insert to BELONGS_TO
        tmp = sp.call('clear', shell=True)
        print ()
        print ("Connect this Personnel to a Wing, Vehicle and Material")
        print ()

        isCorrect = False
        while not isCorrect:
            # pid = input("Enter personnel ID: ")
            cno = input("Enter chassis number: ")
            mdl = input("Enter model: ")
            mat = input("Enter material name: ")
            wng = input("Enter wing name: ")
            isCorrect = h1(pid, cno, mdl, mat, wng)

        print("Inserted Into Database")
        tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>", e)
        tmp = input("Enter any key to CONTINUE>")

    try:
        print()
        while True:
            sid = input("Enter Supervisor's ID. (Leave blank if Personnel does not have a supervisor): ")
            if sid != '':
                try:
                    sid = int(sid)
                    sup_query = "INSERT INTO SUPERVISION (SIDnumber,IDnumber) VALUES ({},{})".format(sid,pid)
                    print(sup_query)
                    cur.execute(sup_query)
                    con.commit()
                    print("Inserted into Database")
                    break
                except Exception as ex:
                    print(">", ex)
            else:
                break
        tmp = input("Enter any key to CONTINUE>")
    
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>", e)
        tmp = input("Enter any key to CONTINUE>")

#Insert Vehicle (Query D112)
def d112():
    

    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Insert Vehicle (Query)")
    print ()

    try:
        row = {}
        print("Enter new Vehicle's details: ")

        while True:
            row["ChassisNo"] = input("Chassis Number (integer): ")
            if row["ChassisNo"] != '':
                try:
                    row["ChassisNo"] = int(row["ChassisNo"])
                    break
                except ValueError:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")

        while True:
            row["Model"] = input("Model (4 char only): ")
            if row["Model"] != '' and len(row["Model"]) == 4:
                row["Model"] = "'" + row["Model"] + "'"
                break
            else:
                print("Enter a valid input")

        while True:
            row["Mileage"] = input("Mileage (float): ")
            if row["Mileage"] != '':
                try:
                    row["Mileage"] = float(row["Mileage"])
                    break
                except:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")

        while True:
            row["PassengerCapacity"] = input("Passenger Capacity (integer): ")
            if row["PassengerCapacity"] != '':
                try:
                    row["PassengerCapacity"] = int(row["PassengerCapacity"])
                    break
                except:
                    print("Enter a valid input")
            else:
                row["PassengerCapacity"] = 'NULL'
                break

        print()
        query = "INSERT INTO VEHICLE(ChassisNo, Model, Mileage, PassengerCapacity) VALUES ({}, {}, {}, {})".format(row["ChassisNo"], row["Model"], row["Mileage"], row["PassengerCapacity"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
        tmp = input("Enter any key to CONTINUE>")

        # insert to BELONGS_TO
        tmp = sp.call('clear', shell=True)
        print ()
        print ("Connect this Vehicle to a Wing, Personnel and Material")
        print ()

        isCorrect = False
        while not isCorrect:
            pid = input("Enter personnel ID: ")
            cno = row["ChassisNo"]
            mdl = row["Model"]
            mat = input("Enter material name: ")
            wng = input("Enter wing name: ")
            isCorrect = h1(pid, cno, mdl[1:-1], mat, wng)

        print("Inserted Into Database")
        tmp = input("\nEnter any key to CONTINUE>")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database\n>> ", e)
        tmp = input("\nEnter any key to CONTINUE>")
        return

    try:
        print()
        print("Does the Vehicle have any specific purposes? If so then enter purposes(comma separated)")
        purposes = input("(If not then leave blank): ")
        if purposes != '':
            purposes = purposes.split(',')
            for p in purposes:
                pquery = "INSERT INTO PURPOSES(ChassisNo, Model, Purpose) VALUES (%d, %s, '%s')" % (row["ChassisNo"], row["Model"], p)
                print(pquery)
                cur.execute(pquery)
            con.commit()
            print("Inserted Into Database")
            tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>", e)
        tmp = input("Enter any key to CONTINUE>")

#Insert Trip (for vehicle X) (Query D113)
def d113():
    """
    Trip is an independent table
    """
    try:
        row = {}
        print("Enter Vehicle's details: ")

        while True:
            row["ChassisNo"] = input("Chassis Number (integer): ")
            if row["ChassisNo"] != '':
                try:
                    row["ChassisNo"] = int(row["ChassisNo"])
                    break
                except ValueError:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")

        while True:
            row["Model"] = input("Model (4 char only): ")
            if row["Model"] != '' and len(row["Model"]) == 4:
                row["Model"] = "'" + row["Model"] + "'"
                break
            else:
                print("Enter a valid input")

        while True:
            row["Distance"] = input("Distance (km): ")
            if row["Distance"] != '':
                try:
                    row["Distance"] = float(row["Distance"])
                    break
                except ValueError:
                    print("Enter a valid input - float value")

        print()
        query = "INSERT INTO TRIP(ChassisNo, Model, Distance) VALUES ({}, {}, {})".format(row["ChassisNo"], row["Model"], row["Distance"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
        print("Trip Cost deducted from Budget")
        print()

        chassisnos = get_values("BELONGS_TO","ChassisNo")
        models = get_values("BELONGS_TO","Model")
        wings = get_values("BELONGS_TO","WingName")

        # get Mileage
        temp_query = f"SELECT Mileage FROM VEHICLE WHERE ChassisNo={row['ChassisNo']} and Model={row['Model']}"
        cur.execute(temp_query)
        mileage = cur.fetchone()["Mileage"]

        vid = [(chassisnos[i],models[i]) for i in range(len(models))]

        if (row["ChassisNo"],row["Model"][1:-1]) in vid:
            ind = vid.index((row["ChassisNo"],row["Model"][1:-1]))
            wng = wings[ind]
            get_budget = f"SELECT Budget FROM WINGS WHERE Wings='{wng}'"
            cur.execute(get_budget)
            budget = cur.fetchone()['Budget']

            new_budget = budget - fuel_cost*(row["Distance"]/mileage)
            set_budget = f"UPDATE WINGS SET BUDGET={new_budget} WHERE Wings='{wng}'"
            cur.execute(set_budget)
            con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert trip into database")
        print(">>", e)

    print()
    tmp = input("Enter any key to CONTINUE>")

#Insert Material (Query D114)
def d114():
    """
    MATERIAL should be updated along with
    BELONGS_TO which contains
    `IDnumber`, `ChassisNo`, `Model`, `MatName`, `WingName`
    """
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Insert Material (Query)")
    print ()

    try:
        row = {}
        print("Enter Material details: ")

        while True:
            row["Name"] = input("Material Name: ")
            if row["Name"] != '':
                row["Name"] = "'" + row["Name"] + "'"
                break
            else:
                print("Enter a valid input")

        while True:
            row["Quantity"] = input("Quantity (integer): ")
            if row["Quantity"] != '':
                try:
                    row["Quantity"] = int(row["Quantity"])
                    break
                except ValueError:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")

        while True:
            row["Cost"] = input("Cost: ")
            if row["Cost"] != '':
                try:
                    row["Cost"] = float(row["Cost"])
                    break
                except ValueError:
                    print("Enter a valid input - float value")

        print()
        query = "INSERT INTO MATERIAL(Name, Quantity, Cost) VALUES ({}, {}, {})".format(row["Name"], row["Quantity"], row["Cost"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
        tmp = input("Enter any key to CONTINUE>")

        # insert to BELONGS_TO
        tmp = sp.call('clear', shell=True)
        print ()
        print ("Connect this material to a Wing, Personnel and Vehicle")
        print ()

        isCorrect = False
        while not isCorrect:
            pid = input("Enter personnel ID: ")
            cno = input("Enter chassis number: ")
            mdl = input("Enter model: ")
            mat = row["Name"]
            wng = input("Enter wing name: ")
            isCorrect = h1(pid, cno, mdl, mat[1:-1], wng)

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert material into database")
        print(">>", e)

    tmp = input("Enter any key to CONTINUE>")

#Insert Intel (for Soldier with ID X and Soldier with ID Y) (Query D115)
def d115():
    """

    """
    tmp = sp.call('clear', shell=True)
    print()
    print ("Insert Intel (Query)")
    print ()

    try:
        row = {}
        print("Enter new Intel's details: ")

        while True:
            row["IDnumber"] = input("Soldier ID (sender): ")
            if row["IDnumber"] != '':
                try:
                    row["IDnumber"] = int(row["IDnumber"])
                    break
                except ValueError:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")

        row["Date"] = "'" + str(datetime.date.today()) + "'"

        row["Time"] = "'" + str(datetime.datetime.now().strftime("%H:%M:%S")) + "'"

        while True:
            row["Content"] = input("Intel content: ")
            if row["Content"] != '':
                row["Content"] = "'" + row["Content"] + "'"
                break
            else:
                print("Enter a valid input")

        print()
        query = "INSERT INTO INTEL (IDnumber, Date, Time, Content) VALUES ({}, {}, {}, {})".format(row["IDnumber"], row["Date"], row["Time"], row["Content"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")


    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>", e)

    tmp = input("Enter any key to CONTINUE>")

#Insert Signal (for Tech with ID X and Tech with ID Y) (Query D116)
def d116():
    """

    """
    tmp = sp.call('clear', shell=True)
    print()
    print ("Insert Signal (Query)")
    print ()

    try:
        row = {}
        print("Enter new Signal's details: ")

        while True:
            row["IDnumber"] = input("Tech ID (sender): ")
            if row["IDnumber"] != '':
                try:
                    row["IDnumber"] = int(row["IDnumber"])
                    break
                except ValueError:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")

        row["Date"] = "'" + str(datetime.date.today()) + "'"

        row["Time"] = "'" + str(datetime.datetime.now().strftime("%H:%M:%S")) + "'"

        while True:
            row["Content"] = input("Signal content: ")
            if row["Content"] != '':
                row["Content"] = "'" + row["Content"] + "'"
                break
            else:
                print("Enter a valid input")

        print()
        query = "INSERT INTO SIG (IDnumber, Date, Time, Content) VALUES ({}, {}, {}, {})".format(row["IDnumber"], row["Date"], row["Time"], row["Content"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")


    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>", e)

    tmp = input("Enter any key to CONTINUE>")

#Update Personnel (Query D131)
def d131():
    """

    """
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Update Personnel (Query)")
    print ()

    try:
        while True:
            pid = input("Enter Personnel's ID: ")
            if pid != '':
                try:
                    pid = int(pid)
                    break
                except ValueError:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")

        get_row = "SELECT * FROM PERSONNEL WHERE IDnumber={}".format(pid)
        cur.execute(get_row)
        row = cur.fetchall()
        print("Personnel details:")
        print()
        print("Table Name - PERSONNEL")
        display_data(row)
        
        tab = get_personnel_spec(pid)
        get_tab = f"SELECT * FROM {tab} WHERE IDnumber={pid}"
        cur.execute(get_tab)
        spec_row = cur.fetchall()
        print(f"Table Name - {tab}")
        display_data(spec_row)
        
        print()
        print("Do not modify IDnumber.")
        keys = get_keys("PERSONNEL")
        table = input("Name of the table you wish to modify: ")
        col = input("Name of the column you wish to modify: ")

        if col in keys:
            print("\nCannot update the primary key")
            tmp = input("\nEnter any key to CONTINUE>")
            return

        val = input("New value: ")
        
        type = get_data_type(table,col)

        if val != "NULL" and (type == 'varchar' or type == 'char'):
            val = "'" + val + "'"

        query = "UPDATE {} SET {}={} WHERE IDnumber={}".format(table,col,val,pid)
        print(query)
        cur.execute(query)
        con.commit()
        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">> ",e)

    tmp = input("Enter any key to CONTINUE>")

#Update Vehicle (Query D132)
def d132():
    """

    """
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Update Vehicle (Query)")
    print ()

    try:
        while True:
            pid1 = input("Enter Vehicle's Chassis Number: ")
            if pid1 != '':
                try:
                    pid1 = int(pid1)
                    print ()
                except ValueError:
                    print ("Enter a valid input")
                    continue
            else:
                print ("Enter a valid input")
                continue

            pid2 = input("Enter Vehicle's Model: ")
            if pid2 != '' and len(pid2) == 4:
                pid2 = "'" + pid2 + "'"
                break
            else:
                print ("Enter a valid input")
                print ()

        get_row = "SELECT * FROM VEHICLE WHERE ChassisNo={} and Model={}".format(pid1, pid2)
        cur.execute(get_row)
        row = cur.fetchall()
        print("Vehicle details:")
        display_data(row)
        print()

        # p_cno = get_values("PURPOSES","ChassisNo")
        # p_mdl = get_values("PURPOSES","Model")
        # p_prp = get_values("PURPOSES","Purpose")

        # purposes = []

        # for i in range(len(p_cno)):
        #     if p_cno[i] == pid1 and p_mdl[i] == pid2:
        #         purposes.append(p_prp[i])

        # if len(purposes) > 0:
        #     print("Table name - PURPOSES: ")
        #     print("Column name - Purspose")
        #     for p in purposes:
        #         print(p)
        # print()

        print()
        print("Do not modify Chassis Number and Model.")
        # table = input("Name of the table you wish to modify: ")
        table = "VEHICLE"
        col = input("\nName of the column you wish to modify: ")

        keys = get_keys("VEHICLE")
        if col in keys:
            print("\nCannot update the primary key")
            tmp = input("\nEnter any key to CONTINUE>")
            return
        
        val = input("New value: ")

        type = get_data_type(table,col)

        if val != "NULL" and (type == 'varchar' or type == 'char'):
            val = "'" + val + "'"

        query = "UPDATE {} SET {}={} WHERE ChassisNo={} and Model={}".format(table,col,val,pid1,pid2)
        print(query)
        cur.execute(query)
        con.commit()
        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">> ",e)
        
    tmp=input("Enter any key to CONTINUE>")

#Update Trip (Query D133)
def d133():
    """
    """
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Update Trip (Query)")
    print ()

    try:
        while True:
            pid = input("Enter Reciept Number: ")
            if pid != '':
                try:
                    pid = int(pid)
                    print ()
                    break
                except ValueError:
                    print ("Enter a valid input")
                    continue
            else:
                print ("Enter a valid input")
                continue

        get_row = "SELECT * FROM TRIP WHERE RecieptNumber={}".format(pid)
        cur.execute(get_row)
        row = cur.fetchall()
        print("Trip details:")
        display_data(row)
        print()
        
        print("Enter the following details: \n")
        while True:
            dist = input("Enter new distance: ")
            if dist != '':
                try:
                    dist = float(dist)
                    print()
                    break
                except ValueError:
                    print ("Enter a valid input")
                    continue
            else:
                print ("Enter a valid input")
                continue
        
        try:
            get_vehicle = f"SELECT Distance,ChassisNo,Model,Mileage FROM TRIP NATURAL JOIN VEHICLE WHERE RecieptNumber={pid}"
            cur.execute(get_vehicle)
            details = cur.fetchall()[0]
            if details != ():
                old_dist, mileage, cno, mdl = details["Distance"], details["Mileage"], details["ChassisNo"],details["Model"]
                chassisnos = get_values("BELONGS_TO","ChassisNo")
                models = get_values("BELONGS_TO","Model")
                wings = get_values("BELONGS_TO","WingName")
                vid = [(chassisnos[i],models[i]) for i in range(len(models))]
                if (cno,mdl) in vid:
                    ind = vid.index((cno,mdl))
                    wng = wings[ind]
                    get_budget = f"SELECT Budget FROM WINGS WHERE Wings='{wng}'"
                    cur.execute(get_budget)
                    budget = cur.fetchone()['Budget']
                    old_cost = fuel_cost*(old_dist/mileage)
                    new_cost = fuel_cost*(dist/mileage)
                    new_budget = budget + old_cost - new_cost
                    set_budget = f"UPDATE WINGS SET BUDGET={new_budget} WHERE Wings='{wng}'"
                    cur.execute(set_budget)
                    con.commit()
                    print(f"\nTrip cost updated in {wng} Wing Budget")
        except Exception as e:
            con.rollback()
            print(e)
            pass

        query = "UPDATE TRIP SET Distance={} WHERE RecieptNumber={}".format(dist, pid)
        print(query)
        cur.execute(query)
        con.commit()
        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">> ",e)
    tmp = input("\nEnter any key to CONTINUE>")

# Update material
def d134():
    
    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Update Material (Query)")
    print ()

    try:
        while True:
            name = input("Enter material name: ")
            if name != '':
                name = "'" + name + "'"
                break
            else:
                print ("Enter a valid input")
                print ()

        get_row = "SELECT * FROM MATERIAL WHERE Name={}".format(name)
        cur.execute(get_row)
        row = cur.fetchall()
        print("Material details: ")
        display_data(row)
        print()

        while True:
            qnt = input("Enter quantity: ")
            if qnt != '':
                try:
                    qnt = int(qnt)
                    print ()
                except ValueError:
                    print ("Enter a valid input")
                    continue
            else:
                print ("Enter a valid input")
                continue

            cost = input("Enter cost: ")
            if cost != '':
                try:
                    cost = float(cost)
                    print ()
                    break
                except ValueError:
                    print ("Enter a valid input")
            else:
                print ("Enter a valid input")

        query = "UPDATE MATERIAL SET Quantity={}, Cost={} WHERE Name={}".format(qnt, cost, name)
        print(query)
        cur.execute(query)
        con.commit()
        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">> ",e)
        
    tmp=input("Enter any key to CONTINUE>")

# Update Intel
def d135():
    
    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Update Intel (Query)")
    print ()

    try:
        while True:
            pid = input("Enter IDnumber: ")
            if pid != '':
                try:
                    pid = int(pid)
                    print ()
                    break
                except ValueError:
                    print ("Enter a valid input")
                    continue
            else:
                print ("Enter a valid input")
                continue

        get_row = "SELECT * FROM INTEL WHERE IDnumber={}".format(pid)
        cur.execute(get_row)
        row = cur.fetchall()

        if row == ():
            print("This personnel did not send any Intel")
            print()
        else:
            print("Intel details:")
            display_data(row)
            print()

            msg = input("Enter new message: ")
            print()
            msg = "'" + msg + "'"
            # dt = "'" + str(datetime.date.today()) + "'"
            # tm = "'" + str(datetime.datetime.now().strftime("%H:%M:%S")) + "'"

            query = "UPDATE INTEL SET Content={} WHERE IDnumber={}".format(msg, pid)
            print(query)
            print()
            cur.execute(query)
            con.commit()
            print("Updated Database")
            print()

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">> ",e)
    tmp = input("Enter any key to CONTINUE>")

# Update signal
def d136():
    
    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Update Signal (Query)")
    print ()

    try:
        while True:
            pid = input("Enter IDnumber: ")
            if pid != '':
                try:
                    pid = int(pid)
                    print ()
                    break
                except ValueError:
                    print ("Enter a valid input")
                    continue
            else:
                print ("Enter a valid input")
                continue

        get_row = "SELECT * FROM SIG WHERE IDnumber={}".format(pid)
        cur.execute(get_row)
        row = cur.fetchall()

        if row == ():
            print("This personnel did not send any Signals")
            print()
        else:
            print("Signal details:")
            display_data(row)
            print()

            msg = input("Enter new message: ")
            print()
            msg = "'" + msg + "'"
            # dt = "'" + str(datetime.date.today()) + "'"
            # tm = "'" + str(datetime.datetime.now().strftime("%H:%M:%S")) + "'"

            query = "UPDATE SIG SET Content={} WHERE IDnumber={}".format(msg, pid)
            print(query)
            print()
            cur.execute(query)
            con.commit()
            print("Updated Database")
            print()

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">> ",e)
    tmp = input("Enter any key to CONTINUE>")    

# Delete Personnel
def d121():
    """
    """
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Delete personnel (Query)")
    print ()

    row = {}
    print("Deletes based on primary key")

    while True:
        row["IDnumber"] = input("Enter personnel ID: ")
        if row["IDnumber"] != '':
            try:
                row["IDnumber"] = int(row["IDnumber"])
                break
            except ValueError:
                print("Enter valid input")
        else:
            print("Enter valid input")

    print()
    tablenames = ["SUPERVISION", "INTEL", "SIG", "MEDIC", "CIVIL", "SOLDIER", "TECH", "BELONGS_TO"]
    for table in tablenames:
        try:
            query = "DELETE FROM {} WHERE IDnumber={}".format(table, row["IDnumber"])
            print(query)
            cur.execute(query)
            if table == "SUPERVISION":
                query = "DELETE FROM {} WHERE SIDnumber={}".format(table, row["IDnumber"])
                print(query)
                cur.execute(query)

        except Exception as e:
            print("Failed to delete from ")
            print(">>", e)

    try:
        print()
        query = "DELETE FROM PERSONNEL WHERE IDnumber={}".format(row["IDnumber"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Deleted from database")
    
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>", e)

    tmp = input("Enter any key to CONTINUE")

# Delete Vehicle
def d122():
    
    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Delete vehicle (Query)")
    print ()

    row = {}
    print("Deletes based on primary key")

    while True:
        row["ChassisNo"] = input("Chassis Number (integer): ")
        if row["ChassisNo"] != '':
            try:
                row["ChassisNo"] = int(row["ChassisNo"])
                break
            except ValueError:
                print("Enter a valid input")
        else:
            print("Enter a valid input")

    while True:
        row["Model"] = input("Model (4 char only): ")
        if row["Model"] != '' and len(row["Model"]) == 4:
            row["Model"] = "'" + row["Model"] + "'"
            break
        else:
            print("Enter a valid input")

    print()
    tablenames = ["TRIP", "PURPOSES", "BELONGS_TO"]
    for table in tablenames:
        try:
            query = "DELETE FROM {} WHERE ChassisNo={} and Model={}".format(table, row["ChassisNo"], row["Model"])
            print(query)
            cur.execute(query)

        except Exception as e:
            con.rollback()
            print("Failed to delete from ")
            print(">>", e)

    try:
        print()
        query = "DELETE FROM VEHICLE WHERE ChassisNo={} and Model={}".format(row["ChassisNo"], row["Model"])
        print(query)
        cur.execute(query)

        con.commit()
        print("Deleted from database")
    
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")

    tmp = input("Enter any key to CONTINUE")

# Delete trip
def d123():
    
    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Delete trip (Query)")
    print ()

    row = {}
    print("Deletes based on primary key")

    while True:
        row["RecieptNumber"] = input("Enter reciept ID: ")
        if row["RecieptNumber"] != '':
            try:
                row["RecieptNumber"] = int(row["RecieptNumber"])
                break
            except ValueError:
                print("Enter valid input")
        else:
            print("Enter valid input")

    try:
        #check if trip exist
        try:
            get_vehicle = f"SELECT Distance,ChassisNo,Model,Mileage FROM TRIP NATURAL JOIN VEHICLE WHERE RecieptNumber={row['RecieptNumber']}"
            cur.execute(get_vehicle)
            details = cur.fetchall()[0]
            if details != ():
                dist, mileage, cno, mdl = details["Distance"], details["Mileage"], details["ChassisNo"],details["Model"]
                chassisnos = get_values("BELONGS_TO","ChassisNo")
                models = get_values("BELONGS_TO","Model")
                wings = get_values("BELONGS_TO","WingName")
                vid = [(chassisnos[i],models[i]) for i in range(len(models))]
                if (cno,mdl) in vid:
                    ind = vid.index((cno,mdl))
                    wng = wings[ind]
                    get_budget = f"SELECT Budget FROM WINGS WHERE Wings='{wng}'"
                    cur.execute(get_budget)
                    budget = cur.fetchone()['Budget']

                    new_budget = budget + fuel_cost*(dist/mileage)
                    set_budget = f"UPDATE WINGS SET BUDGET={new_budget} WHERE Wings='{wng}'"
                    cur.execute(set_budget)
                    con.commit()
                    print(f"\nTrip cost refunded to {wng} Wing Budget")
        except:
            con.rollback()
            pass
        print()
        query = "DELETE FROM TRIP WHERE RecieptNumber={}".format(row["RecieptNumber"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Deleted from database")
    
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>", e)

    tmp = input("Enter any key to CONTINUE")

# Delete material
def d124():
    
    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Delete material (Query)")
    print ()

    row = {}
    print("Deletes based on primary key")

    while True:
        row["Name"] = input("Material name: ")
        if row["Name"] != '' and check_name(row["Name"]):
            row["Name"] = "'" + row["Name"] + "'"
            break
        else:
            print("Enter a valid input")

    print()
    tablenames = ["BELONGS_TO"]
    for table in tablenames:
        try:
            query = "DELETE FROM {} WHERE MatName={}".format(table, row["Name"])
            print(query)
            cur.execute(query)

        except Exception as e:
            print("Failed to delete from ")
            print(">>", e)

    try:
        print()
        query = "DELETE FROM MATERIAL WHERE Name={}".format(row["Name"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Deleted from database")
    
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>", e)

    tmp = input("Enter any key to CONTINUE")

# Delete intel
def d125():
    
    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Delete intel (Query)")
    print ()

    row = {}
    print("Deletes based on primary key")

    while True:
        row["IDnumber"] = input("Enter sender's ID: ")
        if row["IDnumber"] != '':
            try:
                row["IDnumber"] = int(row["IDnumber"])
                break
            except ValueError:
                print("Enter valid input")
        else:
            print("Enter valid input")

    try:
        print()
        query = "DELETE FROM INTEL WHERE IDnumber={}".format(row["IDnumber"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Deleted from database")
    
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>", e)

    tmp = input("Enter any key to CONTINUE")

# Delete signal
def d126():
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Delete signal (Query)")
    print ()

    row = {}
    print("Deletes based on primary key")

    while True:
        row["IDnumber"] = input("Enter sender's ID: ")
        if row["IDnumber"] != '':
            try:
                row["IDnumber"] = int(row["IDnumber"])
                break
            except ValueError:
                print("Enter valid input")
        else:
            print("Enter valid input")

    try:
        print()
        query = "DELETE FROM SIG WHERE IDnumber={}".format(row["IDnumber"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Deleted from database")
    
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>", e)

    tmp = input("Enter any key to CONTINUE")

# General search query
def search():
    print("\nSearch (Query)")
    print("\nSearch for:")
    print("1. Personnel \n2. Vehicles \n3. Materials")
    
    try:
        while True:
            ch = input("\nEnter choice: ")
            try:
                ch = int(ch)
                if not ch in range(1,4):
                    print("Enter valid input")
                    continue
                break
            except:
                print("Enter valid input")
        
        choices = ["PERSONNEL","VEHICLE","MATERIAL"]
        table = choices[ch-1]

        print("\nList of attributes you can search by:")
        temp_query = f"SELECT * FROM {table}"
        cur.execute(temp_query)
        temp = cur.fetchone()
        cols = list(temp.keys())
        for col in cols:
            print(col)
        
        column = input("\nName of attribute: ")
        val = input(f"\nValue to be searched ({get_data_type(table,column)}): ")

        dt = get_data_type(table,column)

        if dt == 'char' or dt == 'varchar':
            val = "'" + val + "'"
        
        query = ""
        if column == "Quantity" or column == "Cost" or column == "Mileage" or column == "PassengerCapacity":
            query = f"SELECT * FROM {table} WHERE {column}>={val}"
            print("\nDisplaying everything with value greater than or equal to the value you specified:")
        elif get_data_type(table,column) == 'varchar' or get_data_type(table,column) == 'char':
            temp_val = "'%" + val[1:-1] + "%'"
            query = f"SELECT * FROM {table} WHERE {column} LIKE {temp_val}"
        else:
            query = f"SELECT * FROM {table} WHERE {column}={val}"
        cur.execute(query)
        rows = cur.fetchall()

        if table == "PERSONNEL":
            for i in range(len(rows)):
                rows[i]["Department"] = get_personnel_spec(rows[i]["IDnumber"])

        if table == "VEHICLE":
            for i in range(len(rows)):
                temp_query = f"SELECT Purpose FROM PURPOSES WHERE ChassisNo={rows[i]['ChassisNo']} and Model='{rows[i]['Model']}'"
                cur.execute(temp_query)
                pur = cur.fetchall()
                pur = [item["Purpose"] for item in pur]
                rows[i]["Purposes"] = ", ".join(pur)
        display_data(rows)
    
    except Exception as e:
        print("\nSearch failed")

    tmp = input("\nEnter any key to CONTINUE>")

#Search Personnel (Query D211)
def d211():
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Search Personnel (Query)")
    print ()

    try:
        while True:
            pid = input("Enter Personnel's ID: ")
            if pid != '':
                try:
                    pid = int(pid)
                    break
                except ValueError:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")


        get_row = "SELECT * FROM PERSONNEL WHERE IDnumber={}".format(pid)
        cur.execute(get_row)
        row = cur.fetchall()
        print("Personnel details:")
        display_data(row)
        table = ''
        msg = ""
        get_spec = get_personnel_spec(pid)
        if get_spec == "MEDIC":
            table = "MEDIC"
            msg = "Personnel is a Medic"
        elif get_spec == "TECH":
            table = "TECH"
            msg = "Personnel is from the Tech department"
        elif get_spec == "CIVIL":
            table = "CIVIL"
            msg = "Personnel is from the Civil department"
        elif get_spec == "SOLDIER":
            table = "SOLDIER"
            msg = "Personnel is a Soldier"

        print(msg)
        spec_query = f"select * from {table} where IDnumber={pid}"
        cur.execute(spec_query)
        spec_row = cur.fetchone()
        if get_spec == 'MEDIC' or get_spec == "CIVIL":
            display_data([spec_row])

    except Exception as e:
        con.rollback()
        not_found()
        print(">> ",e)

    tmp = input("Enter any key to CONTINUE>")

#Search Vehicle (Query D212)
def d212():
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Search Vehicle (Query)")
    print ()

    try:
        while True:
            pid1 = input("Enter Vehicle's Chassis Number: ")
            if pid1 != '':
                try:
                    pid1 = int(pid1)
                    print ()
                except ValueError:
                    print ("Enter a valid input")
                    continue
            else:
                print ("Enter a valid input")
                continue

            pid2 = input("Enter Vehicle's Model: ")
            if pid2 != '' and len(pid2) == 4:
                break
            else:
                print ("Enter a valid input")
                print ()

        get_row = "SELECT * FROM VEHICLE WHERE ChassisNo={} and Model='{}'".format(pid1, pid2)
        cur.execute(get_row)
        row = cur.fetchall()
        print("Vehicle details:")
        display_data(row)
        print()

        p_cno = get_values("PURPOSES","ChassisNo")
        p_mdl = get_values("PURPOSES","Model")
        p_prp = get_values("PURPOSES","Purpose")

        purposes = []

        for i in range(len(p_cno)):
            if p_cno[i] == pid1 and p_mdl[i] == pid2:
                purposes.append(p_prp[i])

        if len(purposes) > 0:
            print("Purposes:")
            for p in purposes:
                print(p)
        print()

    except Exception as e:
        con.rollback()
        not_found()
        print(">> ",e)
    tmp=input("Enter any key to CONTINUE>")

#Search Trip (Query D213)
def d213():
    

    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Search Trip (Query)")
    print ()

    try:
        while True:
            tid = input("Enter Trip Reciept ID: ")
            if tid != '':
                try:
                    tid = int(tid)
                    break
                except ValueError:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")

        get_row = "SELECT * FROM TRIP WHERE RecieptNumber={}".format(tid)
        cur.execute(get_row)
        row = cur.fetchall()
        print("Trip details:")
        display_data(row)
        cost = row[0]["Distance"]*fuel_cost
        print(f"Trip cost is {cost} (fuel cost is {fuel_cost} per km)")
        print()

    except Exception as e:
        con.rollback()
        not_found()
        print(">> ",e)

    tmp=input("Enter any key to CONTINUE>")

#Search Material (Query D214)
def d214():
    

    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Search Material (Query)")
    print ()

    try:
        while True:
            mid = input("Enter Material Name: ")
            if mid != '':
                break
            else:
                print("Enter a valid input")

        get_row = "SELECT * FROM MATERIAL WHERE Name='{}'".format(mid)
        cur.execute(get_row)
        row = cur.fetchall()
        print("Material details:")
        display_data(row)
        print()

    except Exception as e:
        con.rollback()
        not_found()
        print(">> ",e)

    tmp=input("Enter any key to CONTINUE>")

# Search Wing (Query D216)
def d215():
    

    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Search Wing (Query)")
    print ()

    try:
        while True:
            wng = input("Enter Wing Name: ")
            if wng != '':
                break
            else:
                print("Enter a valid input")

        get_row = "SELECT * FROM WINGS WHERE Wings='{}'".format(wng)
        cur.execute(get_row)
        row = cur.fetchall()
        print("Material details:")
        display_data(row)
        print()

    except Exception as e:
        con.rollback()
        not_found()
        print(">> ",e)

    tmp=input("Enter any key to CONTINUE>")

#Search by string (Query D221)
def d221():
    
    
    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Search by String (Query)")
    print ()

    try:
        while True:
            cont = input("Enter Part of message to be searched: ")
            if cont != '':
                break
            else:
                print("Enter a valid input")
        print()
        get_intel = "SELECT * FROM INTEL"
        get_signal = "SELECT * FROM SIG"
        cur.execute(get_intel)
        intel = cur.fetchall()
        cur.execute(get_signal)
        signal = cur.fetchall()

        signals = []
        intels = []

        for inl in intel:
            if cont in inl["Content"]:
                intels.append(inl)
        for sig in signal:
            if cont in sig["Content"]:
                signals.append(sig)

        if len(signals) > 0:
            print("Signals found:")
            display_data(signals)
        print()
        if len(intels) > 0:
            print("Intels found:")
            display_data(intels)

        if len(signals) == 0 and len(intels) == 0:
            not_found()

    except Exception as e:
        con.rollback()
        not_found()
        print(">> ",e)

    print()
    tmp=input("Enter any key to CONTINUE>")

#Search by date (Query D222)
def d222():
    

    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Search by Date (Query)")
    print ()

    try:
        while True:
            pid = input("Enter date (YYYY-MM-DD): ")
            if validate_date(pid):
                break
            else:
                print("Enter a valid input")
        print()

        get_intel = "SELECT * FROM INTEL"
        get_signal = "SELECT * FROM SIG"
        cur.execute(get_intel)
        intel = cur.fetchall()
        cur.execute(get_signal)
        signal = cur.fetchall()

        signals = []
        intels = []

        for inl in intel:
            if datetime.datetime.strptime(pid, '%Y-%m-%d') == datetime.datetime.strptime(str(inl["Date"]), '%Y-%m-%d'):
                intels.append(inl)
        for sig in signal:
            if datetime.datetime.strptime(pid, '%Y-%m-%d') == datetime.datetime.strptime(str(sig["Date"]), '%Y-%m-%d'):
                signals.append(sig)

        if len(signals) > 0:
            print("Signals found:")
            display_data(signals)
        print()
        if len(intels) > 0:
            print("Intels found:")
            display_data(intels)

        if len(signals) == 0 and len(intels) == 0:
            not_found()

    except Exception as e:
        con.rollback()
        not_found()
        print(">> ",e)

    tmp = input("Enter any key to CONTINUE>")

#Search by sender (Query D223)
def d223():
    
    
    
    tmp = sp.call('clear', shell=True)
    print ()
    print ("Search by Sender (Query)")
    print ()

    try:
        while True:
            pid = input("Enter ID of Sender: ")
            if pid != '':
                pid = int(pid)
                break
            else:
                print("Enter a valid input")
        print()
        get_intel = "SELECT * FROM INTEL"
        get_signal = "SELECT * FROM SIG"
        cur.execute(get_intel)
        intel = cur.fetchall()
        cur.execute(get_signal)
        signal = cur.fetchall()

        signals = []
        intels = []

        for inl in intel:
            if pid == inl["IDnumber"]:
                intels.append(inl)
        for sig in signal:
            if pid == sig["IDnumber"]:
                signals.append(sig)

        if len(signals) > 0:
            print("Signals found:")
            display_data(signals)
        print()
        if len(intels) > 0:
            print("Intels found:")
            display_data(intels)
        
        if len(signals) == 0 and len(intels) == 0:
            not_found()

    except Exception as e:
        con.rollback()
        not_found()
        print(">> ",e)

    print()
    tmp=input("Enter any key to CONTINUE>")

#Add a Relationship between Personnel, Vehicle, Material and Wing (Query )
def h1(pid, cno, mdl, mat, wng):
    """
    Only have to make sure that
    there is only one wing per
    personnel and vehicle
    """
    try:
        cur = con.cursor()
        print()

        chassisnos = get_values("BELONGS_TO","ChassisNo")
        models = get_values("BELONGS_TO","Model")

        if wng is None:
            print("This is an invalid input")
            return False

        if pid is None and (cno is None or mdl is None) and mat is None:
            print("This is an invalid input")
            return False

        if pid is not None:
            try:
                pid = int(pid)
            except:
                print("Enter valid Personnel ID")
                return False
            if pid in get_values("BELONGS_TO","IDnumber"):
                pquery = "SELECT * FROM BELONGS_TO WHERE IDnumber={}".format(pid)
                cur.execute(pquery)
                p_row = cur.fetchall()[0]
                if p_row["WingName"] != wng:
                    print(f"Personnel cannot belong to two wings. Already in {p_row['WingName']} wing")
                    return False
        else:
            pid = "NULL"

        if cno is not None and mdl is not None:
            try:
                cno = int(cno)
            except:
                print("Enter valid Chassis No")
                return False
            mdl = "'" + mdl + "'"
            if (cno,mdl[1:-1]) in [(chassisnos[i],models[i]) for i in range(len(models))]:
                cquery = "SELECT * FROM BELONGS_TO WHERE ChassisNo={} and Model={}".format(cno,mdl)
                cur.execute(cquery)
                c_row = cur.fetchall()[0]
                if c_row["WingName"] != wng:
                    print("Vehicle cannot belong to two wings")
                    return False
        else:
            cno = "NULL"
            mdl = "NULL"

        if mat is None:
            mat = "NULL"
        else:
            mat = "'" + mat + "'"

        query = "INSERT INTO BELONGS_TO (IDnumber, ChassisNo, Model, MatName, WingName) VALUES ({},{},{},{},'{}')".format(pid,cno,mdl,mat,wng)
        print(query)
        cur.execute(query)
        con.commit()
        return True

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>", e)
        return False

# Global
while(1):
    tmp = sp.call('clear', shell=True)

    username = input("Username: ")
    password = getpass.getpass("Password: ")
    print ()

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='ASH',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)

                print ()
                print ("(Starting Screen) Select the type of query you want to execute:")
                print ()
                print ("1. Modification")
                print ("2. Retrieval")
                print ("3. Analysis")
                print ("4. Logout")
                print ()

                ch = str(input("Enter choice > "))

                tmp = sp.call('clear', shell=True)
                if ch == "4":
                    break
                else:
                    dispatch(ch)

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")



    """

    a. (Starting Screen) Select the type of query you want to execute:
        1. Modification
        2. Retrieval
        3. Analysis
        4. Logout

        b1. (Modification screen)  Choose your query:
            c11. Insert
            c12. Delete
            c13. Update
            c14. Back

                c11. (Insertion Screen) Choose your query:
                    -d111. Insert Personnel (in subclass Y)
                    -d112. Insert Vehicle
                    -d113. Insert Trip (for vehicle X)
                    -d114. Insert Material
                    -d115. Insert Intel
                    -d116. Insert Signal
                    d117. Back

                c12. (Deletion Screen) Choose your query:
                    -d121. Delete Personnel
                    -d122. Delete Vehicle
                    -d123. Delete Trip
                    -d124. Delete Material
                    -d125. Delete Intel
                    -d126. Delete Signal
                    d127. Back

                c13. (Update Screen) Choose your query:
                    -d131. Update Personnel
                    -d132. Update Vehicle
                    -d133. Update Trip
                    -d134. Update Material
                    -d135. Update Intel
                    -d136. Update Signal
                    d137. Back


        b2. (Retrieval Screen) Choose your query:
            c21. Search Personnel/Vehicles/Materials
            c22. Communication Analysis (Search Messages)
            *c23. Get Personnel with rank X in subclass Y in wing Z
            *c24. Get min/max/average/total cost of fuel used in trips
            c25. Back

                c21. (Search Screen) Choose your query:
                    -d211. Search Personnel
                    -d212. Search Vehicle
                    -d213. Search Trip
                    -d214. Search Material
                    -d215. Search Wing
                    d216. Back

                c22. (Communication screen) Choose your query:
                    -d221. Search by string
                    -d222. Search by date
                    -d223. Search by sender
                    d224. Back


        b3. (Analysis Screen) Choose your query:

            -c31. Wing-wise Report (For wing x)
            -c32. Supervision Report (Specify ID to get Supervisors of ID and Supervisee of ID)
            *c33. Get people that can access more than X vehicles in wing Y
            *c34. Get list of vehicles where money spent is greater than X
            c35. Back

            Hidden functions:
            h1. Add a Relationship between Personnel, Vehicle, Material and Wing

    """


"""
--------------
Changes to be made:

1. In Update and Delete trip 
"""
