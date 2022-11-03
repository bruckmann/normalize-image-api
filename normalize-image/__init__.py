import logging
import normalizeImage
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        name = req_body.get('name')
        image = req_body.get('ímage')
        age = req_body.get('age')


    print(image)
    print(age)
    print(name)
