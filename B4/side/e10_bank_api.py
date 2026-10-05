"""Step 10, on the side: write routes, request bodies, errors -> HTTP statuses.

    uv run uvicorn e10_bank_api:app --reload --app-dir B4/side

Try it in http://127.0.0.1:8000/docs: open an account, deposit, withdraw too
much.
"""

from e10_bank import Bank, BankError, RefusedError, UnknownAccountError
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Bank")
bank = Bank()


# The shape of a JSON body. FastAPI refuses another shape with a 422 by itself.
class OwnerIn(BaseModel):
    owner: str


class AmountIn(BaseModel):
    amount: int


# One handler turns every error of the family into a status: no try in routes.
STATUS = {UnknownAccountError: 404, RefusedError: 409}


@app.exception_handler(BankError)
def bank_error(request: Request, error: BankError) -> JSONResponse:
    status = STATUS.get(type(error), 400)
    return JSONResponse(status_code=status, content={"detail": str(error)})


def account_view(owner: str) -> dict:
    account = bank.get(owner)
    return {"owner": account.owner, "balance": account.balance}


@app.post("/api/accounts", status_code=201)
def open_account(body: OwnerIn) -> dict:
    bank.open(body.owner)
    return account_view(body.owner)


@app.post("/api/accounts/{owner}/deposits", status_code=201)
def deposit(owner: str, body: AmountIn) -> dict:
    bank.get(owner).deposit(body.amount)
    return account_view(owner)


@app.post("/api/accounts/{owner}/withdrawals", status_code=201)
def withdraw(owner: str, body: AmountIn) -> dict:
    bank.get(owner).withdraw(body.amount)
    return account_view(owner)
