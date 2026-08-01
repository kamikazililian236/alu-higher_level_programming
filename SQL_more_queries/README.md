# SQL - More Queries

This directory contains implementation files for advanced SQL tasks using MySQL, covering:
- Managing user privileges and grants.
- Database constraints (primary keys, foreign keys, default values, unique values).
- Subqueries.
- Various joins (Inner Join, Left Join) on relational tables.
- Multiple-table relationships with complex sorting and filtering.

## Tasks

* **0. My privileges!**: Script listing all privileges of `user_0d_1` and `user_0d_2`.
* **1. Root user**: Script creating user `user_0d_1` with all privileges.
* **2. Read user**: Script creating database `hbtn_0d_2` and user `user_0d_2` with SELECT privilege.
* **3. Always a name**: Script creating table `force_name`.
* **4. ID can't be null**: Script creating table `id_not_null`.
* **5. Unique ID**: Script creating table `unique_id`.
* **6. States table**: Script creating database `hbtn_0d_usa` and table `states`.
* **7. Cities table**: Script creating database `hbtn_0d_usa` and table `cities` referencing `states`.
* **8. Cities of California**: Script listing all California cities using a subquery.
* **9. Cities by States**: Script listing cities with their state name using Inner Join.
* **10. Genre ID by show**: Script listing shows with at least one genre.
* **11. Genre ID for all shows**: Script listing all shows and their genres (including NULL).
* **12. No genre**: Script listing shows without a genre.
* **13. Number of shows by genre**: Script counting shows linked to each genre.
* **14. My genres**: Script listing all genres of the show Dexter.
* **15. Only Comedy**: Script listing all Comedy shows.
* **16. List shows and genres**: Script listing all shows and all genres linked to them.
