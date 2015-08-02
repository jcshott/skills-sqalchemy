"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == "Corvette", Model.brand_name == "Chevrolet").all()

# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter(db.or_(Brand.founded < 1950, Brand.discontinued.isnot(None))).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

#style/approach question: is it better to get .all() when I call the query or should I do it in the loop (as i've done)?  I did it the way below because that's how its in my lecture notes, but I think I was doing other way around in ratings.

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    model_info = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(Model.year == year)

	for name, brand_name, headquarters in model_info.all():
		print name, brand_name, headquarters


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     #I really tried a ton of different ways to do this, but given we only want the brand name once, this was the only way I could think to filter out the duplicats while keeping all the models. would love to know if there is a better way!

	brand_summary = db.session.query(Brand.name, Model.name, Model.year).outerjoin(Model)
	brand_sum_dict = {}

	for brand, model, year in brand_summary.all():
		brand_sum_dict.setdefault(brand, [])
		brand_sum_dict[brand].append((model, year))

	for brand, models in brand_sum_dict.items():
		print brand, "(Brand name)" 
		for model in models:
			if model[0] == None:
				print "\t no model in db"
			else:	
				print "\t", model[0], "(%s)" % model[1]

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# object: <flask_sqlalchemy.BaseQuery object at 0x107d4aa10>

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#Association table manages a many-to-many relationship between tables. This is essentially a table that acts as the middle table to link tables via the tables' primary keys. It essentially hosts foriegn keys.
