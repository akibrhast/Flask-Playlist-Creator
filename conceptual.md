### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

  - PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads. The origins of PostgreSQL date back to 1986 as part of the POSTGRES project at the University of California at Berkeley and has more than 30 years of active development on the core platform. PostgreSQL has earned a strong reputation for its proven architecture, reliability, data integrity, robust feature set, extensibility, and the dedication of the open source community behind the software to consistently deliver performant and innovative solutions. PostgreSQL runs on all major operating systems, has been ACID-compliant since 2001, and has powerful add-ons such as the popular PostGIS geospatial database extender. It is no surprise that PostgreSQL has become the open source relational database of choice for many people and organisations.

- What is the difference between SQL and PostgreSQL?

  - Both of these being types of SQL a question may arise about what is the difference between both SQL Server vs PostgreSQL. Microsoft SQL server is a database management and analysis system which is mainly used for e-commerce, line of business and different data warehousing solutions. PostgreSQL, on the other hand, is an advanced object-relational database management system which provides support to the extended subset of SQL standards including different transactions, foreign keys, subqueries, triggers, and different user-defined types and functions.


- In `psql`, how do you connect to a database?

  - psql DBNAME USERNAME

- What is the difference between `HAVING` and `WHERE`?

  - The fundamental difference between WHERE and HAVING is this: WHERE selects input rows before groups and aggregates are computed (thus, it controls which rows go into the aggregate computation), whereas HAVING selects group rows after groups and aggregates are computed. Thus, the WHERE clause must not contain aggregate functions; it makes no sense to try to use an aggregate to determine which rows will be inputs to the aggregates. On the other hand, the HAVING clause always contains aggregate functions. (Strictly speaking, you are allowed to write a HAVING clause that doesn't use aggregates, but it's seldom useful. The same condition could be used more efficiently at the WHERE stage.)

- What is the difference between an `INNER` and `OUTER` join?

  - Inner joins don’t include non-matching rows; whereas, outer joins do include them.



- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

  - The key difference between a left outer join, and a right outer join is that in a left outer join it's the table in the FROM clause whose all rows are returned. Whereas, in a right outer join we are returning all rows from the table specified in the join clause.

- What is an ORM? What do they do?

  - An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.


- What are some differences between making HTTP requests using AJAX and from the server side using a library like `requests`?

  - Server side more secure compared to client side. Server side load is on server. Client side load is on client

- What is CSRF? What is the purpose of the CSRF token?

  - CSRF tokens can prevent CSRF attacks by making it impossible for an attacker to construct a fully valid HTTP request suitable for feeding to a victim user.


- What is the purpose of `form.hidden_tag()`?

  - The form. hidden_tag() template argument generates a hidden field that includes a token that is used to protect the form against CSRF attacks. All you need to do to have the form protected is include this hidden field and have the SECRET_KEY variable defined in the Flask configuration
