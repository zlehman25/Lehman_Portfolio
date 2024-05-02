import psycopg2
import pandas as pd

#Function defined
def create_database():
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=root")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    cur.execute("DROP DATABASE accounts")
    cur.execute("CREATE DATABASE accounts")

    conn.close()

    conn = psycopg2.connect("host=localhost dbname=accounts user=postgres password=root")
    cur = conn.cursor()

    return cur, conn

#Data imported and cleaned
AccountsCountry = pd.read_csv(r"WealthAccountsCountry.csv")
AccountsCountry_Clean = AccountsCountry[['Code', 'Short Name', 'Table Name', 'Long Name', 'Currency Unit']]
AccountsData = pd.read_csv(r"WealthAccountData.csv")
AccountsData_Clean = AccountsData[['Country Name', 'Country Code', 'Series Code', '1995 [YR1995]', '2000 [YR2000]', '2005 [YR2005]', '2010 [YR2010]', '2015 [YR2015]', '2018 [YR2018]']]
AccountsSeries = pd.read_csv(r"WealthAccountSeries.csv")
AccountsSeries = AccountsSeries[['Code', 'Topic', 'Indicator Name']]

#Creating the database
cur, conn = create_database()

#Creating tables
create_accountscountry_table = ("""CREATE TABLE IF NOT EXISTS accountscountry(
                                country_code VARCHAR PRIMARY KEY,
                                short_name VARCHAR,
                                table_name VARCHAR,
                                long_name VARCHAR,
                                currency_unit VARCHAR
                                )""")
cur.execute(create_accountscountry_table)
conn.commit()

create_accountsdata_table = ("""CREATE TABLE IF NOT EXISTS accountsdata(
                                country_name VARCHAR,
                                country_code VARCHAR,
                                series_code VARCHAR,
                                year_1995 VARCHAR,
                                year_2000 VARCHAR,
                                year_2005 VARCHAR,
                                year_2010 VARCHAR,
                                year_2015 VARCHAR,
                                year_2018 VARCHAR                           
                                )""")
cur.execute(create_accountsdata_table)
conn.commit()

create_accountsseries_table = ("""CREATE TABLE IF NOT EXISTS accountsseries(
                                code VARCHAR,
                                indicator_name VARCHAR,
                                long_definition VARCHAR                          
                                )""")
cur.execute(create_accountsseries_table)
conn.commit()

#Inserting data into tables
accountscountry_data_insert = ("""INSERT INTO accountscountry(
                               country_code,
                               short_name,
                               table_name,
                               long_name,
                               currency_unit)
                               VALUES (%s, %s, %s, %s, %s)
                               """)
for i, row in AccountsCountry_Clean.iterrows():
    cur.execute(accountscountry_data_insert, list(row))
conn.commit()

accountsdata_data_insert = ("""INSERT INTO accountsdata(
                               country_name,
                               country_code,
                               series_code,
                               year_1995,
                               year_2000,
                               year_2005,
                               year_2010,
                               year_2015,
                               year_2018)
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                               """)
for i, row in AccountsData_Clean.iterrows():
    cur.execute(accountsdata_data_insert, list(row))
conn.commit()

accountsseries_data_insert = ("""INSERT INTO accountsseries(
                               code,
                               indicator_name,
                               long_definition)
                               VALUES (%s, %s, %s)
                               """)
for i, row in AccountsSeries.iterrows():
    cur.execute(accountsseries_data_insert, list(row))
conn.commit()
