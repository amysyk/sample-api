from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel


class TimeResponse(BaseModel):
    local_time: str


app = FastAPI(
    title="Time API",
    description="A simple API that returns the local time of the server",
    version="1.0.0"
)


@app.get("/time", response_model=TimeResponse, summary="Get local time")
async def get_time():
    """
    Get the current local time of the server.

    Returns:
        TimeResponse: Current local time in ISO 8601 format
    """
    current_time = datetime.now().isoformat()
    return TimeResponse(local_time=current_time)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)