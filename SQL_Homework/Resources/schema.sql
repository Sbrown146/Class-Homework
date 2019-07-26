SET search_path TO "SQL_Homework";

DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS dept_manager;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;

CREATE TABLE departments (
	dept_no character varying(45) NOT NULL,
	dept_name character varying(45) NOT NULL
) ;

CREATE TABLE dept_emp (
	emp_no integer NOT NULL,
	dept_no character varying(45) NOT NULL,
	from_date date NOT NULL,
	to_date date NOT NULL
);

CREATE TABLE dept_manager (
	dept_no character varying(45) NOT NULL,
	emp_no integer NOT NULL,
	from_date date NOT NULL,
	to_date date NOT NULL
);

CREATE TABLE employees (
	emp_no integer NOT NULL,
	birth_date date NOT NULL,
	first_name character varying(45) NOT NULL,
	last_name character varying(45) NOT NULL,
	gender character varying(1) NOT NULL,
	hire_date date NOT NULL
);

CREATE TABLE salaries (
	emp_no integer NOT NULL,
	salary integer NOT NULL,
	from_date date NOT NULL,
	to_date date NOT NULL
);

CREATE TABLE titles (
	emp_no integer NOT NULL,
	title character varying(45) NOT NULL,
	from_date date NOT NULL,
	to_date date NOT NULL
);

