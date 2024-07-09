from fastapi import FastAPI
import GPT_summary
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    test_data = [
        {"title": "Santos Boss Is Racing Against Time to Build a Gas Giant", "ESG": 42.2, "author": "Stephen Stapczynski", "link": "https://www.bloomberg.com/news/articles/2024-07-06/australia-energy-santos-boss-is-racing-against-time-to-build-a-global-gas-giant"},
        {"title": "Anglo American prepares to launch $7b-plus sale of Queensland coal mines", "ESG": 28, "author": "Sarah Thompson", "link": "https://www.afr.com/street-talk/anglo-american-prepares-to-launch-7b-plus-sale-of-queensland-coal-mines-20240707-p5jrpo"},
        {"title": "CSL shares: 'Healthy growth at a reasonable price'", "ESG": 24.7, "author": "James Mickleboro", "link": "https://www.fool.com.au/2024/07/08/csl-shares-healthy-growth-at-a-reasonable-price/"},
        {"title": "Rio Tinto (RIO) Builds Solar Power Plant at Diavik Mine", "ESG": 31.5, "author": "Zacks", "link": "https://finance.yahoo.com/news/rio-tinto-rio-builds-solar-155600256.html"}
    ]
    
    results = []
    counter = 1
    for article in test_data:
        URL = article["link"]
        summary = GPT_summary.generate_summary_ONE_article(URL)
        result = {"id": counter, 'title': article["title"], "ESG": article["ESG"], "author": article["author"], "body": summary, "link": URL}
        results.append(result)
        counter += 1
    
    # Convert to JSON string
    json_esg = json.dumps(results)
    
    return json_esg

if __name__ == "__main__":
    import uvicorn

    # Only start the FastAPI server when this script is run directly
    uvicorn.run(app, host="127.0.0.1", port=8000)