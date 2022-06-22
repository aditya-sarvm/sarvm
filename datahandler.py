import pandas as pd
import os

LANGUAGES = ['Kashmiri', 'Hindi', 'Dogri', 'Punjabi', 'Bhotia', 'Tibetan',
       'Khandeshi', 'Shina', 'Marathi', 'Nepali', 'Urdu', 'Bengali',
       'Gujarati', 'Tamil', 'Telugu', 'Balti', 'Malayalam', 'Odia',
       'Assamese', 'Ladakhi', 'Kannada', 'Lahnda', 'Manipuri', 'Kinnauri',
       'Lahauli', 'Maithili', 'Kurukh/Oraon', 'Nissi/Dafla', 'Halam',
       'Sindhi', 'Bhili', 'Sanskrit', 'Gondi', 'Santali', 'Malto',
       'Konyak', 'AO', 'Lotha', 'Angami', 'Chokri', 'Sangtam',
       'Yimchungre', 'Chang', 'Khiemnungan', 'Rengma', 'Zeliang', 'Phom',
       'Khezha', 'Pochury', 'Kuki', 'Chakhesang', 'Mao', 'Zemi', 'Sema',
       'Dimasa', 'Liangmei', 'Garo', 'Tangkhul', 'Thado', 'Kabui',
       'Paite', 'Hmar', 'Vaiphei', 'Maram', 'Anal', 'Zou', 'Maring',
       'Gangte', 'Kom', 'Mizo', 'Lakher', 'Tripuri', 'Pawi', 'Mogh',
       'Bishnupuriya', 'Munda', 'Savara', 'Khasi', 'Koch', 'Rabha',
       'Karbi', 'Lalung', 'Mising', 'Deori', 'Mundari', 'Kharia', 'Parji',
       'Adi', 'Tamang', 'Wancho', 'Mishmi', 'Tangsa', 'Nocte', 'Monpa',
       'Rai', 'Limbu', 'Lepcha', 'Sherpa', 'Koda/Kora', 'Kisan', 'Bhumij',
       'HO', 'Korwa', 'Kui', 'Koya', 'Khond', 'Gadaba', 'Halabi', 'Juang',
       'Konkani', 'Korku', 'Tulu', 'English', 'Kolami', 'Coorgi/Kodagu']

STATES = ['Jammu & Kashmir', 'Himachal Pradesh', 'Punjab', 'Uttarakhand',
       'Haryana', 'Delhi', 'Rajasthan', 'Uttar Pradesh', 'Bihar',
       'Nagaland', 'Manipur', 'Mizoram', 'Tripura', 'Meghalaya', 'Assam',
       'Arunachal Pradesh', 'Sikkim', 'West Bengal', 'Jharkhand',
       'Orissa', 'Chhattisgarh', 'Madhya Pradesh', 'Gujarat',
       'Maharashtra', 'Goa', 'Andhra Pradesh', 'Telangana', 'Karnataka',
       'Kerala', 'Tamil Nadu']

CITIES = ['Chittoor', 'Guntur', 'Vijayawada', 'Kurnool', 'Vishakhapatnam','Itanagar', 'Siang', 'Dibrugarh', 'Guwahati', 'Jorhat', 'Silchar',
       'Tezpur', 'Bhagalpur', 'Gaya', 'Muzaffarpur', 'Patna', 'Darbhanga','Bhilai', 'Bilaspur', 'Ambikapur', 'Korba', 'Raipur',
       'Delhi Cantonment ', 'Mehrauli', 'New Delhi', 'Karawal Nagar','Vasant Kunj', 'Margao', 'Panaji', 'Ahmedabad', 'Gandhinagar',
       'Rajkot', 'Surat', 'Vadodara', 'Ambala', 'Chandigarh', 'Faridabad','Gurugram', 'Hisar', 'Amritsar', 'Bathinda', 'Jalandhar',
       'Ludhiana', 'Patiala', 'Gangtok', 'Lachung', 'Ajmer', 'Jaipur','Jaisalmer', 'Jodhpur', 'Kota', 'Udaipur', 'Agartala',
       'Dharmanagar', 'Cherrapunjee', 'Shillong', 'Bishnupur', 'Imphal','Aizawl', 'Champhai', 'Kohima', 'Dimapur', 'Jammu', 'Srinagar',
       'Rajouri', 'Anantnag', 'Pulwama', 'Dharamshala', 'Mandi', 'Shimla','Hamirpur', 'Manali', 'Haridwar', 'Dehradun', 'Rudrapur',
       'Haldwani', 'Rishikesh', 'Pragyaraj', 'Lucknow', 'Kanpur','Bareilly', 'Agra', 'Meerut', 'Durgapur', 'Asansol', 'Kharagpur',
       'Kolkata', 'Siliguri', 'Ranchi', 'Dhanbad', 'Jamshedpur','Bokaro Steel City', 'Deoghar', 'Cuttack', 'Rourkela', 'Puri',
       'Bhadrak', 'Bhubaneswar ', 'Indore', 'Jabalpur', 'Bhopal','Gwalior', 'Ujjain', 'Thane', 'Pune', 'Nashik', 'Mumbai', 'Nagpur','Panvel']

