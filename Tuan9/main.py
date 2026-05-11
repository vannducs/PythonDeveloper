#Viết API đăng nhập trả về Token. 
#Dùng Depends tạo một hàm get_current_user. Đưa hàm này vào các API cần bảo vệ (như Tạo, Sửa, Xóa).

from datetime import datetime, timedelta
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jose import JWTError, jwt
from passlib.context import CryptContext

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pass_context.hash("123456")
    }
}

def verify_password(plain_password, hashed_password):
    return pass_context.verify(plain_password, hashed_password)

def get_user(username: str):
    return fake_users_db.get(username)

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode=data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm = ALGORITHM
    )
    return encoded_jwt

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    user = authenticate_user(
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sai tài khoản hoặc mật khẩu"
        )

    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=timedelta(minutes=30)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


def get_current_user(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token không hợp lệ",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = get_user(username)

    if user is None:
        raise credentials_exception

    return user

#api protected
@app.get("/profile")
def read_profile(current_user: dict = Depends(get_current_user)):
    return {
        "message": "Đây là API đã đăng nhập",
        "user": current_user["username"]
    }

@app.post("/create-product")
def create_product(current_user: dict = Depends(get_current_user)):
    return {
        "message": f"{current_user['username']} đã tạo sản phẩm"
    }