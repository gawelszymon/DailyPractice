/* Write your PL/SQL query statement below */
select u.unique_id, e.name from EmployeeUNI u right join Employees e on u.id = e.id;