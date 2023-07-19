# 0x0E. SQL - More queries

<img src="[https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step2.png](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230719%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230719T043954Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8054a431c0051603c0ba60e02ff6d4d7a15eb22df6f3201203e28c5f96a960d4)" width="1200" height="280">

## Description
This project covers advanced SQL topics and query techniques. It includes tasks related to managing users and privileges, creating databases and tables, and retrieving data from multiple tables using joins and subqueries.

## Learning Objectives
By the end of this project, you should be able to:

- Create a new MySQL user and manage privileges
- Understand primary and foreign keys
- Use NOT NULL and UNIQUE constraints
- Retrieve data from multiple tables using joins and subqueries
- Understand the concepts of JOIN and UNION in SQL

## Files

| Filename                   | Description                           |
| -------------------------- | ------------------------------------- |
| [0-privileges.sql](./0-privileges.sql)   | Script to list privileges of MySQL users |
| [1-create_user.sql](./1-create_user.sql) | Script to create the MySQL server user `user_0d_1` |
| [2-create_read_user.sql](./2-create_read_user.sql) | Script to create the database `hbtn_0d_2` and the user `user_0d_2` with SELECT privilege |
| [3-force_name.sql](./3-force_name.sql) | Script to create the table `force_name` with columns `id` and `name` |

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All SQL queries should have a comment just before (i.e., syntax above)
- All SQL keywords should be in uppercase (SELECT, WHERE...)
- A README.md file, at the root of the folder of the project, is mandatory

## How to Use MySQL 8.0 on Ubuntu 20.04 LTS
- Install MySQL 8.0 on Ubuntu 20.04 LTS:
