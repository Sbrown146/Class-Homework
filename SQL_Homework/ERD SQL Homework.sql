-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/hbythw
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "departments" (
    "dept_ID" int   NOT NULL,
    "dept_no" varchar   NOT NULL,
    "dept_name" varchar   NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_ID"
     )
);

CREATE TABLE "dept_emp" (
    "dept_emp_ID" int   NOT NULL,
    "ID" int   NOT NULL,
    "dept_no" varchar   NOT NULL,
    "emp_no" int   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL,
    CONSTRAINT "pk_dept_emp" PRIMARY KEY (
        "ID"
     )
);

CREATE TABLE "dept_manager" (
    "dept_manager_ID" int   NOT NULL,
    "ID" int   NOT NULL,
    "dept_no" varchar   NOT NULL,
    "emp_no" int   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL,
    CONSTRAINT "pk_dept_manager" PRIMARY KEY (
        "ID"
     )
);

CREATE TABLE "employees" (
    "ID" int   NOT NULL,
    "emp_ID" int   NOT NULL,
    "emp_no" int   NOT NULL,
    "birth_date" date   NOT NULL,
    "first_name" varchar   NOT NULL,
    "last_name" varchar   NOT NULL,
    "gender" varchar   NOT NULL,
    "hire_date" datea   NOT NULL,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "ID"
     )
);

CREATE TABLE "salaries" (
    "emp_salary_ID" int   NOT NULL,
    "emp_no" int   NOT NULL,
    "salary" int   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL
);

CREATE TABLE "titles" (
    "emp_title" int   NOT NULL,
    "emp_no" int   NOT NULL,
    "title" varchar   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL
);

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_dept_emp_ID" FOREIGN KEY("dept_emp_ID")
REFERENCES "departments" ("dept_ID");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_dept_manager_ID" FOREIGN KEY("dept_manager_ID")
REFERENCES "departments" ("dept_ID");

ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_ID" FOREIGN KEY("emp_ID")
REFERENCES "departments" ("dept_ID");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_salary_ID" FOREIGN KEY("emp_salary_ID")
REFERENCES "employees" ("ID");

ALTER TABLE "titles" ADD CONSTRAINT "fk_titles_emp_title" FOREIGN KEY("emp_title")
REFERENCES "employees" ("ID");

