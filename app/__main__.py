import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address
from fastapi.staticfiles import StaticFiles
from pathlib import Path
# Import routers
from app.auth.oauth2_route import router as oauth2_compliance_router
from app.routers.auth import router as auth_router
from app.routers.fiu import router as fiu_router
from app.routers.profile import router as profile_router
from app.routers.user import router as user_router
from app.routers.preferences import router as preferences_router
from app.routers.enumeration.all import router as all_enums_router
from app.routers.engagement import router as engagement_router

app = FastAPI()

api = FastAPI()

if os.environ.get("DEBUG", "0") == "1":
    api.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )
else:
    api.add_middleware(
        CORSMiddleware,
        allow_origins=[os.environ.get("HOST_IP", "*")],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )


@api.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Too many requests, please try again later."},
    )


limiter = Limiter(key_func=get_remote_address)
api.state.limiter = limiter
api.add_middleware(SlowAPIMiddleware)

api.include_router(oauth2_compliance_router, prefix="", tags=["OAuth2 Compliance"])
api.include_router(auth_router, prefix="/auth", tags=["Auth"])
api.include_router(profile_router, prefix="/profile", tags=["Profile"])
api.include_router(user_router, prefix="/users", tags=["Users"])
api.include_router(fiu_router, prefix="/fiu", tags=["FIU"])
api.include_router(all_enums_router, prefix="/enums", tags=["Enums"])
api.include_router(preferences_router, prefix="/preferences", tags=["Preferences"])
api.include_router(engagement_router, prefix="/engagement", tags=["Engagement"])

app.mount("/api", api)
api.mount("/uploads", StaticFiles(directory=Path(__file__).parent.parent/'uploads'), name="static")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)