CATEGORIES = ['Bakery', 'Vegetables', 'Grocery', 'Dairy products', 'Flowers',
            'Meat', 'Fruits', 'Fish']

SUB_CATEGORIES = ['Bakery products', 'All season', 'Beverages', 'Household items',
       'Dairy products', 'White flowers', 'Red Meat', 'Citrus Fruits',
       'Freshwater', 'Seasonal', 'Seawater', 'White Meat',
       'Frozen desserts', 'Yellow flowers', 'Pink flowers',
       'Purple flowers', 'Red flowers', 'Melons', 'Orange flowers',
       'Blue flowers', 'nan']

MICR0_CATEGORIES = ['Bread', 'Brinjal', 'Chillies', 'Coffee', 'Cookies', 'Dal', 'Ghee','Jasmine', 'Milk', 'Mutton', 'Orange', 'Paneer', 'Rice', 'Murrel',
       'Sweet lime', 'Tomato', 'Water Lily', 'Banana', 'Cakes', 'Mango','Prawns', 'Tea', 'Wheat', 'Mosambi', 'Water Apple', 'Cucumber',
       'Brownie', 'Chicken', 'Rohu', 'Curd', 'Ice-cream', 'Okra',
       'Marigold', 'Onion', 'Papaya', 'Cup-cakes', 'Frozen yoghurt','Lemon', 'Potato', 'Apple', 'Bamboo shoot', 'Carrot', 'Grapes',
       'Green leafy', 'Kiwi', 'Mahseer', 'Orchid', 'Pork', 'Beef','Catfish', 'Duck', 'Ilish', 'Rose', 'Butter', 'Garlic',
       'Jackfruit', 'Salmon', 'Gourd', 'Cheese', 'Litchi', 'Pumpkin','Catla', 'Lotus', 'Pineapple', 'Lassi', 'Cruciferous vegetables',
       'Guava', 'Sugarcane', 'Carnation', 'Carp', 'Buffalo', 'Pear','Tuna', 'Alfafa', 'Pomegranate', 'Watermelon', 'Pomfret', 'Beans',
       'Sunflower', 'Coconut', 'Mackerel', 'Lobster', 'Tamarind','Dragon Fruit', 'Shrimp', 'Chikoo', 'Kinnow', 'Lily', 'Peas',
       'Peach', 'Katley', 'Mandarin', 'Rhododendron', 'Trout','Musk melon', 'Periwinkle', 'Hibiscus', 'Rohira', 'Sky flower',
       'Berry', 'Catflish', 'Dahlia', 'Olive Barb', 'Petunia', 'Shidol','Beetroot', 'Daisy', 'Cherry Blossom', 'Chrysanthemum', 'Plums',
       'Buttercup', 'Fermented Fish', 'Passion fruit', 'Oil Palm','Ginger', 'Kingfish', 'Senhri', 'Anthurium', 'Apricot', 'Crocus','Tulip', 'nan']


# top_city_df = pd.read_csv(r'\Users/adityajha/Desktop/DEV/sarvm/backend/data/Indian cities database.csv')
# top_city_df = pd.read_csv(r'/Users/adityajha/Desktop/DEV/sarvm/backend/data/IndianCitiesDatabase.csv')
# top_languages_df = pd.read_csv(r'/Users/adityajha/Desktop/DEV/sarvm/backend/data/Languages database.csv')
# top_categories_df = pd.read_csv(r'/Users/adityajha/Desktop/DEV/sarvm/backend/data/product-category database.csv')


top_city_df = pd.read_csv(r'./data/IndianCitiesDatabase.csv')
top_languages_df = pd.read_csv(r'./data/Languages database.csv')
top_categories_df = pd.read_csv(r'./data/product-category database.csv')

    

