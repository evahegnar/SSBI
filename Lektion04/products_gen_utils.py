from random import *
import math
import numpy as np
from typing import List, Dict
from faker import Faker

import pandas as pd
currencyCountry = pd.read_excel('Currencies.xlsx', index_col=0)

n_people = 150


companies = ["Nike", "Nestlé", "Apple", "MicroSoft", "Gunnars Grill och Plastikkirurgi", "McKinsey", "Goldman Sachs", "Ur och Penn", "Tjuvjakt AB"]
company_inventory = {company:{"Product" + str(i) + str(j): randint(20,300) for j in range(randint(10,20))} for i, company in enumerate(companies)}
countries = currencyCountry.index.tolist()

fake_profiles =[{"Name":f.name(), "Country":choice(countries), "Workplace":choice(companies)} for f in [Faker() for _ in range(n_people)]]
company_country = {company:choice(countries) for company in companies}


def transaction(fake_profiles: List, company_inventory: Dict, company_country: Dict, day: int) -> List:
    """
    Generates a fake transaction for a fake customer for a fake user in a fake world.

    Args in: 
    List of fake profiles, dictionary of company inventory, dictionary company location and day of transaction.

    Returns: Transaction information containing selling company, sold product, value of sold product,
    customer name, customer country, customer workplace and day of transaction.
    """

    #Item and company 
    company = choice(list(company_inventory.keys()))
    product = choice(list(company_inventory[company]))
    value = company_inventory[company][product]
    country_comp = company_country[company]
    
    #Customer information
    person = choice(fake_profiles)

    transaction = [company, product, value, country_comp, *list(person.values()), day]
    return transaction



cols = ["Selling Company","Product", "Price (USD)", "Company location", "Customer", "Customer Country", "Customer Workplace","Day"]




