Questions.
* There is no unique identifier for a property in the data. How would you approach this to come
up with a column that can be used as a unique id for each property? Would you combine any 
columns for instance? Can you test your method that it returns unique values? Are there any
issues?

I suggest using a md5 hash  of paon, saon and postcode combination.
Generally, the combination of paon, saon and postcode should be unique for each property.
Although, I was quite shocked by the messiness of dataset and can not conclude anything. 




* Once you have defined a property unique id (unfortunately this doesn’t exist in the data so it
needs to be defined by you), how would you store the data in your SQL database? What table
structure would you use?

I decided to come up with a table structure that will have the following columns.
Of course it could be relational database for the easiness of use. 
But for now it's not. 

I decided to keep the important and unique to the property information in the Property table.
While leaving the information about the transactions in the Transaction table.

```py
class Property(Base):

    unique_id = Column(String(255), primary_key=True)
    postcode = Column(String, unique=False, nullable=True)
    paon = Column(String, unique=False, nullable=True)
    saon = Column(String, unique=False, nullable=True)
    street = Column(String, unique=False, nullable=True)
    locality = Column(String, unique=False, nullable=True)
    town_city = Column(String, unique=False, nullable=True)
    district = Column(String, unique=False, nullable=True)
    country = Column(String, unique=False, nullable=True)
    transactions = Column(String, unique=False, nullable=True)


class Transaction(Base):
    transaction_id = Column(String(255), primary_key=True)
    property_id = Column(String, unique=False, nullable=True)
    price = Column(String, unique=False, nullable=True)
    date_of_transfer = Column(String, unique=False, nullable=True)


class Postcode(Base):
    postcode = Column(String(255), primary_key=True)
    properties = Column(String, unique=False, nullable=True)
```

* How would you work on improving the performance of the queries? Would you use primary
keys, indexes?

Yes. the transaction_id for the Transactions is the primary key. 
And the unique_id for the Property is the primary key.

Indexes can be used for the postcode, date_of_transfer, price columns.
But I am not sure if it will be useful, it depends on the usage, which I am not aware of. 


* Can you write a query that returns the transactions that took place in EC1A between 2018-
04-01 and 2019-12-31?

Considering my table structure, the query would require a join. 

```sql
SELECT transaction_id, date_of_transfer, postcode, unique_id FROM transactions JOIN propertys ON transactions.property_id = propertys.unique_id WHERE propertys.postcode LIKE '%EC1A%' AND transactions.date_of_transfer BETWEEN '2018-04-01' AND '2019-12-31';
```

I also took advice of using only 2019-2020 data, so my results most likely include less rows than expected. 
![IMAGE OF QUERY](https://media.discordapp.net/attachments/1097141968682893484/1226990799611498526/image.png?ex=6626c73b&is=6614523b&hm=e975ef47bbbb6e4240be13744c95dce3a826c799fe950730a120b0b48d725391&=&format=webp&quality=lossless&width=689&height=655)

* Utilizing the class structure in python you have defined, create methods to
- return the number of properties that have been sold in a postcode, and which
transaction_ids refer to those. Test with ST10 4BS. Were there 2 transaction in
2019?
- Given a transaction_id, return which property it refers to. Test with {7C2D0701-
0253-4963-E053-6B04A8C07B97}. Does it return a property in Cornwall?

* Which postcodes have seen the highest increase in transactions during the last 5 years? No
need to do the analysis at the full postcode level; the first part is sufficient. Thus instead of
e.g. SE13 5HA, consider only SE13.

* Can you come up with an indication of a ‘migration’ metric in the UK? Perhaps it would be
best if you combined the postcode coordinates dataset for this exercise (url #6). Where is the
‘centre of gravity’ in terms of number of transactions of the population moving to every year?
Where is the ‘centre of gravity’ in terms of value moving to? For now, consider that the ‘centre
of gravity’ is a weighted average function, so for each year determine the weighted average
of the coordinates based on number of transactions, or value.

* Assume that EC1A is the centre of London. Can you plot the average transaction price of a
postcode as a function of distance from EC1A? There are numerous postcodes within EC1A,
so try to use the centre of all of the postcodes within it. The distance between two points a,
and b, with coordinates (x1, y1) and (x0, y0) is 𝑑 = ඥ(𝑥ଵ − 𝑥଴
)ଶ + (𝑦ଵ − 𝑦଴
)ଶ

* Can you find any correlation between the average house prices (url #4), and a CPI indicator
(url #5)? Do not be concerned about the lag in the CPI and the house prices not being
synchronized. Assume that all data points are normalized (an average price in Aug 2014 can
be matched to an Aug 2014 entry in the CPI dataset). Also, just use United Kingdom as a region
from the first file. 