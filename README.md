# Military Database and Analyser

A database management system (DBMS) designed specifically for a centralised military database, with the capabability of performing specific queries and analysis.

<img src="https://images-ext-1.discordapp.net/external/GlyDNhll4UnT-4iPOZrJbpBWqvgJoo8iOm13QRJYsFI/https/cdn2.cloudpro.co.uk/sites/cloudprod7/files/military_security.jpg?width=659&height=454">

## Authors
1. Arihant Srikar Tadanki (2019113005)
2. Shreyas Pradhan (2019113004)
3. Hrishi Narayanan (2019113022)

# Getting started 

#### Prerequisites
- **MySQL** or **MariaDB** must be installed for utilization of the Database Dump.
  
**Note:** MariaDB is similar to MySQL but is also faster to use and easier to install.
 
- **Python3** is required for running the database CLI

:warning: **You must use Python 3**: Not using python3 might result in errors.

### Initiating the Database
Once the above prerequisites are met in your system, follow these steps:

- Open `mysql` on local server.
- Create a user and grant it priviledges: 
	```sql
    CREATE USER '<user>'@'localhost' IDENTIFIED BY '<password>';
    GRANT ALL PRIVILEGES ON *.* TO '<user>'@'localhost';
	```
- Dump the  database into `ash` from `core/SQL` using:
	```
	mysql -u <user> -p 
	source dumpfile.sql
	```
- Relocate yourself to `core/Python` and run the following:
    ```bash
    python3 ash_world.py 
    ```
- Enter the database using "Host", "User" and "Password" with the details of the user (**with all permissions**).
                                       
:warning: **Use user with all permisions**: Not using user without all permission may cause issues during runtime.

## Map of fuctions:

A map of all funtionalities and the user interface is as given :
```
    a. Initiation:

         b1. Modification:

                c11. Insertion
                        d111. Insert Personnel (in subclass Y)
                        d112. Insert Vehicle
                        d113. Insert Trip (for vehicle X)
                        d114. Insert Material
                        d115. Insert Intel
                        d116. Insert Signal
                        d117. Back

                c12. Deletion
                        d121. Delete Personnel
                        d122. Delete Vehicle
                        d123. Delete Trip
                        d124. Delete Material
                        d125. Delete Intel
                        d126. Delete Signal
                        d127. Back

                c13. Update
                        d131. Update Personnel
                        d132. Update Vehicle
                        d133. Update Trip
                        d134. Update Material
                        d135. Update Intel
                        d136. Update Signal
                        d137. Back

                c14. Back

        b2. Retrieval:

                c21. Search:
                        d211. Search Personnel
                        d212. Search Vehicle
                        d213. Search Trip
                        d214. Search Material
                        d215. Search Wing
                        d216. Back

                c22. (Communication screen) Choose your query:
                        d221. Search by string
                        d222. Search by date
                        d223. Search by sender
                        d224. Back

                c23. Get Personnel with rank X in subclass Y in wing Z
                c24. Get min/max/average/total cost of fuel used in trips
                c25. Back

        b3. Analysis:
                c31. Wing-wise Report (For wing x)
                c32. Supervision Report (Specify ID to get Supervisors of ID and Supervisee of ID)
                c33. Get people that can access more than X vehicles in wing Y
                c34. Get list of vehicles where money spent is greater than X
                c35. Back

        b4. Logout
           
        Hidden functions:
            h1. Add a Relationship between Personnel, Vehicle, Material and Wing           

```


