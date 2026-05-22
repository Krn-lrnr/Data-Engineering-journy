from typing import Optional, Dict, Any
import json
import urllib.request
import urllib.error
import retry_handler

def extract(url: str, retries: int, delay: int) -> Optional[Dict[str, Any]]:
    try:
        # delegate fetching with retry logic to retry_handler
        response = retry_handler.fetch_with_retry(url, retries, delay)
        if response is None:
            return None
        # response expected to be a file-like object from urllib
        content = response.read()
        if isinstance(content, bytes):
            content = content.decode("utf-8")
        return json.loads(content)
    except urllib.error.URLError:
        return None
    except Exception:
        return None