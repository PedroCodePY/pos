#imports
from fastapi import APIRouter, Path
from models.user import UserLogin, UserRegister, UserUpdate, CashierLogin, CashierRegister, CashierUpdate

router = APIRouter()

#admin routes
#Login route
@router.post("/login")
def login(user: UserLogin = Path(description="User login")):
    return user, {"message": "Login successful"}

#Registration route
@router.post("/register")
def register(user: UserRegister = Path(description="User registration")):
    return user, {"message": "Registration successful"}

#Update route
@router.put("/update/user")
def update_user(user: UserUpdate = Path(description="User update")):
    return user, {"message": "User updated successfully"}

@router.delete("/delete ")

#cashier routes
#Login route
@router.post("/login/cashiers")
def login_cashiers(user: CashierLogin = Path(description="Cashier login")):
    return user, {"message": "Cashiers login successfully"}

#Registration route
@router.post("/register/cashiers")
def register_cashiers(user: CashierRegister = Path(description="Cashier registration")):
    return user, {"message": "Cashiers register successfully"}

#Update route
@router.put("/update/cashiers")
def update_cashiers(user: CashierUpdate = Path(description="Cashier update")):
    return user, {"message": "Cashiers updated successfully"}