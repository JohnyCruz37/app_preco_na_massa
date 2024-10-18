from fastapi import APIRouter
from .user import router as user
from .login_router import router as login_router
from .ingrediente_router import router as ingrediente_router
from .insumo_router import router as insumo_router
from .embalagem_router import router as embalagem_router

router = APIRouter()

router.include_router(user, prefix="/users", tags=["users"])

router.include_router(login_router, prefix="/login", tags=["login"])

router.include_router(ingrediente_router, prefix="/ingredientes", tags=["ingredientes"])

router.include_router(insumo_router, prefix="/insumos", tags=["insumos"])

router.include_router(embalagem_router, prefix="/embalagens", tags=["embalagens"])
