IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'PROPERTY_DB')
BEGIN
    CREATE DATABASE [PROPERTY_DB]
END
