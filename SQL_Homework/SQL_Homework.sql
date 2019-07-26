SET search_path TO "SQL_Homework";

SELECT * FROM departments;
SELECT * FROM dept_emp;
SELECT * FROM dept_manager;
SELECT * FROM employees;
SELECT * FROM salaries;
SELECT * FROM titles;

--View and case stuff
DROP VIEW IF EXISTS salary_status;
CREATE VIEW salary_status as
SELECT emp_no, salary,
case
when salary BETWEEN 0 AND 50000 THEN 'Low Tier'
when salary BETWEEN 50001 and 70000 then 'Mid Tier'
ELSE 'High Tier'
END AS Status
FROM salaries;
SELECT * FROM salary_status;



--Question 1
--Merge employees and salaries on emp_id for employee information
DROP VIEW IF EXISTS employee_info;
CREATE VIEW employee_info AS
SELECT s.emp_no, first_name, last_name, gender, s.salary
FROM employees AS e
	JOIN salaries AS s ON (s.emp_no=e.emp_no);
SELECT * FROM employee_info;




--Question 2
--Employees hired in 1986
DROP VIEW IF EXISTS employee_1986;
CREATE VIEW employee_1986 AS
SELECT * FROM employees
WHERE hire_date >= ('1986-01-01')
AND hire_date < ('1987-01-01');
SELECT * FROM employee_1986;




--Question 3
--Department Manager Information
--Merge deparments, dept_emp, employees on emp_id
DROP VIEW IF EXISTS dept_info;
CREATE VIEW dept_info AS
SELECT d.dept_no, d.dept_name, dm.emp_no, e.first_name, e.last_name, from_date, to_date
FROM dept_manager AS dm
	JOIN departments AS d 
	ON (d.dept_no=dm.dept_no)
		JOIN employees AS e
		ON (e.emp_no=dm.emp_no);
SELECT * FROM dept_info;
	



--Question 4
--Department information for employees
DROP VIEW IF EXISTS employee_dept;
CREATE VIEW employee_dept AS
SELECT e.emp_no, e.first_name, e.last_name, d.dept_name
FROM employees as e
	JOIN dept_emp AS de
	ON (de.emp_no=e.emp_no)
		JOIN departments AS d
		ON (d.dept_no=de.dept_no);
SELECT * FROM employee_dept;




--Question 5
--Employees with first name Hercules and last name beginning with B
DROP VIEW IF EXISTS hercules_b;
CREATE VIEW hercules_b AS
SELECT first_name, last_name FROM employees
WHERE first_name='Hercules'
AND last_name LIKE 'B%';
SELECT * FROM hercules_b;




--Question 6
--Employees in the Sales Department
--Use employee_dept view from question 4
DROP VIEW IF EXISTS sales_emp;
CREATE VIEW sales_emp AS
SELECT * FROM employee_dept
WHERE dept_name='Sales';
SELECT * FROM sales_emp;




--Question 7
--Employees in Sales and Development
--Use employee_dept view from question 4
DROP VIEW IF EXISTS sales_dev;
CREATE VIEW sales_dev AS
SELECT * FROM employee_dept
WHERE dept_name='Sales' OR dept_name='Development';
SELECT * FROM sales_dev;




--Question 8
--How many employees share a last name
--Use employee_dept view from question 4.
--Hmmmmm.....Seems legit....
DROP VIEW IF EXISTS last_name_freq;
CREATE VIEW last_name_freq AS
SELECT last_name, COUNT(last_name) as "Number of Repeats"
FROM employee_dept
GROUP BY last_name
ORDER BY "Number of Repeats" DESC;
SELECT * FROM last_name_freq;