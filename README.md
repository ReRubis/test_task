# INSTALLATION 

The recommended way of installation is through the dev-containvers VS Code extension. 

1. Run the containers.
2. Create the data folder and add the .csv data files. 
3. Open up the docker database container. 

(This step might be automated, but I was limited on time.)

Find the container ID by running the following command:
```sh
docker ps
```

Paster the ID here and run the following command:
```sh
docker exec -it <ID> /bin/bash
```

Inside container:
```sh
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P 'YourStrong!Passw0rd'
```

```sql
1> CREATE DATABASE property_db;
2> GO
```
4. Populate the databse by running the analyze.ipynb notebook.
It might take up to 30 minutes.  I wasn't concerned much, since I only had to do it once.

