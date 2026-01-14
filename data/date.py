# Tool that return today's date
import datetime
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    now = datetime.datetime.now(datetime.timezone.utc)
    return func.HttpResponse(now.isoformat())