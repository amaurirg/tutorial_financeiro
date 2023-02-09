from enum import Enum

from fastapi import APIRouter, status, Depends
from pydantic import BaseModel, Field
from decimal import Decimal

from sqlalchemy.orm import Session

from contas_a_pagar_e_receber.models.conta_a_pagar_receber_model import ContaPagarReceber
from shared.dependencies import get_db

router = APIRouter(prefix="/contas-a-pagar-e-receber")


class ContaPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: str

    class Config:
        orm_mode = True


class ContaPagarReceberEnum(str, Enum):
    PAGAR = "PAGAR"
    RECEBER = "RECEBER"


class ContaPagarReceberRequest(BaseModel):
    descricao: str = Field(min_length=3, max_length=30)
    valor: Decimal = Field(gt=0)
    tipo: ContaPagarReceberEnum


@router.get("/", response_model=list[ContaPagarReceberResponse])
def listar_contas(db: Session = Depends(get_db)) -> list[ContaPagarReceberResponse]:
    return db.query(ContaPagarReceber).all()


@router.post("/", response_model=ContaPagarReceberResponse, status_code=status.HTTP_201_CREATED)
def criar_conta(conta_a_pagar_e_receber_request: ContaPagarReceberRequest, db: Session = Depends(get_db)):
    contas_a_pagar_e_receber = ContaPagarReceber(**conta_a_pagar_e_receber_request.dict())
    db.add(contas_a_pagar_e_receber)
    db.commit()
    db.refresh(contas_a_pagar_e_receber)

    return contas_a_pagar_e_receber
