from fastapi import FastAPI
from app.database import Base, engine
from app.routers import agendamento_router, veiculo_router, cliente_router
from app.models import cliente, agendamento, veiculo

app = FastAPI(
    title="API oficina",
    version="1.0.0",
    description="api que gerencia agendamentos, clientes e veiculos"
)

#cria as tabelas
Base.metadata.create_all(bind=engine)

#registra as rotas
app.include_router(agendamento_router.router)
app.include_router(cliente_router.router)
app.include_router(veiculo_router.router)