# def read_datasource(x):
#     top_city_df = pd.read_csv(r'/Users/adityajha/Desktop/DEV/sarvm/backend/data/Indian cities database.csv')
#     top_languages_df = pd.read_csv(r'/Users/adityajha/Desktop/DEV/sarvm/backend/data/Languages database.csv')
#     top_categories_df = pd.read_csv(r'/Users/adityajha/Desktop/DEV/sarvm/backend/data/product-category database.csv')
#     reqd_lists = [top_city_df, top_languages_df, top_categories_df]
#     return (reqd_lists[x])

def get_top_languages():
    
    get_top = top_languages_df.copy()
    # Remove the unnecessary columns
    get_top.drop(['state_code', 'State'], axis=1, inplace=True)
    # Sum the language percentages to get the maximum
    get_top = get_top.groupby(['Languages'], axis=0, as_index=False).sum()
    get_top.rename(columns = {'Percentage (%)':'Sum'}, inplace = True)
    # Sorting by column "Percentage"
    get_top = get_top.sort_values(by=['Sum'], ascending=False) 
    # Normalizing the values and converting back to percentage
    get_top['Sum'] = (get_top['Sum']-get_top['Sum'].min())/(get_top['Sum'].max()-get_top['Sum'].min())
    get_top['Sum'] = get_top['Sum'].apply(lambda x: x*100)
    top_lang = get_top.nlargest(n=20, columns=['Sum'])
    top_lang = top_lang['Languages']
    return list(top_lang)

def get_top_states(language):
    top_languages =  top_languages_df.copy()
    x = (top_languages['Languages'] == language)
    l1 = top_languages[x].sort_values(by=['Percentage (%)'], ascending=False)[:20]
    for language in LANGUAGES:
        return list(l1['State'])

def get_top_cities(state):
    top_city = top_city_df.copy()
    x = (top_city['State'] == state)
    c1 = top_city[x].sort_values(by=['Population (%)'], ascending=False)
    
    for state in STATES:
        return list(c1['District'].tolist())

def get_top_categories(city, language):
    top_languages =  top_languages_df.copy()
    top_categories = top_categories_df.copy()
    merged_df = pd.merge(top_languages, top_categories, on='State', how='right')
    merged_df.drop(['state_code_x', 'state_code_y', 'Percentage (%)'], axis=1, inplace=True)
    
    t1 = merged_df[(merged_df['City'] == city) & (merged_df['Languages'] == language)]
    t2 = t1['Category'].value_counts()
    
    for city in CITIES:
        for language in LANGUAGES:
            return t2.index.tolist()

def get_top_subcategories(city, language, category):
    top_languages =  top_languages_df
    top_categories = top_categories_df
    merged_df = pd.merge(top_languages, top_categories, on='State', how='right')
    merged_df.drop(['state_code_x', 'state_code_y', 'Percentage (%)'], axis=1, inplace=True)
    
    s1 = merged_df[(merged_df['City'] == city) & (merged_df['Languages'] == language) & (merged_df['Category'] == category)]
    s2 = s1['Sub-category'].value_counts()
    
    for city in CITIES:
        for language in LANGUAGES:
            for category in CATEGORIES:
                return s2.index.tolist()

def get_top_microcategories(city, language, category, subcategory):
    top_languages =  top_languages_df
    top_categories = top_categories_df
    merged_df = pd.merge(top_languages, top_categories, on='State', how='right')
    merged_df.drop(['state_code_x', 'state_code_y', 'Percentage (%)'], axis=1, inplace=True)
    
    m1 = merged_df[(merged_df['City'] == city) & (merged_df['Languages'] == language) & (merged_df['Category'] == category) & 
                   (merged_df['Sub-category'] == subcategory)]
    m2 = m1['Micro-category'].value_counts()
    
    for city in CITIES:
        for language in LANGUAGES:
            for category in CATEGORIES:
                for subcategory in SUB_CATEGORIES:
                    return m2.index.tolist()

def get_top_products(city, language, category, subcategory, microcategory):
    top_languages =  top_languages_df
    top_categories = top_categories_df
    merged_df = pd.merge(top_languages, top_categories, on='State', how='right')
    merged_df.drop(['state_code_x', 'state_code_y', 'Percentage (%)'], axis=1, inplace=True)
    
    p1 = merged_df[(merged_df['City'] == city) & (merged_df['Languages'] == language) & (merged_df['Category'] == category) & 
                   (merged_df['Sub-category'] == subcategory) & (merged_df['Micro-category'] == microcategory)]
    p2 = p1['Product'].value_counts()
    
    for city in CITIES:
        for language in LANGUAGES:
            for category in CATEGORIES:
                for subcategory in SUB_CATEGORIES:
                    for microcategory in MICR0_CATEGORIES:
                        return p2.index.tolist()
      