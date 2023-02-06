from fastapi import FastAPI

from contas_a_pagar_e_receber.routers import contas_a_pagar_e_receber_router
from shared.database import Base, engine

'''
ZERA E CRIA O DB NOVAMENTE A CADA ATUALIZAÇÃO (POR ENQUANTO)

from contas_a_pagar_e_receber.models.conta_a_pagar_receber_model import ContaPagarReceber


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
'''


app = FastAPI()


app.include_router(contas_a_pagar_e_receber_router.router)
