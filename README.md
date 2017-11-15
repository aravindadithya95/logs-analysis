# Logs Analysis
This project is an internal reporting tool that analyzes the database logs of a newspaper website.

This project is part of the [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) at _Udacity_.

### Getting Started
- Make sure you have **Python 3.x** installed in your machine.
- Make sure you have the **PostgreSQL** database, and the **psycopg2** package for Python installed.
- Download and extract the [zip file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) that contains the data for the database.
- To load the data, `cd` into the directory and run:
```
psql -d news -f newsdata.sql
```
- Create the following views from the `psql` command line interpreter:
```
create view top3_articles as
select articles.title, count(articles.title) as views
from articles, log
where log.path = '/article/' || articles.slug
group by articles.title
order by views desc
limit 3;
```
```
create view popular_authors as
select authors.name, count(authors.name) as views
from articles, authors, log
where log.path = '/article/' || articles.slug and articles.author = authors.id
group by authors.name
order by views desc;
```
```
create view errors as
select *
from (
    select day, round((err * 100.0) / (err + ok), 2) as errors
    from (
      select date(time) as day, sum(case when status != '200 OK' then 1 else 0 end) as err, sum(case when status = '200 OK' then 1 else 0 end) as ok
      from log
      group by day
    ) as status_count
) as error_percent
where errors > 1;
```
- Exit the `psql` program using `\q`.
- Download and extract the zip file for this repository, or clone the repository using the following command:
```
git clone https://github.com/aravindadithya95/logs-analysis.git
```
- Navigate to the directory using `cd` and run `python3 analysis.py` to get the output.

## Database
The database consists of three tables:
- articles
- authors
- log

## Design
The Python program is designed to connect to the _PostgreSQL_ database using the _psycopg2_ module and answer the following questions:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

The program runs a `select` query on the views we created and prints the results. The database does the heavy lifting to extract just the data we're looking for. Take a look at `sample.txt` for the sample output.
