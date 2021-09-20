# PSQL 

# Takeaways
- psql is an interactive terminal application for connecting and interacting with your local postgres server on your machine.
- Connect using $ psql `<dbname>`
- psql lets you
    -Directly type and execute SQL commands to your database
    -Inspect and preview your database and database tables using psql meta-commands

**Protip**: type `\?` into psql to see a list of available commands

## **Useful basic psql commands**
`psql <dbname> [<username>]`

Starts psql with a connection to dbname. Optionally use another user than current user

In psql:

`# \l`

List all databases on the server, their owners, and user access levels

`# \c <dbname>`

Connect to a database named

`# \dt`

Show database tables

`# \d <tablename>`

Describe table schema

`# \q`

Quit psql, return to the terminal

`# \?`

Get help, see list of available commands

**Resource**: [psql cheatsheet](https://video.udacity-data.com/topher/2019/August/5d5a1055_postgres-psql-cheat-sheet/postgres-psql-cheat-sheet.pdf)

