import os


def ymaps_key(request):
    return {
        "YMAPS_API_KEY": os.getenv("YMAPS_API_KEY", "")
    }
