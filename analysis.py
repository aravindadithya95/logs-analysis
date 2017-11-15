import psycopg2

db_name = "news"

# Connect to database
conn = psycopg2.connect(database=db_name)
cursor = conn.cursor()


def execute_select(query, end):
    """Executes the given SQL select query and prints the formatted results

    Args:
        query (str): The SQL query to be executed.
        end (str): The string to be printed at the end of each row.
    """
    cursor.execute(query)
    results = cursor.fetchall()
    n = len(results)
    for i in range(0, n):
        s = str(results[i][0])
        padding = 50 - len(s)
        print(s, end="")
        print("{}{}".format(results[i][1], end).rjust(padding, " "))


# 1. The most popular three articles by views
print("\nThe most popular three articles by views are: ")
execute_select("select * from top3_articles", " views")

# 2. The most popular authors by views
print("\nThe most popular authors by views are: ")
execute_select("select * from popular_authors", " views")

# 3. The days on which more than 1% of requests led to errors
print("\nThe days on which more than 1% of requests led to errors are: ")
execute_select("select * from errors", "% errors")

print()
conn.close()
