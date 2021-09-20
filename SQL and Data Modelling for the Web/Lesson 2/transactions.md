# Transactions
Transactions only change a database's data on only **UPDATE**, **INSERT **and **DELETE** operations.
Transactions are not concerned with querying the database.
## **Takeaways**
- Databases are interacted using client-server interactions, over a network
- Postgres uses TCP/IP to be interacted with, which is connection-based
- We interact with databases like Postgres during sessions
- Sessions have transactions that commit work to the database
  
**Transactions capture logical bundles of work.**

Work is bundled into transactions, so that in case of system failures, data in your database is still kept in a valid state (by rolling back the entire transaction if any part of it fails). To ensure a database is consistent before and after work is done to it, databases uses atomic transactions, and actions like commits and rollbacks to handle failures appropriately. Transactions are, in other words, ACID.

## Acid Properties
- **A**tomicity: The entire transaction takes place at once or doesn't happen at all.
- **C**onstitency: The database must be consistent before and after the transaction.
- **I**solation: Changes in a particular transaction will not be visible to another transaction till the initial change is committed to the database.
- **D**urability: The data must persist in the database even during system failure.