
import json

file_path = '/Users/piyushpanthi/Documents/Data Analytics/A_B_Testing/A_B_Testing.ipynb'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacements map based on CSV headers and User Request
replacements = {
    # Campaign Columns
    "'facebook_cost_per_ad'": "'facebook_cost_per_ad'",
    "'facebook_ctr'": "'facebook_ctr'",
    "'facebook_conversion_rate'": "'facebook_conversion_rate'",
    "'facebook_cost_per_click'": "'facebook_cost_per_click'",
    
    "'adword_cost_per_ad'": "'adword_cost_per_ad'",
    "'adword_ctr'": "'adword_ctr'",
    "'adword_conversion_rate'": "'adword_conversion_rate'",
    "'adword_cost_per_click'": "'adword_cost_per_click'",
    
    # Clicks and Conversions
    "'facebook_ad_clicks'": "'facebook_ad_clicks'",
    "'adword_ad_clicks'": "'adword_ad_clicks'",
    "'facebook_ad_conversions'": "'facebook_ad_conversions'",
    "'adword_ad_conversions'": "'adword_ad_conversions'",
    
    # Date and Time
    "'Date'": "'date_of_campaign'",
    "'Month'": "'month'",
    "'Day_of_Week'": "'day_of_week'",
    
    # File Path (Fixing absolute path to relative)
    "'/Users/piyushpanthi/Documents/Data Analytics/A:B Testing/A_B_testing_dataset.csv'": "'A_B_testing_dataset.csv'",
    
    # Handling potential Double Quotes usage as fall-back
    '"facebook_cost_per_ad"': '"facebook_cost_per_ad"',
    '"facebook_ctr"': '"facebook_ctr"',
    '"facebook_conversion_rate"': '"facebook_conversion_rate"',
    '"facebook_cost_per_click"': '"facebook_cost_per_click"',
    '"adword_cost_per_ad"': '"adword_cost_per_ad"',
    '"adword_ctr"': '"adword_ctr"',
    '"adword_conversion_rate"': '"adword_conversion_rate"',
    '"adword_cost_per_click"': '"adword_cost_per_click"',
    '"facebook_ad_clicks"': '"facebook_ad_clicks"',
    '"adword_ad_clicks"': '"adword_ad_clicks"',
    '"facebook_ad_conversions"': '"facebook_ad_conversions"',
    '"adword_ad_conversions"': '"adword_ad_conversions"',
    '"Date"': '"date_of_campaign"',
    '"Month"': '"month"',
    '"Day_of_Week"': '"day_of_week"'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated notebook column names.")
