import sys
from pathlib import Path

import uvicorn

BACKEND_DIR = Path(__file__).resolve().parent / "backend"
sys.path.insert(0, str(BACKEND_DIR))

if __name__ == "__main__":
    uvicorn.run(
        "app.app:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        reload_dirs=[str(BACKEND_DIR / "app")],
    )
