# Problem Statement❓

The main goal of this project is to perform extensive Exploratory Data Analysis(`EDA`) on the Zomato Dataset and build an appropriate Machine Learning Model that will help various Zomato Restaurants to predict their respective Ratings based on certain features.

# Dataset

Dataset was taken from [Kaggle](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants?resource=download)

# Technology & Domain

Machine Learning Technology & Ecommerce

# Programming Language and Tools

Python [Jupyter Notebook, MS Excel, FastAPI]

# Conclusion 💡

- From the analysis, `'Onesta'` , `'Empire Restaurant'` & `'KFC'` are the most famous restaurants in bangalore.
- Most Restaurants offer options for online order and delivery.
- Most restaurants don't offer table booking.
- From the analysis, most of the ratings are within 3.5 and 4.5.
- From the analysis. we can see that most of the restaurants located in 'Koramangala 5th Block' , 'BTM' & 'Indiranagar'.Then least restaurants are located 'KR Puram' , 'Kanakapura' , 'Magadi Road'. 'Casual Dining' , 'Quick Bites' , 'Cafe' ,
- 'Dessert Parlor' are the most common types of restaurant.And 'Food Court', 'Casual Dining' ,
- 'Dhaba' are the least common.
- From the analysis, pasta & Pizza most famous food in bangalore restaurants.
- From the analysis, we can see that North Indian Cuisines are most famous in bangalore restaurants.
- Two main service types are Delivery and Dine-out.
- From the analysis, we can see that 'Onesta' , 'Truffles' & 'Empire Restaurant' are highly voted restaurants.

# Demo Video Link :

https://drive.google.com/file/d/1_b0Kz7ljemyjlyX2G5NVQD8iwULOkKex/view?usp=sharing

### Main.ipynb consist of all the codes

**parameters of json**

- `online_order` : Whether Online Ordering is available in restaurant or not.
- `book_table` : Table booking is available or not.
- `votes` : total number of rating for the restaurant.
- `cost` : Contains the approximate cost meal of two people.
- `location` : Location of the restaurant.
- `rest_type` : Type of restaurant.
- `type` :

### Json Request Form

```
{
    "online_order": "Yes",
    "book_table": "Yes",
    "votes" : 775,
    "cost" : 800.0,
    "location" : "Banashankari",
    "rest_type" : "Casual Dining",
    "type" : "Buffet"
}
```
