from collections import Counter
from collections.abc import Iterable
from bs4 import BeautifulSoup
import re
from statistics import mean, median, variance
from operator import itemgetter
from config import load_config
import psycopg2


def create_table():
    """Create colour table in PostgreSQL"""

    command = """CREATE TABLE IF NOT EXISTS shirt_colours (
        colour VARCHAR(50) UNIQUE NOT NULL,
        frequency INTEGER NOT NULL
        );
     """

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            print("Connected to PostgreSQL database")
            with conn.cursor() as cur:
                cur.execute(command)
                conn.commit()
                cur.close()
            conn.close()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def flatten(item):
    """Flattens a list object of arbitrary dimension recursively"""
    for x in item:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


with open('python_class_question.html', 'r') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")

weekday_regex = re.compile(
    'monday|tuesday|wednesday|thursday|friday', flags=re.I)

# Get all table data tags
shirt_colour_rows = soup.find_all("td")

# Remove the table cells under the 'Day' field
filtered = [
    i.contents[0] for i in shirt_colour_rows if not weekday_regex.match(i.contents[0])]

# Separate individual colours in the table rows from the comma separated string form
colour_list = [i.split(",") for i in filtered]


# Flatten list of row lists into a single list of all the individual colours
# Also strip whitespace from strings
flat_colour_list = [i.strip() for i in list(flatten(colour_list))]

# Use Counter object to get the discrete colours and their count values
colour_counter = Counter(flat_colour_list).items()

# Represent the colour count in a dictionary with colour as key and count
# as value
colour_count_dict = dict(colour_counter)

# Represent the colour count as a list of tuples. To be used to easily
# get the most occuring colour and feeding to the database
colour_count_list = list(colour_counter)


# Mean, Median and Variance of the colour counts

count_nums = list(colour_count_dict.values())

mean_count = mean(count_nums)
median_count = median(count_nums)
variance = variance(count_nums)

print("The Mean colour count is: ", mean_count)
print("The Median colour count is: ", median_count)
print("The Variance of the colour count is: ", variance)

# Get the Colour with the highest count from a list of tuples
colour_max = max(colour_count_list, key=itemgetter(1))
print("The most worn shirt colour was: ", colour_max[0])

probability_red = colour_count_dict["RED"] / sum(count_nums)
print("For a shirt drawn at random, the probability of picking red is: ", probability_red)


# SAVE SHIRT COLOURS AND FREQUENCY INTO DATABASE

create_table()

command = "INSERT INTO shirt_colours (colour, frequency) VALUES (%s, %s)"
print("list to feed", colour_count_list)
try:
    config = load_config()
    with psycopg2.connect(**config) as conn:
        print("Connected to PostgreSQL database")
        with conn.cursor() as cur:
            cur.executemany(command, colour_count_list)
            conn.commit()
            cur.close()
        conn.close()
except (psycopg2.DatabaseError, Exception) as error:
    print(error)
