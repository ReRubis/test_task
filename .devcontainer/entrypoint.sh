#!/bin/bash
set -e
/opt/mssql/bin/sqlservr &

# Wait for SQL Server to start
sleep 30s

# Run the SQL script
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'YourStrong!Passw0rd' -d master -i init.sql

# Keep the container running
tail -f /dev/null