from openai import OpenAI
import json


alpha_api = "RKE6GIOQI4JM7LYK"

client = OpenAI(
                    organization='org-eXvNlOiMfgKeziZdN6Qd30Ag',
                    project='proj_gAyJmP46wZbkdOLl4bDL3Gvo',
                    api_key="sk-proj-EBPOQpO4PDLV0FzvETbdT3BlbkFJu3BNwBQ55rODcNJqJt0U"
                )

def generate_summary_ONE_article(URL):


    response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                response_format={ "type": "json_object" },
                messages=[
                    {"role": "system", "content": "You are a financial analyst, skilled in explaining complex financial concepts to people, with no financial understanding, with clarity and design to output JSON,the JSON format is 'Title', put the key points under 'key points "},
                    {"role": "user", "content": f"summary this website {URL} into one clear summary to cover everything about this company, less than 200 words and use 5 to 10 dot points. PLEASE USE DOT POINTS"}
                ]
                )
    result = response.choices[0].message.content
    
    result_json = json.loads(result)

    key_points = result_json["key points"]
    concatenated_string = ' '.join(key_points)

    return concatenated_string

