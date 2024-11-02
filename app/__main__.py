from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers.auth import router as auth_router
from app.routers.profile import router as profile_router
from app.routers.user import router as user_router
from app.routers.fiu import router as fiu_router
from app.auth.oauth2_route import router as oauth2_compliance_router
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

app = FastAPI()


@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(status_code=429, content={"detail": "Too many requests, please try again later."})


limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)


app.include_router(oauth2_compliance_router, prefix="", tags=["OAuth2 Compliance"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(profile_router, prefix="/profile", tags=["Profile"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(fiu_router, prefix="/fiu", tags=["FIU"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
