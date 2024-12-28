from fastapi import APIRouter, Body, status
from workout_api.atleta.schemas import AtletaIn
from workout_api.contrib.depencies import DataBaseDependency

router = APIRouter()


@router.post("/", 
             summary="Criar novo atleta", 
             status_code=status.HTTP_201_CREATED
             )
async def post(db_session: DataBaseDependency, 
               atleta_in: AtletaIn= Body(...)):
    pass
