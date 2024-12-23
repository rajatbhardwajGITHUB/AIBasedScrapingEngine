from bs4 import BeautifulSoup as bs
import requests
import spacy

# Load the spaCy NLP model
nlp = spacy.load("en_core_web_sm")

def web_scraper(url):
    try:
        # Fetch the webpage
        url = "https://" + url
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": "Failed to fetch the webpage."}

        soup = bs(response.text, 'html.parser')

        # NLP-based processing
        print("\nNLP Analysis:")
        page_text = soup.get_text(separator=" ", strip=True)  # Extract all text
        doc = nlp(page_text)

        # Extract industry (based on keywords or context)
        extracted_industry = None
        for sent in doc.sents:
            if "industry" in sent.text.lower():
                extracted_industry = sent.text.strip()
                break
        extracted_industry = extracted_industry or "Industry not found using NLP."
        print(f"Extracted Industry: {extracted_industry}")

        # Extract company size (based on keywords like 'employees' or 'people')
        company_size = None
        for sent in doc.sents:
            if "employees" in sent.text.lower() or "people" in sent.text.lower():
                company_size = sent.text.strip()
                break
        company_size = company_size or "Company size not found."
        print(f"Company Size: {company_size}")

        # Extract location (based on named entity recognition for GPE)
        location = None
        for ent in doc.ents:
            if ent.label_ == "GPE":  # GPE = Geopolitical Entity
                location = ent.text
                break
        location = location or "Location not found."
        print(f"Location: {location}")

        # Return structured results
        return {
            
            "nlp_extracted": {
                "industry": extracted_industry,
                "company_size": company_size,
                "location": location,
            },
        }

    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error": str(e)}


