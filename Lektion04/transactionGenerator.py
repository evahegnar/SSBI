import pandas as pd
from products_gen_utils import *




def main():
    """
    Main script to generate transaction information for SSBI-task.
    """
    days = np.arange(1,60)
    csv = []
    for day in days:
        for i in range(30):
            csv.append(transaction(fake_profiles, company_inventory,company_country, day))
    df = pd.DataFrame(csv, columns = cols)
    df.to_csv("transactions.csv", index = False)


       
    
if __name__ == "__main__":
    main()
