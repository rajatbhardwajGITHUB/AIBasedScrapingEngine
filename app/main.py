from fastapi import FastAPI, Depends, HTTPException
from api.deps import verify_authorization
from services.ai_agent_services import web_scraper
from models import ExtractedData, ResponseModel
from mangum import Mangum
app = FastAPI()

@app.post("/{url}", response_model=ResponseModel)
async def read_root(authorized: None = Depends(verify_authorization), url: str = None):
    
    try:
        # Fetch data from the scraper
        result = web_scraper(url)

        # Check if the scraper encountered an error
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        # Construct the response
        extracted_data = ExtractedData(
            industry=result.get("nlp_extracted", {}).get("industry"),
            company_size=result.get("nlp_extracted", {}).get("company_size"),
            location=result.get("nlp_extracted", {}).get("location"),
        )

        return ResponseModel(
            message=f"Data extracted for {url}",
            data=extracted_data
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")

from mangum import Mangum
handler = Mangum(app)