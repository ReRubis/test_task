Questions.
* There is no unique identifier for a property in the data. How would you approach this to come
up with a column that can be used as a unique id for each property? Would you combine any 
columns for instance? Can you test your method that it returns unique values? Are there any
issues?

I suggest using UUID of the transaction in combination with the date and postcode of the property. 
This will give a unique identifier for each property. 


* Once you have defined a property unique id (unfortunately this doesn’t exist in the data so it
needs to be defined by you), how would you store the data in your SQL database? What table
structure would you use?

I decided to come up with a table structure that will have the following columns:

```py
class TransactionsSchema(BaseModel):
    """Schema for transactions"""
    transaction_id: str
    price: float
    date_of_transfer: str
    postcode: str
    property_type: str
    old_new: str
    duration: str
    paon: Optional[str]
    saon: Optional[str]
    street: str
    locality: str
    town_city: str
    district: str
    county: str
    ppd_category_type: str
    record_status: str
```

* How would you work on improving the performance of the queries? Would you use primary
keys, indexes?

Yes. the unique_id generated out of combination of transaction_id, date_of_transfer and postcode
works great as both primary key and index.

Combination of transaction_id, date_of_transfer and postcode will be unique.


* Can you write a query that returns the transactions that took place in EC1A between 2018-
04-01 and 2019-12-31?

```sql
SELECT * FROM transactions WHERE postcode LIKE '%EC1A%' AND date_of_transfer BETWEEN '2018-04-01' AND '2019-12-31';
```

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