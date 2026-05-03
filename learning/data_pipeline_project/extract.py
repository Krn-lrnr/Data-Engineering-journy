from typing import Optional, Dict, Any
import json
import urllib.request
import urllib.error


def extract(url: str) -> Optional[Dict[str, Any]]:
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError:
        pass
    return None