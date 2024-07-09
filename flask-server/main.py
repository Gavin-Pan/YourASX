from flask import Flask
from flask_cors import CORS
import GPT_summary
import json

app = Flask(__name__)
cors=CORS(app,origins='*')

@app.route('/newsletters')
def summarised_newletters():
    
    general_news_data = [
        {
            "id": 1,
            "title": "Personal bankruptcy threshold to go up in overhaul to be revealed by Labor Attorney-General Mark Dreyfus",
            "author": "Ronald Mizen",
            "body": "Australian Labor Party introduces new policy to reform personal bankruptcy laws Proposed changes aim to provide relief to individuals struggling with debts Under the new policy, bankruptcy period reduced from three years to one year Individuals will have access to financial counseling and debt management services Labor Party emphasizes the need for a fair and accessible bankruptcy system Policy includes measures to prevent exploitation of bankruptcy laws Changes set to benefit individuals facing financial difficulties",
            "link": "http://www.afr.com/politics/federal/labor-reveals-personal-bankruptcy-overhaul-20240707-p5jroa"
        },
        {
            "id": 2,
            "title": "Australia might blink at AUKUS cost, fears Trump\u2019s ex-Pentagon chief",
            "author": "Andrew Tillett",
            "body": "Australia is facing apprehension over the potential costs associated with the AUKUS agreement, according to former Pentagon chief, Mark Esper. The fears stem from the belief that Australia may reconsider its commitment to the pact due to financial burdens. The AUKUS pact involves Australia, the UK, and the US, with a focus on strengthening defense ties and capabilities in the Indo-Pacific region. Esper highlights the importance of Australia upholding its end of the agreement despite challenges. The financial aspect may influence Australia's decision-making regarding the continuation of its involvement in AUKUS. Australia's stance on the agreement and its associated costs could impact the existing dynamics within the alliance. The concerns raised by Esper shed light on the complexities involved in maintaining international defense partnerships.",
            "link": "http://www.afr.com/politics/federal/australia-might-blink-at-aukus-cost-fears-trump-s-ex-pentagon-chief-20240707-p5jrmw"
        },
        {
            "id": 3,
            "title": "Mental health: A daily bucket list could make you happier than that grand trip to Paris",
            "author": "Lucy Dean",
            "body": "The website www.afr.com focuses on life, luxury, health, and wellness topics. It emphasizes the need to reconsider one's bucket list. The content suggests questioning the traditional approach to a bucket list and the importance of aligning it with personal values. The website provides insights on lifestyle choices and decision-making related to health and well-being. It encourages readers to reflect on their aspirations and priorities to lead a fulfilling life. Articles on the website likely offer thought-provoking perspectives and advice on living a purposeful and balanced life. The content aims to inspire readers to make intentional choices that contribute to their overall well-being and happiness. Visitors can expect to find thought-leadership content on various life and luxury-related topics on the website. www.afr.com appears to cater to individuals interested in personal development, health, luxury, and lifestyle enhancement. The website may serve as a resource for those seeking guidance on redefining their goals and achieving a more fulfilling life.",
            "link": "http://www.afr.com/life-and-luxury/health-and-wellness/why-you-probably-need-to-rethink-your-bucket-list-20240613-p5jln5"
        },
        {
            "id": 4,
            "title": "French election: Voting under way as France braces for far-right chaos",
            "author": "Barbara Surk, Helena Alves",
            "body": "France is experiencing political uncertainty as far-right chaos looms over the country during the ongoing voting. The French presidential election is marked by a significant rise in far-right sentiments and potential for unrest. Rival parties are in a race against time to secure votes amid a polarized political landscape. The far-right candidate's popularity has raised concerns about the future direction of French politics and the European Union. Both domestic and international observers are closely monitoring the election outcomes for potential implications. The voting process is crucial in determining the path France will take concerning key issues like immigration, economy, and foreign policy. The election results could have far-reaching consequences on France's relations with its EU partners and the global community. French citizens are divided over the best way forward, reflecting broader societal tensions and ideological conflicts within the nation. The election outcome will shape the political and social dynamics in France for years to come. The anticipation and apprehension surrounding the voting highlight the critical juncture at which France stands in its political evolution.",
            "link": "http://www.afr.com/world/europe/france-braces-for-far-right-chaos-as-voting-underway-20240707-p5jrq8"
        },
        {
            "id": 5,
            "title": "Aware Super, UniSuper, Cbus rule out financing Peter Dutton\u2019s nuclear energy plan",
            "author": "Hannah Wootton",
            "body": "Peter Dutton's plan to investigate nuclear energy in Australia faces funding challenges due to uncertainty and slow progress Some key funds have already ruled out financing Dutton's nuclear plan The uncertainty surrounding the project is a major obstacle in obtaining financial support The slow progress of the plan is causing concerns among potential investors Dutton's nuclear energy proposal is met with skepticism from various financial entities The lack of commitment from key funds hinders the advancement of the nuclear energy agenda There is a clear link between the financial viability of the project and the uncertainty surrounding its implementation The funding landscape for Dutton's nuclear plan remains precarious due to these challenges Financial support for the project is in jeopardy unless the uncertainties and delays are addressed effectively",
            "link": "http://www.afr.com/politics/federal/too-uncertain-too-slow-funds-rule-out-financing-dutton-nuclear-plan-20240706-p5jrku"
        },
        {
            "id": 6,
            "title": "NDIS blowouts:  Bill Shorten says payments for sex work will be banned",
            "author": "Tom McIlroy",
            "body": "The Australian government is planning to ban the use of NDIS funds for activities like sex work, steam rooms, and crypto trading. The government believes that such activities are not sustainable under the NDIS scheme. The move aims to ensure that NDIS funds are used appropriately and effectively to support individuals with disabilities. There are concerns about the misuse of NDIS funds for activities that are not directly related to the care and support of people with disabilities. The ban on using NDIS funds for these activities is part of the government's efforts to improve the oversight and governance of the scheme. The decision has sparked debates about the boundaries and restrictions on the use of NDIS funds.",
            "link": "http://www.afr.com/politics/federal/not-sustainable-sex-work-steam-rooms-crypto-to-be-banned-on-ndis-20240707-p5jrnh"
        },
        {
            "id": 7,
            "title": "PWC spinoff Scyne is winning work, and hiring, after winning back government trust",
            "author": "Edmund Tadros",
            "body": "Scyne was sold to PwC for $1 Scyne managed to recover one-third of PwC's revenue The acquisition by PwC aimed to enhance its technology offerings Scyne specializes in artificial intelligence and business process automation solutions The founder of Scyne, Avishek Sen Gupta, joined PwC post-acquisition The deal signifies PwC's strategic move towards digital transformation Scyne's technology is expected to benefit PwC's consulting services The acquisition indicates PwC's focus on staying competitive in the evolving market PwC aims to leverage Scyne's expertise to drive innovation and growth The $1 deal showcases the strategic value PwC saw in Scyne's technology",
            "link": "http://www.afr.com/companies/professional-services/sold-for-1-scyne-claws-back-a-third-of-pwc-s-revenue-20240701-p5jq97"
        },
        {
            "id": 8,
            "title": "Rural property deals: Manar homestead near Canberra sold for the first time since 1841",
            "author": "Larry Schlesinger",
            "body": "The Georgian homestead, known as 'Lanyon Homestead,' located near Canberra, has been sold for the first time since 1841. The property holds significant historical value, being a heritage-listed estate with ties to early colonial settlement in Australia. The sale marks a significant event in the property market, attracting attention for its historical and cultural significance. The buyer(s) of the homestead have not been disclosed, adding an air of mystery to the transaction. Lanyon Homestead features stunning Georgian architecture and sprawling grounds, making it a unique and desirable property. The sale of such a historically rich property underscores the enduring appeal of well-preserved heritage sites in the real estate market. The transaction highlights the intersection of historical preservation and commercial real estate development. The exact sale price of Lanyon Homestead has not been revealed, leaving room for speculation on its value and the nature of the buyer's intentions for the property. This sale serves as a reminder of the importance of preserving and appreciating Australia's rich architectural and historical heritage. The changing ownership of Lanyon Homestead opens up possibilities for its future use and potential restoration efforts.",
            "link": "http://www.afr.com/property/commercial/georgian-homestead-near-canberra-sold-for-the-first-time-since-1841-20240704-p5jr23"
        },
        {
            "id": 9,
            "title": "Australian shares: ASX to sit out global rally amid iron ore woes",
            "author": "Alex Gluyas",
            "body": "The ASX is expected to not participate in the global market rally. This is due to ongoing issues in the iron ore market adversely affecting the ASX. Iron ore prices have been volatile, impacting Australian companies reliant on this commodity. Global trends are positive, but the ASX may lag behind due to its connections to iron ore. Investors should be cautious about ASX investments given the current market conditions.",
            "link": "http://www.afr.com/markets/equity-markets/asx-to-sit-out-global-rally-amid-iron-ore-woes-20240705-p5jrfg"
        },
        {
            "id": 10,
            "title": "Horse rider Sarah Wheeler honours parents' legacy on outback ride to raise awareness about rare cancer",
            "author": "Danielle Lancaster",
            "body": "The article discusses Sarah Wheeler's ride across the outback of NSW and QLD to raise awareness for a rare cancer. Sarah Wheeler is a cancer survivor and has been advocating for greater awareness and resources for those affected by the disease. The ride aims to bring attention to the lack of specialist services in regional areas for rare cancers. Wheeler's journey will cover 3,000 kilometers over four weeks and will include stops in various towns to engage with communities. The Outback Ride is supported by the Rare Cancers Australia charity organization. Sarah Wheeler hopes to inspire others and highlight the challenges faced by those with rare cancers. The ride will also raise funds for research into rare cancers and support services for patients. The article emphasizes the need for improved access to specialized care and treatments for rare cancer patients in rural areas. Wheeler's efforts provide a platform for raising awareness, advocating for change, and supporting those impacted by rare cancers. The Outback Ride represents a significant personal and charitable endeavor to make a difference in the fight against rare cancers.",
            "link": "https://www.abc.net.au/news/2024-07-07/sarah-wheeler-outback-ride-nsw-qld-raising-awareness-rare-cancer/104061604"
        }
    ]
    company_news_data = [
    {
        "id": 1,
        "title": "Santos Boss Is Racing Against Time to Build a Gas Giant",
        "ESG": 42.2,
        "author": "Stephen Stapczynski",
        "link": "https://www.bloomberg.com/news/articles/2024-07-06/australia-energy-santos-boss-is-racing-against-time-to-build-a-global-gas-giant"
    },
    {
        "id": 2,
        "title": "Anglo American prepares to launch $7b-plus sale of Queensland coal mines",
        "ESG": 28,
        "author": "Sarah Thompson",
        "link": "https://www.afr.com/street-talk/anglo-american-prepares-to-launch-7b-plus-sale-of-queensland-coal-mines-20240707-p5jrpo"
    },
    {
        "id": 3,
        "title": "CSL shares: 'Healthy growth at a reasonable price'",
        "ESG": 24.7,
        "author": "James Mickleboro",
        "link": "https://www.fool.com.au/2024/07/08/csl-shares-healthy-growth-at-a-reasonable-price/"
    },
    {
        "id": 4,
        "title": "Rio Tinto (RIO) Builds Solar Power Plant at Diavik Mine",
        "ESG": 31.5,
        "author": "Zacks",
        "link": "https://finance.yahoo.com/news/rio-tinto-rio-builds-solar-155600256.html"
    }
]
    
    company_news_results = []
    general_news_results = []
    counter = 1
    for counter, article in enumerate(company_news_data, 1):
        URL = article["link"]
        summary = GPT_summary.generate_summary_ONE_article(URL)
        result = {"id": counter, 'title': article["title"], "author": article["author"], "ESG": article["ESG"], "body": summary, "link": URL}
        company_news_results.append(result)
    
    for counter, article in enumerate(general_news_data, 1):
        URL = article["link"]
        summary = GPT_summary.generate_summary_ONE_article(URL)
        result = {"id": counter, 'title': article["title"], "author": article["author"], "body": summary, "link": URL}
        general_news_results.append(result)


    # Convert to JSON string
    json_esg = json.dumps({
        "generalNews": general_news_results,
        "companyNews": company_news_results
    })
    
    return json_esg

if __name__ == "__main__":
    app.run(debug=True,  port= "8080")